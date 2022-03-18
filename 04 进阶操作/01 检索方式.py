# -*- coding: utf-8 -*-
# @Time : 2022/3/1 11:16
# @Author : O·N·E
# @File : 01 检索方式.py
"""
第一种方式
    GET /04_bank/_search # 检索bank下的所有信息，包括 type 和 docs
    # 检索指定id的指定字段
    GET /04_bank/_doc/995?_source=account_number,balance
    插叙全部的话默认情况下只是会查询出前10条的信息

第二种方式
    通过使用 REST request body 来反射检索参数 (uri+请求体)
    # match_all全部信息
    GET /bank/_search
    {
        "query": { "match_all": {} },
        "sort": [
            { "account_number": "asc" }
        ]
    }

    took ElasticSearch执行搜索的时间(毫秒)
    time_out 搜索是否超时
    _shards 有多少个分片被搜索了，统计成功/失败的搜索分片
    hits 搜索结果
    hits.total 搜索结果统计
    hits.hits 实际的搜索结果数组(默认为前10条文档)
    sort 结果的排序key，没有就按照score排序
    score和max_score 相关性得分和最高分(全文检索使用)

# 查询全部的数据，分类：按照account_number字段进行升序排列
# 默认情况下只会显示前10条的信息


"""
