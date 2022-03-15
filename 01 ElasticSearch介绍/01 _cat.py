# -*- coding: utf-8 -*-
# @Time : 2022/2/28 14:29
# @Author : O·N·E
# @File : 01 _cat.py
"""
_cat接口:
    ip:192.168.81.100,192.168.81.101
    1._cat/nodes:查看所有的节点
    因为是集群所以看到2个节点
    2._cat/nodes:查看es节点的健康状况
    3._cat/nodes:查看主节点
    4._cat/indices?v:查看索引值
        health green(集群完整) yellow(单点正常、集群不完整) red(单点不正常)
        status 是否能使用
        index 索引名
        uuid 索引统一编号
        pri 主节点几个
        rep 从节点几个
        docs.count 文档数
        docs.deleted 文档被删了多少
        store.size 整体占空间大小
        pri.store.size 主节点占

"""
