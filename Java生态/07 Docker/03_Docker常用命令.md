# Docker常用命令

[目录](Docker与微服务实战.md) · 基础篇(零基小白)

![配图](images/img-0051.png)

<a id="t-1-3-1"></a>
## 帮助启动类命令

<a id="t-1-3-1-1"></a>
### 启动docker： systemctl start docker

<a id="t-1-3-1-2"></a>
### 停止docker： systemctl stop docker

<a id="t-1-3-1-3"></a>
### 重启docker： systemctl restart docker

<a id="t-1-3-1-4"></a>
### 查看docker状态： systemctl status docker

<a id="t-1-3-1-5"></a>
### 开机启动： systemctl enable docker

<a id="t-1-3-1-6"></a>
### 查看docker概要信息： docker info

<a id="t-1-3-1-7"></a>
### 查看docker总体帮助文档： docker --help

<a id="t-1-3-1-8"></a>
### 查看docker命令帮助文档： docker 具体命令 --help

<a id="t-1-3-2"></a>
## 镜像命令

<a id="t-1-3-2-1"></a>
### docker images

<a id="t-1-3-2-1-1"></a>
#### 列出本地主机上的镜像

![配图](images/img-0052.png)

各个选项说明:

REPOSITORY：表示镜像的仓库源  
TAG：镜像的标签版本号

IMAGE ID：镜像ID

CREATED：镜像创建时间

SIZE：镜像大小

同一仓库源可以有多个 TAG版本，代表这个仓库源的不同个版本，我们使用 REPOSITORY:TAG 来定义不同的镜像。

如果你不指定一个镜像的版本标签，例如你只使用 ubuntu，docker 将默认使用 ubuntu:latest 镜像

<a id="t-1-3-2-1-2"></a>
#### OPTIONS说明：

- -a :列出本地所有的镜像（含历史映像层）
- -q :只显示镜像ID。
<a id="t-1-3-2-2"></a>
### docker search 某个XXX镜像名字

<a id="t-1-3-2-2-1"></a>
#### 网站

- https://hub.docker.com
<a id="t-1-3-2-2-2"></a>
#### 命令

- docker search [OPTIONS] 镜像名字
- 案例

  ![配图](images/img-0053.png)

  ![配图](images/img-0054.png)
- OPTIONS说明：
  - --limit : 只列出N个镜像，默认25个
  - docker search --limit 5 redis
<a id="t-1-3-2-3"></a>
### docker pull 某个XXX镜像名字

<a id="t-1-3-2-3-1"></a>
#### 下载镜像

<a id="t-1-3-2-3-2"></a>
#### docker pull 镜像名字[:TAG]

<a id="t-1-3-2-3-3"></a>
#### docker pull 镜像名字

- 没有TAG就是最新版
- 等价于
- docker pull 镜像名字:latest
- docker pull ubuntu

  ![配图](images/img-0055.png)
<a id="t-1-3-2-4"></a>
### docker system df 查看镜像/容器/数据卷所占的空间

![配图](images/img-0056.png)

<a id="t-1-3-2-5"></a>
### docker rmi 某个XXX镜像名字ID

<a id="t-1-3-2-5-1"></a>
#### 删除镜像

<a id="t-1-3-2-5-2"></a>
#### 删除单个

- docker rmi  -f 镜像ID
<a id="t-1-3-2-5-3"></a>
#### 删除多个

- docker rmi -f 镜像名1:TAG 镜像名2:TAG
<a id="t-1-3-2-5-4"></a>
#### 删除全部

- docker rmi -f $(docker images -qa)
<a id="t-1-3-2-6"></a>
### 面试题：谈谈docker虚悬镜像是什么？

<a id="t-1-3-2-6-1"></a>
#### 是什么

- 仓库名、标签都是&lt;none>的镜像，俗称虚悬镜像dangling image
- 长什么样

  ![配图](images/img-0057.png)
<a id="t-1-3-2-6-2"></a>
#### 后续Dockerfile章节再介绍

<a id="t-1-3-2-7"></a>
### 思考

![配图](images/img-0058.png)

<a id="t-1-3-2-7-1"></a>
#### 结合我们Git的学习心得，大家猜猜是否会有 docker commit /docker push？？

<a id="t-1-3-3"></a>
## 容器命令

<a id="t-1-3-3-1"></a>
### 有镜像才能创建容器， 这是根本前提(下载一个CentOS或者ubuntu镜像演示)

<a id="t-1-3-3-1-1"></a>
#### 说明

![配图](images/img-0059.png)

<a id="t-1-3-3-1-2"></a>
#### docker pull centos

<a id="t-1-3-3-1-3"></a>
#### docker pull ubuntu

![配图](images/img-0060.png)

<a id="t-1-3-3-1-4"></a>
#### 本次演示用ubuntu演示

