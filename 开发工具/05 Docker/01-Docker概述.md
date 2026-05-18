# Docker简介
Docker是基于Go语言实现的云开源项目。



Docker的主要目标是：`Build, Ship and Run Any App, Anywhere`，也就是通过对应用组件的封装、分发、部署、运行等生命周期的管理，使用户的APP及其运行环境能做到**一次镜像,处处运行**。  


# 传统虚拟机和容器


传统虚拟机（virtual machine）：

传统虚拟机技术基于安装在主操作系统上的虚拟机管理系统（如VirtualBox、VMware等），创建虚拟机（虚拟出各种硬件），在虚拟机上安装从操作系统，在从操作系统中安装部署各种应用。

缺点：资源占用多、冗余步骤多、启动慢



Linux容器（Linux Container，简称LXC）：

Linux容器是与系统其他部分分隔开的一系列进程，从另一个镜像运行，并由该镜像提供支持进程所需的全部文件。容器提供的镜像包含了应用的所有依赖项，因而在从开发到测试再到生产的整个过程中，它都具有可移植性和一致性。



Linux容器不是模拟一个完整的操作系统，而是对进程进行隔离。有了容器，就可以将软件运行所需的所有资源打包到一个隔离的容器中。容器与虚拟机不同，不需要捆绑一整套操作系统，只需要软件工作所需的库资源和设置。系统因此而变得高效轻量并保证部署在任何环境中的软件都能始终如一的运行。

  


![](images/图片1.jpg)

  


对比：

| 特性 | 容器 | 虚拟机 |
| --- | --- | --- |
| 启动 | 秒级 | 分钟级 |
| 大小 | 一般为Mb | 一般为Gb |
| 速度 | 接近原生 | 比较慢 |
| 系统支持数量 | 单机支持上千个容器 | 一般几十个 |


  


# Docker运行速度快的原因
  


Docker有比虚拟机更少的抽象层：

由于Docker不需要Hypervisor（虚拟机）实现硬件资源虚拟化，运行在Docker容器上的程序直接使用的都是实际物理机的硬件资源，因此在CPU、内存利用率上docker有明显优势。

  


Docker利用的是宿主机的内核，而不需要加载操作系统OS内核：

当新建一个容器时，Docker不需要和虚拟机一样重新加载一个操作系统内核。进而避免引寻、加载操作系统内核返回等比较耗时耗资源的过程。当新建一个虚拟机时，虚拟机软件需要加载OS，返回新建过程是分钟级别的。而Docker由于直接利用宿主机的操作系统，则省略了返回过程，因此新建一个docker容器只需要几秒钟。

  


Docker容器的本质就是一个进程。

# Docker软件
Docker并非一个通用的容器工具，它依赖于已经存在并运行的Linux内核环境。（在Windows上安装Docker时需要依赖WSL，也即Windows下的Linux子系统）。

  


Docker实质上是在已经运行的Linux下制造了一个隔离的文件环境，因此它执行的效率几乎等同于所部署的Linux主机。

  


Docker的基本组成部分：

+ 镜像（image）
+ 容器（container）
+ 仓库（repository）

  


## Docker镜像
  


Docker镜像就是一个只读的模板。镜像可以用来创建Docker容器，一个镜像可以创建多个容器。

  


## Docker容器
  


Docker利用容器独立运行的一个或一组应用，应用程序或服务运行在容器里面，容器就类似于一个虚拟化的运行环境，容器是用镜像创建的运行实例。

  


## Docker仓库
  


Docker仓库是集中存放镜像文件的场所。

仓库分为公开仓库和私有仓库两种。

最大的公开仓库是Docker官方的Docker Hub：[https://hub.docker.com/](https://hub.docker.com/)

# Docker架构
Docker是一个 C/S（Client-Server） 结构的系统，后端是一个松耦合架构，众多模块各司其职。

  


Docker守护进程运行在主机上，然后通过Socket连接从客户端访问，守护进程从容器接收命令并管理运行在主机上的容器。

  


![](images/图片2.svg)


Docker运行的基本流程为：

1. 用户是使用Docker Client 与 Docker Daemon 建立通信，并发送请求给后者
2. Docker Daemon 作为 Docker 架构的主体部分，首先提供 Docker Server 的功能使其可以接收 Docker Client 的请求
3. Docker Engine 执行 Docker 内部的一系列工作，每一项工作都是以一个 Job 的形式存在
4. Job 的运行过程中，当需要容器镜像时，则从 Docker Registry 中下载镜像，并通过镜像管理驱动 Graph Driver 将下载镜像以 Graph 的形式存储
5. 当需要为 Docker 创建网络环境时，通过网络管理驱动 Network driver 创建并配置 Docker 容器网络环境
6. 当需要限制 Docker 容器运行资源或执行用户指令等操作时，则通过 Exec driver 来完成
7. Libcontainer 是一项独立的容器管理包，Network driver 以及 Exec driver 都是通过 Libcontainer 来实现具体对容器进行的操作

  


![](images/图片3.png)



> 来自: [01-Docker概述](https://www.yuque.com/tmfl/cloud/rifotq)
>





