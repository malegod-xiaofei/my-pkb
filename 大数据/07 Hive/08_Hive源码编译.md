尚硅谷大数据技术之Hive源码编译

（作者：尚硅谷研究院）

版本：V1.0+

# 1 部署Hadoop和Hive

## 1.1 版本选择

## 1.2 Hadoop部署

### 1.2.1 集群规划

### 1.2.2 集群安装

## 1.3 Hive部署

### 1.3.1 集群规划

### 1.3.2 Hive安装

## 1.4 测试

### 1.4.1 测试Hadoop

- 启动Hadoop
[atguigu@hadoop102 ~]$ start-dfs.sh

[atguigu@hadoop103 ~]$ start-yarn.sh

- 运行Hadoop自带的测试任务
[atguigu@hadoop102 ~]$ hadoop jar /opt/module/hadoop-3.1.3/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.3.jar pi 1 1

### 1.4.2 测试Hive

- 启动Hive CLI客户端
[atguigu@hadoop102 ~]$ hive

此时控制台会出现如下报错信息：

java.lang.NoSuchMethodError: com.google.common.base.Preconditions.checkArgument(ZLjava/lang/String;Ljava/lang/Object;)V

# 2 Hadoop和Hive的兼容性问题

## 2.1 问题原因

上述问题是由Hadoop3.1.3版本所依赖的guava-27.0-jre和Hive-3.1.3版本所依赖的guava-19.0不兼容所致。

## 2.2 解决思路

- 更换Hadoop版本
经过观察发现，Hadoop-3.1.0，Hadoop-3.1.1，Hadoop-3.1.2版本的guava依赖均为guava-11.0.2，而到了Hadoop-3.1.3版本，guava依赖的版本突然升级到了guava-27.0-jre。

Hive-3的所有发行版本的guava依赖均为guava-19.0。

而guava-19.0和guava-11.0.2版本是兼容的，所以理论上降低Hadoop版本，这个问题就能得到有效的解决。

- 升级Hive-3.1.3中的guava依赖版本，并重新编译Hive
若将Hive-3.1.3中的guava依赖版本升级到guava-27.0-jre，这样就能避免不同版本的guava依赖冲突，上述问题同样能得到解决。

## 2.3 解决实操

此处，我们选择升级Hive-3.1.3中的guava依赖版本，所以我们需要拉取Hive源码进行修改并重新编译。由于Hive源码的编译工作需要在Linux系统中进行，同时我们需要修改Hive的源码，所以我们需要一个合适的操作环境。

### 2.3.1 搭建编译环境

- 虚拟机准备
准备一台虚拟机，并安装Centos7.5系统（带桌面环境）。

- 安装JDK
  - 卸载现有JDK
[atguigu@hadoop100 opt]# sudo rpm -qa | grep -i java | xargs -n1 sudo rpm -e --nodeps

  - 将JDK上传到虚拟机的/opt/software文件夹下面
  - 解压JDK到/opt/module目录下
[atguigu@hadoop100 software]# tar -zxvf jdk-8u212-linux-x64.tar.gz -C /opt/module/

  - 配置JDK环境变量
    - 新建/etc/profile.d/my_env.sh文件
[atguigu@hadoop100 module]# sudo vim /etc/profile.d/my_env.sh

添加如下内容，然后保存（:wq）退出

#JAVA_HOME

export JAVA_HOME=/opt/module/jdk1.8.0_212

export PATH=$PATH:$JAVA_HOME/bin

让环境变量生效

[atguigu@hadoop100 software]$ source /etc/profile.d/my_env.sh

  - 测试JDK是否安装成功
[atguigu@hadoop100 module]# java -version

如果能看到以下结果，则Java正常安装

java version "1.8.0_212"

- 安装Maven
  - 将Maven安装包上传到虚拟机/opt/software目录
  - 解压Maven到/opt/module目录下
[atguigu@hadoop100 software]$ tar -zxvf apache-maven-3.6.3-bin.tar.gz -C /opt/module/

  - 配置Maven环境变量
    - 编辑/etc/profile.d/my_env.sh文件
[atguigu@hadoop100 module]$ sudo vim /etc/profile.d/my_env.sh

追加以下内容

# MAVEN_HOME

export MAVEN_HOME=/opt/module/apache-maven-3.6.3

export PATH=$PATH:$MAVEN_HOME/bin

让环境变量生效

[atguigu@hadoop100 software]$ source /etc/profile.d/my_env.sh

  - 检测Maven是否安装成功
[atguigu@hadoop100 module]$ mvn -version

如果能看到以下结果，则Maven正常安装

Apache Maven 3.6.3 (cecedd343002696d0abb50b32b541b8a6ba2883f)

Maven home: /opt/module/apache-maven-3.6.3

Java version: 1.8.0_212, vendor: Oracle Corporation, runtime: /opt/module/jdk1.8.0_212/jre

Default locale: zh_CN, platform encoding: UTF-8

OS name: "linux", version: "3.10.0-862.el7.x86_64", arch: "amd64", family: "unix"

  - 配置仓库镜像
    - 修改Maven配置文件
[atguigu@hadoop100 ~]$ vim /opt/module/apache-maven-3.6.3/conf/settings.xml

    - 在<mirrors></mirrors>节点中增加以下内容
<mirror>

<id>aliyunmaven</id>

<mirrorOf>central</mirrorOf>

