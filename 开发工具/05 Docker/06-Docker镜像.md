# 镜像
  


镜像是一种轻量级、可执行的独立软件包，它包含运行某个软件所需的所有内容，我们把应用程序和配置依赖打包好行程一个可交付的运行环境（包括代码、运行时需要的库、环境变量和配置文件等），这个打包好的运行环境就是image镜像文件。

  


# Docker 镜像加载原理
  


## 联合文件系统
  


Docker 中的文件存储驱动叫做 storage driver。

  


Docker 最早支持的stotage driver是 AUFS，它实际上由一层一层的文件系统组成，这种层级的文件系统叫UnionFS。

  


联合文件系统（UnionFS）：Union 文件系统，是一种分层、轻量级并且高性能的文件系统，它支持对文件系统的修改作为一次提交来一层层的叠加，同时可以将不同目录挂载到同一个虚拟文件系统下（unite serveral directories into a single virtual filesystem）。

  


Union文件系统是Docker镜像的基础。镜像可以通过分层来进行集成，基于基础镜像可以制作具体的应用镜像。

  


特性：一次同时加载多个文件系统，但从外面看起来，只能看到一个文件系统，联合加载会把各层文件系统叠加起来，这样最终的文件系统会包含所有底层的文件和目录。

  


后来出现的docker版本中，除了AUFS，还支持OverlayFS、Btrfs、Device Mapper、VFS、ZFS等storage driver。

  


## bootfs和rootfs
  


bootfs（boot file system）主要包含 bootloader 和 kernel，bootloader主要是引导加载 kernel，Linux刚启动时会加载bootfs文件系统。

  


在Docker镜像的最底层是引导文件系统bootfs。这一层与我们典型的Linux/Unix系统是一样的，包含boot加载器和内核。当boot加载完成之后整个内核就都在内存中了，此时内存的使用权已经由 bootfs 转交给内核，此时系统也会卸载 bootfs。

  


rootfs（root file system），在bootfs之上，包含的就是典型Linux系统中的 `/dev`、`/proc`、`/bin`、`/etc`等标准目录和文件。rootfs就是各种不同的操作系统发行版，比如Ubuntu、CentOS等。

  


docker镜像底层层次：

  


![](images/图片5.jpg)

  


对于一个精简的OS，rootfs可以很小，只需要包括最基本的命令、工具和程序库就可以了，因为底层直接使用Host的Kernel，自己只需要提供rootfs就可以。所以，对于不同的Linux发行版，bootfs基本是一致的，rootfs会有差别，不同的发行版可以共用bootfs。

  


有差别的rootfs：

  


![](images/图片6.jpg)

  


## 镜像分层
  


Docker支持扩展现有镜像，创建新的镜像。新镜像是从base镜像一层一层叠加生成的。

  


例如：

  


```dockerfile
# Version: 0.0.1
FROM debian  # 直接在debain base镜像上构建
MAINTAINER mylinux
RUN apt-get update && apt-get install -y emacs # 安装emacs
RUN apt-get install -y apache2 # 安装apache2
CMD ["/bin/bash"] # 容器启动时运行bash
```

  


镜像创建过程：

  


![](images/图片7.png)

  


# 镜像分层的优势
  


镜像分层的一个最大好处就是共享资源，方便复制迁移，方便复用。

  


# 容器层
  


当容器启动时，一个新的**可写层**将被加载到镜像的顶部，这一层通常被称为`容器层`，容器层之下的都叫`镜像层`。

  


所有对容器的改动，无论添加、删除、还是修改文件都只会发生在容器层中。

  


只有容器层是可写的，容器层下面的所有镜像层都是只读的。

  


如图：

  


![](images/图片8.jpg)

