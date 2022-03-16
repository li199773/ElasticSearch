# -*- coding: utf-8 -*-
# @Time : 2022/2/28 16:10
# @Author : O·N·E
# @File : 02 文档查询.py
"""
文档查询:get
    1.
    http://192.168.81.100:9200/02_create_index/_doc/1
    {
    "_index": "02_create_index",
    "_id": "1",
    "_version": 6,
    "_seq_no": 5,
    "_primary_term": 1,
    "found": true,
    "_source": {
        "name": "one"
    }
    }
    _index 索引名称
    _id 记录id
    _version 版本号
    _seq_no 并发控制字段，每次更新都会+1，用来实现乐观锁
    _primary_term 同上，主分片重新分配，如重启，就会发生变化
    found 找到结果
    _source 真正的数据内容
    2.乐观锁
    http://192.168.81.100:9200/02_create_index/_doc/1?if_seq_no=5&if_primary_term=1
    ?if_seq_no=5&if_primary_term=1

"""
