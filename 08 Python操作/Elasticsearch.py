# -*- coding: utf-8 -*-
# @Time : 2022/3/3 18:16
# @Author : O·N·E
# @File : Elasticsearch.py
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch import helpers
import warnings
import time

warnings.filterwarnings("ignore")


class ESClient():
    def __init__(self, index_name, ip):
        """
        :param index_name: 索引名字
        :param ip: ip地址
        """
        self.index_name = index_name
        # 实例化一个ip为localhost，端口为9200,超时时间60s
        self.es = Elasticsearch(
            [ip],
            # 操作之前嗅探elasticsearch,无响应重新连接
            sniff_on_start=True,
            sniff_on_connection_fail=True,
            sniff_timeout=60
        )

    # 计时器
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            print('共耗时约 {:.2f} 秒'.format(time.time() - start))
            return res

        return wrapper

    # 创建索引
    def create_index(self):
        # 请求体
        request_body = {
            "settings": {
                "number_of_shards": 5,
                "number_of_replicas": 1,
            },
            # 映射生成
            "mappings": {
                "properties": {
                    "account_number":
                        {
                            "type": "long"
                        },
                    "address": {
                        "type": "text"
                    },
                    "age": {
                        "type": "long"
                    },
                    "balance": {
                        "type": "long"
                    },
                    "city": {
                        "type": "text"
                    },
                    "email": {
                        "type": "text"
                    },
                    "employer": {
                        "type": "text"
                    },
                    "firstname": {
                        "type": "text"
                    },
                    "gender": {
                        "type": "text"
                    },
                    "lastname": {
                        "type": "text"
                    },
                    "state": {
                        "type": "text"
                    }
                }
            }
        }
        # 索引判断是否存在
        if self.es.indices.exists(index=self.index_name):
            self.es.indices.delete(index=self.index_name)
            print("索引已删除")
        else:
            print('索引不存在，可以创建')
        self.es.indices.create(index=self.index_name, body=request_body, ignore=[400, 404])

    # 索引删除
    def delete_index(self):
        """
        :return:索引删除,忽略400,404报错
        """
        res = self.es.indices.delete(index=self.index_name, ignore=[400, 404])
        return res

    # 索引查询
    def increase_date(self):
        """
        :return: 查询文档的索引
        """
        res = self.es.indices.get(index=self.index_name)
        return res

    # 创建文档,插入数据
    @timer
    def create_doc(self):
        # Mode 1 10000条插入耗时70s左右
        date_list = {
            "account_number": 1,
            "balance": 39225,
            "firstname": "Amber",
            "lastname": "Duke",
            "age": 32,
            "gender": "M",
            "address": "880 Holmes Lane",
            "employer": "Pyrami",
            "email": "amberduke@pyrami.com",
            "city": "Brogan",
            "state": "IL"
        }
        for i in range(10000):
            id_number = i + 1
            res = self.es.index(index=self.index_name, id=id_number, document=data)
            print(res)

        # Mode 2 生成器_bulk批量插入,10000条耗时约1秒
        actions = (
            {
                "_index": self.index_name,
                "_id": i + 1,
                "_source": {
                    "account_number": date_list['account_number'],
                    "balance": date_list['balance'],
                    "firstname": date_list['firstname'],
                    "lastname": date_list['lastname'],
                    "age": date_list['age'],
                    "gender": date_list['gender'],
                    "address": date_list['address'],
                    "employer": date_list['employer'],
                    "email": date_list['email'],
                    "city": date_list['city'],
                    "state": date_list['state']
                }
            }
            for i in range(10000)
        )
        bulk(self.es, actions, index=self.index_name)

    # 文档数据查询
    def doc_query(self):
        """
        :return:查询id=1的全部信息
        """
        res = self.es.get(index=self.index_name, id="1")
        return res

    # 文档数据局部更新(全局更新速度慢)
    def doc_update(self):
        doc = {
            "doc": {
                "balance": 1
            }
        }
        # 将test索引id为1的数据更新为新数据:balance修改为1
        self.es.update(index=self.index_name, id="1", body=doc)
        print("ok")

    # 文档全部数据查询:默认显示10条
    def doc_search_match_all(self):
        """
        match_all检索全部数据
        took ElasticSearch执行搜索的时间(毫秒)
        time_out 搜索是否超时
        _shards 有多少个分片被搜索了，统计成功/失败的搜索分片
        hits 搜索结果
        hits.total 搜索结果统计
        hits.hits 实际的搜索结果数组(默认为前10条文档)
        sort 结果的排序key，没有就按照score排序
        score和max_score 相关性得分和最高分(全文检索使用)
        :return:返回全部检索信息结果
        """
        query_body = {
            "query": {
                "match_all": {}
            }
        }
        res = self.es.search(index=self.index_name, body=query_body)
        return res

    # match特定字段查询
    def doc_search_match(self):
        """
        match模糊检索
        match 和 match_phrase的区别就像是or和and的区别)：在请求中查询地址中同时包含Lolmes和Lane的客户
        multi_match:多字段查询，任意一个字段符合条件就算符合查询条件
            # 查询name和addr包含"深圳"关键字的数据
             "multi_match":{
                "query":"深圳",
                "fields":["name","addr"]
                        }
                    }
                }
        :return:查询address为Lolmes Lane全部信息
        """
        query_body = {
            "query": {
                "match": {
                    "address": "Lolmes Lane"
                }
            }
        }
        res = self.es.search(index=self.index_name, body=query_body)
        return res

    # term,terms精确查询
    def doc_search_term(self):
        """
        term:精确查找
        terms:搜索出balance="1"或balance="10000"的所有数据
            "balance":["1","10000"]
        :return:查询balance="1"的所有数据
        """
        query_body = {
            "query": {
                "term": {
                    "balance": "1"
                }
            }
        }
        res = self.es.search(index=self.index_name, body=query_body)
        return res

    # range范围查询
    def doc_search_range(self):
        """
        range查询，一般应用在对数值类型做范围过滤的时候。比如做价格范围过滤。
        "gte": gte代表大于等于，gt则代表大于
        "lte": lte代表小于等于，lt则代表小于
        "from": 起始数据
        "size": 显示数据的数量
        :return: 查询balance大于等于2,,小于等于100000的所有数据(9999条)
        """
        query_body = {
            "query": {
                "range": {
                    "balance": {
                        "gte": 2,
                        "lte": 100000
                    }
                }
            },
            "from": 0,
            "size": 5

        }
        res = self.es.search(index=self.index_name, body=query_body)
        return res

    # sort排序
    def doc_search_sort(self):
        """
        elasticsearch默认是根据相关度算分(_score)来排序，但是也支持自定义方式对搜索结果排序。可以排序字段类型有：keyword类型、数值类型、地理坐标类型、日期类型等。
        :return:按照balance进行升序排列, 相同情况下按照age降序排列
        """
        query_body = {
            "query": {
                "match_all": {}
            },
            "sort": [
                {
                    "balance": {
                        "order": "asc"  # 先按照balance进行升序排列
                    },
                    "age": {
                        "order": "desc"  # balance相同情况下按照序号降序排列
                    }
                }
            ]
        }
        res = self.es.search(index=self.index_name, body=query_body)
        return res

    # 过滤器:filter
    def doc_search_filter(self):
        """
        5.1版本升级以后，elasticsearch将算法改进为BM25算法
        filter:结果过滤
        :return:过滤出balance在[1,2]之间的全部信息(只有一条)
        """
        query_body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match_all": {}
                        }
                    ],
                    "filter": [
                        {
                            "range": {
                                "balance": {
                                    "gte": 1,
                                    "lte": 2
                                }
                            }
                        }
                    ]
                }
            }
        }
        res = self.es.search(index=self.index_name, body=query_body)
        return res

    def doc_search_bool(self):
        """
        布尔查询是一个或多个查询子句的组合，每一个子句就是一个子查询。子查询的组合方式有：
            must：必须匹配每个子查询，类似“与”，参与算分
            should：选择性匹配子查询，类似“或”，参与算分
            must_not：必须不匹配，不参与算分，类似“非”
            filter：必须匹配，不参与算分
        :return:
        """
        query_body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "address": "Lolmes Lane"
                            }
                        }
                    ],
                    "must_not": [
                        {
                            "range": {
                                "age": {
                                    "gte": 2,
                                    "lte": 100000
                                }
                            }
                        }
                    ],
                    "filter": [
                        {
                            "term": {
                                "balance": {
                                    "value": 456488  # test
                                }
                            }
                        }
                    ]
                }
            }
        }
        res = self.es.search(index=self.index_name, body=query_body)
        return res

    # 聚合函数
    def doc_search_Aggregation(self):
        """
        Elasticsearch中的聚合，包含多种类型，最常用的两种，一个叫桶,一个叫度量,
        :return:搜索address中包含mill的所有人的年龄分布以及平均年龄
        """
        query_body = {
            "query": {
                "match": {
                    "address": "mill"
                }
            },
            "aggs": {
                "ageAggs": {  # 聚合函数名称 自己进行定义即可
                    "terms": {
                        "field": "age",
                        "size": 10
                    }
                },
                "ageavg": {  # 第二个分组名称 平均年龄
                    "avg": {
                        "field": "age"
                    }
                }
            },
            "size": 0  # 不对query查询结果进行输出，方便查看
        }
        res = self.es.search(index=self.index_name, body=query_body)
        return res

    # mapping:映射检索
    def check_mapping(self):
        """
        :return:返回映射检索信息
        """
        res = self.es.indices.get_mapping(index=self.index_name)
        return res

    # mapping:新增映射
    def increase_mapping(self):
        """
        方法:第一个就是先删除索引，然后调整后再新建索引映射，二在已有的基础上新增。
        索引一旦创建，我们是无法修改里边的内容的，不如说修改索引字段的名称。但是我们是可以向索引中添加其他字段
        :return:新增映射sex,type为text,返回创建成功信息
        """
        query_body = {
            "properties": {
                "sex": {
                    "type": "text"
                }
            }
        }
        res = self.es.indices.put_mapping(index=self.index_name, body=query_body)
        return res

    # 索引迁移
    def index_transfer(self):
        """
        常用数据类型:
        text、keyword、number、array、range、boolean、date、geo_point、ip、nested、object。
        text：默认会进行分词，支持模糊查询（5.x之后版本string类型已废弃，请大家使用text）。
        keyword：不进行分词，默认开启doc_values来加速聚合排序操作，占用了大量磁盘io 如非必须可以禁用doc_values。
        number：如果只有过滤场景 用不到range查询的话，使用keyword性能更佳，另外数字类型的doc_values比字符串更容易压缩。
        range：对数据的范围进行索引，目前支持 number range、date range 、ip range。
        array：es不需要显示定义数组类型，只需要在插入数据时用’[]‘表示即可。[]中的元素类型需保持一致。
        boolean: 只接受true、false，也可以是字符串类型的“true”、“false”。
        date：支持毫秒、根据指定的format解析对应的日期格式，内部以long类型存储。
        geo_point：存储经纬度数据对。
        ip：将ip数据存储在这种数据类型中，方便后期对ip字段的模糊与范围查询。
        ested：嵌套类型，一种特殊的object类型，存储object数组，可检索内部子项。
        object：嵌套类型，不支持数组。

        创建出正确的索引，然后使用如下的方式来进行数据的迁移
        :return:返回创建成功信息
        """
        request_body = {
            "settings": {
                "number_of_replicas": 1,
                "number_of_shards": 5
            },
            "mappings": {
                "properties": {
                    "account_number":
                        {
                            "type": "long"
                        },
                    "address": {
                        "type": "text"
                    },
                    "age": {
                        "type": "long"
                    },
                    "balance": {
                        "type": "long"
                    },
                    "city": {
                        "type": "text"
                    },
                    "email": {
                        "type": "text"
                    },
                    "employer": {
                        "type": "text"
                    },
                    "firstname": {
                        "type": "text"
                    },
                    "gender": {
                        "type": "text"
                    },
                    "lastname": {
                        "type": "text"
                    },
                    "state": {  # 上面全部索引没有进行改变，只对state索引值从text改变成keyword
                        "type": "keyword"
                    }
                }
            }
        }
        self.es.indices.create(index="my_index_new", body=request_body, ignore=[400, 404])
        """
            client:原索引所在ES
            source_index:读取documents的索引
            target_index:写入documents的索引
            query:search( )api的主体
            target_client:新索引所在ES集群的host
            chunk_size:es传输docs时每块含有的docs数量
        """
        helpers.reindex(
            client=self.es,
            source_index=self.index_name,
            target_index="my_index_new",
            chunk_size=1000
        )


if __name__ == '__main__':
    es = ESClient("my_index", ip="http://192.168.81.100:9200")
    # es.create_index()
    # es.delete_index()
    # print(es.increase_date())
    # es.create_doc()
    # print(es.doc_query())
    # es.doc_update()
    # print(es.doc_search_match_all())
    # print(es.doc_search_match())
    # print(es.doc_search_term())
    # print(es.doc_search_range())
    # print(es.doc_search_sort())
    # print(es.doc_search_filter())
    # print(es.doc_search_bool())
    # print(es.doc_search_Aggregation())
    # print(es.check_mapping())
    # print(es.increase_mapping())
    # es.index_transfer()
