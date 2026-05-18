尚硅谷大数据技术之Spark入门

（作者：尚硅谷研究院）

版本：V5.0

# 1 Spark概述

## 1.1 什么是Spark

回顾：Hadoop主要解决，海量数据的存储和海量数据的分析计算。

Spark是一种基于内存的快速、通用、可扩展的大数据分析计算引擎。

## 1.2 Hadoop与Spark历史

![图片1.png](images/图片1.png)

![图片2.png](images/图片2.png)

Hadoop的Yarn框架比Spark框架诞生的晚，所以Spark自己也设计了一套资源调度框架。

## 1.3 Hadoop与Spark框架对比

![图片3.png](images/图片3.png)

## 1.4 Spark内置模块

![图片4.png](images/图片4.png)

Spark Core：实现了Spark的基本功能，包含任务调度、内存管理、错误恢复、与存储系统交互等模块。Spark Core中还包含了对弹性分布式数据集(Resilient Distributed DataSet，简称RDD)的API定义。

Spark SQL：是Spark用来操作结构化数据的程序包。通过Spark SQL，我们可以使用 SQL或者Apache Hive版本的HQL来查询数据。Spark SQL支持多种数据源，比如Hive表、Parquet以及JSON等。

Spark Streaming：是Spark提供的对实时数据进行流式计算的组件。提供了用来操作数据流的API，并且与Spark Core中的 RDD API高度对应。

Spark MLlib：提供常见的机器学习功能的程序库。包括分类、回归、聚类、协同过滤等，还提供了模型评估、数据 导入等额外的支持功能。

Spark GraphX：主要用于图形并行计算和图挖掘系统的组件。

集群管理器：Spark设计为可以高效地在一个计算节点到数千个计算节点之间伸缩计算。为了实现这样的要求，同时获得最大灵活性，Spark支持在各种集群管理器（Cluster Manager）上运行，包括Hadoop YARN、Apache Mesos，以及Spark自带的一个简易调度器，叫作独立调度器。

Spark得到了众多大数据公司的支持，这些公司包括Hortonworks、IBM、Intel、Cloudera、MapR、Pivotal、百度、阿里、腾讯、京东、携程、优酷土豆。当前百度的Spark已应用于大搜索、直达号、百度大数据等业务；阿里利用GraphX构建了大规模的图计算和图挖掘系统，实现了很多生产系统的推荐算法；腾讯Spark集群达到8000台的规模，是当前已知的世界上最大的Spark集群。

## 1.5 Spark特点

![图片5.png](images/图片5.png)

# 2 Spark 运行模式

部署Spark集群大体上分为两种模式：单机模式与集群模式

大多数分布式框架都支持单机模式，方便开发者调试框架的运行环境。但是在生产环境中，并不会使用单机模式。因此，后续直接按照集群模式部署Spark集群。

下面详细列举了Spark目前支持的部署模式。

- Local模式：在本地部署单个Spark服务
- Standalone模式：Spark自带的任务调度模式。（国内不常用）
- YARN模式：Spark使用Hadoop的YARN组件进行资源与任务调度。（国内最常用）
- Mesos模式：Spark使用Mesos平台进行资源与任务的调度。（国内很少用）
## 2.1 Spark安装地址

- 官网地址：
- 文档查看地址：
- 下载地址：
htt

## 2.2 Local模式

Local模式就是运行在一台计算机上的模式，通常就是用于在本机上练手和测试。

### 2.2.1 安装使用

- 上传并解压Spark安装包
[atguigu@hadoop102 sorfware]$ tar -zxvf spark-3.3.1-bin-hadoop3.tgz -C /opt/module/

[atguigu@hadoop102 module]$ mv spark-3.3.1-bin-hadoop3 spark-local

- 官方求PI案例
[atguigu@hadoop102 spark-local]$ bin/spark-submit \

--class org.apache.spark.examples.SparkPi \

--master local[2] \

./examples/jars/spark-examples_2.12-3.3.1.jar \

10

可以查看spark-submit所有参数：

[atguigu@hadoop102 spark-local]$ bin/spark-submit

- --class：表示要执行程序的主类；
- --master local[2]
  - local: 没有指定线程数，则所有计算都运行在一个线程当中，没有任何并行计算
  - local[K]:指定使用K个Core来运行计算，比如local[2]就是运行2个Core来执行
20/09/20 09:30:53 INFO TaskSetManager:

20/09/15 10:15:00 INFO Executor: Running task 1.0 in stage 0.0 (TID 1)

