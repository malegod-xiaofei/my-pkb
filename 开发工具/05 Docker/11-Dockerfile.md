# Dockerfile
  


Dockerfile是用来构建Docker镜像的文本文件，是由一条条构建镜像所需的指令和参数构成的脚本。

  


构建步骤：

  


1. 编写Dockerfile文件
2. `docker build`命令构建镜像
3. `docker run`依据镜像运行容器实例

  


# 构建过程
  


Dockerfile编写：

  


+ 每条保留字指令都必须为大写字母，且后面要跟随至少一个参数
+ 指令按照从上到下顺序执行
+ `#`表示注释
+ 每条指令都会创建一个新的镜像层并对镜像进行提交

  


Docker引擎执行Docker的大致流程：

  


1. docker从基础镜像运行一个容器
2. 执行一条指令并对容器做出修改
3. 执行类似`docker commit`的操作提交一个新的镜像层
4. docker再基于刚提交的镜像运行一个新容器
5. 执行Dockerfile中的下一条指令，直到所有指令都执行完成

  


# Dockerfile保留字
  


## FROM
  


基础镜像，当前新镜像是基于哪个镜像的，指定一个已经存在的镜像作为模板。Dockerfile第一条必须是`FROM`

  


```dockerfile
# FROM 镜像名
FROM hub.c.163.com/library/tomcat
```

  


## MAINTAINER
  


镜像维护者的姓名和邮箱地址

  


```dockerfile
# 非必须
MAINTAINER ZhangSan zs@163.com
```

  


## RUN
  


容器构建时需要运行的命令。

  


有两种格式：

  


+  shell格式 

```dockerfile
# 等同于在终端操作的shell命令
# 格式：RUN <命令行命令>
RUN yum -y install vim
```

+  exec格式 

```dockerfile
# 格式：RUN ["可执行文件" , "参数1", "参数2"]
RUN ["./test.php", "dev", "offline"]  # 等价于 RUN ./test.php dev offline
```

  


`RUN`是在`docker build`时运行

  


## EXPOSE
  


当前容器对外暴露出的端口。

  


```dockerfile
# EXPOSE 要暴露的端口
# EXPOSE <port>[/<protocol] ....
EXPOSE 3306 33060
```

  


## WORKDIR
  


指定在创建容器后， 终端默认登录进来的工作目录。

  


```dockerfile
ENV CATALINA_HOME /usr/local/tomcat
WORKDIR $CATALINA_HOME
```

  


## USER
  


指定该镜像以什么样的用户去执行，如果不指定，默认是`root`。（一般不修改该配置）

  


```dockerfile
# USER <user>[:<group>]
USER patrick
```

  


## ENV
  


用来在构建镜像过程中设置环境变量。

  


这个环境变量可以在后续的任何`RUN`指令或其他指令中使用

  


```dockerfile
# 格式 ENV 环境变量名 环境变量值
# 或者 ENV 环境变量名=值
ENV MY_PATH /usr/mytest

# 使用环境变量
WORKDIR $MY_PATH
```

  


## VOLUME
  


容器数据卷，用于数据保存和持久化工作。类似于 `docker run` 的`-v`参数。

  


```dockerfile
# VOLUME 挂载点
# 挂载点可以是一个路径，也可以是数组（数组中的每一项必须用双引号）
VOLUME /var/lib/mysql
```

  


## ADD
  


将宿主机目录下（或远程文件）的文件拷贝进镜像，且会自动处理URL和解压tar压缩包。

  


## COPY
  


类似`ADD`，拷贝文件和目录到镜像中。

  


将从构建上下文目录中`<源路径>`的文件目录复制到新的一层镜像内的`<目标路径>`位置。

  


```dockerfile
COPY src dest
COPY ["src", "dest"]
# <src源路径>：源文件或者源目录
# <dest目标路径>：容器内的指定路径，该路径不用事先建好。如果不存在会自动创建
```

  


## CMD
  


指定容器启动后要干的事情。

  


有两种格式：

  


+  shell格式 

```dockerfile
# CMD <命令>
CMD echo "hello world"
```

+  exec格式 

```dockerfile
# CMD ["可执行文件", "参数1", "参数2" ...]
CMD ["catalina.sh", "run"]
```

+  参数列表格式 

```dockerfile
# CMD ["参数1", "参数2" ....]，与ENTRYPOINT指令配合使用
```

  


Dockerfile中如果出现多个`CMD`指令，只有最后一个生效。`CMD`会被`docker run`之后的参数替换。

  


例如，对于tomcat镜像，执行以下命令会有不同的效果：

  


```shell
# 因为tomcat的Dockerfile中指定了 CMD ["catalina.sh", "run"]
# 所以直接docker run 时，容器启动后会自动执行 catalina.sh run
docker run -it -p 8080:8080 tomcat

# 指定容器启动后执行 /bin/bash
# 此时指定的/bin/bash会覆盖掉Dockerfile中指定的 CMD ["catalina.sh", "run"]
docker run -it -p 8080:8080 tomcat /bin/bash
```

  


`CMD`是在`docker run`时运行，而 `RUN`是在`docker build`时运行。

  


## ENTRYPOINT
  


用来指定一个容器启动时要运行的命令。

  


类似于`CMD`命令，但是`ENTRYPOINT`不会被`docker run`后面的命令覆盖，这些命令参数会被当做参数送给`ENTRYPOINT`指令指定的程序。

  


`ENTRYPOINT`可以和`CMD`一起用，一般是可变参数才会使用`CMD`，这里的`CMD`等于是在给`ENTRYPOINT`传参。

  


当指定了`ENTRYPOINT`后，`CMD`的含义就发生了变化，不再是直接运行期命令，而是将`CMD`的内容作为参数传递给`ENTRYPOINT`指令，它们两个组合会变成 `<ENTRYPOINT> "<CMD>"`。

  


例如：

  


```dockerfile
FROM nginx

ENTRYPOINT ["nginx", "-c"]  # 定参
CMD ["/etc/nginx/nginx.conf"] # 变参
```

  


对于此Dockerfile，构建成镜像 `nginx:test`后，如果执行；

  


+ `docker run nginx test`，则容器启动后，会执行 `nginx -c /etc/nginx/nginx.conf`
+ `docker run nginx:test /app/nginx/new.conf`，则容器启动后，会执行 `nginx -c /app/nginx/new.conf`

  


# 构建镜像
  


创建名称为`Dockerfile`的文件，示例：

  


```dockerfile
FROM ubuntu
MAINTAINER lee<lee@xxx.com>

ENV MYPATH /usr/local
WORKDIR $MYPATH

RUN apt-get update
RUN apt-get install net-tools

EXPOSE 80

CMD echo $MYPATH
CMD echo "install ifconfig cmd into ubuntu success ....."
CMD /bin/bash
```

  


编写完成之后，将其构建成docker镜像。

  


命令：

  


```shell
# 注意：定义的TAG后面有个空格，空格后面有个点
# docker build -t 新镜像名字:TAG .
docker build -t ubuntu:1.0.1 .
```

  


# 虚悬镜像
  


虚悬镜像：仓库名、标签名都是 `<none>`的镜像，称为 dangling images（虚悬镜像）。

  


在构建或者删除镜像时可能由于一些错误导致出现虚悬镜像。

  


例如：

  


```shell
# 构建时候没有镜像名、tag
docker build .
```

  


列出docker中的虚悬镜像：

  


```shell
docker image ls -f dangling=true
```

  


虚悬镜像一般是因为一些错误而出现的，没有存在价值，可以删除：

  


```shell
# 删除所有的虚悬镜像
docker image prune
```

