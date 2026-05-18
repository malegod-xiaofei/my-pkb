# 1  hdfs dfs常用命令

- 查看所有命令
  - hdfs dfs
- 查看某目录下文件列表
  - hdfs dfs -ls /
- 查看某文本文件的内容
  - hdfs dfs -cat /tmp/inndex.html
- 创建目录
  - hdfs dfs -mkdir /tmp/test
- 删除目录
  - hdfs dfs -rmr /tmp/test
  - 注意事项 :
    - 数据去向:默认是被move到当前用户的.Trash目录,即当前用户的垃圾箱当中.
    - Hdfs垃圾箱回收策略:默认6个小时回收一次
    - 强制删除不进垃圾箱
  - hdfs dfs -rm -f -skipTrash /tmp/test
- 从hdfs下载文件
  - hdfs dfs -copyToLocal /tmp/index.html
- 从本地上传文件到hdfs
  - hdfs dfs -copyFromLocal index.html /tmp/test
- 查看压缩的文件内容
  - hdfs dfs -text /tmp/test/index.html.gz | more
- 查看文件大小
  - hdfs dfs -du -h /tmp/test
- 创建文件
  - hdfs dfs -touchz /tmp/test/HelloWorld.txt
- 查看命令帮助信息
  - hdfs dfs -usage cp
# 2 hdfs dfs admin

- 查看可用的管理命令
  - hdfs dfsadmin -help
- 报告文件系统信息
  - hdfs dfsadmin -report
- 设置目录配额
  - 设置目录配额，目录配额是一个长整型数，限定指定目录下的名字个数：
hdfs dfsadmin -setQuota <quota> <dirname>……<dirname>

比如：hdfs dfsadmin -setQuota 10 /tmp/tianliangedu

- 安全模式管理
  - 当集群环境启动时，NameNode会进入一个安全模式。此时不会出现数据块的写操作。NameNode会收到各个DataNode拥有的数据块列表的数据块报告，由此NameNode获得所有的数据块信息。数据块达到最小副本数时，该数据块就被认为是安全的。
hdfs dfsadmin -safemode get ##返回安全模式是否开启的信息，返回Safe mode is OFF/OPEN

hdfs dfsadmin -safemode enter ##进入安全模式

hdfs dfsadmin -safemode leave ##强制NameNode退出安全模式

hdfs dfsadmin -safemode wait ##等待，一直到安全模式结束

# 3 实战

- 统计文件数量
  - hdfs dfs -count
- 查看路径下文件占用的内存大小
hadoop fs -du -h afs://shaolin.afs.baidu.com:9902/user/ubs-ada-querytrade/personal/zhaoyingfei/etl/

hadoop fs -du afs://shaolin.afs.baidu.com:9902/user/ubs-ada-querytrade/personal/zhaoyingfei/etl/
