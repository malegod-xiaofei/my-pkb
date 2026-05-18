# docker下载加速
  


方式1：使用 网易数帆、阿里云等容器镜像仓库进行下载。

  


例如，下载网易数帆镜像中的mysql。（网易数帆的地址为 `hub.c.163.com`，网易数帆对dockerhub官方的镜像命名空间为 `library`）。

  


```shell
docker pull hub.c.163.com/library/mysql:latest
```

  


方式2：配置阿里云加速。

  


登录阿里云，进入 `工作台` -> `容器镜像服务` -> `镜像工具` -> `镜像加速器`。

  


里面提供了一个加速器地址：`https://xxxxx.mirror.aliyuncs.com`，将该地址配置到docker中：

  


```shell
cd /etc/docker

# 初次进来时没有/etc/docker/daemon.json文件，直接创建该文件即可
vi /etc/docker/daemon.json
```

  


在`daemon.json`中写入以下内容：（即加速器地址）

  


```json
{
  "registry-mirrors": ["https://xxxxx.mirror.aliyuncs.com"]  
}
{
  "registry-mirrors": ["https://mirror.ccs.tencentyun.com"]  
}
```

  


然后刷新配置、重启docker即可：

  


```shell
# centos6 的命令
sudo chkconfig daemon-reload
sudo service docker restart

# centos7 的命令
sudo systemctl daemon-reload
sudo systemctl restart docker
```

  


使用方式2可以直接下载官方的镜像，且镜像tag为官方tag，不需要加上云服务商的地址。

  


例如：

  


```shell
docker pull mysql:latest
```

# Docker配置代理
如果使用了科学上网，可以为docker配置代理。

在`/etc/docker/daemon.json`文件中加入以下内容：

```json
{
  "proxies": {
    "http-proxy": "http://127.0.0.1:7890",  // 代理地址
    "https-proxy": "http://127.0.0.1:7890",
    "no-proxy": "localhost"
  }
}
```



