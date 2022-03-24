# -*- coding: utf-8 -*-
# @Time : 2022/3/3 9:56
# @Author : O·N·E
# @File : 07 聚合函数.py
"""
聚合可以让我们极其方便的实现对数据的统计、分析。es里面的聚合跟sql里面的统计求和最大值分组类似。例如：
    什么品牌的手机最受欢迎？
    这些手机的平均价格、最高价格、最低价格？
    这些手机每月的销售情况如何？
    实现这些统计功能的比数据库的sql要方便的多，而且查询速度非常快，可以实现实时搜索效果。
Elasticsearch中的聚合，包含多种类型，最常用的两种，一个叫 桶 ，一个叫 度量 ：
桶（bucket）
    桶的作用，是按照某种方式对数据进行分组，每一组数据在ES中称为一个桶
    Elasticsearch中提供的划分桶的方式有很多：
    Date Histogram Aggregation：根据日期阶梯分组，例如给定阶梯为周，会自动每周分为一组
    Histogram Aggregation：根据数值阶梯分组，与日期类似
    Terms Aggregation：根据词条内容分组，词条内容完全匹配的为一组
    Range Aggregation：数值和日期的范围分组，指定开始和结束，然后按段分组
bucket aggregations 只负责对数据进行分组，并不进行计算，因此往往bucket中往往会嵌套另一种聚合：metrics aggregations即度量
    度量（metrics）
    分组完成以后，我们一般会对组中的数据进行聚合运算，例如求平均值、最大、最小、求和等，这些在ES中称为度量
比较常用的一些度量聚合方式：
    Avg Aggregation：求平均值
    Max Aggregation：求最大值
    Min Aggregation：求最小值
    Percentiles Aggregation：求百分比
    Stats Aggregation：同时返回avg、max、min、sum、count等
    Sum Aggregation：求和
    Top hits Aggregation：求前几
    Value Count Aggregation：求总数
demo1:搜索address中包含mill的所有人的年龄分布以及平均年龄
    GET /04_bank/_search
    {
      "query": { # 搜索address中包含mill的所有人
        "match": {
          "address": "mill"
        }
      },
      "aggs": { # Aggregation聚合缩写
        "ageAggs": { # 聚合函数名称 自己进行定义即可
          "terms": { # 聚合的类型，进行分组terms
            "field": "age", # 分组的字段
            "size": 10 # 分组的个数 例如100分为10组 每组10个
          }
        },
        "ageavg":{ # 第二个分组名称 平均年龄
          "avg": { # avg聚合函数中求平均
            "field": "age" # 进行分组的字段
          }
        }
      },
      "size": 0 # 不对query查询结果进行输出，方便查看
}
demo2:按照年龄聚合，并且请求这些年龄段的这些人的平均薪资
    GET /04_bank/_search
    {
      "query": { # 查询全部的信息
        "match_all": {}
      },
      "aggs": {
        "ageaggs": { # 按照年龄进行分组，分为50个分组
          "terms": {
            "field": "age",
            "size": 50
          },
          "aggs": { # 在年龄的分组基础上在求每个分组的平均工资，这里使用嵌套。。。
            "blanceavg": {
              "avg": {
                "field": "balance" # 字段为工资
              }
            }
          }
        }
      },
      "size": 0
    }
demo3 查出所有年龄分布，并且这些年龄段中M的平均薪资和F的平均薪资以及这个年龄段的总体平均薪资。
    GET /04_bank/_search
    {
      "query": {
        "match_all": {}
      },
      "aggs": {
        "ageagg": { # 按照年龄进行分组
          "terms": {
            "field": "age",
            "size": 50
          },
          "aggs": {
            "genderagg": { # 嵌套，在年龄组里面在进行性别分组
              "terms": {
                "field": "gender.keyword",
                "size": 10
              },
              "aggs": {
                "blanceavg": { # 同样是嵌套，在上述分组中在求出balance的大小
                  "avg": {
                    "field": "balance"
                  }
                }
              }
            }
          }
        }
      },
      "size": 0
    }
"""