# Docker常规安装简介

[目录](Docker与微服务实战.md) · 基础篇(零基小白)

![配图](images/img-0132.png)

<a id="t-1-8-1"></a>
## 总体步骤

<a id="t-1-8-1-1"></a>
### 搜索镜像

<a id="t-1-8-1-2"></a>
### 拉取镜像

<a id="t-1-8-1-3"></a>
### 查看镜像

<a id="t-1-8-1-4"></a>
### 启动镜像

<a id="t-1-8-1-4-1"></a>
#### 服务端口映射

<a id="t-1-8-1-5"></a>
### 停止容器

<a id="t-1-8-1-6"></a>
### 移除容器

<a id="t-1-8-2"></a>
## 安装tomcat

<a id="t-1-8-2-1"></a>
### docker hub上面查找tomcat镜像

<a id="t-1-8-2-1-1"></a>
#### docker search tomcat

![配图](images/img-0133.png)

<a id="t-1-8-2-2"></a>
### 从docker hub上拉取tomcat镜像到本地

<a id="t-1-8-2-2-1"></a>
#### docker pull tomcat

![配图](images/img-0134.png)

![配图](images/img-0135.png)

<a id="t-1-8-2-3"></a>
### docker images查看是否有拉取到的tomcat

![配图](images/img-0136.png)

<a id="t-1-8-2-4"></a>
### 使用tomcat镜像创建容器实例(也叫运行镜像)

<a id="t-1-8-2-4-1"></a>
#### docker run -it -p 8080:8080 tomcat

- -p 小写，主机端口:docker容器端口
- -P 大写，随机分配端口

  ![配图](images/img-0137.png)
- i:交互
- t:终端
- d:后台
<a id="t-1-8-2-5"></a>
### 访问猫首页

<a id="t-1-8-2-5-1"></a>
#### 问题

![配图](images/img-0138.png)

<a id="t-1-8-2-5-2"></a>
#### 解决

- 可能没有映射端口或者没有关闭防火墙

  ![配图](images/img-0139.png)
- 把webapps.dist目录换成webapps
  - 先成功启动tomcat

    ![配图](images/img-0140.png)
  - 查看webapps 文件夹查看为空

    ![配图](images/img-0141.png)
<a id="t-1-8-2-6"></a>
### 免修改版说明

<a id="t-1-8-2-6-1"></a>
#### docker pull billygoo/tomcat8-jdk8

<a id="t-1-8-2-6-2"></a>
#### docker run -d -p 8080:8080 --name mytomcat8 billygoo/tomcat8-jdk8

![配图](images/img-0142.png)

<a id="t-1-8-3"></a>
## 安装mysql

<a id="t-1-8-3-1"></a>
### docker hub上面查找mysql镜像

![配图](images/img-0143.png)

<a id="t-1-8-3-2"></a>
### 从docker hub上(阿里云加速器)拉取mysql镜像到本地标签为5.7

![配图](images/img-0144.png)

<a id="t-1-8-3-3"></a>
### 使用mysql5.7镜像创建容器(也叫运行镜像)

<a id="t-1-8-3-3-1"></a>
#### 命令出处，哪里来的？

![配图](images/img-0145.png)

<a id="t-1-8-3-3-2"></a>
#### 简单版

- 使用mysql镜像

  docker run -p 3306:3306 -e MYSQL\_ROOT\_PASSWORD=123456 -d mysql:5.7

  docker ps

  docker exec -it 容器ID /bin/bash

  mysql -uroot -p

  ![配图](images/img-0146.png)
- 建库建表插入数据

  ![配图](images/img-0147.png)
- 外部Win10也来连接运行在dokcer上的mysql容器实例服务

  ![配图](images/img-0148.png)
- 问题
  - 插入中文数据试试

    ![配图](images/img-0149.png)
    - 为什么报错?
      - docker上默认字符集编码隐患

        docker里面的mysql容器实例查看，内容如下：

        SHOW VARIABLES LIKE 'character%'

        ![配图](images/img-0150.png)
  - 删除容器后，里面的mysql数据如何办
    - 容器实例一删除，你还有什么？ 删容器到跑路。。。。。？
<a id="t-1-8-3-3-3"></a>
#### 实战版

- 新建mysql容器实例

  docker run -d -p 3306:3306 --privileged=true -v /zzyyuse/mysql/log:/var/log/mysql -v /zzyyuse/mysql/data:/var/lib/mysql -v /zzyyuse/mysql/conf:/etc/mysql/conf.d -e MYSQL\_ROOT\_PASSWORD=123456  --name mysql mysql:5.7

  ![配图](images/img-0151.png)
