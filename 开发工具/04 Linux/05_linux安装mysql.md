```shell
[root@localhost ~]#yum list installed mysql*
[root@localhost ~]#rpm –qa|grep mysql*
```



[root@localhost ~]#yum list mysql*

[root@localhost ~]#yum install mysql

![图片1](images/图片1.png)

提示：如果输入此命令没有报错,则跳过下面步骤,继续安装下一个服务端

<font style="color:rgb(255, 0, 0);">1</font> [root@localhost ~]#yum install mysql-server

![图片2](images/图片2.png)

<font style="color:rgb(255, 0, 0);">原因：CentOS7自带有MariaDB而不是MySQL，MariaDB和MySQL一样也是开元的数据库</font>

![图片3](images/图片3.png)

执行完后,则继续执行：yum install mysql-server

![图片4](images/图片4.png)

<font style="color:rgb(255, 0, 0);">2</font> [root@localhost ~]#yum install mysql-devel

![图片5](images/图片5.png)

到此mysql数据库安装完成了,接下来需要对数据库进行一些简单配置

5、在/etc/my.cnf 文件中加入默认字符集

[root@localhost ~]#vim /etc/my.cnf

![图片6](images/图片6.png)

[root@localhost ~]#service mysqld start --启动mysql

[root@localhost ~]#service mysqld stop --关闭mysql·

[root@localhost ~]#lsof -i:3306 --数据库端口是否开启

![图片7](images/图片7.png)

[root@localhost ~]# chkconfig --add mysqld 

mysqladmin -u root password 密码

![图片8](images/图片8.png)

mysql增加权限：mysql库中的user表新增一条记录host为“%”，user为“root”。

use mysql; UPDATE user SET `Host` = <font style="color:rgb(128, 0, 0);">'%'</font> WHERE `User` = <font style="color:rgb(128, 0, 0);">'root'</font> LIMIT <font style="color:rgb(128, 0, 128);">1</font>;

![图片9](images/图片9.png)

![图片10](images/图片10.png)

vi /etc/sysconfig/iptables

加入：-A INPUT -p tcp -m tcp --dport 3306 -j ACCEPT 这段配置，然后进行保存

![图片11](images/图片11.png)

systemctl restart iptables.service -- 重启防火墙 systemctl status iptables.service -- 查看状态 service iptables save -- 保存规则 systemctl enable iptables.service -- 设置开机启动 systemctl start iptables.service -- 开启服务 

<font style="color:rgb(255, 0, 0);">注意：如果用的是阿里</font><font style="color:rgb(255, 0, 0);">云服务器</font><font style="color:rgb(255, 0, 0);">,需要配置安全组规则,否则无法访问</font>

我用的是SQLyog客户端进行连接,如果弹出该提示框,则表示连接成功！

![图片12](images/图片12.png)

在{MySQL5.7}/根目录下，找到my.ini文件，在[mysql]的最后添加如下配置项：

保存后，回到控制台，重启MySQL服务，命令如下：

该方案需要基于**方法一**，先进入系统之后，通过相关的操作，设置密码，命令如下：

show databases; （显示现有数据库）

show tables; （显示mysql数据库里的数据表）

select Host, User, authentication_string from user; （查询user表里现有的用户信息）

update user set authentication_string=password('123456') where user='root' and Host='localhost'; （更新root用户的密码为123456）

将**方法一**中的配置的“_**skip-grant-tables**_”注释掉，以免重启服务后，仍然不需要密码就可以进入MySQL系统了；

net stop mysql （停止MySQL服务）

net start mysql （启动MySQL服务）

mysql -u root -p （重新登录MySQL系统，此时输入的密码就是123456）  

