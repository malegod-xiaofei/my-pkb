# Docker 网络
  


docker安装并启动服务后，会在宿主机中添加一个虚拟网卡。

  


在Docker服务启动前，使用 `ifconfig` 或 `ip addr` 查看网卡信息：

  


+ `ens33`或`eth0`：本机网卡
+ `lo`：本机回环网络网卡
+ 可能有`virbr0`（CentOS安装时如果选择的有相关虚拟化服务，就会多一个以网桥连接的私网地址的`virbr0`网卡，作用是为连接虚拟网卡提供NAT访问外网的功能。如果要移除该服务，可以使用 `yum remove libvirt-libs.x86_64`）

  


使用 `systemctl start docker`启动Docker服务后，会多出一个 `docker0` 网卡。

  


作用：

  


+ 容器间的互联和通信以及端口映射
+ 容器IP变动时候可以通过服务名直接网络通信而不受到影响

  


Docker容器的网络隔离，是通过Linux内核特性 `namespace`和 `cgroup` 实现的。

  


# docker网络命令
  


查看Docker网络模式：

  


```shell
docker network ls
```

  


如果没有修改过docker network，则默认有3个网络模式：

  


+ `bridge`
+ `host`
+ `none`

  


添加Docker网络：

  


```shell
docker network add xxx
```

  


删除Docker网络：

  


```shell
docker network rm xxx
```

  


查看网络元数据：

  


```shell
docker network inspect xxx
```

  


删除所有无效的网络：

  


```shell
docker network prune
```

  


# Docker 网络模式
  


Docker 的网络模式：

| 网络模式 | 简介 | 使用方式 |
| --- | --- | --- |
| bridge | 为每一个容器分配、设置IP等，并将容器连接到一个`docker0`<br/>虚拟网桥，默认为该模式 | `--network bridge` |
| host | 容器将不会虚拟出自己的网卡、配置自己的IP等，而是使用宿主机的IP和端口 | `--network host` |
| none | 容器有独立的 Network namespace，但并没有对齐进行任何网络设置，如分配 `veth pari`<br/>和 网桥连接、IP等 | `--network none` |
| container | 新创建的容器不会创建自己的网卡和配置自己的IP，而是和一个指定的容器共享IP、端口范围等 | `--network container:NAME或者容器ID` |


  


查看某个容器的网络模式：

  


```shell
# 通过inspect获取容器信息，最后20行即为容器的网络模式信息
docker inspect 容器ID | tail -n 20
```

  


# docker0
  


Docker 服务默认会创建一个`docker0`网桥（其上有一个`docker0`内部接口），该桥接网络的名称为 `docker0`，它在内核层连通了其他的物理或虚拟网卡，这就将所有容器和本地主机都放到同一个物理网络。

  


Docker默认指定了`docker0`接口的IP地址和子网掩码，让主机和容器之间可以通过网桥互相通信。

  


查看`bridge`网络的详细信息，并通过`grep`获取名称：

  


```shell
docker network inspect bridge | grep name
```

  


可以看到其名称为`docker0`。

  


# bridge模式
  


Docker使用Linux桥接，在宿主机虚拟一个`Docker`容器网桥（`docker0`），Docker启动一个容器时会根据`Docker`网桥的网段分配给容器一个IP地址，称为`Container-IP`，同时Docker网桥是每个容器的默认网关。因为在同一个宿主机内的容器接入同一个网桥，这样容器之间就能够通过容器的`Container-IP`直接通信。

  


`docker run`的时候，没有指定`--network`的话，默认使用的网桥模式就是`bridge`，使用的就是`docker0`。在宿主机`ifconfig`就可以看到`docker0`和自己`create`的`network`。

  


网桥`docker0`创建一对对等虚拟设备接口，一个叫`veth`，另一个叫`eth0`，成对匹配：

  


整个宿主机的网桥模式都是`docker0`，类似一个交换机有一堆接口，每个接口叫 `veth`，在本地主机和容器内分别创建一个虚拟接口，并让他们彼此联通（这样一对接口叫做 `veth pair`）。

  


每个容器实例内部也有一块网卡，容器内的网卡接口叫做`eth0`。

  


`docker0`上面的每个`veth`匹配某个容器实例内部的`eth0`，两两配对，一一匹配。

  


![](images/图片18.webp)


例如：

  


