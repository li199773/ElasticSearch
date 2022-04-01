# `ElasticSearch+Kibana+Head+ik+Logstash 8.0 Python 3.8`
****
# 一.`ElasticSearch`概述
## 1.`ElasticSearch`介绍 
    ES 是一个开源的高扩展的分布式全文搜索引擎，是整个Elastic Stack技术栈的核心。它可以近乎实时的存储，检索数据；本身扩展性很好，可以扩展到上百台服务器，处理PB级别的数据。
    ElasticSearch的底层是开源库Lucene，但是没办法直接用Lucene，必须自己写代码去调用它的接口，Elastic是Lucene的封装，提供了REST API的操作接口，开箱即用。天然的跨平台。
    全文检索是我们在实际项目开发中最常见的需求了，而ElasticSearch是目前全文检索引擎的首选， 它可以快速的存储，搜索和分析海量的数据，`维基百科，GitHub，Stack Overflow都采用了ElasticSearch`。 
****
## 2.`ElasticSearch`用途
### (1)搜索的数据对象是大量的非结构化的文本数据。
### (2)文件记录达到数十万或数百万个甚至更多。
### (3)支持大量基于交互式文本的查询。
### (4)需求非常灵活的全文搜索查询。
### (5)对高度相关的搜索结果的有特殊需求，但是没有可用的关系数据库可以满足。
### (6)对不同记录类型，非文本数据操作或安全事务处理的需求相对较少的情况。
# 二.系统配置
    Ubuntu：18.04.6 LTS
    ip：192.168.81.100 ,192.168.81.101
****
# 三.`ElasticSearch`配置
## (1)ElasticSearch不能以`root`进行启动，为其添加用户权限。
    sudo chown -R xxx  /usr/local/elasticsearch-8.0.0
## (2)配置`JDK`
    Elasticsearch是使用java开发的，且高版本的ES需要JDK版本1.8以上，默认安装包带有jdk环境，如果系统配置JAVA_HOME，那么使用系统默认的JDK，如果没有配置使用自带的JDK。
    安装包自带JDK配置：
    /usr/local/elasticsearch-8.0.0/bin/elasticsearch-env增加安装包里面JDK即可
    JAVA_HOME="/usr/local/elasticsearch-8.0.0/jdk"
## (3)修改用户拥有的内存权限
    /etc/sysctl.conf文件最后添加一行
    执行sysctl -p使其生效 
## (4)线程数修改
    /etc/security/limits.conf最后一行添加
    执行sysctl -p使其生效
****
# 四.`Kibana`安装
## 1.简介
    Kibana 是一款开源的数据分析和可视化平台，它是 Elastic Stack 成员之一，设计用于和 Elasticsearch 协作。可以使用 Kibana 对 Elasticsearch 索引中的数据进行搜索、查看、交互操作。可以很方便的利用图表、表格及地图对数据进行多元化的分析和呈现。
    Kibana 可以使大数据通俗易懂。它很简单，基于浏览器的界面便快速创建和分享动态数据仪表板来追踪 Elasticsearch 的实时数据变化。
## 2.`Kibana`配置
    详情见pdf文档
****
# 五.`ElasticSearch-Head`安装
## 1.简介
    elasticsearch-head被称为是elasticsearch集群的web前端，head插件主要是用来和elastic Cluster交互的Web前端。
## 2.`ElasticSearch-Head`配置
    ES5以上的版本中安装Elasticsearch-Head必须要安装NodeJs,然后通过NodeJS来启动Head。
****
# 六. `ElasticSearch`操作
### (1) _cat操作
### (2) 索引操作
### (3) 文档操作
### (4) 映射操作
### (5) 高级查询
    1 RESTful
    2 查询所有文档
    3 匹配查询
    4 字段匹配查询
    5 关键字精确查询
    6 范围查询
    7 过滤查询
    8 组合查询
    9 排序查询
    10 分页查询
    11 深度分页
    12 聚合查询
### 详情见`pdf`文件
****
# 七. `ElasticSearch-Head`操作
## 主要包含以下内容：
### 1. 集群健康
### 2. 水平扩容
### 3. 路由计算
### 4. 分片控制
### 5. 写流程
### 6. 读流程
### 7. 更新流程
****
# 八．IK 分词器 
### 所谓的分词就是通过 tokenizer(分词器)将一个字符串拆分为多个独立的 tokens(词元-独立的单词)， 然后输出为 tokens 流的过程。
## 分类：
    1.内置分词器
    2.IK中文分词器
## 自定义词库
    1.本地字典配置
    2.Nginx远程字典配置
********
# 八.Logstash
## 1.简介
    Logstash 主要是用来日志的搜集、分析、过滤日志的工具，支持大量的数据获取方式。一般工作方式为c/s架构，client端安装在需要收集日志的主机上，server端负责将收到的各节点日志进行过滤、修改等操作在一并发往elasticsearch上去。
    logstash从输入源接受数据，直接发送达目的地，或者对数据进行过滤后在传输到目的地。
    主要包括以下内容：
    (1)Input：输入源
    (2)Filter：过滤器
    (3)Output：输出源
## 2.标准输入输出
    logstash启动：
    /usr/local/logstash-8.0.0//logstash -e 'input { stdin {} } output { stdout {} }'
## 3.日志采集
    1 输出到文件
    2 输出到ES
    3 指定文件输出
## 4.过滤器
### 1.rok正则捕获
    过滤ip：
    过滤时间戳：
    过滤报头：
### 2.date插件
### 3.remove_field的用法
### 4.过滤器解析日志存到es
