# -*- coding: utf-8 -*-
# @Time : 2022/3/2 10:23
# @Author : O·N·E
# @File : 02 检索练习.py
"""
# demo1
# 搜索特定的字段，可以使用匹配查询。如下所示，请求搜索地址字段以查询地址中包含 mill 或 lane 的客户
    GET /bank/_search
    {
        "query": { "match": { "address": "mill lane" } }
    }
# 搜索指定字段进行匹配:(match 和 match_phrase 的区别就像是 or 和 and 的区别) 如图所示：在请求中查询地址中同时包含 mill 和 lane 的客户
    GET /bank/_search
    {
        "query": { "match_phrase": { "address": "929 Eldert Lane" } }
    }

# demo2
# 构造更复杂的查询，可以使用布尔查询来组合多个查询条件，must match、should match、must not match
# 请求在银行索引里搜索年龄是 40 的，但不居住在爱达荷州 (ID) 的客户：
    GET /04_bank/_search
    {
      "query": {
        "bool": {
          "must": [
            {"match": {
              "age": "40"
            }}
          ],
          "must_not": [
            {"match": {
              "state": "ID"
            }}
          ]
        }
      }
    }
# 布尔查询中每个 must，should,must_not 都被称为查询子句。每个
# must 或者 should 查询子句中的条件都会影响文档的相关得分。得分越高，文档跟搜索条件匹配得越好。默认情况下，Elasticsearch 返回的文档会根据相关性算分倒序排列。

# demo3
# multi_match查询：多字段查询，任意一个字段符合条件就算符合查询条件
    GET /04_bank/_search
    {
      "query":  {
      "multi_match":{
        "query":"Lucy",
        "fields":["firstname","email"]
        }
      }
    }
"""
