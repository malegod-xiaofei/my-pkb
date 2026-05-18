# Docker Registry
  


Docker Registry是官方提供的工具，用于构建私有镜像仓库。

  


# 环境搭建
  


Docker Registry也是Docker Hub提供的一个镜像，可以直接拉取运行。

  


步骤：

  


1.  拉取镜像 

```shell
docker pull registry
```

1.  启动Docker Registry 

```shell
docker run -d -p 5000:5000 -v /app/myregistry/:/tmp/registry --privileged=true registry
```

1.  验证（查看私服中的所有镜像） 

```shell
curl http://192.168.xxx.xxx:5000/v2/_catalog
```

  
Registry会返回json格式的所有镜像目录 

  


# 向Registry私仓中上传镜像
  


## 配置docker允许接收`http`请求
  


（配置方式和上传到nexus私仓相同）。

  


修改`/etc/docker/daemon.json`，添加`insecure-registries`允许http：

  


```json
{
    "registry-mirros": ["https://xxxx.mirror.aliyuncs.com"],
    "insecure-registries": ["192.168.xxx.xxx:5000"]
}
```

  


然后重启docker：（新版本的docker会立即生效）

  


```shell
# centos6 的命令
sudo chkconfig daemon-reload
sudo service docker restart

# centos7 的命令
sudo systemctl daemon-reload
sudo systemctl restart docker
```

  


## 推送到私仓
  


步骤：

  


1.  添加一个对应私仓地址的tag 

```shell
docker tag lee/myubuntu:1.0.1 192.168.xxx.xxx:5000/lee/myubuntu:1.0.1
```

1.  push到私仓 

```shell
docker push 192.168.xxx.xxx:5000/lee/myubuntu:1.0.1
```

1.  查看私仓中镜像目录验证 

```shell
curl http://192.168.xxx.xxx:5000/v2/_catalog
```

  


拉取验证：

  


```shell
docker pull 192.169.xxx.xxx:5000/lee/myubuntu:1.0.1
```

