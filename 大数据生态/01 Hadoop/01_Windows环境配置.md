Api 客户端环境搭建

- 复制当前文件到一个非中文目录下
![图片1.png](images/图片1.png)

![图片2.png](images/图片2.png)

- 新建环境变量
  - HADOOP_HOME->D:\Tools\hadoop-3.1.0
![图片3.png](images/图片3.png)

  - path添加Hadoop
![图片4.png](images/图片4.png)

  - 双击winutils.exe一闪而过没报错说明安装正常
![图片5.png](images/图片5.png)

验证Hadoop环境变量是否正常。双击winutils.exe，如果报如下错误。说明缺少微软运行库（正版系统往往有这个问题）。再资料包里面有对应的微软运行库安装包双击安装即可。
