# -*- coding: utf-8 -*-
# @Time : 2022/3/2 15:07
# @Author : O·N·E
# @File : 04 复合查询.py
"""
复合（compound）查询：复合查询可以将其它简单查询组合起来，实现更复杂的搜索逻辑。常见的有两种：
    fuction score：算分函数查询，可以控制文档相关性算分，控制文档排名
    bool query：布尔查询，利用逻辑关系组合多个其它的查询，实现复杂搜索

1.相关性算分
    当我们利用match查询时，文档结果会根据与搜索词条的关联度打分（_score），返回结果时按照分值降序排列。
    5.1版本升级中，elasticsearch将算法改进为BM25算法
    TF-IDF算法有一各缺陷，就是词条频率越高，文档得分也会越高，单个词条对文档影响较大。而BM25则会让单个词条的算分有一个上限，曲线更加平滑：
elasticsearch会根据词条和文档的相关度做打分，算法由两种：
    TF-IDF算法
    BM25算法，elasticsearch5.1版本后采用的算法
2. filter[结果过滤]
    并不是所有的查询都需要产生分数，特别是那些仅用于"filtering"的文档，为了不计算分数，
    ElasticSearch会自动检查场景并且优化查询的执行
    GET /04_bank/_search
    {
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
                  "gte": 100,
                  "lte": 1032
                }
              }
            }
          ]
        }
      }
    }
3.布尔查询
布尔查询是一个或多个查询子句的组合，每一个子句就是一个子查询。子查询的组合方式有：
    must：必须匹配每个子查询，类似“与”，参与算分
    should：选择性匹配子查询，类似“或”，参与算分
    must_not：必须不匹配，不参与算分，类似“非”
    filter：必须匹配，不参与算分
    GET /04_bank/_search
    {
      "query": {
        "bool": {
          "must": [
            {
              "match": {
                "address": "mail lane"
              }
            }
          ],
          "must_not": [
            {
              "range": {
                "age": {
                  "gte": 10,
                  "lte": 30
                }
              }
            }
          ],
          "filter": [
            {
              "term": {
                "balance"{
                  "value":45975
                }
              }
            }
          ]
        }
      }
    }
"""