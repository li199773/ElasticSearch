# -*- coding: utf-8 -*-
# @Time : 2022/2/28 15:31
# @Author : O·N·E
# @File : 01 创建文档.py
"""
文档就是database中表的row

提交方式 描述
    PUT 提交的id如果不存在就是新增操作，如果存在就是更新操作，id不能为空
    POST 如果不提供id会自动生成一个id,如果id存在就更新，如果id不存在就新增
    1.创建文档：put
    http://192.168.81.100:9200/02_create_index/_doc/1
    取消了文档类型同意为_doc
    {
    "name":"one",
    "age":24
    }
    2.方式二：post
    http://192.168.81.100:9200/02_create_index/_doc
    不用id号码，系统随机一个id

"""
