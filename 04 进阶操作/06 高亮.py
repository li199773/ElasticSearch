# -*- coding: utf-8 -*-
# @Time : 2022/3/2 16:57
# @Author : O·N·E
# @File : 06 高亮.py
"""
高亮显示的实现分为两步：
    1）给文档中的所有关键字都添加一个标签，例如<em>标签
    2）页面给<em>标签编写CSS样式
GET /04_bank/_search
    {
      "query": {
        "match": {
          "address": 252
        }
      },
      "highlight": {
        "pre_tags": "<p>",
        "post_tags": "<p>",
        "fields": {
          "address":{}
        }
      }
    }

    高亮是对关键字高亮，因此搜索条件必须带有关键字，而不能是范围这样的查询。
    默认情况下，高亮的字段，必须与搜索指定的字段一致，否则无法高亮
    如果要对非搜索字段高亮，则需要添加一个属性：required_field_match=false
"""
