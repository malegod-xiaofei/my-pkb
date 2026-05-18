# Mysql环境搭建
## Docker镜像
Mysql的官方镜像中，当前的LTS版本是8.4.1，基于的Linux版本是Oracle Linux9，但是客户提供的服务器的CPU不支持 x86_64 V2，只支持 x86_64，所以不能使用该版本。故采用 8.4.0-oraclelinux8 版本的镜像。

```shell
docker pull mysql:8.4.0-oraclelinux8
```

  


## 准备映射的容器卷
Mysql需要映射出来的容器卷有：

+ `/var/log/mysql`：存储日志信息
+ `/var/lib/mysql`：存储数据库数据
+ `/etc/mysql/conf.d`：存储配置信息
+ `/root/mysql_workspace/mysql-files`：用于mysql的`LOAD DATA INFILE`导入数据

  


准备对应文件夹：

```shell
mkdir -p /root/mysql_workspace/log
mkdir -p /root/mysql_workspace/data
mkdir -p /root/mysql_workspace/conf
mkdir -p /root/mysql_workspace/mysql-files
```

  


## 准备配置文件
在`/root/mysql_workspace/conf`文件夹（即映射到容器的`/etc/mysql/conf.d`文件夹）中创建MySql的配置文件`my.cnf`：

```properties
[client]
default-character-set=utf8mb4 
[mysqld]
collation_server = utf8mb4_bin
character_set_server = utf8mb4
skip-name-resolve 
log_bin_trust_function_creators=1
lower_case_table_names=1
max_connections=500
table_open_cache=10000
group_concat_max_len=100000
# innodb日志文件大小,不要超过可用内存的一半
innodb_log_file_size = 2G
# 缓存池大小，一般设置为可用内存的60% - 80%
innodb_buffer_pool_size = 4G
# 开启慢查询日志,慢查询时间阈值设置为5秒，日志路径设置到/var/lib/mysql下
slow_query_log = 1
long_query_time = 5
slow_query_log_file = /var/lib/mysql/slow_query.log
# bin日志保存时间（天,旧版5.x的mysql可用）
expire_logs_days = 3
# bin日志保存时间（秒，8.x的mysql可用）
binlog_expire_logs_seconds=86400
```

  


## 启动容器
启动`mysql-master`容器：

```shell
docker run -d \
  -p 8306:3306 \
  --name mysql-master \
  --privileged=true \
  --restart always \
  -v /root/mysql_workspace/log:/var/log/mysql \
  -v /root/mysql_workspace/data:/var/lib/mysql \
  -v /root/mysql_workspace/conf:/etc/mysql/conf.d \
  -v /root/mysql_workspace/mysql-files:/var/lib/mysql-files \
  -e MYSQL_ROOT_PASSWORD=root \
  mysql:8.4.0-oraclelinux8
```

  


# 预警Mysql数据库导入
## 创建用户和数据库
进入容器：

```shell
docker exec -it mysql-master /bin/sh
```

使用root用户登录数据库：

```shell
mysql -uroot -proot
```

创建用户、数据库、授权：

```plain
create user 'myproject'@'%' identified by 'myproject';  -- 创建用户
create database myproject character set utf8mb4  DEFAULT COLLATE utf8mb4_bin;  -- 创建数据库，使用utf8mb4编码，排列方式采用utf8mb4_bin（区分大小写的排列方式）

grant all privileges on myproject.* to 'myproject'@'%';  -- 授权myproject用户对myproject库的权限
-- sql文件中，创建的function需要使用super权限
grant SUPER on *.* to 'myproject'@'%';   -- 授权SUPER权限时，需要授权*.*
grant SYSTEM_USER on *.* to 'myproject'@'%';   
grant select on mysql.help_topic to 'myproject'@'%';  -- 授权使用行转列函数
GRANT FILE ON *.* TO 'myproject'@'%'; -- 授权做Load data infile
-- 刷新权限
flush privileges;

-- 查看授权
SHOW GRANTS FOR 'myproject'@'%';
```

  


## 导入数据
将公司产品的`myproject.sql`文件上传到服务器上，导入到`mysql-master`容器中：

```shell
docker cp myproject.sql mysql-master:/
```

进入docker容器：

```shell
docker exec -it mysql-master bash
```

使用`myproject`用户登录：

```shell
# -u用户名 -p密码 数据库名 -A快速打开（不加该参数时mysql会先读取一遍这个库的所有表用于提示）
mysql -umyproject -pmyproject myproject -A
```

使用`myproject`数据库，导入：

```sql
use myproject;
source /myproject.sql
```

  


# 程序应用中配置连接
`context.xml`：

```xml
<Resource name="jdbc/default" auth="Container"
              type="javax.sql.DataSource" maxTotal="30" maxIdle="10" maxWaitMillis="100000"
              testOnBorrow="false" validationQuery="select 1" testWhileIdle="true" timeBetweenEvictionRunsMillis="30000" numTestsPerEvictionRun="10"
              removeAbandonedOnBorrow="true" removeAbandonedTimeout="60000"
              logAbandoned="true" username="myproject" password="myproject"
              driverClassName="com.mysql.cj.jdbc.Driver"
              url="jdbc:mysql://192.168.xxx.xxx:8306/myproject?autoReconnect=true" />
```

  


# 数据库备份
## 导出
Mysql使用`mysqldump`进行数据库备份。

常用语句示例：

```shell
# 备份全部数据库的数据和结构
mysqldump -uroot -proot -A > /data/mydb.sql

# 备份mydb数据库的数据和机构
mysqldump -uroot -proot mydb > /data/mydb.sql

# -t 只备份表数据
# -d 只备份表结构
mysqldump -uroot -proot mydb -t > /data/mydb.sql

# 备份多个数据库，使用--databases指定
mysqldump -uroot -proot --databases db1 db2 > /data/mydb.sql

# 备份数据库的指定表 t1、t2
mysqldump -uroot -proot mydb t1 t2 > /data/mydb.sql

# 导出存储过程
# -ntd 不导出表结构和数据
mysqldump  -uroot -proot -ntd -R myproject > /data/mydb.sql
```

  


## 导入
导入方式1 ：

在命令行直接进行导入

```shell
mysql -umyproject -pmyproject myproject < /data/mydb.sql
```

  


导入方式2：

登入mysql之后，通过sql的`source`指令及逆行还原：

```sql
source /data/mydb.sql
```