20/09/15 10:15:00 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)

  - local[*]：默认模式。自动帮你按照CPU最多核来设置线程数。比如CPU有8核，Spark帮你自动设置8个线程计算。
20/09/20 09:30:53 INFO TaskSetManager:

20/09/15 10:15:58 INFO Executor: Running task 1.0 in stage 0.0 (TID 1)

20/09/15 10:15:58 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)

20/09/15 10:15:58 INFO Executor: Running task 2.0 in stage 0.0 (TID 2)

20/09/15 10:15:58 INFO Executor: Running task 4.0 in stage 0.0 (TID 4)

20/09/15 10:15:58 INFO Executor: Running task 3.0 in stage 0.0 (TID 3)

20/09/15 10:15:58 INFO Executor: Running task 5.0 in stage 0.0 (TID 5)

20/09/15 10:15:59 INFO Executor: Running task 7.0 in stage 0.0 (TID 7)

20/09/15 10:15:59 INFO Executor: Running task 6.0 in stage 0.0 (TID 6)

- spark-examples_2.12-3.3.1.jar：要运行的程序；
- 10：要运行程序的输入参数（计算圆周率π的次数，计算次数越多，准确率越高）；
- 结果展示
该算法是利用蒙特·卡罗算法求PI。

![图片6.png](images/图片6.png)

### 2.2.2 查看任务运行详情

- 再次运行求PI任务，增加任务次数
[atguigu@hadoop102 spark-local]$ bin/spark-submit \

--class org.apache.spark.examples.SparkPi \

--master local[2] \

./examples/jars/spark-examples_2.12-3.3.1.jar \

1000

- 在任务运行还没有完成时，可登录hadoop102:4040查看程序运行结果
![图片7.png](images/图片7.png)

## 2.3 Yarn模式（重点）

Spark客户端直接连接Yarn

### 2.3.1 安装使用

- 解压spark
[atguigu@hadoop102 software]$ tar -zxvf spark-3.3.1-bin-hadoop3.tgz -C /opt/module/

- 进入到/opt/module目录，修改spark-3.3.1-bin-hadoop3名称为spark-yarn
[atguigu@hadoop102 module]$ mv spark-3.3.1-bin-hadoop3/ spark-3.3.1

- 修改hadoop配置文件/opt/module/hadoop-3.1.3/etc/hadoop/yarn-site.xml，添加如下内容
因为测试环境虚拟机内存较少，防止执行过程进行被意外杀死，做如下配置

[atguigu@hadoop102 hadoop]$ vim yarn-site.xml

<!--是否启动一个线程检查每个任务正使用的物理内存量，如果任务超出分配值，则直接将其杀掉，默认是true -->

<property>

<name>yarn.nodemanager.pmem-check-enabled</name>

<value>false</value>

</property>

<!--是否启动一个线程检查每个任务正使用的虚拟内存量，如果任务超出分配值，则直接将其杀掉，默认是true -->

<property>

<name>yarn.nodemanager.vmem-check-enabled</name>

<value>false</value>

</property>

- 分发配置文件
[atguigu@hadoop102 conf]$ xsync /opt/module/hadoop-3.1.3/etc/hadoop/yarn-site.xml

- 修改/opt/module/spark-yarn/conf/spark-env.sh，添加YARN_CONF_DIR配置，保证后续运行任务的路径都变成集群路径
[atguigu@hadoop102 conf]$ mv spark-env.sh.template spark-env.sh

[atguigu@hadoop102 conf]$ vim spark-env.sh

YARN_CONF_DIR=/opt/module/hadoop-3.1.3/etc/hadoop

- 启动HDFS以及YARN集群
[atguigu@hadoop102 hadoop-3.3.1]$ sbin/start-dfs.sh

[atguigu@hadoop103 hadoop-3.3.1]$ sbin/start-yarn.sh

- 执行一个程序
[atguigu@hadoop102 spark-yarn]$ bin/spark-submit \

--class org.apache.spark.examples.SparkPi \

--master yarn \

./examples/jars/spark-examples_2.12-3.3.1.jar \

10

参数：--master yarn，表示Yarn方式运行；--deploy-mode表示客户端方式运行程序

- 查看hadoop103:8088页面，点击History，查看历史页面
思考：目前是Hadoop的作业运行日志展示，如果想获取Spark的作业运行日志，怎么办？

![图片8.png](images/图片8.png)

### 2.3.2 配置历史服务

由于是重新解压的Spark压缩文件，所以需要针对Yarn模式，再次配置一下历史服务器。

