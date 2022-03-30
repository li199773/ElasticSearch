# -*- coding: utf-8 -*-
# @Time : 2022/3/3 16:06
# @Author : O·N·E
# @File : 01 分词操作.py
"""
所谓的分词就是通过tokenizer(分词器)将一个字符串拆分为多个独立的tokens(词元-独立的单词)，然后输出为tokens流的过程。
例如"my name is HanMeiMei"这样一个字符串就会被默认的分词器拆分为[my,name,isHanMeiMei].ElasticSearch中提供了很多默认的分词器
demo1 英文分词效果很好
    POST /_analyze
    {
      "analyzer": "standard",
      "text": "My name is one is"
    }
demo2 中文分词效果很差
    POST /_analyze
    {
      "analyzer": "standard",
      "text": "我的名字是张三"
    }

ik分词器安装:ik_samrt
    1.https://github.com/medcl/elasticsearch-analysis-ik/releases找到自己elasticrearch的版本号、
    2.elasticsearch-analysis-ik-8.0.0.zip 在/elasticsearch-8.0.0/plugins/ik 解压即可
    3.elasticsearch -list 查看是否安装成功

    主要字典以.dic后缀结尾

    POST /_analyze
    {
      "analyzer": "ik_smart",
      "text": "我是中国人，我热爱我的祖国"
    }
    切词之后[我 是 中国人 我 热 爱我 的 祖国]

自定义mapping分词器：中文切词还是有些不符合句式
    POST /07_ik/_bulk
    {"index":{"_id":"1"}}
    {"text":"我爱双截棍"}
    {"index":{"_id":"2"}}
    {"text":"我爱双棍"}

    GET /07_ik/_search
    {
    "query": {
    "match": {
      "text": "双截棍"
    }
    }
    }
    发现查找之后还是按照默认stand进行分词的
    删除索引(已经确定的索引值是没有办法进行更改的),建立索引时对分词进行赋值

    PUT /07_ik
    {
    "settings":{
        "number_of_shards":5,
        "number_of_replicas":1
    },
    "mappings": {
    "properties": {
      "text":{
        "type": "text",
        "analyzer": "ik_smart" # "analyzer"分析器 使用 ik_smasrt
      }
    }
    }
    }

    # 再次使用查询只能查出一条信息
    POST /07_ik/_bulk
    {"index":{"_id":"1"}}
    {"text":"我爱双截棍"}
    {"index":{"_id":"2"}}
    {"text":"我爱双棍"}

    GET /07_ik/_search
    {
    "query": {
    "match": {
      "text": "双截棍"
    }
    }
    }
"""
