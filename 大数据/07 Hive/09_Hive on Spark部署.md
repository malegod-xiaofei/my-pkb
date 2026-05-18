尚硅谷大数据技术之Hive on Spark部署

（作者：尚硅谷研究院）

版本：V1.0

# 1 Hive on Spark配置

- 在Hive所在节点部署Spark纯净版
  - Spark官网下载jar包地址：
  - 上传并解压解压spark-3.1.3-bin-without-hadoop.tgz
[atguigu@hadoop102 software]$ tar -zxvf spark-3.1.3-bin-without-hadoop.tgz -C /opt/module/

[atguigu@hadoop102 software]$ mv /opt/module/spark-3.1.3-bin-hadoop3 /opt/module/spark

  - 修改spark-env.sh配置文件
修改文件名

[atguigu@hadoop102 conf]$ mv /opt/module/spark/conf/spark-env.sh.template /opt/module/spark/conf/spark-env.sh

增加如下内容

export SPARK_DIST_CLASSPATH=$(hadoop classpath)

- 配置SPARK_HOME环境变量
[atguigu@hadoop102 software]$ sudo vim /etc/profile.d/my_env.sh

添加如下内容

# SPARK_HOME

export SPARK_HOME=/opt/module/spark

export PATH=$PATH:$SPARK_HOME/bin

source 使其生效

[atguigu@hadoop102 software]$ source /etc/profile.d/my_env.sh

- 在hive中创建spark配置文件
[atguigu@hadoop102 software]$ vim /opt/module/hive/conf/spark-defaults.conf

添加如下内容（在执行任务时，会根据如下参数执行）

spark.master                               yarn

spark.eventLog.enabled                   true

spark.eventLog.dir                        hdfs://hadoop102:8020/spark-history

spark.executor.memory                    1g

spark.driver.memory   1g

在HDFS创建如下路径，用于存储历史日志

[atguigu@hadoop102 software]$ hadoop fs -mkdir /spark-history

- 向HDFS上传Spark纯净版jar包
说明1：采用Spark纯净版jar包，不包含hadoop和hive相关依赖，能避免依赖冲突。

说明2：Hive任务最终由Spark来执行，Spark任务资源分配由Yarn来调度，该任务有可能被分配到集群的任何一个节点。所以需要将Spark的依赖上传到HDFS集群路径，这样集群中任何一个节点都能获取到。

[atguigu@hadoop102 software]$ hadoop fs -mkdir /spark-jars

[atguigu@hadoop102 software]$ hadoop fs -put /opt/module/spark/jars/* /spark-jars

- 修改hive-site.xml文件
[atguigu@hadoop102 ~]$ vim /opt/module/hive/conf/hive-site.xml

添加如下内容

<!--Spark依赖位置（注意：端口号8020必须和namenode的端口号一致）-->

<property>

<name>spark.yarn.jars</name>

<value>hdfs://hadoop102:8020/spark-jars/*</value>

</property>

<!--Hive执行引擎-->

<property>

<name>hive.execution.engine</name>

<value>spark</value>

</property>
