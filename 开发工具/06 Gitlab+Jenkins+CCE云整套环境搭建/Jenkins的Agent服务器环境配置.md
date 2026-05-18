# Jenkins节点服务器配置
作为Jenkins的节点，需要承担以下任务。

编译系统：

+ 使用Maven打包编译后台项目（直接解压Maven即可）
+ 使用Node打包编译Vue项目（直接解压Node即可）
+ 使用Docker制作镜像、推送CCE
+ 使用CCE客户端登录CCE
+ 使用kubectl更新远程CCE上的deployment

  


编译本系统之外其他项目：

+ 使用Ant打包编译移动端等传统非maven项目（直接解压Ant即可）

  


# 安装CCE客户端
从CCE页面（`镜像管理`-`Linux客户端上传`）得到CCE客户端的下载链接，例如：x86_64版客户端

将该文件上传到服务器上。

在服务器上创建`$HOME/.kube`文件夹（即`/root/.kube`文件夹）。

在服务器上配置hosts映射（在`/etc/hosts`文件中加入`192.168.xxx.xxx cce.test.com`）。

  


在服务器上执行CCE的初始化命令：

```shell
cce init
```

填写 cce的地址（即`cce.test.com`）等信息。

  


登录验证：

```shell
cce login
```

  


退出登录：

```shell
cce logout
```

  


# 离线安装Docker
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

也可以放到`/usr/local/bin`下，系统便不会控制docker的更新。但是`docker.service`中默认配置的docker启动命令在`/usr/bin`下，如果移动到了`/usr/local/bin`下，则需要调整`docker.service`文件中的启动命令路径。

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

如果前面将docker命令复制到了`/usr/local/bin`而不是`/usr/bin`下，下面的`ExecStart`中的命令路径也需要对应进行调整

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

  


配置`docker.socket`

编辑文件`/usr/lib/systemd/system/docker.socket`。

文件内容参考：[github的docker-ce官方文档](https://github.com/docker-archive/docker-ce/blob/master/components/engine/contrib/init/systemd/docker.socket)

```properties
[Unit]
Description=Docker Socket for the API

[Socket]
# If /var/run is not implemented as a symlink to /run, you may need to
# specify ListenStream=/var/run/docker.sock instead.
ListenStream=/run/docker.sock
SocketMode=0660
SocketUser=root
SocketGroup=docker

[Install]
WantedBy=sockets.target
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
        "https://cce.test.com",
            "192.168.xxx.xxx:8889"
    ],
    "data-root":"/data/docker",
        "log-driver":"json-file",
        "log-opts":{
            "max-size":"200m",
            "max-file":"3"
        },
  "features": {
    "buildkit": true
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

  


## 安装docker-compose（非必须）
`Docker-Compose`的版本需要和Docker引擎版本对应，可以参照官网上的[对应关系](https://docs.docker.com/compose/compose-file/compose-file-v3/)。

安装Compose：

```shell
# 例如从github下载 2.28.1 版本的docker-compose
# 下载下来的文件放到 /usr/local/bin目录下，命名为 docker-compose
curl -L https://github.com/docker/compose/releases/download/v2.28.1/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

# 添加权限
chmod +x /usr/local/bin/docker-compose

# 验证
docker-compose version
```

  


卸载Compose：直接删除 `usr/local/bin/docker-compose`文件即可

  


## 安装docker-buildx（非必须）
`docker build`已经被标记为过时，可以使用`docker buildx build`进行替换。

`docker build` 只能编译同Linux内核的镜像，在x86_64内核的Linux上就只能编译`linux/amd64`内核镜像，在`arm64`内核的linux上只能编译`linux/arm64`内核镜像。如果想要跨平台编译，就需要使用`docker buildx build`。

  


如果安装的是Docker桌面版，则自带了`docker-buildx`。如果是linux离线安装的docker时，需要单独安装docker-buildx插件。

从[github docker-buildx](https://github.com/docker/buildx#manual-download)下载对应系统的docker-buildx的编译后的插件包。例如[linux x86_64版安装包](https://github.com/docker/buildx/releases/download/v0.16.2/buildx-v0.16.2.linux-amd64)

根据`README.md`文档的步骤：

1. 将安装包放到服务器的`$HOME/.docker/cli-plugins`文件夹中
2. 将安装包名称修改为`docker-buildx`，并添加执行权限

验证：

```shell
docker buildx version
```

  


# 离线安装kubectl
## 查看CCE上的kubectl版本
登录CCE页面，点击`kubectl`连接页面，执行以下命令查看`kubectl`版本：

```shell
# --client 只需要查看客户端kubectl工具的版本，无需查看k8s集群版本
kubectl version --client
```

可以看到输出结果：`kubectl`工具的版本为`v1.21.7`

```plain
Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"v1.21.7", GitCommit:"1f86634ff08f37e54e8bfcd86bc90b61c98f84d4", GitTreeState:"clean", BuildDate:"2021-11-17T14:41:19Z", GoVersion:"go1.16.10", Compiler:"gc", Platform:"linux/amd64"}
```

  


## 下载安装kubectl
从K8S官网下载`v1.21.7`版本、内核为`x86_64`（即`amd64`）的`kubectl`工具：

```shell
# 或者直接在浏览器下载
curl -LO https://dl.k8s.io/release/v1.21.7/bin/linux/amd64/kubectl
```

下载`sha256`验证文件：

```shell
curl -LO https://dl.k8s.io/release/v1.21.7/bin/linux/amd64/kubectl.sha256
```

将下载的`kubectl`、`kubectl.sha256`文件上传到服务器，进行sha256验证下载的完整性：

```shell
echo "$(cat kubectl.sha256) kubectl" | sha256sum --check
```

如果验证成功，则执行命令进行安装：

```shell
# 需要root身份安装
install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

