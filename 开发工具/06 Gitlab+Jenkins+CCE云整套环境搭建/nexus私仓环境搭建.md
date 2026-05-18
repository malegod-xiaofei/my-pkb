# Nexus安装
1. 检查服务器上是否安装有 JDK 1.8 +，如果没有则需要下载安装JDK。
2. 到sonatype官网下载[Nexus Repository Manager OSS](https://www.sonatype.com/products/repository-oss-download)

nexus有OSS版和PRO版。OSS版开源免费，PRO版需要付费。

此处下载OSS版

1. 将下载的压缩包放到服务器解压

sonatype将Nexus安装包托管到了 Fastly CDN，国内访问Fastly CDN非常卡顿。可能会下载失败，需要多试几次。

```shell
tar -zxvf  nexus-3.30.0-01-unix.tar.gz
```

解压后会有两个文件夹：

    - nexus-3.69.0-02

nexus软件

    - sonatype-work

nexus工作目录。

该文件夹和nexus软件在相同路径中，最好不要改动。

1. 修改nexus的配置

编辑 nexus-3.69.0-02/etc/nexus-default.properties 文件。

或者编辑sonatype-work/nexus3/etc/nexus.properties文件（推荐）

```properties
## DO NOT EDIT - CUSTOMIZATIONS BELONG IN $data-dir/etc/nexus.properties
##
# Jetty section
application-port=9091
application-host=0.0.0.0
nexus-args=${jetty.etc}/jetty.xml,${jetty.etc}/jetty-http.xml,${jetty.etc}/jetty-requestlog.xml
nexus-context-path=/

# Nexus section
nexus-edition=nexus-pro-edition
nexus-features=\
 nexus-pro-feature

nexus.hazelcast.discovery.isEnabled=true
```

1. 在linux上创建nexus用户：

```shell
# 添加用户
useradd nexus
# 配置密码 nexus
passwd nexus
```

1. 使用`nexus`用户登录，并启动nexus：

```shell
# 启动
./nexus start
# 关闭
./nexus stop
# 查看状态
./nexus status
# 重启
./nexus restart
```

1. 浏览器放问nexus

启动较缓慢，需要等待一段时间才能连上

[http://192.168.xxx.xxx:9091/](http://192.168.xxx.xxx:9091/)

  


# 首次登录时修改密码
1. 进入nexus的web管理页面后，所有的配置都是只读的，需要登录才能操作
2. 点击Sign In 进行登录默认用户名：admin默认密码：在 `/home/nexus/sonatype-work/nexus3/admin.password ` 文件中

旧版本Nexus没有该密码文件，默认密码为：admin123

1. 首次登录需要修改密码，将密码改为：admin

修改密码后，admin.password文件会被自动删除

1. 配置是否允许匿名访问（配置为允许）

启用匿名访问意味着，用户可以在没有凭据的情况下从仓库搜索、浏览和下载组件。

  


# Maven私仓
## 创建maven私仓
1. 使用`admin`登录nexus
2. 点击系统管理设置按钮（左上角小齿轮）
3. 创建文件夹保存maven数据：进入 `Repository` -> `Blob Stores`，`create blob store`，类型选择`File`，名称输入`my-maven-file`，路径会自动生成，也可以自己调整。
4. 创建私仓：进入 `Repository` -> `Repositories`，`create repository`，选择 `maven2(hosted)`（内网无法连接代理，只能为本机Maven）。  
Name: my-mavenOnline：默认勾选Version policy：选择`Mixed`（快照版和发布版都允许上传）Layout policy：默认StrictContent Disposition：默认 inlineBlob store：选择刚刚创建的`my-maven-file`Strict Content Type Validation：默认勾选Deployment policy：选择 Allow redeploy（允许重复上传）点击`Create repository`完成创建

  


## 向maven私仓上传jar包
方式1（适合上传单个jar）：使用admin登录页面，点击左侧`Upload`，选择`my-maven`，将需要上传的jar包上传即可。

  


方式2（适合上传多个jar）：将需要上传的自己本地的资源库整体上传。

1. 先将本地repository仓库文件夹打成一个完整的zip压缩包
2. 上传到nexus服务器上
3. 解压zip
4. 进入repository目录
5. 清理`*.lastUpdated`、`_remote.repositories`文件

```shell
# 查看所有*.lastUpdated
find . -name '*.lastUpdated' -type f
# 删除*.lastUpdated
find . -name '*.lastUpdated' -type f -exec rm {} +
# 检查
find . -name '*.lastUpdated' -type f

# 查看所有 _remote.repositories 文件
find . -name '_remote.repositories' -type f
# 删除所有 _remote.repositories 文件
find . -name '_remote.repositories' -type f -exec rm {} +
# 检查
find . -name '_remote.repositories' -type f

# 查看所有resolver-status.properties 文件
find . -name 'resolver-status.properties' -type f
# 删除所有 resolver-status.properties 文件
find . -name 'resolver-status.properties' -type f -exec rm {} +
# 检查
find . -name 'resolver-status.properties' -type f
```

1. 将本地仓库里面所有的`maven-metadata-alimaven.xml`改名为`maven-metadata.xml`（`alimaven`是本地maven的settings文件中设置的镜像仓库名）

```shell
find . -name "maven-metadata-alimaven.xml" -execdir mv {} maven-metadata.xml \;
```

1. 编写 `mvnimport.sh` 脚本，内容如下

```shell
#!/bin/bash
# copy and run this script to the root of the repository directory containing files
# this script attempts to exclude uploading itself explicitly so the script name is important
# Get command line params
 
while getopts ":r:u:p:" opt; do
    case $opt in
        r) REPO_URL="$OPTARG"
        ;;
        u) USERNAME="$OPTARG"
        ;;
        p) PASSWORD="$OPTARG"
        ;;
    esac
done
 
find . -type f -not -path './mavenimport\.sh*' -not -path '*/\.*' -not -path '*/\^archetype\-catalog\.xml*' -not -path '*/\^maven\-metadata\-local*\.xml' -not -path '*/\^maven\-metadata\-deployment*\.xml' | sed "s|^\./||" | xargs -I '{}' curl -u "$USERNAME:$PASSWORD" -X PUT -v -T {} ${REPO_URL}/{} ;
```

1. 将私仓文件、sh脚本授权
2. 执行shell脚本并传入参数

```shell
./mvnimport.sh -u admin -p admin -r http://192.168.xxx.xxx:9091/repository/my-maven/
```

1. 等全部导入完毕后，在nexus控制台页面刷新即可看到已导入的jar

  


## 项目中使用该私仓
配置本地的maven的`settings.xml`配置文件，加入该私仓。例如：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">
 
  <!-- 设置本地资源库存储路径 -->
  <localRepository>D:\PC_Document\Maven_Workspace\repository</localRepository>

  <pluginGroups></pluginGroups>

  <proxies></proxies>

  <servers></servers>

  <mirrors>
     <!-- 设置为内网nexus的maven私仓地址 -->
     <mirror>
      <id>nexus</id>

      <mirrorOf>*</mirrorOf>

      <name>my maven</name>

      <url>http://192.168.xxx.xxx:9091/repository/my-maven/</url>

     </mirror>

  </mirrors>

  <profiles>

    <profile>
      <id>jdk-1.8</id>

      <activation>
        <activeByDefault>true</activeByDefault>

        <jdk>1.8</jdk>

      </activation>

      <properties>
        <maven.compiler.source>1.8</maven.compiler.source>

        <maven.compiler.target>1.8</maven.compiler.target>

        <maven.compiler.compilerVersion>1.8</maven.compiler.compilerVersion>

      </properties>

    </profile>

    <profile>
      <!-- 设置一个profile，声明snapshots版的依赖、插件依赖的下载地址也为内网私仓地址 -->
      <id>nexus</id>

      <repositories>
        <repository>
          <id>central</id>

          <url>http://192.168.xxx.xxx:9091/repository/my-maven/</url>

          <releases>
            <enabled>true</enabled>

          </releases>

          <snapshots>
            <enabled>true</enabled>

          </snapshots>

        </repository>

      </repositories>

      <pluginRepositories>
        <pluginRepository>
          <id>central</id>

          <url>http://192.168.xxx.xxx:9091/repository/my-maven/</url>

          <releases>
            <enabled>true</enabled>

          </releases>

          <snapshots>
            <enabled>true</enabled>

          </snapshots>

        </pluginRepository>

      </pluginRepositories>

    </profile>

  </profiles>

  <activeProfiles>
    <!-- 启用上面声明的profile -->
    <activeProfile>nexus</activeProfile>

  </activeProfiles>

</settings>
```

  


# Docker私仓
## 创建Docker私仓
1. 使用`admin`登录nexus
2. 点击系统管理设置按钮（左上角小齿轮）
3. nexus默认docker是失效的，需要 在`security` --> `Realms`，将docker配置成`Active`
4. 创建文件夹保存maven数据：进入 `Repository` -> `Blob Stores`，`create blob store`，类型选择`File`，名称输入`my-docker-file`，路径会自动生成，也可以自己调整。
5. 创建私仓：进入 `Repository` -> `Repositories`，`create repository`，选择 `docker(hosted)`。  
Name: my-dockerOnline：默认勾选Http: 勾选，并填入将来连接该Docker仓库的端口号8889Https：已经勾选了http，可以不再勾选httpsAllow anonymous docker pull：勾选。（允许不登录时匿名下载镜像）Enable Docker V1 API：默认不勾选。（无需启动对V1旧版本API的支持）Blob store：选择刚刚创建的 my-docker-fileDeployment policy：选择 Allow redeploy（允许重复提交）点击`Create repository`完成创建

  


## docker客户端对私仓镜像上传下载
需要先安装好Docker客户端，在`/etc/docker/daemon.json`中加入可信仓库，允许http连接：

```json
{
        "insecure-registries": [
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

加入配置后，重启docker：

```shell
sudo systemctl daemon-reload
sudo systemctl restart docker
```

  


下载镜像：

```shell
# docker私仓配置了允许匿名下载，无需登录即可进行pull镜像
docker pull 192.168.xxx.xxx/my/tomcat:9.0.90-jre8
```

  


上传镜像：

```shell
# 上传镜像到私仓时，需要先登录
docker login -u admin -p admin 192.168.xxx.xxx:8889
# 将镜像push到私仓
docker push 192.168.xxx.xxx/aaa/aaa-portal:20241031-100820
# 登出
docker logout 192.168.xxx.xxx:8889
```

  


# 其他仓库
npm私仓、helm私仓等与前面搭建几乎一致。

与docker私仓类似，nexus默认npm也是是失效的，需要 在`security` --> `Realms`，将npm配置成`Active`

