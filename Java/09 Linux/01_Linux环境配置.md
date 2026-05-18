- Linux下目录管理
- / 根目录，Linux文件系统的最顶层目录，所有其他目录和文件都位于此目录下
- /bin，包含基本的二进制文件，即系统命令，这些命令在单用户模式下仍可用
- /sbin，包含系统二进制文件，通常是一些只有系统管理员才能使用的命令
- /etc，包含系统配置文件，这些文件通常用于配置系统服务和应用程序
- /dev，包含设备文件，这些文件代表系统中的硬件设备，如硬盘、光驱、声卡等
- /proc，虚拟文件系统，包含了系统运行时的信息，如进程、内存使用情况、CPU状况
- /var，包含经常变化的文件，如日志文件、邮件、缓存等
- /tmp，用于存放临时文件，系统会定期清理这些文件
- /usr，用户相关的应用程序和文件的存放地址 ，如用户安装的软件、库文件等
- /home，用户的主目录，每个用户都有，用于存放用户的个人文件和配置
- /root，系统管理员（root用户）的主目录，通常包括root用户的个人文件和配置
- /opt，安装额外的软件包，通常不是由系统的包管理器安装，而是用户手动安装
- /boot，包含启动Linux系统所需的核心文件，如内核文件、引导加载器文件等
- /lib，系统运行所需的库文件，这些库文件被系统中的程序调用以执行特定功能
- /media，挂载外部存储设备，插入设备时，系统自动在/media下创建挂载点
- /mnt，用于临时挂载文件系统，通常用于挂载额外的存储设备或网络文件系统
- /run，包含系统运行时的临时文件，/run是/var/run的替代目录，用于提高性能
- /srv，用于存放服务数据，即由特定服务提供的数据，如网站内容、文件等
- Windows下目录管理
- Software 软件安装目录
- Module 根目录，存放安装包（压缩版文件）
- Code 代码区
- Api 文档区
- Tools 工具区
- Datas 数据区
- Linux下安装Java运行环境
  - 下载java8的包，并上传到服务器/usr/local目录下
    - wget命令是一个从网络上下载文件的自由工具，它支持http协议，https协议和ftp协议。因此我们可以通过wget命令来下载JDK。
    - wget的格式：wget 要下载的url。下载的目录为当前执行wget命令的目录。

```
wget https://repo.huaweicloud.com/java/jdk/8u201-b09/jdk-8u201-linux-x64.tar.gz
tar -zxvf jdk-8u201-linux-x64.tar.gz
mv jdk1.8.0_201 /usr/local/jdk1.8/
```

- 配置环境变量

```
vim /etc/profile
按下insert键，然后移动到最后一行，添加如下语句
export JAVA_HOME=/opt/jdk1.8/jdk1.8.0_201
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$JAVA_HOME/bin:$PATH
```

- 追加完成后更新配置

```
source /etc/profile
```

- 查看是否安装成功

```bash
java -version
```

- Linux下安装Spark运行环境

```
wget https://mirrors.huaweicloud.com/apache/spark/spark-2.2.0/spark-2.2.0-bin-hadoop2.7.tgz
tar -zxvf spark-2.2.0-bin-hadoop2.7.tgz
mv spark-2.2.0-bin-hadoop2.7 spark
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH:$SPARK_HOME:sbin
spark-shell
```

- Linux下安装Hadoop运行环境

```
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.1.3/hadoop-3.1.3.tar.gz
tar -zxvf hadoop-3.1.3.tar.gz
vim /etc/profile

#set hadoop environment
export HADOOP_HOME=/opt/hadoop-3.1.3
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
# 生效环境变量
source ~/.zshrc
```

- linux下配置chrome和chromedriver
  - 运行chromedriver报错
- 配置阿里云镜像源
  - 1、备份

```
sudo mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```

  - 2、CentOS 7

```
sudo wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

注意：修改Centos-7.repo文件将所有$releasever替换为7

```
sudo vim /etc/yum.repos.d/CentOS-Base.repo
:%s/$releasever/7/g
```

```
sudo wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
```

  - 3、之后运行yum makecache生成缓存

```
sudo yum makecache
```