安装完后查看版本：

```shell
kubectl version
```

  


## 验证连接CCE
当服务器上的`cce`客户端执行过`cce init`之后，会在`$HOME/.cce`（即`/root/.cce`）下生成连接的配置文件。

当服务器上的`cce`客户端执行过`cce login`登录之后，会在`$HOME/.kube/`下生成kubectl连接配置文件。（即`/root/.kube/config`）

  


将需要连接到的K8S配置文件设置为环境变量`KUBECONFIG`：

```shell
export KUBECONFIG=/root/.kube/config
```

`kubectl`命令便可以连接到CCE上，执行`kubectl`命令操作CCE：

```shell
# 查看帮助
kubectl --help

# 查看myproject命名空间下的所有无状态工作负载（在CCE上创建的每一个项目实际都是在K8S上创建的命名空间）
kubectl get deployment -n myproject
# 查看myproject命名空间下的所有容器组
kubectl get pods -n myproject
# 查看myproject命名空间下的所有容器组（显示IP等信息）
kubectl get pods -o wide -n myproject

# 查看myproject下的ingress
kubectl get ingress -n myproject
# 查看myproject下的service
# 简写为 kubectl get svc -n myproject
kubectl get service -n myproject
# 查看myproject下的configmap
# 简写为 kubectl get cm -n myproject
kubectl get configmap -n myproject
# 查看myproject下的statefulset
kubectl get statefulset -n myproject
# 查看myproject下的job
kubectl get job -n myproject
# 查看myproject下的cronjob
kubectl get cronjob -n myproject
# 查看myproject下的secret
kubectl get secret -n myproject

# 查看ingress-myproject这个ingress的详情
kubectl describe ingress ingress-myproject -n myproject
# 查看cl-uat这个service的详情
# 简写 kubectl describe svc cl-uat -n myproject
kubectl describe service cl-uat -n myproject
# 查看myproject-sys这个deploy的详情
kubectl describe deploy myproject-sys -n myproject
# 查看na

# 查看PV
kubectl get pv
# 查看PVC
kubectl get pvc
# 查看K8S集群节点
kubectl get nodes

# 查看指定pod的日志
kubectl logs myproject-vue-786b5fd8b5-tg9m5 -n myproject

# 查看指定pod、指定容器的日志，-f持续输出
kubectl logs myproject-sys-7dc857dd96-66jhz container-app -f

# 生成一个deployment的yaml文件，但是不部署
# kubectl create xxxx 从文件或者输入流中创建一个资源
# --dry-run=client 尝试创建资源但是不真正部署，只是生成一个yaml文件
kubectl create deployment mydep --image=cce.test.com/tomcat:9.0.90-jre8 --dry-run=client -o yaml -n myproject > mydep.yaml
# 生成一个service的yaml文件，但是不部署。（需要是一个存在的deployment才可以创建service）
# kubectl expose xxxxx暴露一个新的service
kubectl expose deployment mydep --name=service-mydep --port=80 --target-port=80 --type=NodePort --dry-run=client -o yaml -n myproject > service-mydep.yaml
# 更新 myproject-vue 这个工作负载的container-0容器的镜像为cce.test.com/myproject/myproject-web:20240724-154216
# kubectl set xxxx 为objects设置一个指定的特征
kubectl set image deployment/myproject-vue container-0=cce.test.com/myproject/myproject-web:20240724-154216 -n myproject

# 根据yaml内容创建相应负载、service等资源
kubectl apply -f mydep.yaml

# 进入容器vue-ui-doc-d66dbb6d4-5fk7s 内部
# 类似于docker exec 命令。
# kubectl最后面也可以直接加要进入的命令 kubectl exec -it xxxxx bash，但是已经标记为过时，新写法为 kubectl exec -it xxxxx -- bash
kubectl exec -it vue-ui-doc-d66dbb6d4-5fk7s -n myproject -- bash
```

  


