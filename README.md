# `ElasticSearch+Kibana+Head+ik+Logstash 8.0 Python 3.8`
****
# 一.`ElasticSearch`概述
## 1.`ElasticSearch`介绍 
### ES 是一个开源的高扩展的分布式全文搜索引擎，是整个Elastic Stack技术栈的核心。它可以近乎实时的存储，检索数据；本身扩展性很好，可以扩展到上百台服务器，处理PB级别的数据。
### ElasticSearch的底层是开源库Lucene，但是没办法直接用Lucene，必须自己写代码去调用它的接口，Elastic是Lucene的封装，提供了REST API的操作接口，开箱即用。天然的跨平台。
### 全文检索是我们在实际项目开发中最常见的需求了，而ElasticSearch是目前全文检索引擎的首选， 它可以快速的存储，搜索和分析海量的数据，`维基百科，GitHub，Stack Overflow都采用了ElasticSearch`。 
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
# 三.`ElasticSearch`配置
## (1)ElasticSearch不能以root进行启动，为其添加用户权限。
    sudo chown -R xxx  /usr/local/elasticsearch-8.0.0
## (2)配置JDK
    Elasticsearch是使用java开发的，且高版本的ES需要JDK版本1.8以上，默认安装包带有jdk环境，如果系统配置JAVA_HOME，那么使用系统默认的JDK，如果没有配置使用自带的JDK。
    安装包自带JDK配置：
    /usr/local/elasticsearch-8.0.0/bin/elasticsearch-env增加安装包里面JDK即可
## (3)修改用户拥有的内存权限
    /etc/sysctl.conf文件最后添加一行
    执行sysctl -p使其生效 
## (4)线程数修改
    /etc/security/limits.conf最后一行添加
    执行sysctl -p使其生效
