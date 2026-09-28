# Docker微服务实战

[目录](Docker与微服务实战.md) · 高级篇(大厂进阶)

![配图](images/img-0251.png)

<a id="t-2-3-1"></a>
## 通过IDEA新建一个普通微服务模块

<a id="t-2-3-1-1"></a>
### 建Module

<a id="t-2-3-1-1-1"></a>
#### docker\_boot

<a id="t-2-3-1-2"></a>
### 改POM

&lt;?xml version="1.0" encoding="UTF-8"?>  
&lt;project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">  
&lt;modelVersion>4.0.0&lt;/modelVersion>  
&lt;parent>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-parent&lt;/artifactId>  
&lt;version>2.5.6&lt;/version>  
&lt;relativePath/>  
&lt;/parent>

&lt;groupId>com.atguigu.docker&lt;/groupId>  
&lt;artifactId>docker\_boot&lt;/artifactId>  
&lt;version>0.0.1-SNAPSHOT&lt;/version>

&lt;properties>  
&lt;project.build.sourceEncoding>UTF-8&lt;/project.build.sourceEncoding>  
&lt;maven.compiler.source>1.8&lt;/maven.compiler.source>  
&lt;maven.compiler.target>1.8&lt;/maven.compiler.target>  
&lt;junit.version>4.12&lt;/junit.version>  
&lt;log4j.version>1.2.17&lt;/log4j.version>  
&lt;lombok.version>1.16.18&lt;/lombok.version>  
&lt;mysql.version>5.1.47&lt;/mysql.version>  
&lt;druid.version>1.1.16&lt;/druid.version>  
&lt;mapper.version>4.1.5&lt;/mapper.version>  
&lt;mybatis.spring.boot.version>1.3.0&lt;/mybatis.spring.boot.version>  
&lt;/properties>

&lt;dependencies>  
&lt;!--SpringBoot通用依赖模块-->  
&lt;dependency>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-web&lt;/artifactId>  
&lt;/dependency>  
&lt;dependency>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-actuator&lt;/artifactId>  
&lt;/dependency>  
&lt;!--test-->  
&lt;dependency>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-starter-test&lt;/artifactId>  
&lt;scope>test&lt;/scope>  
&lt;/dependency>  
&lt;/dependencies>

&lt;build>  
&lt;plugins>  
&lt;plugin>  
&lt;groupId>org.springframework.boot&lt;/groupId>  
&lt;artifactId>spring-boot-maven-plugin&lt;/artifactId>  
&lt;/plugin>  
&lt;plugin>  
&lt;groupId>org.apache.maven.plugins&lt;/groupId>  
&lt;artifactId>maven-resources-plugin&lt;/artifactId>  
&lt;version>3.1.0&lt;/version>  
&lt;/plugin>  
&lt;/plugins>  
&lt;/build>

&lt;/project>

<a id="t-2-3-1-3"></a>
### 写YML

**server.port**=**6001**

<a id="t-2-3-1-4"></a>
### 主启动

**package** com.atguigu.docker;  

**import** org.springframework.boot.SpringApplication;  
**import** org.springframework.boot.autoconfigure.SpringBootApplication;  

@SpringBootApplication  
**public class** DockerBootApplication  
{  
    **public static void** main(String[] args)  
    {  
        SpringApplication.*run*(DockerBootApplication.**class**, args);  
    }  

}

<a id="t-2-3-1-5"></a>
### 业务类

package com.atguigu.docker.controller;

import org.springframework.beans.factory.annotation.Value;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RequestMethod;  
import org.springframework.web.bind.annotation.RestController;

import java.util.UUID;

/\*\*  
\* @auther zzyy  
\* @create 2021-10-25 17:43  
\*/  
@RestController  
public class OrderController  
{  
@Value("${server.port}")  
private String port;

@RequestMapping("/order/docker")  
public String helloDocker()  
{  
return "hello docker"+"\\t"+port+"\\t"+ UUID.randomUUID().toString();  
}

@RequestMapping(value ="/order/index",method = RequestMethod.GET)  
public String index()  
{  
return "服务端口号: "+"\\t"+port+"\\t"+UUID.randomUUID().toString();  
}  
}

<a id="t-2-3-2"></a>
## 通过dockerfile发布微服务部署到docker容器

<a id="t-2-3-2-1"></a>
### IDEA工具里面搞定微服务jar包

docker\_boot-0.0.1-SNAPSHOT.jar

![配图](images/img-0252.png)

<a id="t-2-3-2-2"></a>
### 编写Dockerfile

<a id="t-2-3-2-2-1"></a>
#### Dockerfile内容

\# 基础镜像使用java

FROM java:8

\# 作者

MAINTAINER zzyy

\# VOLUME 指定临时文件目录为/tmp，在主机/var/lib/docker目录下创建了一个临时文件并链接到容器的/tmp

VOLUME /tmp

**# 将jar包添加到容器中并更名为zzyy\_docker.jar**

**ADD docker\_boot-0.0.1-SNAPSHOT.jar zzyy\_docker.jar**

\# 运行jar包

RUN bash -c 'touch /zzyy\_docker.jar'

ENTRYPOINT ["java","-jar","/zzyy\_docker.jar"]

\#暴露6001端口作为微服务

EXPOSE 6001

<a id="t-2-3-2-2-2"></a>
#### 将微服务jar包和Dockerfile文件上传到同一个目录下/mydocker

![配图](images/img-0253.png)

docker build -t zzyy\_docker:1.6 .

<a id="t-2-3-2-3"></a>
### 构建镜像

![配图](images/img-0254.png)

<a id="t-2-3-2-3-1"></a>
#### docker build -t zzyy\_docker:1.6 .

<a id="t-2-3-2-3-2"></a>
#### 打包成镜像文件

![配图](images/img-0255.png)

<a id="t-2-3-2-4"></a>
### 运行容器

docker run -d -p 6001:6001 zzyy\_docker:1.6

![配图](images/img-0256.png)

<a id="t-2-3-2-5"></a>
### 访问测试

![配图](images/img-0257.png)

---

[上一篇 DockerFile解析](10_DockerFile解析.md) · [目录](Docker与微服务实战.md) · [下一篇 Docker网络](12_Docker网络.md)
