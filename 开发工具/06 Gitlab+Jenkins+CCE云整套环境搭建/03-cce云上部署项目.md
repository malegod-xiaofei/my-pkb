# 检查CCE云上镜像仓库
在Jenkins编译打包之后，会生成Docker镜像并推送到CCE镜像仓库中，CCE云上便可以进行项目部署。

检查镜像是否已经被成功放到CCE镜像仓库中：

1. 登录CCE，进入`镜像仓库`-`镜像管理`
2. 列表的右上角镜像空间选择项目的`myproject`
3. 查看已经被推送到CCE上的镜像名称和镜像版本

  


# 配置配置项（ConfigMap）
后台代码中的，有些配置文件需要改动的，可以放到ConfigMap中，例如：

+ `app-web`模块的`context.xml`需要修改数据源配置
+ `system-server`模块的`application-dev.properties`配置文件需要修改数据源、IP等配置

  


## application-dev.properties配置到ConfigMap
1. 登录CCE ，进入`配置中心` - `配置项（ConfigMap）`
2. 添加配置项
3. 名称任意起，例如`system-server-dev`
4. 项目选择项目`myproject`
5. `数据`-`添加更多数据`。（也可以从文件读取，但是从文件读取时无法修改key）  
输入键`application-dev.properties`（即文件名），将程序中的`application-dev.properties`文件的内容贴到值中。

  


`application-dev.properties`配置文件内容：

其中，`spring.redis.password`、`spring.datasource.username`、`spring.datasource.password`改为读取系统环境变量中的值。系统环境变量会通过`secret`进行绑定

```properties
# 添加修改jsp文件后热更新
server.servlet.jsp.init-parameters.development=true
server.port=8093
# 配置秘钥
#Jasypt.encryptor.password=als9
#指定redis的库
spring.redis.database=1
#指定redis服务的端口号
spring.redis.port=6379
#指定redis服务的主机ip
spring.redis.host=192.168.xxx.xxx
#指定redis服务的密码
spring.redis.password=${REDIS_PASSWORD}

#---------------------------------------- mysql连接池配置 ------------------------------------------
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.jdbc-url=jdbc:mysql://192.168.xxx.xxx:8306/myproject
spring.datasource.username=${MYSQL_USERNAME}
spring.datasource.password=${MYSQL_PASSWORD}
spring.datasource.minimumIdle=2
spring.datasource.maximumPoolSize=5
spring.datasource.idleTimeout=2000
spring.datasource.maxLifetime=1800000
spring.datasource.leakDetectionThreshold=180000
```

  


## context.xml配置到ConfigMap
1. 登录CCE ，进入`配置中心` - `配置项（ConfigMap）`
2. 添加配置项
3. 名称任意起，例如`system-server-dev`
4. 项目选择项目`myproject`
5. `数据`-`添加更多数据`。（也可以从文件读取，但是从文件读取时无法修改key）  
输入键`context.xml`（即文件名），将程序中`context.xml`的文件内容贴到值中。

  


```xml
<?xml version="1.0" encoding="UTF-8"?>
<Context>

    <Resource name="jdbc/default" auth="Container"
              type="javax.sql.DataSource" maxTotal="30" maxIdle="10" maxWaitMillis="100000"
              testOnBorrow="ture" validationQuery="select 1 from dual"
              removeAbandonedOnBorrow="true" removeAbandonedTimeout="60000"
              logAbandoned="true" username="myproject" password="myproject"
              driverClassName="com.mysql.cj.jdbc.Driver"
              url="jdbc:mysql://192.168.xxx.xxx:8306/myproject?autoReconnect=true" />
</Context>
```

  


# 配置密钥（secret）
`application-dev.properties`中会读取容器的系统环境变量的数据库用户名密码，容器的这几个敏感系统环境变量会从密钥中导入。

步骤：

1. 登录CCE，进入`配置中心`-`密钥(secret)`
2. 添加密钥
3. 名称任意起，例如`secret-database`
4. 项目选择项目`myproject`
5. 密钥类型`Opaque`
6. `数据`中添加以下配置：

| 键              | 值（base64加密后的值） |
| -------------- | -------------- |
| MYSQL_USERNAME | bXlwcm9qZWN0   |
| MYSQL_PASSWORD | bXlwcm9qZWN0   |
| REDIS_PASSWORD | bXlwcm9qZWN0   |


此处配置的值是经过base64加密后的值。

配置到系统环境变量中之后，系统环境变量读取到的是解密后的原始值。

  


# 后台项目部署
微服务模块都可以配置为 无状态（Development）类型的工作负载。

根据规划，系统的后台采用1个负载2个副本方式部署，所以需要将`app-web`模块、`systmer-server`模块打到同一个负载中。

故采用以下方案：

+ 部署一个后台development，里面的pod中带有两个容器
+ 部署一个前端development，里面的pod中放前端容器

  


## 创建Development
登录CCE，进入`工作负载`-`无状态（Development）`	，`创建无状态工作负载`。

## 基本信息
配置基本信息：

名称：`	myproject`

项目：选择项目`myproject`

