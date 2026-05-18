- 查看远程客户端的文件路径
hadoop fs -cat afs://tianqi.afs.baidu.com:9902/user/ubs-ada-querytrade/personal/zhaoyingfei/test1.txt

- 创建文件夹
hadoop fs -mkdir afs://tianqi.afs.baidu.com:9902/user/ubs-ada-querytrade/personal/zhaoyingfei/output

- 新建文件
  - hadoop fs -mkdir
- 上传linux中的文件到hadoop中
  - hadoop fs -put test1.txt
- 集群启动
  - sh myhadoop.sh start
- 启动完成之后查看是否正常
  - jpsall
![图片9.png](images/图片9.png)
