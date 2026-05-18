# Gitlab环境搭建
## Docker镜像
使用Gitlab的cc社区版镜像：

```shell
docker pull gitlab/gitlab-ce:17.1.1-ce.0
```

  


## 准备映射的容器卷
Gitlab需要映射出来的容器卷有：

+ `/var/log/gitlab`：存储日志信息
+ `/var/opt/gitlab`：存储数据库数据
+ `/etc/gitlab`：存储配置信息

  


准备对应文件夹：

```shell
mkdir -p /root/gitlab_workspace/logs
mkdir -p /root/gitlab_workspace/data
mkdir -p /root/gitlab_workspace/config
```

  


## 启动容器
启动容器`gitlab`：

```shell
docker run -d \
  -h gitlab.example.com \
  -e GITLAB_OMNIBUS_CONFIG="external_url 'http://192.168.xxx.xxx:8090';gitlab_rails['gitlab_shell_ssh_port'] = 8022" \
  -p 8090:8090 \
  -p 8022:22 \
  --name gitlab \
  --restart always \
  -v /root/gitlab_workspace/config:/etc/gitlab \
  -v /root/gitlab_workspace/logs:/var/log/gitlab \
  -v /root/gitlab_workspace/data:/var/opt/gitlab \
  --shm-size 1g \
  gitlab/gitlab-ce:17.1.1-ce.0
```

其中，gitlab容器内的http端口由映射的端口决定，例如 -p 8090:8090 ，那么容器内的http端口会自动开放为8090。配置external_url。

22端口如果映射到宿主机其他端口，需要配置gitlab_rails['gitlab_shell_ssh_port']

# 浏览器访问
访问地址：[http://192.168.xxx.xxx:8090/](http://192.168.xxx.xxx:8090/)

初始用户：root

执行命令查看初始密码：

```shell
sudo docker exec -it gitlab grep 'Password:' 
/etc/gitlab/initial_root_password
```

# 初始化项目
## gitlab上创建项目
在gitlab上创建一个`群组(groups)`（例如`我的测试项目myproject`），在群组中新建一个项目（例如`myproject-vue`）。（新建项目时<font style="background-color:#f3bb2f;">不要</font>勾选自动创建README）

  


## 本地代码上传
需要先在本地安装好git，配置好`user.name`、`user.email`。

### 方式1
直接从gitlab上拉取新创建的项目：

```shell
git clone http://192.168.xxx.xxx:8090/myproject/myproject-vue.git
```

拉取后，会自动创建出项目文件夹。将本地代码拷贝到该文件夹中，进行`commit`、`push`即可：

```shell
git add .
git commit -m "初始化项目"
git push
```

  


### 方式2
进入本地代码目录，初始化为git项目，并设置远程仓库地址，然后进行`commit`、`push`操作：

```shell
# 进入本地项目目录
cd amamrrwms
git init
git remote add origin http://192.168.xxx.xxx:8090/myproject/myproject-vue.git
git add .
git commit -m "初始化项目"

# 需要注意gitlab上该项目的默认分支名。旧版本的gitlab自动创建的默认分支为master，新版本的gitlab自动创建的分支为main
git push -u origin main
```