# 安装Helm客户端（非必须）
## 下载
Helm是一个K8S应用程序包管理器。安装Helm后可以创建Helm模板来简化部署、升级、管理K8S程序。

cce使用的是Helm V3，可以到[Helm官网](https://helm.sh/docs/intro/install/)查看V3最新的稳定版。例如下载 [Helm V3.14.0 amd64版](https://get.helm.sh/helm-v3.14.0-linux-amd64.tar.gz)。

  


## 安装
将下载下来的压缩包上传到服务器上解压：

```shell
tar -zxvf helm-v3.14.0-linux-amd64.tar.gz
```

解压出来的`linux-amd64`文件夹中有3个文件：

+ `helm`：Helm命令文件
+ `README.md`：Helm说明文档
+ `LICENSE`：license声明

  


将`helm`命令文件移动到`/usr/local/bin`目录下：

```shell
mv linux-amd64/helm /usr/local/bin
```

  


## 验证
需要先登录CCE，并配置环境变量。

将需要连接到的K8S配置文件设置为环境变量`KUBECONFIG`：

```shell
export KUBECONFIG=/root/.kube/config
```

  


验证：

```shell
# 查看helm版本号
helm version
```

  


## 常用命令
helm常用命令：

```shell
# 查看版本号
helm version
# 查看helm中的模板
helm list
# 查看helm连接到的远程helm仓库列表
helm repo list
# 为helm添加内网Nexus远程仓库
helm repo add myproject http://192.168.xxx.xxx:9091/repository/my-helm/
# 更新helm仓库
helm repo update
# 搜索远程仓库中名字带有myproject的chart(如果是新上传到仓库的chart，需要先执行更新仓库命令才能搜索到)
helm search repo myproject
# 查看远程仓库中myproject/myproject-vue的信息（myproject是配置的本地helm远程repo名称，myproject-vue是远程仓库中的chart名称）
helm show chart myproject/myproject-vue
# 或者填写tgz文件的完整路径
helm show chart http://192.168.xxx.xxx:9091/repository/myproject/myproject-vue-1.0.20240803.tgz

# 创建一个chart（会在linux本地创建一个文件夹mychart，里面存放有示例模板文件）
helm create mychart
# 删除mychart文件夹中的templates内的示例文件，将自己deployment、service等yaml放到templates中
# 按需调整Chart.yaml中配置的该helm模板名称、版本、描述等信息
# 按需从templates中抽取需要复用的变量，在values.yaml中统一配置
# 之后可以执行helm的安装
# （CCE上无法使用Jenkins节点服务器上的文件夹进行安装，也无法直接连接到nexus私仓或CCE私仓进行安装，报错连接已关闭）
helm install mydep mychart/
# 打包成tgz文件，可以上传到仓库中
helm package mychart/
```

  


# 修改JDK的配置
项目上的SVN server版本比较旧，使用的是TLS1.0协议。

使用Jenkins连接该SVN时会报错。Jenkins配置页面显示`Unable to access the repository`，连接时控制台报错：

```plain
org.tmatesoft.svn.core.SVNException: svn: E175002: SSL handshake failed: 'The server selected protocol version TLS10 is not accepted by client preferences [TLS13, TLS12]'
```

原因：高版本的JDK的安全策略中，禁用了低版本的TLS 1.0、TLS 1.1，只能接受 TLS 1.2、TLS 1.3等。

  


解决方案：修改JDK的配置文件，将 TLS 1.0、 TLS 1.1 从禁止项中移除。

修改文件`/root/build/jenkins/jdk-17.0.12/conf/security/java.security`，找到`jdk.tls.disabledAlgorithms`项，删除其中的`TLSv1, TLSv1.1,`。

Jenkins管理员页面断开重新连接该节点即可。

