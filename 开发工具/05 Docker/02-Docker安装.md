# CentOS安装Docker
  


参考官网：[https://docs.docker.com/engine/install/centos/](https://docs.docker.com/engine/install/centos/)

  


## 卸载旧版本
  


如果之前安装过Docker，需要先卸载旧版本：

  


```shell
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```

  


旧版本的Docker引擎包可能叫做：`docker`、`docker-engine`。

新版本的Docker引擎包叫做：`docker-ce`

  


## 配置yum资源库
  


安装`yum-config-manager`：

  


```shell
# yum-util提供yum-config-manager功能 
sudo yum install -y yum-utils
```

  


配置docker的资源库地址：

  


官方地址：（比较慢，不推荐）

  


```shell
# 在yum资源库中添加docker资源库
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

  


阿里云镜像地址：

  


```shell
sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

  


阿里云官网提供了很多资源镜像，镜像地址：`https://mirrors.aliyun.com`，进入之后可以选择自己需要的资源进行配置

  


创建缓存（可选）：

  


```shell
yum makecache fast
```

  


## 安装Docker引擎
  


安装最新版本的Docker引擎、Docker客户端：

  


```shell
# docker-ce是Docker引擎，docker-ce-cli是客户端
sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

  


此时，默认安装的docker引擎、客户端都是最新版本。

  


如果要安装指定版本：

  


```shell
# 查询版本列表
yum list docker-ce --showduplicates | sort -r

# 指定版本安装17.09.0.ce版
# sudo yum install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io docker-compose-plugin
sudo yum install docker-ce-17.09.0.ce docker-ce-cli-17.09.0.ce containerd.io docker-compose-plugin
```

  


## 启动docker引擎
  


如果没有启动Docker引擎，那么执行 `docker version`查看版本号时，只能看到 `Client: Docker Engine`（Docker引擎客户端）的版本号。

  


启动Docker引擎：

  


```shell
# 新版本的Docker就是一个系统服务，可以直接使用启动系统服务方式启动
systemctl start docker

# 此时查看docker版本，可以看到Server: Docker Engine（Docker引擎）版本号
docker version
```

  


# 卸载Docker
  


卸载Docker步骤：

  


1.  关闭服务 

```shell
systemctl stop docker
```

1.  使用`yum`删除docker引擎 

```shell
sudo yum remove docker-ce docker-ce-cli containerd.io
```

1.  删除镜像、容器、卷、自定义配置等文件 

```shell
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```

  


# 运行HelloWorld测试
  


运行HelloWorld：

  


```shell
docker run hello-world
```

# Ubuntu安装Docker
## 卸载旧版本
卸载旧版本Docker（如果已经安装）：

```shell
sudo apt-get remove docker docker-engine docker.io containerd runc
```

## 安装依赖
安装必要的依赖：

```shell
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
```

## 添加docker软件源
官网源：(不推荐，可能会连不上报错)

```shell
# 导入源仓库的 GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 将 Docker APT 软件源添加到你的系统
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

  


阿里云源（推荐）：

```shell
# 添加Docker GPG密钥
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 添加Docker软件源信息
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

  


## 安装docker
更新软件源并安装Docker：

```shell
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

  


## 启动并测试Docker
```shell
sudo systemctl start docker
sudo docker run hello-world
```

# 离线安装
## 下载安装
从docker官网（或者国内镜像站）下载对应linux版本的安装包，例如[docker-27.0.3.tgz](https://mirrors.ustc.edu.cn/docker-ce/linux/static/stable/x86_64/docker-27.0.3.tgz)。

将安装包上传到服务器，解压：

```shell
tar -zxvf docker-27.0.3.tgz
```

解压出来的文件的所有者可能不是root，修改为root用户：

```shell
chown -R root:root docker/
```

将解压的文件移动到`/usr/bin`下：

```shell
\cp -f docker/* /usr/bin
```

启动测试：

```shell
dockerd
```

  


## 配置成系统服务
将docker添加到systemd：

编辑文件`/usr/lib/systemd/system/docker.service`。

文件内容参考：[github的docker-ce官方文档](https://github.com/docker-archive/docker-ce/blob/master/components/engine/contrib/init/systemd/docker.service)

```properties
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target docker.socket firewalld.service 
Wants=network-online.target 
Requires=docker.socket

[Service]
Type=notify
ExecStart=/usr/bin/dockerd
ExecReload=/bin/kill -s HUP $MAINPID
TimeoutStartSec=0
RestartSec=2
Restart=always

StartLimitBurst=3
StartLimitInterval=60s
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity

TasksMax=infinity

Delegate=yes

KillMode=process
OOMScoreAdjust=-500

[Install]
WantedBy=multi-user.target
```

为`docker.service`添加执行权限：

```shell
chmod +x /usr/lib/systemd/system/docker.service
```

  


## 配置docker
创建`docker`组：

```shell
groupadd docker
```

编辑`daemon.json`配置文件：

文件：`/etc/docker/daemon.json`

```json
{
    // 还可以在这个文件中配置加速器、镜像仓库地址等
    "insecure-registries": [
        // 配置不验证https证书、允许http连接
        "192.168.xxx.xxx:8088"
    ],
    "data-root":"/data/docker",
    "log-driver":"json-file",
    "log-opts":{
        "max-size":"200m","max-file":"3"
    }
}
```

重载配置：

```shell
systemctl daemon-reload
```

  


## 启动docker并设置开机自启
启动docker：

```shell
systemctl start docker
```

设置开机自启：

```shell
systemctl enable docker
```

检验：

```shell
docker version
```

  


## 配置命令自动补全
从docker的github官方仓库获取命令补全的文件：[docker](https://github.com/docker-archive/docker-ce/blob/master/components/cli/contrib/completion/bash/docker)

将该文件放到`/usr/share/bash-completion/completions`，启用该文件：

```shell
source /usr/share/bash-completion/completions/docker
```