启动tomcat容器，进入tomcat容器后，执行 `ip addr`，可以看到其网卡信息：

  


```plain
1: lo ..................

容器内的网卡为 eth0
@符号后面就是宿主机上对应的veth网卡的编号28
27: eth0@if28 ...............................
```

  


在宿主机执行 `ip addr` 查看宿主机网卡信息：

  


```plain
每个veth都有个编号：vethXXXXXX
@符号后面对应就是容器内的eth0网卡编号27

28: vethXXXXXX@if27  ................
```

  


# host模式
  


直接使用宿主机的 IP 地址与外界进行通信，不再需要额外进行 NAT 转换。

  


容器将不会获得一个独立的 Network Namespace，而是和宿主机共用一个 Network space。

  


容器将不会虚拟出自己的网卡，而是直接使用宿主机的 IP 和端口。

  


![](images/图片19.webp)


如果在 `docker run` 命令中同时使用了 `--network host` 和 `-p`端口映射，例如：

  


```shell
docker run -p 8082:8080 --network host tomcat
```

  


那么会出现一个警告：

  


```plain
WARNING: Published ports are discarded when using host network mode
```

  


因为此时已经使用了`host`模式，本身就是直接使用的宿主机的IP和端口，此时的`-p`端口映射就没有了意义，也不会生效，端口号还是会以主机端口号为主。

  


正确做法是：不再进行`-p`端口映射，或者改用`bridge`模式

  


# none模式
  


禁用网络功能。

  


在`none`模式下，并不为docker容器进行任何网络配置。进入容器内，使用 `ip addr`查看网卡信息，只能看到 `lo`（本地回环网络`127.0.0.1`网卡）。

  


# container模式
  


新建的容器和已经存在的一个容器共享网络IP配置，而不是和宿主机共享。

  


新创建的容器不会创建自己的网卡、IP，而是和一个指定的容器共享IP、端口范围。两个容器除了网络共享，其他的如文件系统、进程列表依然是隔离的。

  


![](images/图片20.webp)


示例：

  


```shell
docker run -it --name alpine1 alpine /bin/sh

# 指定和 alpine1 容器共享网络
docker run -it --network container:alpine1 --name alpine2 alpine /bin/sh
```

  


此时使用 `ip addr`查看两台容器的网络，会发现两台容器的`eth0`网卡内的IP等信息完全相同。

  


如果关掉了`alpine1`容器，因为`alpine2`的网络使用的`alpine1`共享网络，所以关掉`alpin1`后，`alpine2`的`eth0`网卡也随之消失了。

  


# 自定义网络
  


容器间的互联和通信以及端口映射。

  


容器 IP 变动时候可以通过服务名直接网络通信而不受影响。（类似Eureka，通过服务名直接互相通信，而不是写死IP地址）。

  


docker中还有一个 `--link` 进行容器网络互联，但是已经被标记为过时的，可能会在将来的版本中移除这个功能。推荐使用自定义网络替换link。

  


自定义桥接网络（自定义网络默认使用的是桥接网络 `bridge`）：

  


1.  新建自定义网络 

```shell
docker network create tomcat_network
```

1.  查看网络列表 

```shell
docker network ls
```

1.  创建容器时，指定加入我们自定义的网络中 

```shell
docker run -d -p 8081:8080 --network tomcat_network --name tomcat1 tomcat:8.5-jdk8-corretto

docker run -d -p 8082:8080 --network tomcat_network --name tomcat2 tomcat:8.5-jdk8-corretto
```

1.  此时进入`tomcat1`中，使用`ping`命令测试连接`tomcat2`容器名，发现可以正常连通 

```shell
# 安装ifconfig命令
yum install -y net-tools
# 安装ip addr命令
yum install -y iproute
# 安装ping命令
yum install -y iputils

# 直接ping容器名，不需要ping IP地址
ping tomcat2
```

  


# link连接
  


示例：

  


```shell
# 启动一台mysql容器
# --name 为容器指定一个别名
docker run --name mysql-matomo -p 3308:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0.28

# 启动另一个容器，通过--link连接到mysql容器
# --link 容器名称:本容器连接对方时的别名
docker run -d -p 8888:80 --link mysql-matomo:db --name matomo matomo:4.9.0

# 此时，在matomo容器中，便可以通过 db 这个hostname连接到mysql-matomo容器，而无须再通过ip
# 连接地址：db:3306
```

