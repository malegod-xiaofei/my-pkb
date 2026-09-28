# Docker-compose容器编排

[目录](Docker与微服务实战.md) · 高级篇(大厂进阶)

![配图](images/img-0291.png)

<a id="t-2-5-1"></a>
## 是什么

Compose 是 Docker 公司推出的一个工具软件，可以管理多个 Docker 容器组成一个应用。你需要定义一个 YAML 格式的配置文件docker-compose.yml，**写好多个容器之间的调用关系**。然后，只要一个命令，就能同时启动/关闭这些容器

<a id="t-2-5-1-1"></a>
### Docker-Compose是Docker官方的开源项目， 负责实现对Docker容器集群的快速编排。

<a id="t-2-5-2"></a>
## 能干嘛

docker建议我们每一个容器中只运行一个服务,因为docker容器本身占用资源极少,所以最好是将每个服务单独的分割开来但是这样我们又面临了一个问题？

如果我需要同时部署好多个服务,难道要每个服务单独写Dockerfile然后在构建镜像,构建容器,这样累都累死了,所以docker官方给我们提供了docker-compose多服务部署的工具

例如要实现一个Web微服务项目，除了Web服务容器本身，往往还需要再加上后端的数据库mysql服务容器，redis服务器，注册中心eureka，甚至还包括负载均衡容器等等。。。。。。

Compose允许用户通过一个单独的docker-compose.yml模板文件（YAML 格式）来定义**一组相关联的应用容器为一个项目（project）。**

可以很容易地用一个配置文件定义一个多容器的应用，然后使用一条指令安装这个应用的所有依赖，完成构建。Docker-Compose 解决了容器与容器之间如何管理编排的问题。

<a id="t-2-5-3"></a>
## 去哪下

<a id="t-2-5-3-1"></a>
### 官网

<a id="t-2-5-3-1-1"></a>
#### https://docs.docker.com/compose/compose-file/compose-file-v3/

<a id="t-2-5-3-2"></a>
### 官网下载

<a id="t-2-5-3-2-1"></a>
#### https://docs.docker.com/compose/install/

<a id="t-2-5-3-3"></a>
### 安装步骤

curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose

docker-compose --version

![配图](images/img-0292.png)

<a id="t-2-5-3-4"></a>
### 卸载步骤

![配图](images/img-0293.png)

<a id="t-2-5-4"></a>
## Compose核心概念

<a id="t-2-5-4-1"></a>
### 一文件

<a id="t-2-5-4-1-1"></a>
#### docker-compose.yml

<a id="t-2-5-4-2"></a>
### 两要素

<a id="t-2-5-4-2-1"></a>
#### 服务（service）

- 一个个应用容器实例，比如订单微服务、库存微服务、mysql容器、nginx容器或者redis容器
<a id="t-2-5-4-2-2"></a>
#### 工程（project）

- 由一组关联的应用容器组成的一个完整业务单元，在 docker-compose.yml 文件中定义。
<a id="t-2-5-5"></a>
## Compose使用的三个步骤

<a id="t-2-5-5-1"></a>
### 编写Dockerfile定义各个微服务应用并构建出对应的镜像文件

<a id="t-2-5-5-2"></a>
### 使用 docker-compose.yml 定义一个完整业务单元，安排好整体应用中的各个容器服务。

<a id="t-2-5-5-3"></a>
### 最后，执行docker-compose up命令 来启动并运行整个应用程序，完成一键部署上线

<a id="t-2-5-6"></a>
## Compose常用命令

**Compose常用命令**

docker-compose -h                           # 查看帮助

docker-compose up                           # 启动所有docker-compose服务

**docker-compose up -d                        # 启动所有docker-compose服务并后台运行**

**docker-compose down                         # 停止并删除容器、网络、卷、镜像。**

docker-compose exec  yml里面的服务id                 # 进入容器实例内部  docker-compose exec **docker-compose.yml文件中写的服务id** /bin/bash

docker-compose ps                      # 展示当前docker-compose编排过的运行的所有容器

docker-compose top                     # 展示当前docker-compose编排过的容器进程

docker-compose logs  yml里面的服务id     # 查看容器输出日志

**docker-compose config     # 检查配置**

**docker-compose config -q  # 检查配置，有问题才有输出**

docker-compose restart   # 重启服务

docker-compose start     # 启动服务

docker-compose stop      # 停止服务

<a id="t-2-5-7"></a>
## Compose编排微服务

这一节单独记在 [Compose编排微服务](13b_Compose编排微服务.md)。

---

[上一篇 Docker网络](12_Docker网络.md) · [目录](Docker与微服务实战.md) · [下一篇 Compose编排微服务](13b_Compose编排微服务.md)
