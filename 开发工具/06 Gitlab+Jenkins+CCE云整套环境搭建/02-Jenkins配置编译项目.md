# Jenkins配置编译任务
项目的大致流程：

1. 从gitlab上拉取程序
2. 运行 maven/Node 编译打包
3. 运行Dockerfile打包成镜像
4. 上传镜像到cce云上镜像仓库
5. 使用kubectl更新cce云上的负载镜像

  


需要打包编译的内容：

+ 后台项目的`app-web`模块
+ 后台项目的`system-server`模块
+ 前端VUE项目

  


## 后台编译
1. 以admin登录Jenkins，选择`新建任务`。
2. 任务名称：任意起，例如`dev_myproject_java`
3. 选择`构建一个自由风格的软件项目`（也可以选择`复制`，填写需要复制的任务的任务名称）

  


`General`组：

1. `限制项目的运行节点`：填写节点服务器的标签表达式，限制只在该服务器上运行任务。`myproject_dev`
2. 点击`高级`
3. 使用自定义的工作空间：填写源程序下载到的服务器路径。`/root/build/source/myproject/myproject-vue`
4. 显示名称：可以配置一个中文名，用于在列表页面展示。`dev-后台-app`

  


`源码管理`组：

1. 选择`Git`
2. Repository URL：代码路径。填写`git@xxxxxx`那个。`http:xxxxx`的没有设置会报错。  
从gitlab复制下来的路径需要进行调整，前面加上`ssh://`前缀，ip后面加上gitlab的22端口映射出来的端口号8022。例如：从gitlab复制出来的路径为`git@192.168.xxx.xxx:myproject/myproject-vue.git`，调整后为`ssh://git@192.168.xxx.xxx:8022/myproject/myproject-vue.git`
3. Credentials：选择前面创建的Jenkins用户私钥的那个凭据
4. Branches to build：指定要拉取的分支。例如本项目的`*/dev_20240712`
5. 源码库浏览器：用于在jenkins上直接看本地构建时的代码差异。  
源码库浏览器：`gitlab`  
URL：gitlab的本项目页面：[http://192.168.xxx.xxx:8090/myproject/myproject-vue/](http://192.168.xxx.xxx:8090/myproject/myproject-vue/)  
version：gitlab版本：17.0

  


`构建触发器`组：

可以配置每次有代码push到gitlab时自动构建。为避免频繁构建，项目采用手动点击构建，不配置触发器。

  


`构建环境`组：

用于给节点服务器准备构建环境，使用Ant构建时可以配置。项目使用Maven、Node构建，且已经在节点服务器上手工部署了Maven、Node，无需进行配置。

  


`Build Steps`组：配置从gitlab拉取代码之后操作，即具体的构建执行步骤。项目全部使用shell方式执行。

1. 登录CCE云：

```shell
/root/cce login <<EOF
aaa   # cce用户名
aaaaaaa # cce密码
EOF
```

1. 执行Maven编译打包

```shell
cd /root/build/source/myproject/myproject-vue

source /etc/profile.d/maven.sh
export JAVA_HOME=/root/build/jdk1.8.0_411

# maven打包（跳过测试）
mvn clean package -Dmaven.test.skip=true
```

1. 执行Dockerfile制作镜像、推送CCE镜像仓库、更新cce上的负载镜像

```shell
curDate=`date +%Y%m%d`
curTime=`date +%H%M%S`
export VERSION_ALL_TAG=${curDate}-${curTime}

# build app-web image; push to cce; delete local image
cd /root/build/source/myproject/myproject-vue/app-web
docker build -t cce.test.com/myproject/app-web:${VERSION_ALL_TAG} .
docker push cce.test.com/myproject/app-web:${VERSION_ALL_TAG} 
docker rmi cce.test.com/myproject/app-web:${VERSION_ALL_TAG} 

# build system-server image; push to cce; delete local image
cd /root/build/source/myproject/myproject-vue/system/system-server
docker build -t cce.test.com/myproject/system-server:${VERSION_ALL_TAG} .
docker push cce.test.com/myproject/system-server:${VERSION_ALL_TAG} 
docker rmi cce.test.com/myproject/system-server:${VERSION_ALL_TAG} 

# update cce deployment
export KUBECONFIG=/root/.kube/config
kubectl set image deployment/myproject container-app=cce.test.com/myproject/app-web:${VERSION_ALL_TAG} container-system=cce.test.com/myproject/system-server:${VERSION_ALL_TAG} -n myproject
```

1. 登出CCE

```shell
/root/cce logout
```

  


## 前端VUE编译
与`app-web`模块的操作步骤类似，只是将Maven编译换成Node编译：

```shell
cd /root/build/source/myproject/vue-web

export NODE_HOME=/root/build/node-v12.22.12
export PATH=$NODE_HOME/bin:$PATH

npm run build:clouddev
```

  


# Jenkins打包docker镜像
86服务器上安装的Docker版本比较高，save出来的docker镜像tar文件无法直接在页面导入进CCE中。

164服务器上的Docker版本低，导出的镜像可以在页面导入CCE中，但是无法使用CCE客户端。

所以项目源码拉取、编译打包、生成镜像、kubectl更新等操作在86服务器上进行。如果需要导出docker镜像，则在164服务器上进行。

  


## 配置打包Docker的任务
在Jenkins上新建一个164节点。

新建一个任务`save_docker`，在164上运行，用于将docker镜像导出成tar文件。

勾选`参数化构建过程`：

+ 字符参数`IMAGE_LIST`：需要打包的镜像列表（多个镜像以分号分隔）
+ 布尔参数`NEED_SAVE_TAR`：是否需要导出成tar

增加一个执行shell的步骤：

```shell
if [ "$NEED_SAVE_TAR" = true ] && [ -n "$NEED_SAVE_TAR" ]; then
    # 检查 IMAGE_LIST 是否为空
    if [ -z "$IMAGE_LIST" ]; then
        echo "IMAGE_LIST is empty."
    else
        # 保存原始的 IFS
        OLD_IFS=$IFS

        # 设置 IFS 为分号
        IFS=';'

        # 遍历 IMAGE_LIST
        for image in $IMAGE_LIST; do
            # 还原 IFS 为默认的值
            IFS=''
            
            fullImagePath=${image}
            echo "开始下载镜像：${fullImagePath}"
            docker pull ${fullImagePath}
            echo '镜像下载完成.'

            # 提取 registry, namespace, image, 和 tag
            registry_and_namespace_and_image=${image%:*}
            tag=${image##*:}

            # 将 registry 和 namespace/image 分开
            registry=${registry_and_namespace_and_image%%/*}
            namespace_and_image=${registry_and_namespace_and_image#*/}

            # 提取 namespace 和 image
            namespace=${namespace_and_image%%/*}
            image=${namespace_and_image#*/}
            imageName=${image%%:*}
            
            echo "转换tag"
            newImageName=${namespace}/${imageName}:${tag}
            docker tag ${fullImagePath} ${newImageName}
            echo "转换完成"
            
            echo "开始将镜像打成tar包：${namespace}-${imageName}-${tag}.tar"
            docker save -o /root/DockerSaveTar/${namespace}-${imageName}-${tag}.tar  ${newImageName}
            echo "打成tar包完成."		
            
            echo "删除本地下载的镜像"
            docker rmi ${fullImagePath} ${newImageName}
            echo "删除完成"
        done

        # 恢复原始的 IFS
        IFS=$OLD_IFS
    fi
else
    echo "NEED_SAVE_TAR为false或空,不执行保存tar包的操作"
    exit 0
fi
```

  


## 直接调用该任务
可以在Jenkins上直接调用该任务，需要传入参数。例如：

```properties
IMAGE_LIST=192.168.xxx.xxx:8889/myproject/app-web:20240903-194055;192.168.xxx.xxx:8889/myproject/system-server:20240903-194055
NEED_SAVE_TAR=true # 勾选即可
```

任务便会自动拉取这两个镜像导出成tar

  


## 在其他任务执行后自动调用该任务
例如在预警后台的编译任务中，生成docker镜像推送仓库后，将docker镜像名称写入一个文件中：

```shell
echo "IMAGE_LIST=192.168.xxx.xxx:8889/myproject/app-web:${VERSION_ALL_TAG};192.168.xxx.xxx:8889/myproject/system-server:${VERSION_ALL_TAG}" > /root/build/source/myproject/myproject-java-env.properties
```

  


新增一个`构建后操作`：选择`Trigger parameterized build on other projects`（需要安装对应插件后才会有该选项）。

+ `Projects to build`（构建后需要执行的任务，多个任务逗号分隔）：`save_docker`（即打包docker任务）
+ `Trigger when build is`（什么情况下调用后续任务）：`Stable or unstable but not failed`（稳定、有警告都执行，只要不是失败）

添加参数：

+ `Parameters from properties file`（从properties文件中获取参数）：路径为前面写入的文件`/root/build/source/myproject/myproject-java-env.properties`
+ `Boolean parameters`（添加一个布尔参数）：`NEED_SAVE_TAR`，手动修改该参数的值来控制是否生成tar