实例数量：2个

  


## 容器设置
部署两个容器，一个运行`app-web`的镜像，一个运行`systmer-server`的镜像

以下以`app-web`镜像所在容器为例。

### 基本信息
镜像：选择镜像，选择Jenkins打包上传的镜像、该镜像最新一个版本号。例如`app-web:20240718-153330`

容器名称：改为方便识别的，例如：`container-app`

配置CPU、内存初始大小，以及最大CPU、最大内存限制。

  


### 数据存储
因为`app-web`的`context.xml`配置在ConfigMap中，可以在数据存储这里配置，替换掉容器内的tomcat的`tomcat/conf/context.xml`。

1. `添加本地磁盘`
2. 存储类型：选择`配置项（ConfigMap）`
3. 配置项：选择我们前面创建的配置项`context-dev`
4. 挂载路径：`/usr/local/tomcat/conf/context.xml`
5. `context.xml`并不是文件夹，且我们只是替换`conf`文件夹中的`context.xml`这一个文件，不改变其他文件，所以还需要配置`子路径`
6. 子路径：`context.xml`。（声明我们只是要替换容器内`/usr/local/tomcat/conf/`下的`context.xml`这一个文件）
7. 权限：只读即可

  


### 环境变量
`system-server`模块的配置文件中，数据库用户名、密码读取的是环境变量。另外，还需要将pod的名称作为环境变量传入，用于生成全局唯一流水号。

环境变量类型：

+ 手动添加：手动指定环境变量名和值
+ 配置项导入：读取指定的`ConfigMap`，将其中的键值作为环境变量导入
+ 配置项键值导入：读取指定的`ConfigMap`的指定项的值，环境变量名称自定义
+ 密钥导入：读取指定的`secret`，将其中的键值作为环境变量导入
+ 密钥键值导入：读取指定的`secret`的指定项的值，环境变量名称自定义
+ 变量/变量引用：将pod的相关属性作为环境变量传入
+ 资源引用：读取指定容器的cpu限制个数等资源作为值，环境变量名称自定义

添加以下环境变量：

| 类型 | 变量 | 值 |
| --- | --- | --- |
| 变量/变量引用 | POD_NAME | metadata.name |
| 变量/变量引用 | POD_ID | metadata.uid |
| 密钥键值导入 | MYSQL_USERNAME | secret-database / MYSQL_USERNAME |
| 密钥键值导入 | MYSQL_PASSWORD | secret-database / MYSQL_PASSWORD |
| 密钥键值导入 | REDIS_PASSWORD | secret-database / REDIS_PASSWORD |


### 生命周期、健康检查、安全设置
根据需要可以自己配置生命周期钩子脚本、存活探针、容器内注入的环境变量等配置

  


### 新增一个容器
新增一个容器用来部署`system-server`镜像，与`app-web`模块几乎一致，只是挂载的ConfigMap不同。

需要将配置的ConfigMap `system-server-dev` 挂载到 ` /usr/src/system-server/application-dev.properties`，子路径配置为`application-dev.properties`。

  


## 访问设置
添加服务。服务名称任意起，例如`service-myproject`。

访问方式：根据情况选择`集群内访问`或`NodePort`访问。

如果配置为`集群内访问`，则无法直接连到该节点。如果配置为`NodePort`则可以直接访问。  
我们后面会配置Ingress，所以此处配置成`集群内访问`。

  


端口配置：

配置容器暴露的端口：

+ `app-web`暴露的是tomcat的8080。服务端口也可以直接填8080。
+ `system-server`暴露的是springboot的8093。服务端口也配置为8093。

  


## 高级设置
升级方式：配置滚动升级或是替换升级。

我们部署的开发环境是为了看修改代码之后的效果，所以选择替换升级。

  


因为192.168.1.108节点环境和其他不一致，分配到108上的容器都启动不了，所以部署时需要配置调整策略，来排除掉108节点。

调整策略：添加反亲和对象 - 节点 - 勾选 `node-108`

  


# 前端项目部署
VUE前端项目部署和后台部署几乎一致，不需要挂载配置文件，只需要一个容器即可。

  


# 配置Ingress
正式发布项目时，行方会提供F5转发到K8S集群，不需要再配置Ingress。

只用作开发使用。

使用Ingress作为Nginx转发服务到集群内的Pod。

登录CCE，进入`资源管理`-`网络管理`-`Ingresses`，点击`添加Ingress`。

Ingress名称：`ingress-myproject`

项目：项目`myproject`

负载均衡器：默认的`global(全局nginx-ingress)`

协议：`http`

域名：没有，不写

路由配置：

| 映射URL | 服务名称 | 服务端口 |
| --- | --- | --- |
| /myproject/SYS | service-myproject | 8093 |
| /myproject | service-myproject | 8080 |
| /vue | service-vue | 80 |


路径类型统一默认的`ImplementationSpecific`。

高级设置中，后端协议`HTTP`。

提交即可。

  


配置好之后，Ingresses列表中会显示该Ingress的访问地址（一组地址），随便挑其中一个连接访问即可。

