# 使用nexus创建docker私有仓库
  


Nexus的安装请参考该文档：[https://www.yuque.com/tmfl/pom/uumrx2](https://www.yuque.com/tmfl/pom/uumrx2)

  


  


Nexus配置Docker仓库步骤；

  


1.  nexus默认docker是失效的，需要 在`security` --> `Realms`，将docker配置成`Active`
2.  在 `Repository` 的 `Blob Store` 中创建一个用于存放docker镜像的存储。内网没有`S3`的话，把`Type`配置为`file`就行。 

S3：Simple Storage Service，简单对象存储服务，即云存储。

1.  在 `Repository` 的 `Repositories` 中创建一个新的资源库，类型为 `docker-hosted`。 

  


创建的 `docker-hosted`资源库的相关配置：

  


1. `Name`：指定该资源库的名称，例如就叫 `docker-hosted`
2. `Online`：默认勾选即可
3. `HTTP`：与下面的HTTPS，至少需要勾选其中一个选择框，并配置一个和nexus不同的端口号，例如 `8881`。将来docker客户端向镜像中心上传镜像时，需要向该端口号进行上传。
4. `HTTPS`：如果服务器可以开启https服务，则也可以勾选`HTTPS`，然后配置一个端口号，接收docker客户端上传上来的镜像。
5. `Allow anonymous docker pull`：允许匿名上传，默认不勾选
6. `Enable docker V1 API`：是否启用 docker早期`V1`版本的API，默认不勾选，即只启用`V2 API`：`http://xxx.xxx.xxx.xxx:8881/v2/`
7. `Blob Store`：选择上面创建的docker镜像的存储
8. `Deployment Policy`：是否允许重复上传同一个资源，默认允许

  


配置好之后，修改防火墙设置，开启刚刚配置的`8881` 端口：

  


```shell
vim /etc/sysconfig/iptables
```

  


添加：

  


```plain
-A INPUT -p tcp -m tcp --dport 8881 -j ACCEPT
```

  


重启iptables：

  


```shell
service iptables restart
```

  


# docker客户端的镜像导出和导入
  


镜像下载和导出：

  


```shell
# 下载镜像
docker pull mysql:8.0.28
# 将镜像导出成本地tar文件
docker save -o mysql-8.0.28.tar mysql:8.0.28
```

  


镜像的导入：

  


```shell
# 将本地文件导入到docker镜像中（docker会自动解析出文件中的tag，无需手动指定）
docker load < mysql-8.0.28.tar
```

  


# docker 客户端向私仓上传镜像
  


## 配置docker允许接收`http`请求
  


docker默认只接收`https`请求，而我们的`nexus`私仓如果配置的是`HTTP`接口的话，docker直接连会报错：

  


```plain
server gave HTTP response to HTTPS client
```

  


需要配置docker允许连接我们私仓的`http`。

  


```shell
vim /usr/lib/systemd/system/docker.service
```

  


在其中的`ExecStart` 选项后面，添加 `--insecure-registry {docker 私有镜像库 IP} --ipv6=false`。

  


例如：

  


```plain
[Service]

#  前面的-H参数可能不同，不需要管，只需在最后面加上我们的私仓地址即可：--insecure-registry 192.168.x.xxx:8881 --ipv6=false

ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock --insecure-registry 192.168.x.xxx:8881 --ipv6=false
```

  


然后重启docker：

  


```shell
# centos6 的命令
sudo chkconfig daemon-reload
sudo service docker restart

# centos7 的命令
sudo systemctl daemon-reload
sudo systemctl restart docker
```

  


也可以在`/etc/docker/daemon.json` 中进行配置：

  


```json
{
    "insecure-reigstries":["192.168.xxx.xxx:8881"]
}
```

  


## 向私仓推送镜像
  


1.  如果私仓不允许匿名上传镜像，则需要先进行登陆。（一般私仓都不允许匿名上传，`nexus`默认匿名上传也没有勾选） 

```shell
# --username后面为nexus用户名，执行命令后会提示输入密码
docker login --username=admin http://192.168.xxx.xxx:8881
# 登录之后，会在 $HOME/.docker/config.json 中记录下登录的用户信息，之后便不需要再进行登陆操作
# 如果要取消登录，则只需执行以下命令
# docker logout http://192.168.xxx.xxx:8881
```

1.  将要上传的镜像重新设置`Tag`。  
docker按照镜像名称区分上传的资源库。  
例如：  
`mysql:8.0.28`会被上传到docker官方`dockerhub`；  
`tengyer/helloworld:lasted`会被上传到dockerhub的`tengyer`命名空间中；  
`registry.cn-hangzhou.aliyuncs.com/命名空间/镜像名称:[镜像版本号]` 会上传到阿里云指定命名空间中；  
`ccr.ccs.tencentyun.com/命名空间/hello-world`：会上传到腾讯云指定命名空间中；  
`hub.c.163.com/命名空间/hello-world`：会上传到网易数帆指定命名空间中；  
所以，我们如果要上传到我们的私仓，需要将`Tag`修改为`xxx.xxx.xxx.xxx:8881/命名空间/mysql:5.0.27`格式： 

```shell
# 将mysql:8.0.28复制出一个私仓格式的Tag
# 该操作在 docker images中会多出一个复制出来的tag，但是ImageId和原始的相同
# 加个official命名空间，方便区分这个镜像是从官方镜像下载下来的，不加命名空间也可以上传
docker tag [ImageId] xxx.xxx.xxx.xxx:8881/official/mysql:8.0.28
```

1.  将修改好`Tag`的镜像进行上传： 

```shell
docker push xxx.xxx.xxx.xxx:8881/official/mysql:8.0.28
```

