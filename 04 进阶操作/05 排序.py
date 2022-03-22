# -*- coding: utf-8 -*-
# @Time : 2022/3/2 15:51
# @Author : O·N·E
# @File : 05 排序.py
"""
排序：
    elasticsearch默认是根据相关度算分（_score）来排序，但是也支持自定义方式对搜索结果排序。可以排序字段类型有：keyword类型、数值类型、地理坐标类型、日期类型等。
    GET /04_bank/_search
    {
      "query": {
        "match_all": {}
      },
      "sort": [
        {
          "age": {
            "order": "desc" # 先按照age进行降序排列
          },
          "account_number": {
            "order": "asc" # age相同情况下按照序号升序排列
          }
        }
      ]
    }
"""
