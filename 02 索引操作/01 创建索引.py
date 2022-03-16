# -*- coding: utf-8 -*-
# @Time : 2022/2/28 14:59
# @Author : O·N·E
# @File : 01 创建索引.py
"""
    elasticsearch 索引相当于mysql里面的database
    1.索引的创建:put
    http://192.168.81.100:9200/02_create_index
    {
        "settings":{
            "number_of_shards": 5, # 分片为5
            "number_of_replicas": 2 # 副本为2
        }
    }
    postman格式为put json格式的数据
    创建02_create_index索引值
    出现以下表示创建成功
    {
        "acknowledged": true,
        "shards_acknowledged": true,
        "index": "02_create_index"
    }
    2.查看索引值:get
    http://192.168.81.100:9200/02_create_index
    "02_create_index": {
        "aliases": {},
        "mappings": {},
        "settings": {
            "index": {
                "routing": {
                    "allocation": {
                        "include": {
                            "_tier_preference": "data_content"
                        }
                    }
                },
                "number_of_shards": "5",
                "provided_name": "02_create_index",
                "creation_date": "1646032485405",
                "number_of_replicas": "1",
                "uuid": "_RrB5TFnQb2rRDBN-I8OBw",
                "version": {
                    "created": "8000099"
                    }
                }
            }
        }
    }
    会显示以上的信息
    或者使用http:192.168.81.100:9200/*
    3.删除索引 delete
    http://192.168.81.100:9200/
    显示以下即为成功
    {
    "acknowledged": true
    }
"""
