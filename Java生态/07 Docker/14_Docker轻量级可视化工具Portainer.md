# Docker轻量级可视化工具Portainer

[目录](Docker与微服务实战.md) · 高级篇(大厂进阶)

![配图](images/img-0299.png)

<a id="t-2-6-1"></a>
## 是什么

Portainer 是一款轻量级的应用，它提供了图形化界面，用于方便地管理Docker环境，包括单机环境和集群环境。

<a id="t-2-6-2"></a>
## 安装

<a id="t-2-6-2-1"></a>
### 官网

<a id="t-2-6-2-1-1"></a>
#### https://www.portainer.io/

<a id="t-2-6-2-1-2"></a>
#### https://docs.portainer.io/v/ce-2.9/start/install/server/docker/linux

<a id="t-2-6-2-2"></a>
### 步骤

<a id="t-2-6-2-2-1"></a>
#### docker命令安装

docker run -d -p 8000:8000 -p 9000:9000 --name portainer     --restart=always     -v /var/run/docker.sock:/var/run/docker.sock     -v portainer\_data:/data     portainer/portainer

![配图](images/img-0300.png)

<a id="t-2-6-2-2-2"></a>
#### 第一次登录需创建admin，访问地址：xxx.xxx.xxx.xxx:9000

用户名，直接用默认admin

密码记得8位，随便你写

![配图](images/img-0301.png)

<a id="t-2-6-2-2-3"></a>
#### 设置admin用户和密码后首次登陆

![配图](images/img-0302.png)

<a id="t-2-6-2-2-4"></a>
#### 选择local选项卡后本地docker详细信息展示

![配图](images/img-0303.png)

<a id="t-2-6-2-2-5"></a>
#### 上一步的图形展示，能想得起对应命令吗？

![配图](images/img-0304.png)

<a id="t-2-6-3"></a>
## 登陆并演示介绍常用操作case

---

[上一篇 Compose编排微服务](13b_Compose编排微服务.md) · [目录](Docker与微服务实战.md) · [下一篇 Docker容器监控之 CAdvisor+InfluxDB+Granfana](15_Docker容器监控之%20CAdvisor+InfluxDB+Granfana.md)
