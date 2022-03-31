# -*- coding: utf-8 -*-
# @Time : 2022/3/9 14:29
# @Author : O·N·E
# @File : 02 自定义词库.py
"""
对于一些常见的信息可以进行中文分词，但是对于一些网络热词并不能进行分词，例如
    GET /_analyze
    {
      "analyzer": "ik_smart",
      "text":"潘嘎之交"
    }
/elasticsearch-8.0.0/plugins/ik/config/IKAnalyzer.cfg.xml 修改即可
        <comment>IK Analyzer 扩展配置</comment>
        <!--用户可以在这里配置自己的扩展字典 -->
        <entry key="ext_dict">wangluo.dic</entry> # 本地修改,在本文件夹下面生成一个.dic即可,然后重启elasticsearch
         <!--用户可以在这里配置自己的扩展停止词字典-->
        <entry key="ext_stopwords"></entry> # 远程修改

"""
