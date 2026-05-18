# Portainer：Docker轻量级可视化工具
  


Portainer是一款轻量级的应用，它提供了图形化界面，用于方便地管理Docker环境，包括单机环境和集群环境。

  


Portainer分为开源社区版（CE版）和商用版（BE版/EE版）。

  


# 安装
  


Portainer也是一个Docker镜像，可以直接使用Docker运行。

  


```shell
# 旧版镜像地址为portainer/portainer，从2022年1月标记为过期
# 新版镜像地址为portainer/portainer-ce

# --restart=always 如果Docker引擎重启了，那么这个容器实例也会在Docker引擎重启后重启，类似开机自启
docker run -d -p 8000:8000 -p 9000:9000 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.13.0-alpine
```

  


启动之后，便可以在浏览器中进行访问：[http://xxx.xxx.xxx.xxx:9000](http://xxx.xxx.xxx.xxx:9000)

  


首次进来时，需要创建 admin 的用户名（默认`admin`）、密码（必须满足校验规则，例如`portainer.io123`）。

  


选择 `local`管理本地docker，即可看到本地Docker的详细信息，包括其中的镜像（images）、容器（containers）、网络（networks）、容器卷（volumes）、compose编排（stacks）等等。