<a id="t-1-3-3-2"></a>
### 新建+启动容器

<a id="t-1-3-3-2-1"></a>
#### docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

- OPTIONS说明

  OPTIONS说明（常用）：有些是一个减号，有些是两个减号

  --name="容器新名字"       为容器指定一个名称；

  -d: 后台运行容器并返回容器ID，也即启动守护式容器(后台运行)；

  **-i：以交互模式运行容器，通常与 -t 同时使用；**

  **-t：为容器重新分配一个伪输入终端，通常与 -i 同时使用；**

  也即**启动交互式容器(前台有伪终端，等待交互)**；

  -P: **随机**端口映射，大写P

  -p: **指定**端口映射，小写p

  ![配图](images/img-0061.png)
- 启动交互式容器(前台命令行)

  ![配图](images/img-0062.png)

  \#使用镜像centos:latest以**交互模式**启动一个容器,在容器内执行/bin/bash命令。

  docker run -it centos /bin/bash

  参数说明：  
  -i: 交互式操作。

  -t: 终端。

  centos : centos 镜像。

  /bin/bash：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。

  要退出终端，直接输入 exit:
<a id="t-1-3-3-3"></a>
### 列出当前所有正在运行的容器

<a id="t-1-3-3-3-1"></a>
#### docker ps [OPTIONS]

- OPTIONS说明

  OPTIONS说明（常用）：

  -a :列出当前所有**正在运行**的容器+**历史上运行过**的

  -l :显示最近创建的容器。

  -n：显示最近n个创建的容器。

  **-q :静默模式，只显示容器编号。**
<a id="t-1-3-3-4"></a>
### 退出容器

<a id="t-1-3-3-4-1"></a>
#### 两种退出方式

- exit
  - run进去容器，exit退出，容器停止
- ctrl+p+q
  - run进去容器，ctrl+p+q退出，容器不停止
<a id="t-1-3-3-5"></a>
### 启动已停止运行的容器

<a id="t-1-3-3-5-1"></a>
#### docker start 容器ID或者容器名

<a id="t-1-3-3-6"></a>
### 重启容器

<a id="t-1-3-3-6-1"></a>
#### docker restart 容器ID或者容器名

<a id="t-1-3-3-7"></a>
### 停止容器

<a id="t-1-3-3-7-1"></a>
#### docker stop 容器ID或者容器名

<a id="t-1-3-3-8"></a>
### 强制停止容器

<a id="t-1-3-3-8-1"></a>
#### docker kill 容器ID或容器名

<a id="t-1-3-3-9"></a>
### 删除已停止的容器

<a id="t-1-3-3-9-1"></a>
#### docker rm 容器ID

- 一次性删除多个容器实例
  - docker rm -f $(docker ps -a -q)
  - docker ps -a -q | xargs docker rm
<a id="t-1-3-3-10"></a>
### 重要

<a id="t-1-3-3-10-1"></a>
#### 有镜像才能创建容器，这是根本前提(下载一个Redis6.0.8镜像演示)

<a id="t-1-3-3-10-2"></a>
#### 启动守护式容器(后台服务器)

- 在大部分的场景下，我们希望 docker 的服务是在后台运行的， 我们可以过 -d 指定容器的后台运行模式。
- docker run -d 容器名

  \#使用镜像centos:latest以后台模式启动一个容器

  docker run -d centos

  问题：然后docker ps -a 进行查看, 会发现容器已经退出

  很重要的要说明的一点: **Docker容器后台运行,就必须有一个前台进程.**

  容器运行的命令如果不是那些**一直挂起的命令**（比如运行top，tail），就是会自动退出的。

  这个是docker的机制问题,比如你的web容器,我们以nginx为例，正常情况下,

  我们配置启动服务只需要启动响应的service即可。例如service nginx start

  但是,这样做,nginx为后台进程模式运行,就导致docker前台没有运行的应用,

  这样的容器后台启动后,会立即自杀因为他觉得他没事可做了.

  所以，最佳的解决方案是,**将你要运行的程序以前台进程的形式运行，**

  **常见就是命令行模式，表示我还有交互操作，别中断，O(∩\_∩)O哈哈~**
- redis 前后台启动演示case
  - 前台交互式启动
    - docker run -it redis:6.0.8
  - 后台守护式启动
    - docker run -d redis:6.0.8
<a id="t-1-3-3-10-3"></a>
#### 查看容器日志

- docker logs 容器ID
<a id="t-1-3-3-10-4"></a>
#### 查看容器内运行的进程

- docker top 容器ID
<a id="t-1-3-3-10-5"></a>
#### 查看容器内部细节

- docker inspect 容器ID
<a id="t-1-3-3-10-6"></a>
#### 进入正在运行的容器并以命令行交互

- docker exec -it 容器ID bashShell

  ![配图](images/img-0063.png)

  ![配图](images/img-0064.png)
