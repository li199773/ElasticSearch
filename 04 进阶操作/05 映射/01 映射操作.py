# -*- coding: utf-8 -*-
# @Time : 2022/3/3 14:15
# @Author : O·N·E
# @File : 01 映射操作.py
"""
1.关系型数据库中两个数据表示是独立的，即使他们里面有相同名称的列也不影响使用，但ES中不是这样的。elasticsearch是基于Lucene开发的搜索引擎，
而ES中不同type下名称相同的filed最终在Lucene中的处理方式是一样的。
    两个不同type下的两个user_name，在ES同一个索引下其实被认为是同一个filed，你必须在两个不同的type中定义相同的filed映射。
否则，不同type中的相同字段名称就会在处理中出现冲突的情况，导致Lucene处理效率下降。
Elasticsearch 7.x
    URL中的type参数为可选。比如，索引一个文档不再要求提供文档类型。
Elasticsearch 8.x
    不再支持URL中的type参数。
    解决：将索引从多类型迁移到单类型，每种类型文档一个独立索引
2.什么是映射？
    映射是定义文档的过程，文档包含哪些字段，这些字段是否保存，是否索引，是否分词等
3.创建mapping映射
    PUT /06_mapping
    {
      "settings":{
            "number_of_shards":5,
            "number_of_replicas":1
        },
      "mappings": {
        "properties": {
          "age":{"type": "integer"},
          "emile":{"type": "keyword"},
          "address":{"type": "text"}
        }
      }
    }
4.查看映射
    GET /06_mapping/_mapping
5.新增映射字段
    第一个就是先删除索引，然后调整后再新建索引映射，二在已有的基础上新增。
    索引一旦创建，我们是无法修改里边的内容的，不如说修改索引字段的名称。但是我们是可以向索引中添加其他字段的
    PUT /06_mapping/_mapping
    {
      "properties":{
        "sex":{
          "type":"text"
        }
      }
    }
6.删除映射
    delete /06_mapping
7.索引迁移
    创建出正确的索引，然后使用如下的方式来进行数据的迁移
    创建新的索引
    PUT /04_bank_new
    {
      "settings": {
        "number_of_replicas": 1,
        "number_of_shards": 5
      },
      "mappings": {
        "properties": {
          "account_number" :
          {
              "type" : "long"
            },
            "address" : {
              "type" : "text"
            },
            "age" : {
              "type" : "long"
            },
            "balance" : {
              "type" : "long"
            },
            "city" : {
              "type" : "text"
            },
            "email" : {
              "type" : "text"
            },
            "employer" : {
              "type" : "text"
            },
            "firstname" : {
              "type" : "text"
            },
            "gender" : {
              "type" : "text"
            },
            "lastname" : {
              "type" : "text"
            },
            "state" : { # 上面全部索引没有进行改变，只对state索引值从text改变成keyword
              "type" : "keyword"
            }
        }
      }
    }
    # 进行数据的迁移
    POST _reindex
    {
      "source": { # 需要迁移的索引
        "index": "04_bank"
      },
      "dest": { # 迁移目的索引
        "index": "04_bank_new"
      }
    }
    在大数据量的情况，reindex操作不知道效率如何，慎用。
8.常用数据类型
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
"""