- 修改spark-default.conf.template名称
[atguigu@hadoop102 conf]$ mv spark-defaults.conf.template spark-defaults.conf

- 修改spark-default.conf文件，配置日志存储路径（写）
[atguigu@hadoop102 conf]$ vim spark-defaults.conf

spark.eventLog.enabled             true

spark.eventLog.dir                 hdfs://hadoop102:8020/directory

- 修改spark-env.sh文件，添加如下配置：
[atguigu@hadoop102 conf]$ vim spark-env.sh

export SPARK_HISTORY_OPTS="

-Dspark.history.ui.port=18080

-Dspark.history.fs.logDirectory=hdfs://hadoop102:8020/directory

-Dspark.history.retainedApplications=30"

# 参数1含义：WEBUI访问的端口号为18080

# 参数2含义：指定历史服务器日志存储路径（读）

# 参数3含义：指定保存Application历史记录的个数，如果超过这个值，旧的应用程序信息将被删除，这个是内存中的应用数，而不是页面上显示的应用数。

### 2.3.3 配置查看历史日志

为了能从Yarn上关联到Spark历史服务器，需要配置spark历史服务器关联路径。

目的：点击yarn（8088）上spark任务的history按钮，进入的是spark历史服务器（18080），而不再是yarn历史服务器（19888）。

- 修改配置文件/opt/module/spark-yarn/conf/spark-defaults.conf
添加如下内容：

spark.yarn.historyServer.address=hadoop102:18080

spark.history.ui.port=18080

- 重启Spark历史服务
[atguigu@hadoop102 spark-yarn]$ sbin/stop-history-server.sh

[atguigu@hadoop102 spark-yarn]$ sbin/start-history-server.sh

- 提交任务到Yarn执行
[atguigu@hadoop102 spark-yarn]$ bin/spark-submit \

--class org.apache.spark.examples.SparkPi \

--master yarn \

./examples/jars/spark-examples_2.12-3.3.1.jar \

10

- Web页面查看日志：http://hadoop103:8088/cluster
![图片9.png](images/图片9.png)

点击“history”跳转到http://hadoop102:18080/

![图片10.png](images/图片10.png)

### 2.3.4 运行流程

Spark有yarn-client和yarn-cluster两种模式，主要区别在于：Driver程序的运行节点。

yarn-client：Driver程序运行在客户端，适用于交互、调试，希望立即看到app的输出。

yarn-cluster：Driver程序运行在由ResourceManager启动的APPMaster，适用于生产环境。

- 客户端模式（默认）
[atguigu@hadoop102 spark-yarn]$ bin/spark-submit \

--class org.apache.spark.examples.SparkPi \

--master yarn \

--deploy-mode client \

./examples/jars/spark-examples_2.12-3.3.1.jar \

10

![图片11.png](images/图片11.png)

- 集群模式
[atguigu@hadoop102 spark-yarn]$ bin/spark-submit \

--class org.apache.spark.examples.SparkPi \

--master yarn \

--deploy-mode cluster \

./examples/jars/spark-examples_2.12-3.3.1.jar \

10

  - 查看http://hadoop103:8088/cluster页面，点击History按钮，跳转到历史详情页面
![图片12.png](images/图片12.png)

  - http://hadoop102:18080点击Executors->点击driver中的stdout
![图片13.png](images/图片13.png)

![图片14.png](images/图片14.png)

![图片15.png](images/图片15.png)

注意：如果在yarn日志端无法查看到具体的日志，则在yarn-site.xml中添加如下配置并启动Yarn历史服务器

![图片16.png](images/图片16.png)

<property>

<name>yarn.log.server.url</name>

<value>http://hadoop102:19888/jobhistory/logs</value>

</property>

注意：hadoop历史服务器也要启动 mr-jobhistory-daemon.sh start historyserver

![图片17.png](images/图片17.png)

## 2.4 Standalone模式（了解）

Standalone模式是Spark自带的资源调度引擎，构建一个由Master + Worker构成的Spark集群，Spark运行在集群中。

这个要和Hadoop中的Standalone区别开来。这里的Standalone是指只用Spark来搭建一个集群，不需要借助Hadoop的Yarn和Mesos等其他框架。

## 2.5 Mesos模式（了解）

Spark客户端直接连接Mesos；不需要额外构建Spark集群。国内应用比较少，更多的是运用Yarn调度。

## 2.6 几种模式对比

## 2.7 端口号总结

- Spark查看当前Spark-shell运行任务情况端口号：4040
- Spark历史服务器端口号：18080（类比于Hadoop历史服务器端口号：19888）