# Jenkins环境搭建
## Docker镜像
使用jenkins 2.464镜像：

```shell
docker pull jenkins/jenkins:2.464
```

  


## 准备映射的容器卷
Jenkins需要映射出来的容器卷有：

+ `/var/jenkins_home`：存储信息

  


准备对应文件夹：

```shell
mkdir -p /root/jenkins_workspace/jenkins_home
```

  


## 端口
Jenkins需要映射出来的端口有：

+ `8080`：浏览器页面端口，可以映射为别的端口，例如（`-p 9988:8080`）
+ `50000`：代理节点访问端口。如果要映射为别的端口，需要配置环境变量，例如（` -p 50001:50001 --env JENKINS_SLAVE_AGENT_PORT=50001`)

  


## 启动容器
启动容器`jenkins`：

```shell
docker run -d \
  -p 9988:8080 \
  -p 50000:50000 \
  --name jenkins \
  --restart always \
  -v /root/jenkins_workspace/jenkins_home:/var/jenkins_home \
  jenkins/jenkins:2.464
```

  


启动之后，设置管理员用户 admin/admin。

  


# 安装插件
容器启动完成后，将SVN上的Jenkins插件装到Jenkins中，先安装旧插件，然后安装新插件进行升级替换。如果安装时缺少依赖报错，则根据报错提示先安装对应的依赖插件（依赖插件也都在插件文件夹中）。

  


# 浏览器访问
访问地址：[http://192.168.xxx.xxx:9988/](http://192.168.xxx.xxx:9988/)
