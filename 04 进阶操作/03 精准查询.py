# -*- coding: utf-8 -*-
# @Time : 2022/3/2 14:48
# @Author : O·N·E
# @File : 03 精准查询.py
"""
精确查询一般是查找keyword、数值、日期、boolean等类型字段。所以不会对搜索条件分词。常见的有：
    term：根据词条精确值查询
    range：根据值的范围查询

term 查询
    因为精确查询的字段搜是不分词的字段，因此查询的条件也必须是不分词的词条。查询时，用户输入的内容跟自动值完全匹配时才认为
    符合条件。如果用户输入的内容过多，反而搜索不到数据。
    GET /04_bank/_search
    {
      "query": {
        "term": {
          "balance": {
            "value": 17803
          }
        }
      }
    }
range 查询，一般应用在对数值类型做范围过滤的时候。比如做价格范围过滤。
    "gte": 10, // 这里的gte代表大于等于，gt则代表大于
    "lte": 20 // lte代表小于等于，lt则代表小于
    GET /04_bank/_search
    {
      "query": {
        "range": {
          "account_number": {
            "gte": 995,
            "lte": 1000
          }
        }
      },
      "sort": [
        {
          "account_number": {
            "order": "asc"
          }
        }
      ]
    }
"""
