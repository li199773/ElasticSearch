# -*- coding: utf-8 -*-
# @Time : 2022/2/28 16:53
# @Author : O·N·E
# @File : 04 批量操作.py
"""
_bulk:批量操作
操作类型：
    create 如果文档不存在就创建，但如果文档存在就返回错误
    index 如果文档不存在就创建，如果文档存在就更新
    update 更新一个文档，如果文档不存在就返回错误
    delete 删除一个文档，如果要删除的文档id不存在，就返回错误

    POST /02_create_index/_bulk
    语法操作:post
    {"index":{"_id":"2"}}
    {"name":"two"}
使用kibana

    demo练习
    POST /_bulk # 直接进行批量操作 不用指定特定的index
    {"delete":{"_index":"03_doc_operation","_id":"100"}}
    {"create":{"_index":"03_doc_operation","_id":"100"}}
    {"title":"_bulk demo ..."}
    {"index":{"_index":"03_doc_operation"}}
    {"title":"_bulk demo..."}
    {"update":{"_index":"03_doc_operation","_id":"123"}}
    {"doc":{"title":"My updated demo post ..."}}

    delete 不存在显示not_found
"""
