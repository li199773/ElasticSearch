# -*- coding: utf-8 -*-
# @Time : 2022/3/10 14:26
# @Author : O·N·E
# @File : 01 logstash日志信息.py
"""
/usr/local/logstash-8.0.0/ 新建my文件夹
    下载mysql-connector-java-8.0.28驱动

启动:/usr/local/logstash-8.0.0/
    ./logstash -e 'input { stdin {} } output { stdout {} }'
    一般不会这样子进行启动 需要写的配置太多，放到脚本即可
标准的配置文件：
    包含：input{},filter{},output{}三部分

logstash采集日志信息传入es和控制台(单节点操作)
    ./logstash -e 'input { stdin {} } output { stdout {} elasticsearch{hosts=>["192.168.81.100:9200"]}}'
    文件名称会按照时间进行建立.ds-logs-generic-default-2022.03.11-000001
    (多节点操作)

"""