<name>阿里云公共仓库</name>

<url>https://maven.aliyun.com/repository/public</url>

</mirror>

- 安装Git
  - 安装第三方仓库
[atguigu@hadoop100 ~]$ sudo yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

  - 安装Git
[atguigu@hadoop100 ~]$ sudo yum install -y git236

- 安装IDEA
  - 将IDEA安装包上传到虚拟机/opt/software目录
  - 解压IDEA到/opt/module目录下
[atguigu@hadoop100 software]$ tar -zxvf ideaIU-2021.1.3.tar.gz -C /opt/module/

  - 启动IDEA（在图形化界面启动）
[atguigu@hadoop100 ~]$ nohup /opt/module/idea-IU-211.7628.21/bin/idea.sh 1>/dev/null 2>&1 &

  - 配置Maven
![图片106.png](images/图片106.png)

![图片107.png](images/图片107.png)

### 2.3.2 修改并编译Hive源码

- 在IDEA中新建项目拉取Hive源码
Hive源码的远程仓库地址：

国内镜像地址：

- 测试编译环境
在修改依赖和代码之前，先测试一下打包是否能成功，用来检测环境是否正常。

  - 打开终端
![图片108.png](images/图片108.png)

  - 输入打包命令
mvn clean package -Pdist -DskipTests -Dmaven.javadoc.skip=true

![图片109.png](images/图片109.png)

注：打包命令参考官网

打包成功的标志如下：

![图片110.png](images/图片110.png)

  - 修改Maven父工程的pom.xml文件中的guava.version参数
将

<guava.version>19.0</guava.version>

改为

<guava.version>27.0-jre</guava.version>

  - 重新执行Hive的编译打包命令，并根据错误提示修改代码
mvn clean package -Pdist -DskipTests -Dmaven.javadoc.skip=true

  - 反复执行上一步骤，直至编译打包成功
注：以下文件是根据修改guava版本的相关内容制作的补丁，可应用该补丁快速修改代码。

![图片111.png](images/图片111.png)

## 2.4 测试

将重新编译得到的Hive-3.1.3安装包上传到测试集群，替换安装的Hive。重新进行测试。

# 3 Hive插入数据StatsTask失败问题

## 3.1 插入数据测试

- 启动hive客户端
[atguigu@hadoop102 hive]$ bin/hive

- 创建一张测试表
hive (default)> create table student(id int, name string);

- 执行insert语句
hive (default)> insert into table student values(1,'abc');

测试发现过程发现如下错误信息：

FAILED: Execution Error, return code 1 from org.apache.hadoop.hive.ql.exec.StatsTask

## 3.2 问题原因

上述问题是由Hive自身存在的bug所致，bug详情可参照以下连接

。

## 3.3 解决思路

经过观察，该bug已经在3.2.0, 4.0.0, 4.0.0-alpha-1等版本修复了，所以可以参考修复问题的PR，再修改Hive源码并重新编译。

## 3.4 解决实操

- 根据修复bug的相关内容制作补丁
补丁文件如下：

![图片112.png](images/图片112.png)

- 应用该补丁
- 重新执行编译打包命令
mvn clean package -Pdist -DskipTests -Dmaven.javadoc.skip=true

## 3.5 测试

将重新编译得到的Hive-3.1.3安装包上传到测试集群，替换安装的Hive。重新进行测试。

# 4 Hive on Spark部署

## 4.1 版本选择

## 4.2 Hive on Spark配置

# 5 测试

- 启动hive客户端
[atguigu@hadoop102 hive]$ bin/hive

- 执行insert语句
hive (default)> insert into table student values(1,'abc');

测试发现过程发现如下错误信息：

Job failed with java.lang.NoSuchMethodError: org.apache.spark.api.java.JavaSparkContext.accumulator(Ljava/lang/Object;Ljava/lang/String;Lorg/apache/spark/AccumulatorParam;)Lorg/apache/spark/Accumulator;

# 6 Hive和Spark兼容性问题

## 6.1 问题原因

上述问题是由Hive-3.1.3版本和Spark-3.1.3版本不兼容所致。

## 6.2 解决思路

- 降低Spark版本
经过观察发现Hive-3.1.3，版本所兼容的Spark版本为Spark-2.3.0，故降低Spark版本便可有效解决该问题。

- 升级Hive-3.1.3中的Spark依赖版本至Spark-3.1.3，并重新编译Hive
将Hive源码中的Spark依赖版本升级为Spark-3.1.3，并修改源码，重新编译打包后，同样能解决该问题。

## 6.3 解决实操

此处，我们选择第二种方案。

- 修改Hive项目的pom.xml文件，将spark依赖的版本改为3.1.3
将

<spark.version>2.3.0</spark.version>

<scala.binary.version>2.11</scala.binary.version>

<scala.version>2.11.8</scala.version>

改为

<spark.version>3.1.3</spark.version>

<scala.binary.version>2.12</scala.binary.version>

<scala.version>2.12.10</scala.version>

- 重新执行打包命令，根据错误提示修改源码。
- 反复执行步骤2），直至打包成功。
注：以下文件是根据修改Spark版本的相关内容制作的补丁，可应用该补丁快速修改代码。

![图片113.png](images/图片113.png)

## 6.4 测试

将重新编译得到的Hive-3.1.3安装包上传到测试集群，替换安装的Hive。重新进行测试。