- 新建my.cnf
  - 通过容器卷同步给mysql容器实例

    [client]  
    default\_character\_set=utf8

    [mysqld]

    collation\_server = utf8\_general\_ci

    character\_set\_server = utf8

    ![配图](images/img-0152.png)
- 重新启动mysql容器实例再重新进入并查看字符编码

  ![配图](images/img-0153.png)

  ![配图](images/img-0154.png)
- 再新建库新建表再插入中文测试

  ![配图](images/img-0155.png)

  ![配图](images/img-0156.png)
- 结论

  之前的DB  无效

  修改字符集操作+重启mysql容器实例

  之后的DB  有效，需要新建

  结论：**docker安装完MySQL并run出容器后，建议请先修改完字符集编码后再新建mysql库-表-插数据**

  ![配图](images/img-0157.png)
- 假如将当前容器实例删除，再重新来一次，之前建的db01实例还有吗？trytry
<a id="t-1-8-4"></a>
## 安装redis

<a id="t-1-8-4-1"></a>
### 从docker hub上(阿里云加速器)拉取redis镜像到本地标签为6.0.8

![配图](images/img-0158.png)

<a id="t-1-8-4-2"></a>
### 入门命令

![配图](images/img-0159.png)

<a id="t-1-8-4-3"></a>
### 命令提醒：容器卷记得加入--privileged=true

Docker挂载主机目录Docker访问出现cannot open directory .: Permission denied

解决办法：在挂载目录后多加一个--privileged=true参数即可

<a id="t-1-8-4-4"></a>
### 在CentOS宿主机下新建目录/app/redis

![配图](images/img-0160.png)

1 建目录

mkdir -p /app/redis

<a id="t-1-8-4-4-1"></a>
#### mkdir -p /app/redis

<a id="t-1-8-4-5"></a>
### 将一个redis.conf文件模板拷贝进/app/redis目录下

![配图](images/img-0161.png)

2 拷贝配置文件

将准备好的redis.conf文件放进/app/redis目录下

<a id="t-1-8-4-6"></a>
### /app/redis目录下修改redis.conf文件

3 /app/redis目录下修改redis.conf文件

3.1 开启redis验证    **可选**

requirepass 123

**3.2 允许redis外地连接  必须**

**注释掉 # bind 127.0.0.1**

![配图](images/img-0162.png)

**3.3   daemonize no**

**将daemonize yes注释起来或者 daemonize no设置，因为该配置和docker run中-d参数冲突，会导致容器一直启动失败**

![配图](images/img-0163.png)

3.4 开启redis数据持久化  appendonly yes  可选

<a id="t-1-8-4-6-1"></a>
#### 默认出厂的原始redis.conf

逐行注释单独记在 [redis出厂配置](08b_redis出厂配置.md)。

<a id="t-1-8-4-7"></a>
### 使用redis6.0.8镜像创建容器(也叫运行镜像)

docker run  -p 6379:6379 --name myr3 --privileged=true -v /app/redis/redis.conf:/etc/redis/redis.conf -v /app/redis/data:/data -d redis:6.0.8 redis-server /etc/redis/redis.conf

![配图](images/img-0164.png)

<a id="t-1-8-4-8"></a>
### 测试redis-cli连接上来

![配图](images/img-0165.png)

docker exec -it 运行着Rediis服务的容器ID redis-cli

<a id="t-1-8-4-9"></a>
### 请证明docker启动使用了我们自己指定的配置文件

<a id="t-1-8-4-9-1"></a>
#### 修改前

![配图](images/img-0166.png)

我们用的配置文件，数据库默认是16个

<a id="t-1-8-4-9-2"></a>
#### 修改后

![配图](images/img-0167.png)

宿主机的修改会同步给docker容器里面的配置。

- 记得重启服务
<a id="t-1-8-4-10"></a>
### 测试redis-cli连接上来第2次

![配图](images/img-0168.png)

<a id="t-1-8-5"></a>
## 安装Nginx

<a id="t-1-8-5-1"></a>
### 见高级篇Portainer

---

[上一篇 Docker容器数据卷](07_Docker容器数据卷.md) · [目录](Docker与微服务实战.md) · [下一篇 Docker复杂安装详说](09_Docker复杂安装详说.md)