- 重新进入docker attach 容器ID
- 案例演示，用centos或者unbuntu都可以
- 上述两个区别
  - attach 直接进入容器启动命令的终端，不会启动新的进程 用exit退出，会导致容器的停止。

    ![配图](images/img-0065.png)
  - exec 是在容器中打开新的终端，并且可以启动新的进程 用exit退出，不会导致容器的停止。

    ![配图](images/img-0066.png)
- 推荐大家使用 docker exec 命令，因为退出容器终端，不会导致容器的停止。
- 用之前的redis容器实例进入试试
  - 进入redis服务
    - docker exec -it 容器ID /bin/bash
    - docker exec -it 容器ID redis-cli
    - 一般用-d后台启动的程序，再用exec进入对应容器实例
<a id="t-1-3-3-10-7"></a>
#### 从容器内拷贝文件到主机上

- 容器→主机
- docker cp  容器ID:容器内路径 目的主机路径

  ![配图](images/img-0067.png)

  公式：docker cp  容器ID:容器内路径 目的主机路径
<a id="t-1-3-3-10-8"></a>
#### 导入和导出容器

- export 导出容器的内容留作为一个tar归档文件[对应import命令]
- import 从tar包中的内容创建一个新的文件系统再导入为镜像[对应export]
- 案例
  - docker export 容器ID > 文件名.tar

    ![配图](images/img-0068.png)
  - cat 文件名.tar | docker import - 镜像用户/镜像名:镜像版本号

    ![配图](images/img-0069.png)
<a id="t-1-3-4"></a>
## 小总结

<a id="t-1-3-4-1"></a>
### 常用命令

图片正下方还有命令

![配图](images/img-0070.png)

attach    Attach to a running container                 # 当前 shell 下 attach 连接指定运行镜像

build     Build an image from a Dockerfile              # 通过 Dockerfile 定制镜像

commit    Create a new image from a container changes   # 提交当前容器为新的镜像

cp        Copy files/folders from the containers filesystem to the host path   #从容器中拷贝指定文件或者目录到宿主机中

create    Create a new container                        # 创建一个新的容器，同 run，但不启动容器

diff      Inspect changes on a container's filesystem   # 查看 docker 容器变化

events    Get real time events from the server          # 从 docker 服务获取容器实时事件

exec      Run a command in an existing container        # 在已存在的容器上运行命令

export    Stream the contents of a container as a tar archive   # 导出容器的内容流作为一个 tar 归档文件[对应 import ]

history   Show the history of an image                  # 展示一个镜像形成历史

images    List images                                   # 列出系统当前镜像

import    Create a new filesystem image from the contents of a tarball # 从tar包中的内容创建一个新的文件系统映像[对应export]

info      Display system-wide information               # 显示系统相关信息

inspect   Return low-level information on a container   # 查看容器详细信息

kill      Kill a running container                      # kill 指定 docker 容器

load      Load an image from a tar archive              # 从一个 tar 包中加载一个镜像[对应 save]

login     Register or Login to the docker registry server    # 注册或者登陆一个 docker 源服务器

logout    Log out from a Docker registry server          # 从当前 Docker registry 退出

logs      Fetch the logs of a container                 # 输出当前容器日志信息

port      Lookup the public-facing port which is NAT-ed to PRIVATE\_PORT    # 查看映射端口对应的容器内部源端口

pause     Pause all processes within a container        # 暂停容器

ps        List containers                               # 列出容器列表

pull      Pull an image or a repository from the docker registry server   # 从docker镜像源服务器拉取指定镜像或者库镜像

push      Push an image or a repository to the docker registry server    # 推送指定镜像或者库镜像至docker源服务器

restart   Restart a running container                   # 重启运行的容器

rm        Remove one or more containers                 # 移除一个或者多个容器

rmi       Remove one or more images       # 移除一个或多个镜像[无容器使用该镜像才可删除，否则需删除相关容器才可继续或 -f 强制删除]

run       Run a command in a new container              # 创建一个新的容器并运行一个命令

save      Save an image to a tar archive                # 保存一个镜像为一个 tar 包[对应 load]

search    Search for an image on the Docker Hub         # 在 docker hub 中搜索镜像

start     Start a stopped containers                    # 启动容器

stop      Stop a running containers                     # 停止容器

tag       Tag an image into a repository                # 给源中镜像打标签

top       Lookup the running processes of a container   # 查看容器中运行的进程信息

unpause   Unpause a paused container                    # 取消暂停容器

version   Show the docker version information           # 查看 docker 版本号

wait      Block until a container stops, then print its exit code   # 截取容器停止时的退出状态值

---

[上一篇 Docker安装](02_Docker安装.md) · [目录](Docker与微服务实战.md) · [下一篇 Docker镜像](04_Docker镜像.md)
