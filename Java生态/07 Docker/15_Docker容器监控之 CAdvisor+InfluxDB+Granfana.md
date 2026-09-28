# Docker容器监控之 CAdvisor+InfluxDB+Granfana

[目录](Docker与微服务实战.md) · 高级篇(大厂进阶)

![配图](images/img-0305.png)

<a id="t-2-7-1"></a>
## 原生命令

<a id="t-2-7-1-1"></a>
### 操作

![配图](images/img-0306.png)

**docker stats命令的结果**

![配图](images/img-0307.png)

<a id="t-2-7-1-2"></a>
### 问题

通过docker stats命令可以很方便的看到当前宿主机上所有容器的CPU,内存以及网络流量等数据，**一般小公司够用了。。。。**

但是，

docker stats统计结果只能是当前宿主机的全部容器，数据资料是实时的，没有地方存储、没有健康指标过线预警等功能

<a id="t-2-7-2"></a>
## 是什么

<a id="t-2-7-2-1"></a>
### 容器监控3剑客

<a id="t-2-7-2-1-1"></a>
#### 一句话

![配图](images/img-0308.png)

- CAdvisor监控收集+InfluxDB存储数据+Granfana展示图表
<a id="t-2-7-2-1-2"></a>
#### CAdvisor

![配图](images/img-0309.png)

<a id="t-2-7-2-1-3"></a>
#### InfluxDB

![配图](images/img-0310.png)

<a id="t-2-7-2-1-4"></a>
#### Granfana

![配图](images/img-0311.png)

<a id="t-2-7-2-1-5"></a>
#### 总结

![配图](images/img-0312.png)

<a id="t-2-7-3"></a>
## compose容器编排，一套带走

<a id="t-2-7-3-1"></a>
### 新建目录

![配图](images/img-0313.png)

<a id="t-2-7-3-2"></a>
### 新建3件套组合的 docker-compose.yml

version: '3.1'

volumes:

grafana\_data: {}

services:

influxdb:

image: tutum/influxdb:0.9

restart: always

environment:

\- PRE\_CREATE\_DB=cadvisor

ports:

\- "8083:8083"

\- "8086:8086"

volumes:

\- ./data/influxdb:/data

cadvisor:

image: google/cadvisor

links:

\- influxdb:influxsrv

command: -storage\_driver=influxdb -storage\_driver\_db=cadvisor -storage\_driver\_host=influxsrv:8086

restart: always

ports:

\- "8080:8080"

volumes:

\- /:/rootfs:ro

\- /var/run:/var/run:rw

\- /sys:/sys:ro

\- /var/lib/docker/:/var/lib/docker:ro

grafana:

user: "104"

image: grafana/grafana

user: "104"

restart: always

links:

\- influxdb:influxsrv

ports:

\- "3000:3000"

volumes:

\- grafana\_data:/var/lib/grafana

environment:

\- HTTP\_USER=admin

\- HTTP\_PASS=admin

\- INFLUXDB\_HOST=influxsrv

\- INFLUXDB\_PORT=8086

\- INFLUXDB\_NAME=cadvisor

\- INFLUXDB\_USER=root

\- INFLUXDB\_PASS=root

<a id="t-2-7-3-3"></a>
### 启动docker-compose文件

<a id="t-2-7-3-3-1"></a>
#### docker-compose up

![配图](images/img-0314.png)

![配图](images/img-0315.png)

<a id="t-2-7-3-4"></a>
### 查看三个服务容器是否启动

![配图](images/img-0316.png)

<a id="t-2-7-3-5"></a>
### 测试

<a id="t-2-7-3-5-1"></a>
#### 浏览cAdvisor收集服务，http://ip:8080/

![配图](images/img-0317.png)

- 第一次访问慢，请稍等
- cadvisor也有基础的图形展现功能，这里主要用它来作数据采集
<a id="t-2-7-3-5-2"></a>
#### 浏览influxdb存储服务，http://ip:8083/

<a id="t-2-7-3-5-3"></a>
#### 浏览grafana展现服务，http://ip:3000

- ip+3000端口的方式访问,默认帐户密码（admin/admin）

  ![配图](images/img-0318.png)
- 配置步骤
  - 配置数据源

    ![配图](images/img-0319.png)
  - 选择influxdb数据源

    ![配图](images/img-0320.png)
  - 配置细节
    - 1

      ![配图](images/img-0321.png)
    - 2

      ![配图](images/img-0322.png)

      ![配图](images/img-0323.png)
  - 配置面板panel
    - 1

      ![配图](images/img-0324.png)
    - 2

      ![配图](images/img-0325.png)
    - 3

      ![配图](images/img-0326.png)
    - 4

      ![配图](images/img-0327.png)
    - 5

      ![配图](images/img-0328.png)
    - 6

      ![配图](images/img-0329.png)
  - 到这里cAdvisor+InfluxDB+Grafana容器监控系统就部署完成了

---

[上一篇 Docker轻量级可视化工具Portainer](14_Docker轻量级可视化工具Portainer.md) · [目录](Docker与微服务实战.md) · [下一篇 终章の总结](16_终章の总结.md)
