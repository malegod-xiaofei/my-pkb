# Jenkins配置
系统的代码位于gitlab上，当Jenkins安装了gitlab插件、git插件之后可以很方便的连接上gitlab（在Jenkins部署文档中安装的插件已经包含了gitlab插件和git插件）。

## gitlab创建账号
使用管理员登录gitlab，创建账号 jenkins，并赋予相应权限，用于在 Jenkins 中使用该账号拉取代码。

## gitlab上配置SSH密钥
在docker服务器上进入Jenkins容器：

```shell
docker exec -it jenkins bash
```

进入容器后，生成公私密钥对：

```shell
# 执行下面的命令，然后一路回车即可
# 最后会在 /var/jenkins_home 目录中创建 .ssh 文件夹
# .ssh 文件夹中的 id_rsa 文件内容为私钥字符串，id_rsa.pub文件内容为公钥字符串
ssh-keygen -t rsa
```

  


使用前面创建的jenkins账号登录gitlab，进入 `用户设置` - `SSH密钥` - `添加新密钥`，将刚刚生成的`.id_rsa.pub`文件内容（公钥）粘贴进来，标题可以任意起，到期时间清空。

  


## Jenkins上配置不验证gitlab的host key
首次连接时，Jenkins的`know_hosts`中没有gitlab地址，如果验证host key则可能会校验失败。

可以配置不验证host key：

1. 使用admin登录Jenkins
2. 进入 `系统管理` - `全局安全配置`
3. 找到`Git Host Key Verification Configuration`，将Host key验证策略改为`No verification`不验证

  


## Jenkins上配置gitlab api token
使用jenkins账号登录 gitlab，进入 `用户管理` - `访问令牌` - `添加新令牌`：

1. 令牌名称可以任意起
2. 到期时间清空
3. 选择为token授权范围，如果不清楚直接都勾上即可。
4. 点击创建个人访问令牌

页面会显示创建出来的token字符串，将该token复制出来等会用。

  


使用admin登录 Jenkins ，进入 `系统管理` - `凭据管理` - `System` - `全局凭据` - `add Credentials`新建一个凭据：

+ 类型：Gitlab API Token
+ 范围：全局
+ API Token：前面复制的token字符串
+ ID：任意起，例如叫做`gitlab-jenkins`

  


进入 `系统管理`-`系统配置`，找到`GitLab`项，配置Gitlab连接：

+ Connection name：任意起，例如`docker-gitlab`
+ Gitlab host URL：填写GitLab的URL（[http://192.168.xxx.xxx:8090/）](http://192.168.xxx.xxx:8090/）)
+ Credentials：选择刚刚创建的GitLab API Token

点击`Test Connection`验证是否连通。

  


## jenkins配置git用户名和邮箱
使用admin登录 Jenkins ，进入 `系统管理`-`系统配置`，找到`Git plugin`项，配置git用户名和邮箱：

+ Global Config user.name Value：配置git的`user.name`，配置为`jenkins`
+ Global Config user.email Value：配置git的`user.email`，配置为`jenkins@amarsoft.com`

  


## Jenkins上配置jenkins服务器的私钥
Jenkins上创建自己的私钥凭据，用于jenkins任务从gitlab上拉取代码。

  


使用admin登录 Jenkins ，进入 `系统管理` - `凭据管理` - `System` - `全局凭据` - `add Credentials`新建一个凭据：

+ 类型：SSH Username with private key
+ 范围：全局
+ API Token：前面复制的token字符串
+ ID：任意起，例如叫做`gitlab-jenkins-private`
+ Username：jenkins（jenkins容器中的服务器用户名）
+ Private Key：
    - 勾选`Enter directly`
    - 添加key
    - 将Jenkins容器中之前创建的公私钥对的私钥粘贴进来（即`id_rsa`文件内容）

  


# 节点服务器配置
## 节点服务器环境准备
在节点服务器上创建`/root/.jenkins`文件夹，作为Jenkins的远程工作目录。Jenkins服务器会给该文件夹发送两个jar包用于远程连接。

  


在节点服务器上创建`build`文件夹，用于存放打包编译等所需的环境。

`build`文件夹内需要有：

+ JDK 17 解压版安装包：用于连接上Jenkins服务器
+ JDK 8 解压版安装包：用于编译程序项目
+ Node-v12 解压版安装包：用于编译前端VUE项目
+ maven-3.6.3 解压版安装包：用于编译程序项目。（maven需要在`settings.xml`中配置好内网的nexus私仓路径、本地仓库路径）
+ `mvn-repo`文件夹：作为maven的本地仓库路径，存放maven下载的jar包
+ `source`文件夹：用于存放从gitlab上拉取的代码

  


配置Maven环境变量：

新建文件`/etc/profile.d/maven.sh`，写入Maven环境变量：

```shell
export MAVEN_HOME=/root/build/apache-maven-3.6.3
export M2_HOME=/root/build/apache-maven-3.6.3

export PATH=$M2_HOME/bin:$PATH
```

  


另外，项目使用Jenkins打包编译之后会制作Docker镜像，所以项目的节点服务器需要安装配置好docker环境。

  


## Jenkins配置节点服务器
正常的创建节点服务器。

使用admin登录Jenkins，进入`系统管理`-`节点和云管理`-`New Node`，创建一个节点：

1. 节点名称：可以任意起，最好起一个方便识别服务器IP的，例如直接用服务器IP：`192-168`
2. 选择`固定节点`
3. `Number of executors`配置为1，防止一台服务器并发执行多个任务时出现冲突
4. 远程工作目录`/root/.jenkins`
5. 标签：配置为方便识别的标签，后面配置项目时可以根据服务器标签选择在哪个服务器上执行。`myproject_dev`
6. 用法：只允许运行绑定到这台服务器上的JOB
7. 启动方式：`Lauch agents via SSH`（需要安装了SSH对应插件才有该选项，前面安装的插件包中已经包含了该插件）  
主机：服务器IP  
Credentials：登录的凭据，如果已经创建过则直接选，没有创建过则新建。可以选择新建一个`Username with Password`的，直接配置服务器用户名密码即可。Host Key Verification Strategy：配置为不验证Host  
点开高级，在Java路径上配置上节点服务器的JDK 17路径 `/root/build/jenkins/jdk-17.0.12/bin/java`
8. 可用性：尽量保持代理在线（默认）

  


创建之后，点击查看日志，看是否连接成功。





