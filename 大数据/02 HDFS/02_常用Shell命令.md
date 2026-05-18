# 1 HDFS 的 shell 操作（开发重点）

## 1.1 基本语法

hadoop fs 具体命令    OR    hdfs dfs 具体命令

两个是完全相同的。

## 1.2 命令大全
```

[atguigu@hadoop102hadoop-3.1.3]$ bin/hadoop fs

[-appendToFile<localsrc> ... <dst>]

[-cat [-ignoreCrc] <src> ...]

[-chgrp [-R] GROUP PATH...]

[-chmod [-R] <MODE[,MODE]... |OCTALMODE> PATH...]

[-chown [-R] [OWNER][:[GROUP]] PATH...]

[-copyFromLocal [-f] [-p]<localsrc> ... <dst>]

[-copyToLocal [-p] [-ignoreCrc] [-crc]<src> ... <localdst>]

[-count [-q] <path> ...]

[-cp [-f] [-p] <src> ...<dst>]

[-df [-h] [<path> ...]]

[-du [-s] [-h] <path> ...]

[-get [-p] [-ignoreCrc] [-crc]<src> ... <localdst>]

[-getmerge [-nl] <src><localdst>]

[-help [cmd ...]]

[-ls [-d] [-h] [-R] [<path> ...]]

[-mkdir [-p] <path> ...]

[-moveFromLocal <localsrc> ...<dst>]

[-moveToLocal <src><localdst>]

[-mv <src> ... <dst>]

[-put [-f] [-p] <localsrc> ...<dst>]

[-rm [-f] [-r|-R] [-skipTrash]<src> ...]

[-rmdir [--ignore-fail-on-non-empty]<dir> ...]

<acl_spec><path>]]

[-setrep [-R] [-w] <rep><path> ...]

[-stat [format] <path> ...]

[-tail [-f] <file>]

[-test -[defsz] <path>]

[-text [-ignoreCrc] <src> ...]
```
## 1.3 常用命令实操

### 1.3.1 准备工作

1）启动Hadoop集群（方便后续的测试）

[atguigu@hadoop102hadoop-3.1.3]$ sbin/start-dfs.sh

[atguigu@hadoop103hadoop-3.1.3]$ sbin/start-yarn.sh

2）-help：输出这个命令参数

[atguigu@hadoop102hadoop-3.1.3]$ hadoop fs -help rm

3）创建/sanguo文件夹

[atguigu@hadoop102hadoop-3.1.3]$ hadoop fs -mkdir /sanguo

### 1.3.2 上传

1）-moveFromLocal：从本地剪切粘贴到HDFS

[atguigu@hadoop102 hadoop-3.1.3]$ vim shuguo.txt

输入：

shuguo

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -moveFromLocal ./shuguo.txt /sanguo

2）-copyFromLocal：从本地文件系统中拷贝文件到HDFS路径去

[atguigu@hadoop102 hadoop-3.1.3]$ vim weiguo.txt

输入：

weiguo

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -copyFromLocal weiguo.txt /sanguo

3）-put：等同于copyFromLocal，生产环境更习惯用put

[atguigu@hadoop102 hadoop-3.1.3]$ vim wuguo.txt

输入：

wuguo

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -put ./wuguo.txt /sanguo

4）-appendToFile：追加一个文件到已经存在的文件末尾

[atguigu@hadoop102 hadoop-3.1.3]$ vim liubei.txt

输入：

liubei

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -appendToFile liubei.txt /sanguo/shuguo.txt

### 1.3.3 下载

1）-copyToLocal：从HDFS拷贝到本地

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -copyToLocal /sanguo/shuguo.txt ./

2）-get：等同于copyToLocal，生产环境更习惯用get

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -get /sanguo/shuguo.txt ./shuguo2.txt

### 1.3.4 HDFS直接操作

1）-ls: 显示目录信息

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -ls /sanguo

2）-cat：显示文件内容

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -cat /sanguo/shuguo.txt

3）-chgrp、-chmod、-chown：Linux文件系统中的用法一样，修改文件所属权限

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs  -chmod 666  /sanguo/shuguo.txt

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs  -chown  atguigu:atguigu   /sanguo/shuguo.txt

4）-mkdir：创建路径

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -mkdir /jinguo

5）-cp：从HDFS的一个路径拷贝到HDFS的另一个路径

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -cp /sanguo/shuguo.txt /jinguo

6）-mv：在HDFS目录中移动文件

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -mv /sanguo/wuguo.txt /jinguo

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -mv /sanguo/weiguo.txt /jinguo

7）-tail：显示一个文件的末尾1kb的数据

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -tail /jinguo/shuguo.txt

8）-rm：删除文件或文件夹

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -rm /sanguo/shuguo.txt

9）-rm -r：递归删除目录及目录里面内容

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -rm -r /sanguo

10）-du统计文件夹的大小信息

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -du -s -h /jinguo

27  81  /jinguo

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -du  -h /jinguo

14  42  /jinguo/shuguo.txt

7   21   /jinguo/weiguo.txt

6   18   /jinguo/wuguo.tx

说明：27表示文件大小；81表示27*3个副本；/jinguo表示查看的目录

11）-setrep：设置HDFS中文件的副本数量

[atguigu@hadoop102 hadoop-3.1.3]$ hadoop fs -setrep 10 /jinguo/shuguo.txt

这里设置的副本数只是记录在NameNode的元数据中，是否真的会有这么多副本，还得看DataNode的数量。因为目前只有3台设备，最多也就3个副本，只有节点数的增加到10台时，副本数才能达到10。

![图片22.png](images/图片22.png)

这里设置的副本数只是记录在NameNode的元数据中，是否真的会有这么多副本，还得看DataNode的数量。因为目前只有3台设备，最多也就3个副本，只有节点数的增加到10台时，副本数才能达到10。

进入文件系统：请求hadoop102:9870端口：在点击箭头

![图片23.png](images/图片23.png)
