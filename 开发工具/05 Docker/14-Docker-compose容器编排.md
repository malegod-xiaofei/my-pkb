# Docker-compose
  


`Docker-Compose` 是 Docker 官方的开源项目，负责实现对Docker容器集群的快速编排。

  


`Docker-Compose`可以管理多个Docker容器组成一个应用。需要定义一个yaml格式的配置文件 `docker-compose.yml`，配置好多个容器之间的调用关系，然后只需要一个命令就能同时启动/关闭这些容器。

  


Docker建议我们每个容器中只运行一个服务，因为Docker容器本身占用资源极少，所以最好是将每个服务单独的分割开来。但是如果我们需要同时部署多个服务，每个服务单独构建镜像构建容器就会比较麻烦。所以 Docker 官方推出了 `docker-compose` 多服务部署的工具。

  


Compose允许用户通过一个单独的 `docker-compose.yml` 模板文件来定义一组相关联的应用容器为一个项目（`project`）。可以很容易的用一个配置文件定义一个多容器的应用，然后使用一条指令安装这个应用的所有依赖，完成构建。

  


核心概念：

+ 服务（`service`）：一个个应用容器实例
+ 工程（`project`）：由一组关联的应用容器组成的一个完整业务单元，在`docker-compose.yml`中定义

  


Compose使用的三个步骤：

1. 编写 Dockerfile 定义各个应用容器，并构建出对应的镜像文件
2. 编写 `docker-compose.yml`，定义一个完整的业务单元，安排好整体应用中的各个容器服务
3. 执行 `docker-compose up` 命令，其创建并运行整个应用程序，完成一键部署上线

  


# 安装Docker-Compose
  


`Docker-Compose`的版本需要和Docker引擎版本对应，可以参照官网上的[对应关系](https://docs.docker.com/compose/compose-file/compose-file-v3/)。

  


安装Compose：

```shell
# 例如从github下载 2.5.0版本的docker-compose
# 下载下来的文件放到 /usr/local/bin目录下，命名为 docker-compose
curl -L https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

# 添加权限
chmod +x /usr/local/bin/docker-compose

# 验证
docker-compose version
```

  


卸载Compose：直接删除 `usr/local/bin/docker-compose`文件即可

  


# 常用命令
  


执行命令时，需要在对应的`docker-compose.yml`文件所在目录下执行。

  


查看帮助：

```shell
docker-compose -h
```

  


创建并启动`docker-compose`服务：（类似 `docker run`）

```shell
docker-compose up

# 后台运行
docker-compose up -d
```

  


停止并删除容器、网络、卷、镜像：（类似 `docker stop` +  `docker rm`）

```shell
docker-compose down
```

  


进入容器实例内部：

```shell
docker-compose exec <yml里面的服务id> /bin/bash
```

  


展示当前`docker-compose`编排过的运行的所有容器：

```shell
docker-compose ps
```

  


展示当前`docker-compose`编排过的容器进程：

```shell
docker-compose top
```

  


查看容器输出日志：

```shell
docker-compose log <yml里面的服务id>
```

  


检查配置：

```shell
docker-compose config

# 有问题才输出
docker-compose config -q
```

  


重启服务：

```shell
docker-compose restart
```

  


启动服务：（类似 `docker start`）

```shell
docker-compose start
```

  


停止服务：

```shell
docker-compose stop
```

  


# compose编排实例
  


示例：

```yaml
# docker-compose文件版本号
version: "3"

# 配置各个容器服务
services:
  microService:
    image: springboot_docker:1.0
    container_name: ms01  # 容器名称，如果不指定，会生成一个服务名加上前缀的容器名
    ports:
      - "6001:6001"
    volumes:
      - /app/microService:/data
    networks:
      - springboot_network
    depends_on:  # 配置该容器服务所依赖的容器服务
      - redis
      - mysql

  redis:
    image: redis:6.0.8
    ports:
      - "6379:6379"
    volumes:
      - /app/redis/redis.conf:/etc/redis/redis.conf
      - /app/redis/data:/data
    networks:
      - springboot_network
    command: redis-server /etc/redis/redis.conf

  mysql:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: '123456'
      MYSQL_ALLOW_EMPTY_PASSWORD: 'no'
      MYSQL_DATABASE: 'db_springboot'
      MYSQL_USER: 'springboot'
      MYSQL_PASSWORD: 'springboot'
    ports:
      - "3306:3306"
    volumes:
      - /app/mysql/db:/var/lib/mysql
      - /app/mysql/conf/my.cnf:/etc/my.cnf
      - /app/mysql/init:/docker-entrypoint-initdb.d
    networks:
      - springboot_network
    command: --default-authentication-plugin=mysql_native_password # 解决外部无法访问

networks:
  # 创建 springboot_network 网桥网络
  springboot_network:
```

  


编写完成`docker-compose.yml`后，进行语法检查：

```shell
# 进行语法检查
docker-compose config -q
```

  


如果语法检查没有任何问题，进行创建、启动：

```shell
docker-compose up -d
```

