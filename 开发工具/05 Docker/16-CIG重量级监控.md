# CIG
通过`docker stats` 命令可以很方便的查看当前宿主机上所有容器的CPU、内存、网络流量等数据，可以满足一些小型应用。

但是 `docker stats` 统计结果只能是当前宿主机的全部容器，数据资料是实时的，没有地方存储、没有健康指标过线预警等功能。

  


CAdvisor（监控收集） + InfluxDB（存储数据） + Granfana（展示图表），合称 `CIG`。

![](images/图片21.png)

  


## CAdvisor
  


CAdvisor是一个容器资源监控工具，包括容器的内存、CPU、网络IO、磁盘IO等监控，同时提供了一个Web页面用于查看容器的实时运行状态。

  


CAdvisor默认存储2分钟的数据，而且只是针对单物理机。不过CAdvisor提供了很多数据集成接口，支持 InfluxDB、Redis、Kafka、Elasticsearch等集成，可以加上对应配置将监控数据发往这些数据库存储起来。

  


CAdvisor主要功能：

+ 展示Host和容器两个层次的监控数据
+ 展示历史变化数据

  


## InfluxDB
  


InfluxDB是用Go语言编写的一个开源分布式时序、事件和指标数据库，无需外部依赖。

  


CAdvisor默认只在本机保存2分钟的数据，为了持久化存储数据和统一收集展示监控数据，需要将数据存储到InfluxDB中。InfluxDB是一个时序数据库，专门用于存储时序相关数据，很适合存储 CAdvisor 的数据。而且 CAdvisor本身已经提供了InfluxDB的集成方法，在启动容器时指定配置即可。

  


InfluxDB主要功能：

+ 基于时间序列，支持与时间有关的相关函数（如最大、最小、求和等）
+ 可度量性，可以实时对大量数据进行计算
+ 基于事件，支持任意的事件数据

  


## Granfana
Grafana是一个开源的数据监控分析可视化平台，支持多种数据源配置（支持的数据源包括InfluxDB、MySQL、Elasticsearch、OpenTSDB、Graphite等）和丰富的插件及模板功能，支持图表权限控制和报警。

  


Granfana主要功能：

+ 灵活丰富的图形化选项
+ 可以混合多种风格
+ 支持白天和夜间模式
+ 多个数据源

  


# 安装部署
1.  编写`docker-compose.yml`服务编排文件 

```yaml
version: '3.1'

volumes:
  grafana_data: {}

services:
  influxdb:
	# tutum/influxdb 相比influxdb多了web可视化视图。但是该镜像已被标记为已过时
    image: tutum/influxdb:0.9
    restart: always
    environment:
      - PRE_CREATE_DB=cadvisor
    ports:
      - "8083:8083"         # 数据库web可视化页面端口
      - "8086:8086"         # 数据库端口
    volumes:
      - ./data/influxdb:/data

  cadvisor:
    image: google/cadvisor:v0.32.0
    links:
      - influxdb:influxsrv
    command:
      - -storage_driver=influxdb
      - -storage_driver_db=cadvisor
      - -storage_driver_host=influxsrv:8086
    restart: always
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:rw
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro

  grafana:
    image: grafana/grafana:8.5.2
    user: '104'
    restart: always
    links:
      - influxdb:influxsrv
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      - HTTP_USER=admin
      - HTTP_PASS=admin
      - INFLUXDB_HOST=influxsrv
      - INFLUXDB_PORT=8086
```

1.  检查语法 

```shell
docker-compose config -q
```

1.  创建并启动容器 

```shell
docker-compose up -d
```

  


容器启动之后：

1.  在浏览器打开InfluxDB数据库的页面： http://xxx.xxx.xxx.xxx:8083，使用命令查看当前数据库中的数据库实例： 

```plain
SHOW DATABASES
```

  
查看其中是否自动创建了我们在配置文件中配置的 `cadvisor` 数据库实例 

1.  在浏览器打开CAdvisor页面：http://xxx.xxx.xxx.xxx8080/，查看当前docker中的cpu、内存、网络IO等统计信息 
2.  在浏览器打开Grafana页面：http://xxx.xxx.xxx.xxx:3000/，默认用户名密码是：`admin`/`admin`。 

  


# Grafana配置
## 添加数据源
在`Configuration`（小齿轮）选项卡中，选择`Data Sources`，添加一个InfluxDB数据源：

+ name：自定义一个数据源名称，例如`InfluxDB`
+ Query Language：查询语言，默认`InfluxQL`即可
+ URL：根据compose中的容器服务名连接，`http://influxdb:8086`
+ database：我们在InfluxDB中创建的数据库实例，`cadvisor`
+ User：InfluxDB的默认用户，`root`
+ Password：`root`

  


保存并测试，可以连通即可

## 添加工作台
1.  在`Create`（加号）选项卡中，选择创建 `Dash Board`工作台。右上角配置中可以配置创建出来的工作台的标题、文件夹等信息。 
2.  在创建出来的工作台中，选择`Add panel`中的`Add a new panel`添加一个新的面板。 
    1. 在右上角`Time series`（时序图）位置可以切换展示的图表样式（柱状图、仪表盘、表格、饼图等等）
    2. 右侧边栏为该图表配置相关信息：标题、描述
    3. 图表下方可以配置该图表展示的数据的查询语句，例如： 
        * FROM：`cpu_usage_total`（Grafana会自动获取InfluxDB数据库中的元数据，可以直接选择对应表名）
        * WHERE：添加一个条件，`container_name=cig-cadvisor-1`
        * ALIAS：配置一个别名，`CPU使用情况汇总`

