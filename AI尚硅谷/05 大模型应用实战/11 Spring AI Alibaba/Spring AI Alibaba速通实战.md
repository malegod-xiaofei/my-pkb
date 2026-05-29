# 1 Spring AI Alibaba之理论概述

![图片-001](images/图片-001.png)

## 1.1 SAA为什么会出现之AB法则(Before | After)

随着人工智能（AI）技术的迅猛发展，越来越多的开发者开始将目光投向AI应用的开发。然而，目前市场上大多数AI框架和工具如LangChain、PyTorch等主要支持Python，而Java开发者常常面临工具缺乏和学习门槛较高的问题，但是不用担心，谁让Java/Spring群体强大那？，O(∩_∩)O

任何一个框架/XXX云服务器，想要大面积推广，应该不会忘记庞大的Spring社区和Java程序员

### 1.1.1 Before

![图片-002](images/图片-002.jpeg)

### 1.1.2 After

![图片-003](images/图片-003.jpeg)

## 1.2 是什么

### 1.2.1 什么是 Spring AI Alibaba

![图片-004](images/图片-004.jpeg)

![图片-005](images/图片-005.png)

### 1.2.2 SAA公式化一句话表达

![图片-006](images/图片-006.png)

![图片-007](images/图片-007.png)

#### 1.2.2.1 Spring AI Alibaba 开源项目基于 Spring AI 构建，是阿里云通义系列模型及服务在 Java AI 应用开发领域的最佳实践，提供高层次的 AI API 抽象与云原生基础设施集成方案和企业级 AI 应用生态集成。

### 1.2.3 官网知识出处

#### 1.2.3.1 SpringAI官网

##### 1.2.3.1.1 https://spring.io/projects/spring-ai#learn

#### 1.2.3.2 Spring AI Alibaba 1.0 GA 正式发布

##### 1.2.3.2.1 https://java2ai.com/

##### 1.2.3.2.2 https://java2ai.com/blog/spring-ai-alibaba-10-ga-release/?spm=5176.29160081.0.0.2856aa5cww2t9D

#### 1.2.3.3 阿里云百炼平台

##### 1.2.3.3.1 https://bailian.console.aliyun.com/console?tab=model#/model-market

## 1.3 能干嘛

![图片-008](images/图片-008.jpeg)

Spring AI Alibaba 基于 Spring AI 构建，因此SAA继承了SpringAI 的所有原子能力抽象并在此

基础上扩充丰富了模型、向量存储、记忆、RAG 等核心组件适配，让其能够接入阿里云的 AI 生态。

## 1.4 去哪下

![图片-009](images/图片-009.jpeg)

Spring AI 官网：https://spring.io/projects/spring-ai#overview

Spring AI Alibaba 官网：https://java2ai.com

Spring AI Alibaba 仓库：https://github.com/alibaba/spring-ai-alibaba

Spring AI Alibaba 官方示例仓库：https://github.com/springaialibaba/spring-ai-alibaba-examples

Spring AI 1.0 GA 文章：https://java2ai.com/blog/spring-ai-100-ga-released

Spring AI 仓库：https://github.com/spring-projects/spring-ai

## 1.5 怎么玩

![图片-010](images/图片-010.jpeg)

### 1.5.1 核心概念

#### 1.5.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/concepts/?spm=0.29160081.0.0.25a974b1WVFya0

![图片-011](images/图片-011.jpeg)

## 1.6 SpringAI VS SpringAI Alibaba VS LangChain4J

![图片-012](images/图片-012.jpeg)
![图片-013](images/图片-013.jpeg)

# 2 永远的HelloWorld

![图片-014](images/图片-014.png)

## 2.1 前置约定

### 2.1.1 动手前模型约定

![图片-015](images/图片-015.jpeg)

![图片-016](images/图片-016.png)

![图片-017](images/图片-017.png)

### 2.1.2 SpringAI Alibaba 与 SpringAI、SpringBoot版本依赖关系

![图片-018](images/图片-018.jpeg)

https://java2ai.com/docs/1.0.0.2/faq/?spm=4347728f.6d9f13c1.0.0.17177187POpLHJ#%E6%80%8E%E4%B9%88%E7%A1%AE%E5%AE%9A-spring-ai-alibaba-%E4%B8%8E-spring-aispring-boot-%E7%89%88%E6%9C%AC%E7%9A%84%E5%85%BC%E5%AE%B9%E5%85%B3%E7%B3%BB

### 2.1.3 配置门道和关键点

#### 2.1.3.1 通过后续讲解配置规则，所有调用均基于 OpenAI协议标准或者SpringAI Aalibaba官方推荐模型服务灵积(DashScope)整合规则，实现一致的接口设计与规范，确保多模型切换的便利性，提供高度可扩展的开发支持

## 2.2 阿里云百炼平台入口官网

### 2.2.1 接入阿里百炼平台的通义模型

#### 2.2.1.1 https://bailian.console.aliyun.com/

### 2.2.2 大模型调用三件套

#### 2.2.2.1 获得Api-key

![图片-019](images/图片-019.jpeg)

#### 2.2.2.2 获得模型名

##### 2.2.2.2.1 1

![图片-020](images/图片-020.jpeg)

##### 2.2.2.2.2 2

![图片-021](images/图片-021.jpeg)

##### 2.2.2.2.3 模型名

###### 2.2.2.2.3.1 qwen-plus

#### 2.2.2.3 获得baseUrl开发地址

![图片-022](images/图片-022.jpeg)

#### 2.2.2.4 备注

##### 2.2.2.4.1 假设你要换一个模型实例

![图片-023](images/图片-023.jpeg)

### 2.2.3 小总结

#### 2.2.3.1 API Key

##### 2.2.3.1.1 sk-xxx你自己的API Key

#### 2.2.3.2 模型名

##### 2.2.3.2.1 qwen-plus

#### 2.2.3.3 调用地址

##### 2.2.3.3.1 使用SDK调用时需配置的base_url：https://dashscope.aliyuncs.com/compatible-mode/v1

## 2.3 IDEA工具中建project父工程

### 2.3.1 SpringAIAlibaba-atguiguV1

![图片-024](images/图片-024.jpeg)

### 2.3.2 使用 bom 管理依赖版本

#### 2.3.2.1 知识出处

##### 2.3.2.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/starters-and-quick-guide/?spm=5176.29160081.0.0.2856aa5c0l3sEA#%E4%BD%BF%E7%94%A8-bom-%E7%AE%A1%E7%90%86%E4%BE%9D%E8%B5%96%E7%89%88%E6%9C%AC

#### 2.3.2.2 初始总POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.atguigu.study</groupId>
    <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <name>SpringAIAlibaba-Maven父工程POM配置</name>


    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <java.version>21</java.version>
        <!-- Spring Boot 新建2025.9-->
        <spring-boot.version>3.5.5</spring-boot.version>
        <!-- Spring AI 新建2025.9-->
        <spring-ai.version>1.0.0</spring-ai.version>
        <!-- Spring AI Alibaba 新建2025.9-->
        <SpringAIAlibaba.version>1.0.0.2</SpringAIAlibaba.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <!-- Spring Boot -->
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring-boot.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <!-- Spring AI Alibaba -->
            <dependency>
                <groupId>com.alibaba.cloud.ai</groupId>
                <artifactId>spring-ai-alibaba-bom</artifactId>
                <version>${SpringAIAlibaba.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <!-- Spring AI -->
            <dependency>
                <groupId>org.springframework.ai</groupId>
                <artifactId>spring-ai-bom</artifactId>
                <version>${spring-ai.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>


    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>${spring-boot.version}</version>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

## 2.4 开发5步骤

### 2.4.1 建Module

#### 2.4.1.1 SAA-01HelloWorld

![图片-025](images/图片-025.jpeg)

#### 2.4.1.2 第2步

![图片-026](images/图片-026.jpeg)

### 2.4.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-01HelloWorld</artifactId>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!-- 引入 springai alibaba DashScope 模型适配的 Starter -->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

#### 2.4.2.1 模型服务灵积(DashScope)

![图片-027](images/图片-027.jpeg)

##### 2.4.2.1.1 https://dashscope.aliyun.com/

#### 2.4.2.2 核心组件-知识出处

![图片-028](images/图片-028.jpeg)

### 2.4.3 写YML

```properties
server.port=8001

#大模型对话中文乱码UTF8编码处理
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-01HelloWorld

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
spring.ai.dashscope.base-url=https://dashscope.aliyuncs.com/compatible-mode/v1
spring.ai.dashscope.chat.options.model=qwen-plus
```

### 2.4.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa01HelloWorldApplication
{

    public static void main(String[] args)
    {
        SpringApplication.run(Saa01HelloWorldApplication.class, args);
    }

}
```

### 2.4.5 业务类

#### 2.4.5.1 ApiKey不可以明文 需配置进环境变量

##### 2.4.5.1.1 修改环境变量

![图片-029](images/图片-029.jpeg)

##### 2.4.5.1.2 K-V键值对设置

![图片-030](images/图片-030.jpeg)

##### 2.4.5.1.3 需要重启IDEA

#### 2.4.5.2 配置类SaaLLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyy
 * @create 2025-07-22 0:51
 */
@Configuration
public class SaaLLMConfig
{
    /*方式1

    1.1
    yml文件配置：spring.ai.dashscope.api-key=${aliQwen-api}

    1.2
    @Value("${spring.ai.dashscope.api-key}")
    private String apiKey;、

    1.3
    @Bean
    public DashScopeApi dashScopeApi()
    {
        return DashScopeApi.builder().apiKey(apiKey).build();
    }
    */

    /**
     * 方式2
     * yml文件配置：spring.ai.dashscope.api-key=${aliQwen-api}
     * @return
     */
    @Bean
    public DashScopeApi dashScopeApi()
    {
        return DashScopeApi.builder()
                    .apiKey(System.getenv("aliQwen-api"))
                .build();
    }
}
```

##### 2.4.5.2.1 方式1

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-22 0:51
 */
@Configuration
public class SaaLLMConfig
{

    /**
     * 方式1:${}
     * 持有yml文件配置：spring.ai.dashscope.api-key=${aliQwen-api}
     */
    @Value("${spring.ai.dashscope.api-key}")
    private String apiKey;

    @Bean
    public DashScopeApi dashScopeApi()
    {
        return DashScopeApi.builder().apiKey(apiKey).build();
    }
}
```

##### 2.4.5.2.2 方式2

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-22 0:51
 */
@Configuration
public class SaaLLMConfig
{
    /**
     * 方式2:System.getenv("环境变量")
     * 持有yml文件配置：spring.ai.dashscope.api-key=${aliQwen-api}
     * @return
     */
    @Bean
    public DashScopeApi dashScopeApi()
    {
        return DashScopeApi.builder()
                    .apiKey(System.getenv("aliQwen-api"))
                .build();
    }
}
```

#### 2.4.5.3 对话模型(Chat Model)

##### 2.4.5.3.1 ChatModel，文本聊天交互模型

![图片-031](images/图片-031.jpeg)

![图片-032](images/图片-032.jpeg)

##### 2.4.5.3.2 知识出处

###### 2.4.5.3.2.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/chat-model/?spm=5176.29160081.0.0.2856aa5ctpxysy

#### 2.4.5.4 controller

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-22 0:47
 */
@RestController
public class ChatHelloController
{
    @Resource //阿里云百炼
    private ChatModel dashScopeChatModel;

    /**
     * http://localhost:8001/hello/dochat
     * @param msg
     * @return
     */
    @GetMapping("/hello/dochat")
    public String doChat(@RequestParam(name = "msg",defaultValue = "你是谁") String msg)
    {
        String result = dashScopeChatModel.call(msg);
        System.out.println("响应：" + result);
        return result;
    }

    /**
     *  http://localhost:8001/hello/streamchat
     * @param msg
     * @return
     */
    @GetMapping("/hello/streamchat")
    public Flux<String> streamChat(@RequestParam(name = "msg",defaultValue = "你是谁") String msg)
    {
        return dashScopeChatModel.stream(msg);
    }
}
```

#### 2.4.5.5 测试

##### 2.4.5.5.1 http://localhost:8001/hello/dochat

##### 2.4.5.5.2 http://localhost:8001/hello/streamchat

## 2.5 问题思考，小总结更进一步，O(∩_∩)O

### 2.5.1 切换其它大模型

#### 2.5.1.1 https://bailian.console.aliyun.com/console?tab=model#/model-market?provider=

![图片-033](images/图片-033.jpeg)

#### 2.5.1.2 yml配置文件修改

```properties
server.port=8001

server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-01HelloWorld

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
spring.ai.dashscope.chat.options.model=deepseek-v3
```

### 2.5.2 配置省略下

#### 2.5.2.1 O(∩_∩)O

### 2.5.3 和OpenAI协议对比下

```text
#通过openai协议调用通义千问
#spring.ai.openai.api-key=${aliQwen-api}
#spring.ai.openai.base-url=https://dashscope.aliyuncs.com/compatible-mode
#spring.ai.openai.chat.options.model=qwen-plus
```

```xml
<!--spring-ai-openai-->
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-model-openai</artifactId>
        </dependency>
```

```xml
<!-- 引入 springai alibaba DashScope 模型适配的 Starter -->
<dependency>
    <groupId>com.alibaba.cloud.ai</groupId>
    <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
</dependency>
```

### 2.5.4 yml配置文件修改v2

# 3 Ollama私有化部署和对接本地大模型

![图片-034](images/图片-034.png)

## 3.1 Ollama本地大模型部署

![图片-035](images/图片-035.png)

#### 3.1.1.1 LLM大模型工具Ollama

##### 3.1.1.1.1 是什么

![图片-036](images/图片-036.jpeg)

###### 3.1.1.1.1.1 官网

![图片-037](images/图片-037.jpeg)

###### 3.1.1.1.1.2 Docker Hub玩镜像

###### 3.1.1.1.1.3 Ollama Hub玩模型

##### 3.1.1.1.2 能干嘛

###### 3.1.1.1.2.1 产品定位

![图片-038](images/图片-038.jpeg)

##### 3.1.1.1.3 去哪下

![图片-039](images/图片-039.jpeg)
![图片-040](images/图片-040.jpeg)

###### 3.1.1.1.3.1 https://ollama.com/download

![图片-041](images/图片-041.jpeg)

##### 3.1.1.1.4 怎么玩

![图片-042](images/图片-042.jpeg)

#### 3.1.1.2 安装Ollama

##### 3.1.1.2.1 自定义Ollama安装路径

![图片-043](images/图片-043.gif)

##### 3.1.1.2.2 手动创建大模型存储目录

![图片-044](images/图片-044.jpeg)

新建一个环境变量

OLLAMA_MODELS

D:\devSoft\Ollama\models

##### 3.1.1.2.3 复制转移大模型存储目录

![图片-045](images/图片-045.jpeg)

#### 3.1.1.3 安装通义千问大模型

##### 3.1.1.3.1 验证是否安装成功

![图片-046](images/图片-046.jpeg)

###### 3.1.1.3.1.1 netstat -ano | findstr 11434

###### 3.1.1.3.1.2 ollama --version

##### 3.1.1.3.2 千问模型为例

![图片-047](images/图片-047.jpeg)
![图片-048](images/图片-048.jpeg)

###### 3.1.1.3.2.1 ollama run qwen:4b

##### 3.1.1.3.3 deepseek

![图片-049](images/图片-049.jpeg)

###### 3.1.1.3.3.1 ollama run deepseek-r1:14b

#### 3.1.1.4 退出

![图片-050](images/图片-050.jpeg)

## 3.2 微服务对接本地大模型

### 3.2.1 编码案例

#### 3.2.1.1 建Module

##### 3.2.1.1.1 SAA-02Ollama

#### 3.2.1.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-02Ollama</artifactId>


    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--ollama-->
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-model-ollama</artifactId>
            <version>1.0.0</version>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

#### 3.2.1.3 写YML

```properties
server.port=8002

server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-02Ollama

# ====ollama Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
spring.ai.ollama.base-url=http://localhost:11434
spring.ai.ollama.chat.model=qwen2.5:latest
```

#### 3.2.1.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @auther zzyy
 * @create 2025-07-22 18:50
 */
@SpringBootApplication
public class Saa02OllamaApplication
{
    public static void main(String[] args)
    {
        SpringApplication.run(Saa02OllamaApplication.class,args);
    }
}
```

#### 3.2.1.5 业务类

##### 3.2.1.5.1 controller

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyy
 * @create 2025-07-22 18:56
 */
@RestController
public class OllamaController
{
    @Resource
    private ChatModel chatModel;

    /**
     * http://localhost:8002/ollama/chat?msg=你是谁
     * @param msg
     * @return
     */
    @GetMapping("/ollama/chat")
    public String chat(@RequestParam(name = "msg") String msg)
    {
        String result = chatModel.call(msg);
        System.out.println("---结果：" + result);
        return result;
    }

    @GetMapping("/ollama/streamchat")
    public Flux<String> streamchat(@RequestParam(name = "msg",defaultValue = "你是谁") String msg)
    {
        return chatModel.stream(msg);
    }
}
```

###### 3.2.1.5.1.1 故障现象

![图片-051](images/图片-051.jpeg)

###### 3.2.1.5.1.2 导致原因

![图片-052](images/图片-052.jpeg)

![图片-053](images/图片-053.jpeg)

##### 3.2.1.5.2 controller

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyy
 * @create 2025-07-22 18:56
 */
@RestController
public class OllamaController
{
    @Resource(name = "ollamaChatModel")
    private ChatModel chatModel;

    /**
     * http://localhost:8002/ollama/chat?msg=你是谁
     * @param msg
     * @return
     */
    @GetMapping("/ollama/chat")
    public String chat(@RequestParam(name = "msg") String msg)
    {
        String result = chatModel.call(msg);
        System.out.println("---结果：" + result);
        return result;
    }

    @GetMapping("/ollama/streamchat")
    public Flux<String> streamchat(@RequestParam(name = "msg",defaultValue = "你是谁") String msg)
    {
        return chatModel.stream(msg);
    }
}
```

###### 3.2.1.5.2.1 或者

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyy
 * @create 2025-07-22 18:56
 */
@RestController
public class OllamaController
{
    /*@Resource(name = "ollamaChatModel")
    private ChatModel chatModel;*/

    //方式2
    @Resource
    @Qualifier("ollamaChatModel")
    private ChatModel chatModel;

    /**
     * http://localhost:8002/ollama/chat?msg=你是谁
     * @param msg
     * @return
     */
    @GetMapping("/ollama/chat")
    public String chat(@RequestParam(name = "msg") String msg)
    {
        String result = chatModel.call(msg);
        System.out.println("---结果：" + result);
        return result;
    }

    @GetMapping("/ollama/streamchat")
    public Flux<String> streamchat(@RequestParam(name = "msg",defaultValue = "你是谁") String msg)
    {
        return chatModel.stream(msg);
    }
}
```

# 4 ChatClient VS ChatModel

![图片-054](images/图片-054.png)

## 4.1 问题回顾

### 4.1.1 之前的调用都是使用ChatModel进行

![图片-055](images/图片-055.jpeg)

### 4.1.2 认识一个新的接口ChatClient

![图片-056](images/图片-056.jpeg)

![图片-057](images/图片-057.jpeg)

## 4.2 ChatModel

### 4.2.1 官网

#### 4.2.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/chat-model/?spm=5176.29160081.0.0.2856aa5cmUTyXC

![图片-058](images/图片-058.jpeg)

![图片-059](images/图片-059.jpeg)

### 4.2.2 说明

#### 4.2.2.1 对话模型(ChatModel)是底层接口，直接与具体大语言模型交互， 提供call()和stream()方法，适合简单大模型交互场景

## 4.3 ChatClient

### 4.3.1 官网

#### 4.3.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/chat-client/?spm=5176.29160081.0.0.2856aa5cmUTyXC

![图片-060](images/图片-060.jpeg)

#### 4.3.1.2 何为样板代码？ ChatClient对ChatModel吐槽

![图片-061](images/图片-061.jpeg)

### 4.3.2 说明

#### 4.3.2.1 ChatClient是高级封装，基于ChatModel构建，适合快速构建标准化复杂AI服务，支持同步和流式交互，集成多种高级功能。

## 4.4 编码案例

### 4.4.1 建Module

#### 4.4.1.1 SAA-03ChatModelChatClient

### 4.4.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-03ChatModelChatClient</artifactId>


    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

### 4.4.3 写YML

```properties
server.port=8003

server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-03ChatModelChatClient

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

### 4.4.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa03ChatModelChatClientApplication
{

    public static void main(String[] args)
    {
        SpringApplication.run(Saa03ChatModelChatClientApplication.class, args);
    }

}
```

### 4.4.5 业务类第1版

#### 4.4.5.1 Only ChatModel

#### 4.4.5.2 新建配置类SaaLLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyy
 * @create 2025-07-22 0:51
 */
@Configuration
public class SaaLLMConfig
{
    @Bean
    public DashScopeApi dashScopeApi()
    {
        return DashScopeApi.builder().apiKey(System.getenv("aliQwen-api")).build();
    }
}
```

#### 4.4.5.3 controller

```java
package com.atguigu.study.controller;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @auther zzyy
 * @create 2025-07-23 18:20
 */
@RestController
public class ChatModelController
{
    @Resource //阿里云百炼
    private ChatModel dashScopeChatModel;

    @GetMapping("/chatmodel/dochat")
    public String doChat(@RequestParam(name = "msg",defaultValue = "你是谁") String msg)
    {
        String result = dashScopeChatModel.call(msg);
        System.out.println("响应：" + result);
        return result;
    }
}
```

#### 4.4.5.4 进一步新增ChatClient

![图片-062](images/图片-062.png)

##### 4.4.5.4.1 重启下微服务看看效果

![图片-063](images/图片-063.jpeg)

##### 4.4.5.4.2 上步结论

###### 4.4.5.4.2.1 ChatClient不支持自动注入，只能手动注入，/(ㄒoㄒ)/~~

### 4.4.6 业务类第2版

#### 4.4.6.1 知识出处

##### 4.4.6.1.1 chat源码

###### 4.4.6.1.1.1 https://java2ai.com/docs/1.0.0.2/spring-ai-sourcecode-explained/chapter-1-chat-first-experience/?spm=5176.29160081.0.0.2856aa5cbeDVer

##### 4.4.6.1.2 ChatClient使用

###### 4.4.6.1.2.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/chat-client/?spm=5176.29160081.0.0.2856aa5cmUTyXC#%E5%88%9B%E5%BB%BA-chatclient

#### 4.4.6.2 Only ChatClient

#### 4.4.6.3 新建ChatClientController

```java
package com.atguigu.study.controller;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-23 19:22
 * 知识出处：
 * https://java2ai.com/docs/1.0.0.2/tutorials/basics/chat-client/?spm=5176.29160081.0.0.2856aa5cmUTyXC#%E5%88%9B%E5%BB%BA-chatclient
 */
@RestController
public class ChatClientController
{
    private final ChatClient dashScopechatClient;

    /**
     * 使用自动配置的 ChatClient.Builder
     * @param dashscopeChatModel
     */
    public ChatClientController(ChatModel dashscopeChatModel)
    {
        this.dashScopechatClient = ChatClient.builder(dashscopeChatModel).build();
    }

    /**
     * http://localhost:8003/chatclient/dochat
     * @param msg
     * @return
     */
    @GetMapping("/chatclient/dochat")
    public String doChat(@RequestParam(name = "msg",defaultValue = "2加4等于几") String msg)
    {
        String result = dashScopechatClient.prompt().user(msg).call().content();
        System.out.println("响应：" + result);
        return result;
    }
}
```

#### 4.4.6.4 ChatModel对ChatClient吐槽

##### 4.4.6.4.1 离开我你什么都不是，O(∩_∩)O

### 4.4.7 业务类第3版

#### 4.4.7.1 ChatModel + ChatClient混合使用

#### 4.4.7.2 修改配置类SaaLLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyy
 * @create 2025-07-22 0:51
 */
@Configuration
public class SaaLLMConfig
{
    @Bean
    public DashScopeApi dashScopeApi()
    {
        return DashScopeApi.builder()
                    .apiKey(System.getenv("aliQwen-api"))
                .build();
    }

    /**
     * 知识出处：
     * https://java2ai.com/docs/1.0.0.2/tutorials/basics/chat-client/?spm=5176.29160081.0.0.2856aa5cmUTyXC#%E5%88%9B%E5%BB%BA-chatclient
     * @param dashscopeChatModel
     * @return
     */
    @Bean
    public ChatClient chatClient(ChatModel dashscopeChatModel)
    {
        return ChatClient.builder(dashscopeChatModel).build();
    }
}
```

#### 4.4.7.3 新建ChatClientControllerV2

```java
package com.atguigu.study.controller;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @auther zzyy
 * @create 2025-07-23 19:31
 */
@RestController
public class ChatClientControllerV2
{
    /**
     * chatModel + ChatClient 混合使用
     */
    @Resource
    private ChatModel chatModel;

    @Resource
    private ChatClient dashScopechatClientv2;

    /**
     * http://localhost:8003/chatclientv2/dochat
     * @param msg
     * @return
     */
    @GetMapping("/chatclientv2/dochat")
    public String doChat(@RequestParam(name = "msg",defaultValue = "你是谁") String msg)
    {
        String result = dashScopechatClientv2.prompt().user(msg).call().content();
        System.out.println("ChatClient响应：" + result);
        return result;
    }

    /**
     * http://localhost:8003/chatmodelv2/dochat
     * @param msg
     * @return
     */
    @GetMapping("/chatmodelv2/dochat")
    public String doChat2(@RequestParam(name = "msg",defaultValue = "你是谁") String msg)
    {
        String result = chatModel.call(msg);
        System.out.println("ChatModel响应：" + result);
        return result;
    }
}
```

### 4.4.8 小总结

#### 4.4.8.1 生产推荐

##### 4.4.8.1.1 混合使用

##### 4.4.8.1.2 两者不是非此即彼，可以同时出现交替使用

#### 4.4.8.2 对比

![图片-064](images/图片-064.jpeg)

## 4.5 问题思考，更进一步，O(∩_∩)O

### 4.5.1 要求同时存在多种大模型产品在系统里共存使用

# 5 Server-SentEvents(SSE) 实现Stream流式输出及多模型共存

![图片-065](images/图片-065.png)

## 5.1 Response Streaming流式输出

### 5.1.1 是什么

流式输出(StreamingOutput)

是一种逐步返回大模型生成结果的技术，生成一点返回一点，允许服务器将响应内容

分批次实时传输给客户端，而不是等待全部内容生成完毕后再一次性返回。

这种机制能显著提升用户体验，尤其适用于大模型响应较慢的场景（如生成长文本或复杂推理结果）。

### 5.1.2 SpringAI Alibaba流式输出有两种

#### 5.1.2.1 通过ChatModel实现stream实现流式输出

#### 5.1.2.2 通过ChatClient实现stream实现流式输出

### 5.1.3 前置知识点说明---Springboot3响应式编程

https://www.bilibili.com/video/BV1Es4y1q7Bf?spm_id_from=333.788.videopod.episodes&vd_source=f3f60f7acbef49d38b97c4d660d439fc&p=110

![图片-066](images/图片-066.jpeg)

## 5.2 SSE(Server-Sent Events)服务器发送事件

### 5.2.1 Server-Sent：由服务器发送。

### 5.2.2 Events：事件，指服务器主动推送给客户端的数据或消息

### 5.2.3 Server-SentEvents(SSE)服务器发送事件 实现流式输出

Server-Sent Events (SSE) 是一种允许服务端可以持续推送数据片段（如逐词或逐句）到前端的 Web 技术。通过单向的HTTP长连接，使用一个长期存在的连接，让服务器可以主动将数据"推"给客户端，SSE是轻量级的单向通信协议，适合AI对话这类服务端主导的场景

核心概念

SSE 的核心思想是：客户端发起一个请求，服务器保持这个连接打开并在有新数据时，通过这个连接将数据发送给客户端。这与传统的请求-响应模式（客户端请求一次，服务器响应一次，连接关闭）有本质区别。SSE下一代（Stream able Http）

![图片-067](images/图片-067.jpeg)

### 5.2.4 一句话

#### 5.2.4.1 一种让服务器能够主动、持续地向客户端（比如你的网页浏览器）推送数据的技术

### 5.2.5 SSE适用场景

![图片-068](images/图片-068.png)

## 5.3 开发步骤

### 5.3.1 要求同时存在多种大模型产品在系统里共存使用

### 5.3.2 新建子模块Module

#### 5.3.2.1 SAA-04StreamingOutput

### 5.3.3 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-04StreamingOutput</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

### 5.3.4 写YML

```properties
server.port=8004

server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-04StreamingOutput

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

### 5.3.5 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 18:53
 * @Description 流式输出
 */
@SpringBootApplication
public class Saa04StreamingOutputApplication
{

    public static void main(String[] args)
    {
        SpringApplication.run(Saa04StreamingOutputApplication.class, args);
    }
}
```

### 5.3.6 业务类

#### 5.3.6.1 通过ChatModel实现stream实现流式输出

##### 5.3.6.1.1 配置类LLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatModel;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatOptions;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.ChatOptions;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 18:53
 * @Description ChatModel+ChatClient+多模型共存
 */
@Configuration
public class SaaLLMConfig
{
    // 模型名称常量定义
    private final String DEEPSEEK_MODEL = "deepseek-v3";
    private final String QWEN_MODEL = "qwen-plus";

    @Bean(name = "deepseek")
    public ChatModel deepSeek()
    {
        return DashScopeChatModel.builder()
                        .dashScopeApi(DashScopeApi.builder()
                                    .apiKey(System.getenv("aliQwen-api"))
                                .build())
                .defaultOptions(
                        DashScopeChatOptions.builder().withModel(DEEPSEEK_MODEL).build()
                )
                .build();
    }

    @Bean(name = "qwen")
    public ChatModel qwen()
    {
        return DashScopeChatModel.builder().dashScopeApi(DashScopeApi.builder()
                        .apiKey(System.getenv("aliQwen-api"))
                        .build())
                .defaultOptions(
                        DashScopeChatOptions.builder()
                                .withModel(QWEN_MODEL)
                                .build()
                )
                .build();
    }
}
```

##### 5.3.6.1.2 controller第1版

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 18:53
 * @Description 流式输出
 */
@RestController
public class StreamOutputController
{
    //V1 通过ChatModel实现stream实现流式输出
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
```

```java
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;


    @GetMapping(value = "/stream/chatflux1")
    public Flux<String> chatflux(@RequestParam(name = "question",defaultValue = "你是谁") String question)
    {
        return deepseekChatModel.stream(question);
    }

    @GetMapping(value = "/stream/chatflux2")
    public Flux<String> chatflux2(@RequestParam(name = "question",defaultValue = "你是谁") String question)
    {
        return qwenChatModel.stream(question);
    }
}
```

#### 5.3.6.2 通过ChatClient实现stream实现流式输出

##### 5.3.6.2.1 配置类LLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatModel;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatOptions;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.ChatOptions;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 18:53
 * @Description ChatModel+ChatClient+多模型共存
 */
@Configuration
public class SaaLLMConfig
{
    // 模型名称常量定义
    private final String DEEPSEEK_MODEL = "deepseek-v3";
    private final String QWEN_MODEL = "qwen-plus";

    @Bean(name = "deepseek")
    public ChatModel deepSeek()
    {
        return DashScopeChatModel.builder()
                        .dashScopeApi(DashScopeApi.builder()
                                    .apiKey(System.getenv("aliQwen-api"))
                                .build())
                .defaultOptions(
                        DashScopeChatOptions.builder().withModel(DEEPSEEK_MODEL).build()
                )
                .build();
    }

    @Bean(name = "qwen")
    public ChatModel qwen()
    {
        return DashScopeChatModel.builder().dashScopeApi(DashScopeApi.builder()
                        .apiKey(System.getenv("aliQwen-api"))
                        .build())
                .defaultOptions(
                        DashScopeChatOptions.builder()
                                .withModel(QWEN_MODEL)
                                .build()
                )
                .build();
    }

    @Bean(name = "deepseekChatClient")
    public ChatClient deepseekChatClient(@Qualifier("deepseek") ChatModel deepSeek)
    {
        return ChatClient.builder(deepSeek)
                .defaultOptions(ChatOptions.builder()
                        .model(DEEPSEEK_MODEL)
                        .build())
                .build();
    }


    @Bean(name = "qwenChatClient")
    public ChatClient qwenChatClient(@Qualifier("qwen") ChatModel qwen)
    {
        return ChatClient.builder(qwen)
                .defaultOptions(ChatOptions.builder()
                        .model(QWEN_MODEL)
                        .build())
                .build();
    }
}
```

##### 5.3.6.2.2 controller第2版

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 18:53
 * @Description 流式输出
 */
@RestController
public class StreamOutputController
{
    //V1 通过ChatModel实现stream实现流式输出
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;

    //V2 通过ChatClient实现stream实现流式输出
    @Resource(name = "deepseekChatClient")
    private ChatClient deepseekChatClient;
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;

    @GetMapping(value = "/stream/chatflux1")
    public Flux<String> chatflux(@RequestParam(name = "question",defaultValue = "你是谁") String question)
    {
        return deepseekChatModel.stream(question);
    }

    @GetMapping(value = "/stream/chatflux2")
    public Flux<String> chatflux2(@RequestParam(name = "question",defaultValue = "你是谁") String question)
    {
        return qwenChatModel.stream(question);
    }

    @GetMapping(value = "/stream/chatflux3")
    public Flux<String> chatflux3(@RequestParam(name = "question",defaultValue = "你是谁") String question)
    {
        return deepseekChatClient.prompt(question).stream().content();
    }

    @GetMapping(value = "/stream/chatflux4")
    public Flux<String> chatflux4(@RequestParam(name = "question",defaultValue = "你是谁") String question)
    {
        return qwenChatClient.prompt(question).stream().content();
    }
}
```

## 5.4 新增前端代码trytry

### 5.4.1 前端效果

![图片-069](images/图片-069.jpeg)

![图片-070](images/图片-070.jpeg)

### 5.4.2 Flux<T>本质提一嘴

![图片-071](images/图片-071.jpeg)

Flux是SpringWebFlux中的一个核心组件，属于响应式编程模型的一部分。它主要用于处理异步、非阻塞的流式数据，能够高效地处理高并发场景。Flux可以生成和处理一系列的事件或数据如流式输出等。

看类注释和类所在的jar包我们就明白：

SAA中的流式输出是通过ReactorStreams技术实现的和SpringWebFlux的底层实现是一样的技术。

具体执行流程：

ReactorStreams会订阅数据源，当有数据时，ReactorStreams以分块流的方式发送给客户端用户。

### 5.4.3 SSE

#### 5.4.3.1 index.html

```text
<!DOCTYPE html>
<html>
<head>
    <title>SSE流式chat</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }

        #messageInput {
            width: 90%;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
            margin-bottom: 10px;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        #messages {
            margin-top: 20px;
            padding: 15px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 8px;
            max-height: 300px;
            overflow-y: auto;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        #messages div {
            padding: 8px 0;
            border-bottom: 1px solid #eee;
            font-size: 14px;
            color: #333;
        }

        #messages div:last-child {
            border-bottom: none;
        }
    </style>
</head>
<body>
<textarea id="messageInput" rows="4" cols="50" placeholder="请输入你的问题..."></textarea><br>
<button onclick="sendMsg()">发送提问</button>
<div id="messages"></div>
<script>
    function sendMsg() {
        // 获取用户输入的消息
        const message = document.getElementById('messageInput').value;
        if (message == "") return false;

        //1 客户端使用 JavaScript 的 EventSource 对象连接到服务器上的一个特定端点（URL）
        const eventSource = new EventSource('stream/chatflux2?question=' + message);
        //2 监听消息事件
        eventSource.onmessage = function (event) {
            // 获取流式返回的数据
            const data = event.data;
            // 将接收到的数据展示到页面上
            const messagesDiv = document.getElementById('messages');
            messagesDiv.innerHTML += event.data;
        };

        //3 监听错误事件
        eventSource.onerror = function (error) {
            console.error('EventSource 发生错误：', error);
            eventSource.close(); // 关闭连接
        };
    }
</script>
</body>
</html>
```

#### 5.4.3.2 存放位置

![图片-072](images/图片-072.png)

### 5.4.4 测试

#### 5.4.4.1 http://localhost:8004/index.html

# 6 提示词Prompt

![图片-073](images/图片-073.png)

## 6.1 DeepSeek提示词样例

### 6.1.1 https://api-docs.deepseek.com/zh-cn/prompt-library/

![图片-074](images/图片-074.jpeg)

## 6.2 是什么

### 6.2.1 官网

![图片-075](images/图片-075.jpeg)

#### 6.2.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/prompt/?spm=5176.29160081.0.0.2856aa5cdeol7a

### 6.2.2 先从最简单的API调用说起

![图片-076](images/图片-076.jpeg)

![图片-077](images/图片-077.jpeg)

可以近似的理解

Prompt > Message > String简单的字符串

#### 6.2.2.1 API 概览

![图片-078](images/图片-078.jpeg)

### 6.2.3 再从源码Prompt说起

#### 6.2.3.1 String

##### 6.2.3.1.1 最初的Prompt只是简单的文本字符串提问

#### 6.2.3.2 Message

![图片-079](images/图片-079.jpeg)

##### 6.2.3.2.1 enum MessageType

![图片-080](images/图片-080.jpeg)

##### 6.2.3.2.2 上述也称为

###### 6.2.3.2.2.1 Prompt 中的四大角色（Role）

#### 6.2.3.3 Prompt

最下面

![图片-081](images/图片-081.jpeg)

![图片-082](images/图片-082.jpeg)

可以近似的理解

Prompt > Message > String 简单的文本字符串提问

## 6.3 Prompt中的四大角色（Role）

### 6.3.1 总体概述

![图片-083](images/图片-083.jpeg)

#### 6.3.1.1 源码说明

![图片-084](images/图片-084.jpeg)

![图片-085](images/图片-085.png)

#### 6.3.1.2 设定AI行为边界/角色/定位。指导AI的行为和响应方式，设置AI如何解释和回复输入的

![图片-086](images/图片-086.png)

#### 6.3.1.3 用户原始提问输入。代表用户的输入他们向AI提出的问题、命令或陈述。

![图片-087](images/图片-087.png)

#### 6.3.1.4 AI返回的响应信息，定义为”助手角色”消息。用它可以确保上下文能够连贯的交互。

#### 6.3.1.5 记忆对话，积累回答

![图片-088](images/图片-088.jpeg)

![图片-089](images/图片-089.png)

#### 6.3.1.6 桥接外部服务，可以进行函数调用如，支付/数据查询等操作，类似调用第3方util工具类，后面章节详细介绍

### 6.3.2 小总结

![图片-090](images/图片-090.jpeg)

## 6.4 开发步骤

### 6.4.1 新建子模块Module

#### 6.4.1.1 springAI-05chat-Prompt

### 6.4.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.zzyy.stduy</groupId>
        <artifactId>SpringAI-zyfanV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>springAI-05chat-Prompt</artifactId>


    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>


    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-openai-->
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-model-openai</artifactId>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.34</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>17</source>
                    <target>17</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### 6.4.3 写YML

```properties
server.port=8005

server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-05Prompt


# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

### 6.4.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 20:56
 * @Description 知识出处，https://java2ai.com/docs/1.0.0.2/tutorials/basics/prompt/?spm=5176.29160081.0.0.2856aa5cdeol7a
 */
@SpringBootApplication
public class Saa05PromptApplication
{
    public static void main(String[] args)
    {
        SpringApplication.run(Saa05PromptApplication.class,args);
    }
}
```

### 6.4.5 业务类

#### 6.4.5.1 配置类LLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatModel;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatOptions;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.ChatOptions;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 18:53
 * @Description ChatModel+ChatClient+多模型共存
 */
@Configuration
public class SaaLLMConfig
{
    // 模型名称常量定义
    private final String DEEPSEEK_MODEL = "deepseek-v3";
    private final String QWEN_MODEL = "qwen-plus";

    @Bean(name = "deepseek")
    public ChatModel deepSeek()
    {
        return DashScopeChatModel.builder()
                        .dashScopeApi(DashScopeApi.builder()
                                    .apiKey(System.getenv("aliQwen-api"))
                                .build())
                .defaultOptions(
                        DashScopeChatOptions.builder().withModel(DEEPSEEK_MODEL).build()
                )
                .build();
    }

    @Bean(name = "qwen")
    public ChatModel qwen()
    {
        return DashScopeChatModel.builder().dashScopeApi(DashScopeApi.builder()
                        .apiKey(System.getenv("aliQwen-api"))
                        .build())
                .defaultOptions(
                        DashScopeChatOptions.builder()
                                .withModel(QWEN_MODEL)
                                .build()
                )
                .build();
    }

    @Bean(name = "deepseekChatClient")
    public ChatClient deepseekChatClient(@Qualifier("deepseek") ChatModel deepSeek)
    {
        return ChatClient.builder(deepSeek)
                .defaultOptions(ChatOptions.builder()
                        .model(DEEPSEEK_MODEL)
                        .build())
                .build();
    }


    @Bean(name = "qwenChatClient")
    public ChatClient qwenChatClient(@Qualifier("qwen") ChatModel qwen)
    {
        return ChatClient.builder(qwen)
                .defaultOptions(ChatOptions.builder()
                        .model(QWEN_MODEL)
                        .build())
                .build();
    }
}
```

#### 6.4.5.2 controller第1版

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.AssistantMessage;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 21:25
 * @Description 知识出处，https://java2ai.com/docs/1.0.0.2/tutorials/basics/prompt/?spm=5176.29160081.0.0.2856aa5cdeol7a
 */
@RestController
public class PromptController
{
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;

    @Resource(name = "deepseekChatClient")
    private ChatClient deepseekChatClient;
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;

    // http://localhost:8005/prompt/chat?question=火锅介绍下
    @GetMapping("/prompt/chat")
    public Flux<String> chat(String question)
    {
        return deepseekChatClient.prompt()
                // AI 能力边界
                              .system("你是一个法律助手，只回答法律问题，其它问题回复，我只能回答法律相关问题，其它无可奉告")
                .user(question)
                .stream()
                .content();
    }
}
```

##### 6.4.5.2.1 通过ChatClient实现

![图片-091](images/图片-091.png)

![图片-092](images/图片-092.png)

##### 6.4.5.2.2 测试

![图片-093](images/图片-093.jpeg)

#### 6.4.5.3 controller第2版

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.AssistantMessage;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 21:25
 * @Description 知识出处，https://java2ai.com/docs/1.0.0.2/tutorials/basics/prompt/?spm=5176.29160081.0.0.2856aa5cdeol7a
 */
@RestController
public class PromptController
{
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;

    @Resource(name = "deepseekChatClient")
    private ChatClient deepseekChatClient;
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;

    // http://localhost:8005/prompt/chat?question=火锅介绍下
    @GetMapping("/prompt/chat")
    public Flux<String> chat(String question)
    {
        return deepseekChatClient.prompt()
                // AI 能力边界
                .system("你是一个法律助手，只回答法律问题，其它问题回复，我只能回答法律相关问题，其它无可奉告")
                .user(question)
                .stream()
                .content();
    }


    @GetMapping("/prompt/chat2")
    public Flux<ChatResponse> chat2(String question)
    {
        // 用户消息
        UserMessage userMessage = new UserMessage(question);
        // 系统消息
        SystemMessage systemMessage = new SystemMessage("你是一个讲故事的助手,每个故事控制在300字以内");

        Prompt prompt = new Prompt(userMessage, systemMessage);

        return deepseekChatModel.stream(prompt);

    }

    @GetMapping("/prompt/chat3")
    public Flux<String> chat3(String question)
    {
        // 用户消息
        UserMessage userMessage = new UserMessage(question);
        // 系统消息
        SystemMessage systemMessage = new SystemMessage("你是一个讲故事的助手,每个故事控制在300字以内");

        Prompt prompt = new Prompt(userMessage, systemMessage);

        return deepseekChatModel.stream(prompt)
                .map(response -> response.getResults().get(0).getOutput().getText());

    }
}
```

##### 6.4.5.3.1 通过ChatModel实现

![图片-094](images/图片-094.jpeg)

#### 6.4.5.4 controller第3版

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.AssistantMessage;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 21:25
 * @Description 知识出处，https://java2ai.com/docs/1.0.0.2/tutorials/basics/prompt/?spm=5176.29160081.0.0.2856aa5cdeol7a
 */
@RestController
public class PromptController
{
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;

    @Resource(name = "deepseekChatClient")
    private ChatClient deepseekChatClient;
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;

    // http://localhost:8005/prompt/chat?question=火锅介绍下
    @GetMapping("/prompt/chat")
    public Flux<String> chat(String question)
    {
        return deepseekChatClient.prompt()
                // AI 能力边界
                .system("你是一个法律助手，只回答法律问题，其它问题回复，我只能回答法律相关问题，其它无可奉告")
                .user(question)
                .stream()
                .content();
    }


    @GetMapping("/prompt/chat2")
    public Flux<ChatResponse> chat2(String question)
    {
        // 用户消息
        UserMessage userMessage = new UserMessage(question);
        // 系统消息
        SystemMessage systemMessage = new SystemMessage("你是一个讲故事的助手,每个故事控制在300字以内");

        Prompt prompt = new Prompt(userMessage, systemMessage);

        return deepseekChatModel.stream(prompt);

    }

    @GetMapping("/prompt/chat3")
    public Flux<String> chat3(String question)
    {
        // 用户消息
        UserMessage userMessage = new UserMessage(question);
        // 系统消息
        SystemMessage systemMessage = new SystemMessage("你是一个讲故事的助手,每个故事控制在300字以内");

        Prompt prompt = new Prompt(userMessage, systemMessage);

        return deepseekChatModel.stream(prompt)
                .map(response -> response.getResults().get(0).getOutput().getText());

    }
    @GetMapping("/prompt/chat4")
    public String chat4(String question)
    {
        AssistantMessage assistantMessage = deepseekChatClient.prompt()
                    .user(question)
                    .call()
                    .chatResponse()
                    .getResult()
                    .getOutput();

        return assistantMessage.getText();
    }

}
```

![图片-095](images/图片-095.png)

###### 6.4.5.4.1.1 AI返回的响应信息，定义为”助手角色”消息。用它可以确保上下文能够连贯的交互。

###### 6.4.5.4.1.2 记忆对话，积累回答

![图片-096](images/图片-096.jpeg)

#### 6.4.5.5 controller第4版

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.AssistantMessage;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.ToolResponseMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

import java.util.List;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 21:25
 * @Description 知识出处，https://java2ai.com/docs/1.0.0.2/tutorials/basics/prompt/?spm=5176.29160081.0.0.2856aa5cdeol7a
 */
@RestController
public class PromptController
{
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;

    @Resource(name = "deepseekChatClient")
    private ChatClient deepseekChatClient;
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;

    // http://localhost:8005/prompt/chat?question=火锅介绍下
    @GetMapping("/prompt/chat")
    public Flux<String> chat(String question)
    {
        return deepseekChatClient.prompt()
                // AI 能力边界
                .system("你是一个法律助手，只回答法律问题，其它问题回复，我只能回答法律相关问题，其它无可奉告")
                .user(question)
                .stream()
                .content();
    }


    /**
     * http://localhost:8005/prompt/chat2?question=葫芦娃
     * @param question
     * @return
     */
    @GetMapping("/prompt/chat2")
    public Flux<ChatResponse> chat2(String question)
    {
        // 系统消息
        SystemMessage systemMessage = new SystemMessage("你是一个讲故事的助手,每个故事控制在300字以内");

        // 用户消息
        UserMessage userMessage = new UserMessage(question);

        Prompt prompt = new Prompt(userMessage, systemMessage);

        return deepseekChatModel.stream(prompt);

    }

    /**
     * http://localhost:8005/prompt/chat3?question=葫芦娃
     * @param question
     * @return
     */
    @GetMapping("/prompt/chat3")
    public Flux<String> chat3(String question)
    {
        // 系统消息
        SystemMessage systemMessage = new SystemMessage("你是一个讲故事的助手," +
                "每个故事控制在600字以内且以HTML格式返回");

        // 用户消息
        UserMessage userMessage = new UserMessage(question);

        Prompt prompt = new Prompt(userMessage, systemMessage);

        return deepseekChatModel.stream(prompt)
                .map(response -> response.getResults().get(0).getOutput().getText());

    }

    /**
     * http://localhost:8005/prompt/chat4?question=葫芦娃
     * @param question
     * @return
     */
    @GetMapping("/prompt/chat4")
    public String chat4(String question)
    {
        AssistantMessage assistantMessage = deepseekChatClient.prompt()
                    .user(question)
                    .call()
                    .chatResponse()
                    .getResult()
                    .getOutput();

        return assistantMessage.getText();

    }

    /**
     * http://localhost:8005/prompt/chat5?city=北京
     * 近似理解Tool后面章节讲解......
     * @param city
     * @return
     */
    @GetMapping("/prompt/chat5")
    public String chat5(String city)
    {

        String answer = deepseekChatClient.prompt()
                .user(city + "未来3天天气情况如何?")
                .call()
                .chatResponse()
                .getResult()
                .getOutput()
                .getText();

        ToolResponseMessage toolResponseMessage =
                new ToolResponseMessage(
                        List.of(new ToolResponseMessage.ToolResponse("1","获得天气",city)
                        )
                );

        String toolResponse = toolResponseMessage.getText();

        String result = answer + toolResponse;

        return result;
    }


}
```

![图片-097](images/图片-097.png)

###### 6.4.5.5.1.1 桥接外部服务，可以进行函数调用如，支付/数据查询等操作，类似调用第3方util工具类

##### 6.4.5.5.2 测试效果

![图片-098](images/图片-098.jpeg)

### 6.4.6 小总结

![图片-099](images/图片-099.jpeg)

# 7 提示词Prompt Template

![图片-100](images/图片-100.png)

## 7.1 Prompt演化历程

### 7.1.1 简单纯字符串提问问题

#### 7.1.1.1 最初的Prompt只是简单的文本字符串。

### 7.1.2 多角色消息

#### 7.1.2.1 将消息分为不同角色（如用户、助手、系统等），设置功能边界，增强交互的复杂性和上下文感知能力

#### 7.1.2.2 springai vs langchain4j vs spring ai alibaba

##### 7.1.2.2.1 langchain4j

![图片-101](images/图片-101.jpeg)

##### 7.1.2.2.2 springAI

![图片-102](images/图片-102.jpeg)

##### 7.1.2.2.3 springAI Alibaba

![图片-103](images/图片-103.jpeg)

### 7.1.3 占位符(Prompt Template)

#### 7.1.3.1 引入占位符(如{占位符变量名})以动态插入内容。

## 7.2 提示词模板是什么

![图片-104](images/图片-104.jpeg)

### 7.2.1 知识出处

#### 7.2.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/prompt/?spm=4347728f.4dc6f515.0.0.538b4305NobuzA#prompt-template

### 7.2.2 模板

#### 7.2.2.1 入职邀请函模板

主题：欢迎加入！给 [候选人姓名] 的入职邀请函

嗨 [候选人姓名]，

重磅好消息！经过团队的一致认可，我们真诚地邀请你加入我司，成为我们的 [职位名称]！

从面试中的沟通，我们深深感受到了你的专业能力和对工作的热情，相信你的加入一定会让我们的团队更加出色。

以下是你的入职详情，请查收：

职位： [职位名称]

团队： [部门/团队名称]

工作地点： [公司地址]

入职时间： [年]月[日](星期[几])，记得那天 [时间] 来找我们哦！

薪资待遇：

月薪：[金额] 元（税前）

试用期：[时长]，薪资为转正后的 [百分比]%

五险一金：齐全！公司会为你全额缴纳。

其他福利，如：零食饮料无限供应、年度旅游、弹性工作时间等

在第一天，你需要准备：

身份证、学历学位证、离职证明的原件和复印件

一张开心的笑脸！：）

为了能顺利迎接你，请在 [日期] 前回复这封邮件告诉我们“我愿意！”

如果你有任何疑问，别客气，随时找我聊（联系人：[HR姓名]，电话：[电话]）。

非常期待与你见面，一起做些酷的事情！

Best regards,

[你的名字/HR名字]

[公司名称] 团队

[日期]

#### 7.2.2.2 短信模板

#### 7.2.2.3 邮件模板

#### 7.2.2.4 ......

##### 7.2.2.4.1 PromptTemplate

## 7.3 开发步骤

### 7.3.1 新建子模块Module

#### 7.3.1.1 SAA-06PromptTemplate

### 7.3.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-06PromptTemplate</artifactId>


    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

### 7.3.3 写YML

```properties
server.port=8006

server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-06PromptTemplate


# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

### 7.3.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa06PromptTemplateApplication
{
    public static void main(String[] args)
    {
        SpringApplication.run(Saa06PromptTemplateApplication.class, args);
    }
}
```

### 7.3.5 业务类

#### 7.3.5.1 配置类LLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatModel;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatOptions;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.ChatOptions;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 18:53
 * @Description ChatModel+ChatClient+多模型共存
 */
@Configuration
public class SaaLLMConfig
{
    // 模型名称常量定义
    private final String DEEPSEEK_MODEL = "deepseek-v3";
    private final String QWEN_MODEL = "qwen-plus";

    @Bean(name = "deepseek")
    public ChatModel deepSeek()
    {
        return DashScopeChatModel.builder()
                        .dashScopeApi(DashScopeApi.builder()
                                    .apiKey(System.getenv("aliQwen-api"))
                                .build())
                .defaultOptions(
                        DashScopeChatOptions.builder().withModel(DEEPSEEK_MODEL).build()
                )
                .build();
    }

    @Bean(name = "qwen")
    public ChatModel qwen()
    {
        return DashScopeChatModel.builder().dashScopeApi(DashScopeApi.builder()
                        .apiKey(System.getenv("aliQwen-api"))
                        .build())
                .defaultOptions(
                        DashScopeChatOptions.builder()
                                .withModel(QWEN_MODEL)
                                .build()
                )
                .build();
    }

    @Bean(name = "deepseekChatClient")
    public ChatClient deepseekChatClient(@Qualifier("deepseek") ChatModel deepSeek)
    {
        return ChatClient.builder(deepSeek)
                .defaultOptions(ChatOptions.builder()
                        .model(DEEPSEEK_MODEL)
                        .build())
                .build();
    }


    @Bean(name = "qwenChatClient")
    public ChatClient qwenChatClient(@Qualifier("qwen") ChatModel qwen)
    {
        return ChatClient.builder(qwen)
                .defaultOptions(ChatOptions.builder()
                        .model(QWEN_MODEL)
                        .build())
                .build();
    }
}
```

#### 7.3.5.2 重点步骤

##### 7.3.5.2.1 PromptTemplate基本使用

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.chat.prompt.SystemPromptTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import org.springframework.beans.factory.annotation.Value;

import java.util.List;
import java.util.Map;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-26 16:25
 * @Description TODO
 */
@RestController
public class PromptTemplateController
{
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;

    @Resource(name = "deepseekChatClient")
    private ChatClient deepseekChatClient;
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;

    /**
     * @Description: PromptTemplate基本使用，使用占位符设置模版 PromptTemplate
     * @Auther: zzyybs@126.com
     * 测试地址
     * http://localhost:8006/prompttemplate/chat?topic=java&output_format=html&wordCount=200
     */
    @GetMapping("/prompttemplate/chat")
    public Flux<String> chat(String topic, String output_format, String wordCount)
    {
        PromptTemplate promptTemplate = new PromptTemplate("" +
                "讲一个关于{topic}的故事" +
                "并以{output_format}格式输出，" +
                "字数在{wordCount}左右");

        // PromptTempate -> Prompt
        Prompt prompt = promptTemplate.create(Map.of(
                "topic", topic,
                "output_format",output_format,
                "wordCount",wordCount));

        return deepseekChatClient.prompt(prompt).stream().content();
    }
}
```

##### 7.3.5.2.2 PromptTemplate读取模版文件实现模版功能

###### 7.3.5.2.2.1 /src/main/resources路径下新建

###### 7.3.5.2.2.1.1 prompttemplate/atguigu-template.txt

讲一个关于{topic}的故事，并以{output_format}格式输出。

![图片-105](images/图片-105.jpeg)

###### 7.3.5.2.2.2 代码

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.chat.prompt.SystemPromptTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import org.springframework.beans.factory.annotation.Value;

import java.util.List;
import java.util.Map;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-26 16:25
 * @Description TODO
 */
@RestController
public class PromptTemplateController
{
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;

    @Resource(name = "deepseekChatClient")
    private ChatClient deepseekChatClient;
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;


    @Value("classpath:/prompttemplate/atguigu-template.txt")
    private org.springframework.core.io.Resource userTemplate;

    /**
     * @Description: PromptTemplate基本使用，使用占位符设置模版 PromptTemplate
     * @Auther: zzyybs@126.com
     * 测试地址
     * http://localhost:8006/prompttemplate/chat?topic=java&output_format=html&wordCount=200
     */
    @GetMapping("/prompttemplate/chat")
    public Flux<String> chat(String topic, String output_format, String wordCount)
    {
        PromptTemplate promptTemplate = new PromptTemplate("" +
                "讲一个关于{topic}的故事" +
                "并以{output_format}格式输出，" +
                "字数在{wordCount}左右");

        // PromptTempate -> Prompt
        Prompt prompt = promptTemplate.create(Map.of(
                "topic", topic,
                "output_format",output_format,
                "wordCount",wordCount));

        return deepseekChatClient.prompt(prompt).stream().content();
    }

    /**
     * @Description: PromptTemplate读取模版文件实现模版功能
     * @Auther: zzyybs@126.com
     * 测试地址
     * http://localhost:8006/prompttemplate/chat2?topic=java&output_format=html
     */
    @GetMapping("/prompttemplate/chat2")
    public String chat2(String topic,String output_format)
    {
        PromptTemplate promptTemplate = new PromptTemplate(userTemplate);

        Prompt prompt = promptTemplate.create(Map.of("topic", topic, "output_format", output_format));

        return deepseekChatClient.prompt(prompt).call().content();
    }
}
```

##### 7.3.5.2.3 PromptTemplate多角色设定

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.chat.prompt.SystemPromptTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import org.springframework.beans.factory.annotation.Value;

import java.util.List;
import java.util.Map;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-26 16:25
 * @Description TODO
 */
@RestController
public class PromptTemplateController
{
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;

    @Resource(name = "deepseekChatClient")
    private ChatClient deepseekChatClient;
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;


    @Value("classpath:/prompttemplate/atguigu-template.txt")
    private org.springframework.core.io.Resource userTemplate;

    /**
     * @Description: PromptTemplate基本使用，使用占位符设置模版 PromptTemplate
     * @Auther: zzyybs@126.com
     * 测试地址
     * http://localhost:8006/prompttemplate/chat?topic=java&output_format=html&wordCount=200
     */
    @GetMapping("/prompttemplate/chat")
    public Flux<String> chat(String topic, String output_format, String wordCount)
    {
        PromptTemplate promptTemplate = new PromptTemplate("" +
                "讲一个关于{topic}的故事" +
                "并以{output_format}格式输出，" +
                "字数在{wordCount}左右");

        // PromptTempate -> Prompt
        Prompt prompt = promptTemplate.create(Map.of(
                "topic", topic,
                "output_format",output_format,
                "wordCount",wordCount));

        return deepseekChatClient.prompt(prompt).stream().content();
    }

    /**
     * @Description: PromptTemplate读取模版文件实现模版功能
     * @Auther: zzyybs@126.com
     * 测试地址
     * http://localhost:8006/prompttemplate/chat2?topic=java&output_format=html
     */
    @GetMapping("/prompttemplate/chat2")
    public String chat2(String topic,String output_format)
    {
        PromptTemplate promptTemplate = new PromptTemplate(userTemplate);

        Prompt prompt = promptTemplate.create(Map.of("topic", topic, "output_format", output_format));

        return deepseekChatClient.prompt(prompt).call().content();
    }


    /**
     *  @Auther: zzyybs@126.com
     * @Description:
     * 系统消息(SystemMessage)：设定AI的行为规则和功能边界(xxx助手/什么格式返回/字数控制多少)。
     * 用户消息(UserMessage)：用户的提问/主题
     * http://localhost:8006/prompttemplate/chat3?sysTopic=法律&userTopic=知识产权法
     *
     * http://localhost:8006/prompttemplate/chat3?sysTopic=法律&userTopic=夫妻肺片
     */
    @GetMapping("/prompttemplate/chat3")
    public String chat3(String sysTopic, String userTopic)
    {
        // 1.SystemPromptTemplate
        SystemPromptTemplate systemPromptTemplate = new SystemPromptTemplate("你是{systemTopic}助手，只回答{systemTopic}其它无可奉告，以HTML格式的结果。");
        Message sysMessage = systemPromptTemplate.createMessage(Map.of("systemTopic", sysTopic));
        // 2.PromptTemplate
        PromptTemplate userPromptTemplate = new PromptTemplate("解释一下{userTopic}");
        Message userMessage = userPromptTemplate.createMessage(Map.of("userTopic", userTopic));
        // 3.组合【关键】 多个 Message -> Prompt
        Prompt prompt = new Prompt(List.of(sysMessage, userMessage));
        // 4.调用 LLM
        return deepseekChatClient.prompt(prompt).call().content();
    }
}
```

###### 7.3.5.2.3.1 测试

![图片-106](images/图片-106.jpeg)

##### 7.3.5.2.4 PromptTemplate人物设定

###### 7.3.5.2.4.1 通过ChatModel实现

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.chat.prompt.SystemPromptTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import org.springframework.beans.factory.annotation.Value;

import java.util.List;
import java.util.Map;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-26 16:25
 * @Description TODO
 */
@RestController
public class PromptTemplateController
{
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;

    @Resource(name = "deepseekChatClient")
    private ChatClient deepseekChatClient;
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;


    @Value("classpath:/prompttemplate/atguigu-template.txt")
    private org.springframework.core.io.Resource userTemplate;

    /**
     * @Description: PromptTemplate基本使用，使用占位符设置模版 PromptTemplate
     * @Auther: zzyybs@126.com
     * 测试地址
     * http://localhost:8006/prompttemplate/chat?topic=java&output_format=html&wordCount=200
     */
    @GetMapping("/prompttemplate/chat")
    public Flux<String> chat(String topic, String output_format, String wordCount)
    {
        PromptTemplate promptTemplate = new PromptTemplate("" +
                "讲一个关于{topic}的故事" +
                "并以{output_format}格式输出，" +
                "字数在{wordCount}左右");

        // PromptTempate -> Prompt
        Prompt prompt = promptTemplate.create(Map.of(
                "topic", topic,
                "output_format",output_format,
                "wordCount",wordCount));

        return deepseekChatClient.prompt(prompt).stream().content();
    }

    /**
     * @Description: PromptTemplate读取模版文件实现模版功能
     * @Auther: zzyybs@126.com
     * 测试地址
     * http://localhost:8006/prompttemplate/chat2?topic=java&output_format=html
     */
    @GetMapping("/prompttemplate/chat2")
    public String chat2(String topic,String output_format)
    {
        PromptTemplate promptTemplate = new PromptTemplate(userTemplate);

        Prompt prompt = promptTemplate.create(Map.of("topic", topic, "output_format", output_format));

        return deepseekChatClient.prompt(prompt).call().content();
    }


    /**
     *  @Auther: zzyybs@126.com
     * @Description:
     * 系统消息(SystemMessage)：设定AI的行为规则和功能边界(xxx助手/什么格式返回/字数控制多少)。
     * 用户消息(UserMessage)：用户的提问/主题
     * http://localhost:8006/prompttemplate/chat3?sysTopic=法律&userTopic=知识产权法
     *
     * http://localhost:8006/prompttemplate/chat3?sysTopic=法律&userTopic=夫妻肺片
     */
    @GetMapping("/prompttemplate/chat3")
    public String chat3(String sysTopic, String userTopic)
    {
        // 1.SystemPromptTemplate
        SystemPromptTemplate systemPromptTemplate = new SystemPromptTemplate("你是{systemTopic}助手，只回答{systemTopic}其它无可奉告，以HTML格式的结果。");
        Message sysMessage = systemPromptTemplate.createMessage(Map.of("systemTopic", sysTopic));
        // 2.PromptTemplate
        PromptTemplate userPromptTemplate = new PromptTemplate("解释一下{userTopic}");
        Message userMessage = userPromptTemplate.createMessage(Map.of("userTopic", userTopic));
        // 3.组合【关键】 多个 Message -> Prompt
        Prompt prompt = new Prompt(List.of(sysMessage, userMessage));
        // 4.调用 LLM
        return deepseekChatClient.prompt(prompt).call().content();
    }


    /**
     * @Description: 人物角色设定，通过SystemMessage来实现人物设定，本案例用ChatModel实现
     * 设定AI为”医疗专家”时，仅回答医学相关问题
     * 设定AI为编程助手”时，专注于技术问题解答
     * @Auther: zzyybs@126.com
     * http://localhost:8006/prompttemplate/chat4?question=牡丹花
     */
    @GetMapping("/prompttemplate/chat4")
    public String chat4(String question)
    {
        //1 系统消息
        SystemMessage systemMessage = new SystemMessage("你是一个Java编程助手，拒绝回答非技术问题。");
        //2 用户消息
        UserMessage userMessage = new UserMessage(question);
        //3 系统消息+用户消息=完整提示词
        //Prompt prompt = new Prompt(systemMessage, userMessage);
        Prompt prompt = new Prompt(List.of(systemMessage, userMessage));
        //4 调用LLM
        String result = deepseekChatModel.call(prompt).getResult().getOutput().getText();
        System.out.println(result);
        return result;
    }

}
```

###### 7.3.5.2.4.2 通过ChatClient实现

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.chat.prompt.SystemPromptTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import org.springframework.beans.factory.annotation.Value;

import java.util.List;
import java.util.Map;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-26 16:25
 * @Description TODO
 */
@RestController
public class PromptTemplateController
{
    @Resource(name = "deepseek")
    private ChatModel deepseekChatModel;
    @Resource(name = "qwen")
    private ChatModel qwenChatModel;

    @Resource(name = "deepseekChatClient")
    private ChatClient deepseekChatClient;
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;


    @Value("classpath:/prompttemplate/atguigu-template.txt")
    private org.springframework.core.io.Resource userTemplate;

    /**
     * @Description: PromptTemplate基本使用，使用占位符设置模版 PromptTemplate
     * @Auther: zzyybs@126.com
     * 测试地址
     * http://localhost:8006/prompttemplate/chat?topic=java&output_format=html&wordCount=200
     */
    @GetMapping("/prompttemplate/chat")
    public Flux<String> chat(String topic, String output_format, String wordCount)
    {
        PromptTemplate promptTemplate = new PromptTemplate("" +
                "讲一个关于{topic}的故事" +
                "并以{output_format}格式输出，" +
                "字数在{wordCount}左右");

        // PromptTempate -> Prompt
        Prompt prompt = promptTemplate.create(Map.of(
                "topic", topic,
                "output_format",output_format,
                "wordCount",wordCount));

        return deepseekChatClient.prompt(prompt).stream().content();
    }

    /**
     * @Description: PromptTemplate读取模版文件实现模版功能
     * @Auther: zzyybs@126.com
     * 测试地址
     * http://localhost:8006/prompttemplate/chat2?topic=java&output_format=html
     */
    @GetMapping("/prompttemplate/chat2")
    public String chat2(String topic,String output_format)
    {
        PromptTemplate promptTemplate = new PromptTemplate(userTemplate);

        Prompt prompt = promptTemplate.create(Map.of("topic", topic, "output_format", output_format));

        return deepseekChatClient.prompt(prompt).call().content();
    }


    /**
     *  @Auther: zzyybs@126.com
     * @Description:
     * 系统消息(SystemMessage)：设定AI的行为规则和功能边界(xxx助手/什么格式返回/字数控制多少)。
     * 用户消息(UserMessage)：用户的提问/主题
     * http://localhost:8006/prompttemplate/chat3?sysTopic=法律&userTopic=知识产权法
     *
     * http://localhost:8006/prompttemplate/chat3?sysTopic=法律&userTopic=夫妻肺片
     */
    @GetMapping("/prompttemplate/chat3")
    public String chat3(String sysTopic, String userTopic)
    {
        // 1.SystemPromptTemplate
        SystemPromptTemplate systemPromptTemplate = new SystemPromptTemplate("你是{systemTopic}助手，只回答{systemTopic}其它无可奉告，以HTML格式的结果。");
        Message sysMessage = systemPromptTemplate.createMessage(Map.of("systemTopic", sysTopic));
        // 2.PromptTemplate
        PromptTemplate userPromptTemplate = new PromptTemplate("解释一下{userTopic}");
        Message userMessage = userPromptTemplate.createMessage(Map.of("userTopic", userTopic));
        // 3.组合【关键】 多个 Message -> Prompt
        Prompt prompt = new Prompt(List.of(sysMessage, userMessage));
        // 4.调用 LLM
        return deepseekChatClient.prompt(prompt).call().content();
    }


    /**
     * @Description: 人物角色设定，通过SystemMessage来实现人物设定，本案例用ChatModel实现
     * 设定AI为”医疗专家”时，仅回答医学相关问题
     * 设定AI为编程助手”时，专注于技术问题解答
     * @Auther: zzyybs@126.com
     * http://localhost:8006/prompttemplate/chat4?question=牡丹花
     */
    @GetMapping("/prompttemplate/chat4")
    public String chat4(String question)
    {
        //1 系统消息
        SystemMessage systemMessage = new SystemMessage("你是一个Java编程助手，拒绝回答非技术问题。");
        //2 用户消息
        UserMessage userMessage = new UserMessage(question);
        //3 系统消息+用户消息=完整提示词
        //Prompt prompt = new Prompt(systemMessage, userMessage);
        Prompt prompt = new Prompt(List.of(systemMessage, userMessage));
        //4 调用LLM
        String result = deepseekChatModel.call(prompt).getResult().getOutput().getText();
        System.out.println(result);
        return result;
    }

    /**
     * @Description: 人物角色设定，通过SystemMessage来实现人物设定，本案例用ChatClient实现
     * 设定AI为”医疗专家”时，仅回答医学相关问题
     * 设定AI为编程助手”时，专注于技术问题解答
     * @Auther: zzyybs@126.com
     * http://localhost:8006/prompttemplate/chat5?question=火锅
     */
    @GetMapping("/prompttemplate/chat5")
    public Flux<String> chat5(String question)
    {
        return deepseekChatClient.prompt()
                .system("你是一个Java编程助手，拒绝回答非技术问题。")
                .user(question)
                .stream()
                .content();
    }
}
```

# 8 格式化输出(Structured Output)

![图片-107](images/图片-107.png)

## 8.1 是什么

![图片-108](images/图片-108.jpeg)

### 8.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/structured-output/?spm=5176.29160081.0.0.2856aa5cPJ9Ha8

## 8.2 开发步骤

### 8.2.1 假设我们期望将模型输出转换为Record记录类结构体，不再是传统的String

### 8.2.2 新建子模块Module

#### 8.2.2.1 SAA-07StructuredOutput

### 8.2.3 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-07StructuredOutput</artifactId>


    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

### 8.2.4 写YML

```properties
server.port=8006

server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-06PromptTemplate


# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

### 8.2.5 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-26 17:16
 * @Description 知识出处，https://java2ai.com/docs/1.0.0.2/tutorials/basics/structured-output/?spm=5176.29160081.0.0.2856aa5cPJ9Ha8
 */
@SpringBootApplication
public class Saa07StructuredOutputApplication
{

    public static void main(String[] args)
    {
        SpringApplication.run(Saa07StructuredOutputApplication.class, args);
    }

}
```

### 8.2.6 业务类

#### 8.2.6.1 配置类LLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatModel;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatOptions;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.ChatOptions;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 18:53
 * @Description ChatModel+ChatClient+多模型共存
 */
@Configuration
public class SaaLLMConfig
{
    // 模型名称常量定义
    private final String DEEPSEEK_MODEL = "deepseek-v3";
    private final String QWEN_MODEL = "qwen-plus";

    @Bean(name = "deepseek")
    public ChatModel deepSeek()
    {
        return DashScopeChatModel.builder()
                        .dashScopeApi(DashScopeApi.builder()
                                    .apiKey(System.getenv("aliQwen-api"))
                                .build())
                .defaultOptions(
                        DashScopeChatOptions.builder().withModel(DEEPSEEK_MODEL).build()
                )
                .build();
    }

    @Bean(name = "qwen")
    public ChatModel qwen()
    {
        return DashScopeChatModel.builder().dashScopeApi(DashScopeApi.builder()
                        .apiKey(System.getenv("aliQwen-api"))
                        .build())
                .defaultOptions(
                        DashScopeChatOptions.builder()
                                .withModel(QWEN_MODEL)
                                .build()
                )
                .build();
    }

    @Bean(name = "deepseekChatClient")
    public ChatClient deepseekChatClient(@Qualifier("deepseek") ChatModel deepSeek)
    {
        return ChatClient.builder(deepSeek)
                .defaultOptions(ChatOptions.builder()
                        .model(DEEPSEEK_MODEL)
                        .build())
                .build();
    }


    @Bean(name = "qwenChatClient")
    public ChatClient qwenChatClient(@Qualifier("qwen") ChatModel qwen)
    {
        return ChatClient.builder(qwen)
                .defaultOptions(ChatOptions.builder()
                        .model(QWEN_MODEL)
                        .build())
                .build();
    }
}
```

#### 8.2.6.2 重点步骤

##### 8.2.6.2.1 新建记录类StudentRecord

```java
package com.atguigu.study.records;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-26 17:18
 * @Description jdk14后的新特性，记录类替代lombok
 */
public record StudentRecord(String id,String sname,String major,String email) { }
```

###### 8.2.6.2.1.1 record-记录类学习资料

https://www.bilibili.com/video/BV1PY411e7J6?spm_id_from=333.788.videopod.episodes&vd_source=f3f60f7acbef49d38b97c4d660d439fc&p=199

22分钟后开始观看

![图片-109](images/图片-109.jpeg)

##### 8.2.6.2.2 controllerV1

```java
package com.atguigu.study.controller;

import com.atguigu.study.records.StudentRecord;
import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.function.Consumer;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-26 17:16
 * @Description TODO
 */
@RestController
public class StructuredOutputController
{
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;

    /**
     * http://localhost:8007/structuredoutput/chat?sname=李四&email=zzyybs@126.com
     * @param sname
     * @return
     */
    @GetMapping("/structuredoutput/chat")
    public StudentRecord chat(String sname,String email)
    {
        return qwenChatClient.prompt()
                .user(new Consumer<ChatClient.PromptUserSpec>() {
            @Override
            public void accept(ChatClient.PromptUserSpec promptUserSpec)
            {
                promptUserSpec.text("学号1001,我叫{sname},大学专业是计算机科学与技术,邮箱{email}")
                        .param("sname",sname)
                        .param("email",email);
            }
        }).call().entity(StudentRecord.class);
    }
}
```

##### 8.2.6.2.3 controllerV2

```java
package com.atguigu.study.controller;

import com.atguigu.study.records.StudentRecord;
import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.function.Consumer;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-26 17:16
 * @Description TODO
 */
@RestController
public class StructuredOutputController
{
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;

    /**
     * http://localhost:8007/structuredoutput/chat?sname=李四&email=zzyybs@126.com
     * @param sname
     * @return
     */
    @GetMapping("/structuredoutput/chat")
    public StudentRecord chat(String sname,String email)
    {
        return qwenChatClient.prompt()
                .user(new Consumer<ChatClient.PromptUserSpec>() {
            @Override
            public void accept(ChatClient.PromptUserSpec promptUserSpec)
            {
                promptUserSpec.text("学号1001,我叫{sname},大学专业是计算机科学与技术,邮箱{email}")
                        .param("sname",sname)
                        .param("email",email);
            }
        }).call().entity(StudentRecord.class);
    }


    /**
     * http://localhost:8007/structuredoutput/chat2?sname=孙伟&email=zzyybs@126.com
     * @param sname
     * @return
     */
    @GetMapping("/structuredoutput/chat2")
    public StudentRecord chat2(@RequestParam(name = "sname") String sname,
                               @RequestParam(name = "email") String email)
    {
        String stringTemplate = """
                学号1002,我叫{sname},大学专业是软件工程,邮箱{email}
                """;

        return qwenChatClient.prompt()
                .user(promptUserSpec -> promptUserSpec.text(stringTemplate)
                        .param("sname",sname)
                        .param("email",email))
                .call()
                .entity(StudentRecord.class);
    }
}
```

# 9 Chat Memory连续对话保存和持久化

![图片-110](images/图片-110.png)

## 9.1 是什么

### 9.1.1 官网知识出处

![图片-111](images/图片-111.jpeg)

#### 9.1.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/memory/?spm=4347728f.4dc6f515.0.0.538b4305NobuzA

### 9.1.2 记忆对话，积累回答

![图片-112](images/图片-112.jpeg)

#### 9.1.2.1 1

![图片-113](images/图片-113.jpeg)

#### 9.1.2.2 2

![图片-114](images/图片-114.jpeg)

### 9.1.3 一句话

#### 9.1.3.1 Spring AI Alibaba中的聊天记忆提供了维护 AI 聊天应用程序的对话上下文和历史的机制。

### 9.1.4 记忆类型

![图片-115](images/图片-115.jpeg)

#### 9.1.4.1 因大模型本身不存储数据，需将历史对话信息一次性提供给它以实现连续对话，不然服务一重启就什么都没了......所以，必须持久化

#### 9.1.4.2 痛点2个

##### 9.1.4.2.1 持久化媒介

##### 9.1.4.2.2 消息对话窗口，聊天记录上限

## 9.2 持久化开发步骤

### 9.2.1 需求说明

#### 9.2.1.1 将客户和大模型的对话问答保存进Redis进行持久化记忆留存

#### 9.2.1.2 请再看看官网

https://java2ai.com/docs/1.0.0.2/tutorials/basics/memory/?spm=4347728f.4dc6f515.0.0.538b4305NobuzA

![图片-116](images/图片-116.jpeg)

#### 9.2.1.3 自己动手，丰衣足食

![图片-117](images/图片-117.png)

### 9.2.2 新建子模块Module

#### 9.2.2.1 SAA-08Persistent

### 9.2.3 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-08Persistent</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--spring-ai-alibaba memory-redis-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-memory-redis</artifactId>
        </dependency>
        <!--jedis-->
        <dependency>
            <groupId>redis.clients</groupId>
            <artifactId>jedis</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

#### 9.2.3.1 RedisChatMemoryRepository源码

![图片-118](images/图片-118.jpeg)

### 9.2.4 写YML

```properties
server.port=8008

# 设置响应的字符编码
server.servlet.encoding.charset=utf-8
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true

spring.application.name=SAA-08Persistent

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}


# ==========redis config ===============
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.database=0
spring.data.redis.connect-timeout=3
spring.data.redis.timeout=2
```

### 9.2.5 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-28 17:59
 * @Description
 * 1  将客户和大模型的对话问答保存进Redis进行持久化记忆留存
 */
@SpringBootApplication
public class Saa08PersistentApplication
{
    public static void main(String[] args)
    {
        SpringApplication.run(Saa08PersistentApplication.class,args);
    }
}
```

### 9.2.6 业务类

#### 9.2.6.1 前置知识

##### 9.2.6.1.1 ChatMemoryRepository接口

###### 9.2.6.1.1.1 实现SpringAI框架规定的ChatMemoryRepository接口

翻译见最下面 翻译见最下面

![图片-119](images/图片-119.jpeg)

![图片-120](images/图片-120.jpeg)

###### 9.2.6.1.1.2 接口ChatMemoryRepository

![图片-121](images/图片-121.jpeg)

###### 9.2.6.1.1.3 RedisChatMemoryRepository源码

![图片-122](images/图片-122.jpeg)

###### 9.2.6.1.1.4 编码新建RedisMemoryConfig配置类

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.memory.redis.RedisChatMemoryRepository;
import org.springframework.ai.chat.memory.ChatMemory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-28 18:24
 * @Description TODO
 */
@Configuration
public class RedisMemoryConfig
{
    @Value("${spring.data.redis.host}")
    private String host;
    @Value("${spring.data.redis.port}")
    private int port;

    @Bean
    public RedisChatMemoryRepository redisChatMemoryRepository()
    {
        return RedisChatMemoryRepository.builder()
                    .host(host)
                    .port(port)
                .build();
    }
}
```

##### 9.2.6.1.2 MessageWindowChatMemory 消息窗口聊天记忆

###### 9.2.6.1.2.1 https://docs.spring.io/spring-ai/reference/api/chat-memory.html#_message_window_chat_memory

###### 9.2.6.1.2.2 编码配置

![图片-123](images/图片-123.jpeg)

##### 9.2.6.1.3 顾问（Advisors） MessageChatMemoryAdvisor

###### 9.2.6.1.3.1 1

![图片-124](images/图片-124.jpeg)

###### 9.2.6.1.3.2 2

![图片-125](images/图片-125.jpeg)

###### 9.2.6.1.3.3 3

![图片-126](images/图片-126.jpeg)

#### 9.2.6.2 配置类SaaLLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatModel;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatOptions;
import com.alibaba.cloud.ai.memory.redis.RedisChatMemoryRepository;
import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.client.advisor.MessageChatMemoryAdvisor;
import org.springframework.ai.chat.memory.MessageWindowChatMemory;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.ChatOptions;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 18:53
 * @Description ChatModel+ChatClient+多模型共存
 */
@Configuration
public class SaaLLMConfig
{
    // 模型名称常量定义
    private final String DEEPSEEK_MODEL = "deepseek-v3";
    private final String QWEN_MODEL = "qwen-plus";

    @Bean(name = "deepseek")
    public ChatModel deepSeek()
    {
        return DashScopeChatModel.builder()
                        .dashScopeApi(DashScopeApi.builder()
                                    .apiKey(System.getenv("aliQwen-api"))
                                .build())
                .defaultOptions(
                        DashScopeChatOptions.builder().withModel(DEEPSEEK_MODEL).build()
                )
                .build();
    }

    @Bean(name = "qwen")
    public ChatModel qwen()
    {
        return DashScopeChatModel.builder().dashScopeApi(DashScopeApi.builder()
                        .apiKey(System.getenv("aliQwen-api"))
                        .build())
                .defaultOptions(
                        DashScopeChatOptions.builder()
                                .withModel(QWEN_MODEL)
                                .build()
                )
                .build();
    }

    @Bean(name = "qwenChatClient")
    public ChatClient qwenChatClient(@Qualifier("qwen") ChatModel qwen,
                                     RedisChatMemoryRepository redisChatMemoryRepository)
    {

        MessageWindowChatMemory windowChatMemory = MessageWindowChatMemory.builder()
                            .chatMemoryRepository(redisChatMemoryRepository)
                            .maxMessages(10)
                        .build();

        return ChatClient.builder(qwen)
                .defaultOptions(ChatOptions.builder().model(QWEN_MODEL).build())
                .defaultAdvisors(MessageChatMemoryAdvisor.builder(windowChatMemory).build())
                .build();
    }


    /**
     * 家庭作业，按照上述模范qwen完成基于deepseek的模型存储
     * @param deepSeek
     * @return
     */
    @Bean(name = "deepseekChatClient")
    public ChatClient deepseekChatClient(@Qualifier("deepseek") ChatModel deepSeek)
    {
        return ChatClient.builder(deepSeek)
                .defaultOptions(ChatOptions.builder()
                        .model(DEEPSEEK_MODEL)
                        .build())
                .build();
    }
}
```

##### 9.2.6.2.1 before

![图片-127](images/图片-127.jpeg)

对比

![图片-128](images/图片-128.jpeg)

##### 9.2.6.2.2 after

![图片-129](images/图片-129.jpeg)

#### 9.2.6.3 controller

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.web.bind.annotation.GetMapping;
import static org.springframework.ai.chat.memory.ChatMemory.CONVERSATION_ID;
import org.springframework.web.bind.annotation.RestController;

import java.util.function.Consumer;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-28 18:40
 * @Description TODO
 */
@RestController
public class ChatMemory4RedisController
{
    @Resource(name = "qwenChatClient")
    private ChatClient qwenChatClient;

    @GetMapping("/chatmemory/chat")
    public String chat(String msg, String userId)
    {
        /*return qwenChatClient.prompt(msg).advisors(new Consumer<ChatClient.AdvisorSpec>()
        {
            @Override
            public void accept(ChatClient.AdvisorSpec advisorSpec)
            {
                advisorSpec.param(CONVERSATION_ID, cid);
            }
        }).call().content();*/

        return qwenChatClient.prompt(msg)
                .advisors(advisorSpec -> advisorSpec.param(CONVERSATION_ID, userId))
                .call()
                .content();
    }
}
```

### 9.2.7 测试

![图片-130](images/图片-130.jpeg)

#### 9.2.7.1 http://localhost:8008/chatmemory/chat?msg=2加5等于多少&userId=7

# 10 文生图

![图片-131](images/图片-131.png)

## 10.1 阿里百炼文生图

### 10.1.1 文本生成图像

![图片-132](images/图片-132.jpeg)

#### 10.1.1.1 https://help.aliyun.com/zh/model-studio/text-to-image?spm=a2c4g.11186623.help-menu-2400256.d_0_5_0.1a457d9dv6o7Kc&accounttraceid=6ec3bf09599f424a91a2a88b27b31570nrdd

## 10.2 开发步骤

### 10.2.1 通义万相-文生图V2版API参考

#### 10.2.1.1 https://help.aliyun.com/zh/model-studio/text-to-image-v2-api-reference?spm=a2c4g.11186623.0.0.79c74680qv54KQ

### 10.2.2 新建子模块Module

#### 10.2.2.1 SAA-09Text2image

### 10.2.3 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-09Text2image</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

### 10.2.4 写YML

```properties
server.port=8009

# 设置响应的字符编码
server.servlet.encoding.charset=utf-8
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true

spring.application.name=SAA-09Text2image

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

### 10.2.5 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa09Text2imageApplication
{
    public static void main(String[] args)
    {
        SpringApplication.run(Saa09Text2imageApplication.class, args);
    }
}
```

### 10.2.6 业务类

#### 10.2.6.1 controller

```java
package com.atguigu.study.controller;

import com.alibaba.cloud.ai.dashscope.audio.DashScopeSpeechSynthesisModel;
import com.alibaba.cloud.ai.dashscope.audio.DashScopeSpeechSynthesisOptions;
import com.alibaba.cloud.ai.dashscope.audio.synthesis.SpeechSynthesisModel;
import com.alibaba.cloud.ai.dashscope.audio.synthesis.SpeechSynthesisOptions;
import com.alibaba.cloud.ai.dashscope.audio.synthesis.SpeechSynthesisPrompt;
import com.alibaba.cloud.ai.dashscope.audio.synthesis.SpeechSynthesisResponse;
import com.alibaba.cloud.ai.dashscope.image.DashScopeImageOptions;
import jakarta.annotation.Resource;
import org.springframework.ai.image.ImageModel;
import org.springframework.ai.image.ImagePrompt;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.File;
import java.io.FileOutputStream;
import java.nio.ByteBuffer;
import java.util.UUID;


/**
 * @auther zzyybs@126.com
 * @create 2025-07-28 20:10
 * @Description 知识出处
 * https://help.aliyun.com/zh/model-studio/text-to-image?spm=a2c4g.11186623.help-menu-2400256.d_0_5_0.1a457d9dv6o7Kc&accounttraceid=6ec3bf09599f424a91a2a88b27b31570nrdd
 */
@RestController
public class Text2ImageController
{
    // img model
    public static final String IMAGE_MODEL = "wanx2.1-t2i-turbo";

    @Resource
    private ImageModel imageModel;

    @GetMapping(value = "/t2i/image")
    public String image(@RequestParam(name = "prompt",defaultValue = "刺猬") String prompt)
    {
        return imageModel.call(
                    new ImagePrompt(prompt, DashScopeImageOptions.builder().withModel(IMAGE_MODEL).build())
                )
                .getResult()
                .getOutput()
                .getUrl();
    }
}
```

# 11 文生音

![图片-133](images/图片-133.png)

## 11.1 阿里百炼文生音

### 11.1.1 语音合成-CosyVoice

#### 11.1.1.1 https://help.aliyun.com/zh/model-studio/cosyvoice-large-model-for-speech-synthesis/?spm=a2c4g.11186623.help-menu-2400256.d_2_6_0.2a7474473XyDNE&scm=20140722.H_2817551._.OR_help-T_cn~zh-V_1

### 11.1.2 语音合成CosyVoice Java SDK

#### 11.1.2.1 https://help.aliyun.com/zh/model-studio/cosyvoice-java-sdk?spm=a2c4g.11186623.0.0.77e07447jgP4N0

### 11.1.3 SpeechSynthesizer类提供了语音合成的关键接口

#### 11.1.3.1 同步调用

同步提交语音合成任务，直接获取完整结果

![图片-134](images/图片-134.jpeg)

##### 11.1.3.1.1 提交文本后，服务端立即处理并返回完整的语音合成结果。整个过程是阻塞式的，客户端需要等待服务端完成处理后才能继续下一步操作。适合短文本语音合成场景

### 11.1.4 阿里内置接口一览

![图片-135](images/图片-135.jpeg)

### 11.1.5 DashScopeSpeechSynthesisOptions

#### 11.1.5.1 SpeechSynthesisParam的链式方法配置模型、音色等参数

![图片-136](images/图片-136.jpeg)

##### 11.1.5.1.1 https://help.aliyun.com/zh/model-studio/cosyvoice-java-sdk#2e9a9a89aclc8

#### 11.1.5.2 代码

![图片-137](images/图片-137.jpeg)

## 11.2 开发步骤

### 11.2.1 新建子模块Module

#### 11.2.1.1 SAA-10Text2voice

### 11.2.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-10Text2voice</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

### 11.2.3 写YML

```properties
server.port=8010

# 设置响应的字符编码
server.servlet.encoding.charset=utf-8
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true

spring.application.name=SAA-10Text2voice

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

### 11.2.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa10Text2voiceApplication
{

    public static void main(String[] args)
    {
        SpringApplication.run(Saa10Text2voiceApplication.class, args);
    }

}
```

### 11.2.5 业务类

#### 11.2.5.1 音色列表配置

![图片-138](images/图片-138.jpeg)

##### 11.2.5.1.1 https://help.aliyun.com/zh/model-studio/cosyvoice-java-sdk#722dd7ca66a6x

#### 11.2.5.2 controller

```java
package com.atguigu.study.controller;

import com.alibaba.cloud.ai.dashscope.audio.DashScopeSpeechSynthesisOptions;
import com.alibaba.cloud.ai.dashscope.audio.synthesis.SpeechSynthesisModel;
import com.alibaba.cloud.ai.dashscope.audio.synthesis.SpeechSynthesisPrompt;
import com.alibaba.cloud.ai.dashscope.audio.synthesis.SpeechSynthesisResponse;
import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.FileOutputStream;
import java.nio.ByteBuffer;
import java.util.UUID;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-29 18:35
 * @Description TODO
 */
@RestController
public class Text2VoiceController
{
    @Resource
    private SpeechSynthesisModel speechSynthesisModel;

    // voice model
    public static final String BAILIAN_VOICE_MODEL = "cosyvoice-v2";
    // voice timber 音色列表：https://help.aliyun.com/zh/model-studio/cosyvoice-java-sdk#722dd7ca66a6x
    public static final String BAILIAN_VOICE_TIMBER = "longyingcui";//龙应催


    /**
     * http://localhost:8010/t2v/voice
     * @param msg
     * @return
     */
    @GetMapping("/t2v/voice")
    public String voice(@RequestParam(name = "msg",defaultValue = "温馨提醒，支付宝到账100元请注意查收") String msg)
    {
        String filePath = "d:\\" + UUID.randomUUID() + ".mp3";

        //1 语音参数设置
        DashScopeSpeechSynthesisOptions options = DashScopeSpeechSynthesisOptions.builder()
                .model(BAILIAN_VOICE_MODEL)
                .voice(BAILIAN_VOICE_TIMBER)
                .build();

        //2 调用大模型语音生成对象
        SpeechSynthesisResponse response = speechSynthesisModel.call(new SpeechSynthesisPrompt(msg, options));

        //3 字节流语音转换
        ByteBuffer byteBuffer = response.getResult().getOutput().getAudio();

        //4 文件生成
        try (FileOutputStream fileOutputStream = new FileOutputStream(filePath))
        {
            fileOutputStream.write(byteBuffer.array());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        //5 生成路径OK
        return filePath;
    }
}
```

# 12 向量化和向量数据库

![图片-139](images/图片-139.png)

## 12.1 向量

### 12.1.1 是什么

![图片-140](images/图片-140.jpeg)

## 12.2 文本向量化

### 12.2.1 是什么

![图片-141](images/图片-141.jpeg)

#### 12.2.1.1 官网-嵌入模型 (Embedding Model)

##### 12.2.1.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/embedding/?spm=5176.29160081.0.0.2856aa5cXggpMJ

##### 12.2.1.1.2 说人话

![图片-142](images/图片-142.jpeg)

#### 12.2.1.2 案例1

##### 12.2.1.2.1 维度

![图片-143](images/图片-143.jpeg)

##### 12.2.1.2.2 如何确定相似

![图片-144](images/图片-144.jpeg)

#### 12.2.1.3 案例2

##### 12.2.1.3.1 对比图片

![图片-145](images/图片-145.jpeg)

##### 12.2.1.3.2 维度

![图片-146](images/图片-146.jpeg)

### 12.2.2 小总结

![图片-147](images/图片-147.jpeg)

![图片-148](images/图片-148.jpeg)

## 12.3 向量数据库

### 12.3.1 是什么

#### 12.3.1.1 官网-向量存储(Vector Store)

##### 12.3.1.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/vectorstore/?spm=5176.29160081.0.0.2856aa5cXggpMJ

##### 12.3.1.1.2 说人话

![图片-149](images/图片-149.jpeg)

#### 12.3.1.2 一种专门用于存储、管理和检索向量数据（即高维数值数组）的数据库系统。

#### 12.3.1.3 其核心功能是通过高效的索引结构和相似性计算算法，支持大规模向量数据的快速查询与分析，向量数据库维度越高，查询精准度也越高，查询效果也越好。

### 12.3.2 下方是LangChain4J支持的向量数据库List清单

#### 12.3.2.1 https://docs.langchain4j.dev/integrations/embedding-stores/

### 12.3.3 下方是SpringAI支持的向量数据库List清单

#### 12.3.3.1 https://docs.spring.io/spring-ai/reference/api/vectordbs.html

## 12.4 能干嘛

### 12.4.1 将文本、图像和视频转换为称为向量（Vectors）的浮点数数组在 VectorStore中，查询与传统关系数据库不同。它们执行相似性搜索，而不是精确匹配。当给定一个向量作为查询时，VectorStore 返回与查询向量“相似”的向量

![图片-150](images/图片-150.jpeg)

### 12.4.2 指征特点

#### 12.4.2.1 捕捉复杂的词汇关系（如语义相似性、同义词、多义词）

#### 12.4.2.2 向量嵌入为检索增强生成 (RAG) 应用程序提供支持

### 12.4.3 小总结

#### 12.4.3.1 将文本映射到高维空间中的点，使语义相似的文本在这个空间中距离较近。

#### 12.4.3.2 例如，“肯德基”和”麦当劳”的向量可能会比”肯德基”和”新疆大盘鸡”的向量更接近

## 12.5 开发步骤

### 12.5.1 建Module

#### 12.5.1.1 SAA-11Embed2vector

### 12.5.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-11Embed2vector</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!-- 添加 Redis 向量数据库依赖 -->
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-vector-store-redis</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

### 12.5.3 写YML

```properties
server.port=8011

# 设置响应的字符编码
server.servlet.encoding.charset=utf-8
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true

spring.application.name=SAA-11Embed2vector

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
spring.ai.dashscope.chat.options.model=qwen-plus
spring.ai.dashscope.embedding.options.model=text-embedding-v3


# =======Redis Stack==========
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.username=default
spring.data.redis.password=
spring.ai.vectorstore.redis.initialize-schema=true
spring.ai.vectorstore.redis.index-name=custom-index
spring.ai.vectorstore.redis.prefix=custom-prefix
```

#### 12.5.3.1 阿里云百炼平台向量大模型

![图片-151](images/图片-151.jpeg)

##### 12.5.3.1.1 text-embedding-v3

##### 12.5.3.1.2 https://bailian.console.aliyun.com/?tab=api#/api/?type=model&url=https%3A%2F%2Fhelp.aliyun.com%2Fdocument_detail%2F2712515.html

#### 12.5.3.2 配置参考信息来源和知识出处

![图片-152](images/图片-152.gif)

##### 12.5.3.2.1 https://docs.spring.io/spring-ai/reference/api/vectordbs/redis.html

### 12.5.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa11Embed2vectorApplication
{

    public static void main(String[] args)
    {
        SpringApplication.run(Saa11Embed2vectorApplication.class, args);
    }
}
```

### 12.5.5 用redisStack作为向量存储

#### 12.5.5.1 https://docs.spring.io/spring-ai/reference/api/vectordbs/redis.html

#### 12.5.5.2 RedisStack是什么

![图片-153](images/图片-153.jpeg)

![图片-154](images/图片-154.png)

#### 12.5.5.3 RedisStack相比原生 Redis 的优势

![图片-155](images/图片-155.jpeg)

#### 12.5.5.4 RedisStack核心组件

##### 12.5.5.4.1 RediSearch：

###### 12.5.5.4.1.1 提供全文搜索能力，支持复杂的文本搜索、聚合和过滤，以及向量数据的存储和检索

##### 12.5.5.4.2 RedisJSON：

###### 12.5.5.4.2.1 原生支持JSON数据的存储、索引I和查询，可高效存储和操作嵌套的JSON文档。

##### 12.5.5.4.3 RedisGraph：

###### 12.5.5.4.3.1 支持图数据模型，使用Cypher查询语言进行图遍历查询。

##### 12.5.5.4.4 RedisBloom:

###### 12.5.5.4.4.1 支持 Bloom、Cuckoo、Count-Min Sketch等概率数据结构。

#### 12.5.5.5 一句话(重要)

##### 12.5.5.5.1 RedisStack = 原生Redis + 搜索 + 图 + 时间序列 + JSON + 概率结构 + 可视化工具 + 开发框架支持

#### 12.5.5.6 RedisStack安装

##### 12.5.5.6.1 docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server

#### 12.5.5.7 基础api（编码入库OK后，再后面讲解操作）

![图片-156](images/图片-156.jpeg)

### 12.5.6 业务类

#### 12.5.6.1 知识出处

##### 12.5.6.1.1 https://docs.spring.io/spring-ai/reference/api/vectordbs.html

#### 12.5.6.2 controller

```java
package com.atguigu.study.controller;

import com.alibaba.cloud.ai.dashscope.embedding.DashScopeEmbeddingOptions;
import jakarta.annotation.Resource;
import lombok.extern.slf4j.Slf4j;
import org.springframework.ai.document.Document;
import org.springframework.ai.embedding.EmbeddingModel;
import org.springframework.ai.embedding.EmbeddingRequest;
import org.springframework.ai.embedding.EmbeddingResponse;
import org.springframework.ai.vectorstore.SearchRequest;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-29 19:54
 * @Description TODO
 */
@RestController
@Slf4j
public class Embed2VectorController
{
    @Resource
    private EmbeddingModel embeddingModel;

    @Resource
    private VectorStore vectorStore;

    /**
     * 文本向量化
     * http://localhost:8011/text2embed?msg=射雕英雄传
     *
     * @param msg
     * @return
     */
    @GetMapping("/text2embed")
    public EmbeddingResponse text2Embed(String msg)
    {
        //EmbeddingResponse embeddingResponse = embeddingModel.call(new EmbeddingRequest(List.of(msg), null));

        EmbeddingResponse embeddingResponse = embeddingModel.call(new EmbeddingRequest(List.of(msg),
                DashScopeEmbeddingOptions.builder().withModel("text-embedding-v3").build()));

        System.out.println(Arrays.toString(embeddingResponse.getResult().getOutput()));

        return embeddingResponse;
    }

    @GetMapping("/embed2vector/add")
    public void add()
    {
        List<Document> documents = List.of(
                new Document("i study LLM"),
                new Document("i love java")
        );

        vectorStore.add(documents);
    }

    @GetMapping("/embed2vector/get")
    public List getAll(@RequestParam(name = "msg") String msg)
    {
        SearchRequest searchRequest = SearchRequest.builder()
                .query(msg)
                .topK(2)
                .build();

        List<Document> list = vectorStore.similaritySearch(searchRequest);

        System.out.println(list);

        return list;
    }
}
```

##### 12.5.6.2.1 文本向量化

##### 12.5.6.2.2 向量化存储

##### 12.5.6.2.3 向量化查询

#### 12.5.6.3 测试

##### 12.5.6.3.1 http://localhost:8011/text2embed?msg=射雕英雄传

##### 12.5.6.3.2 http://localhost:8011/embed2vector/get?msg=LLM

#### 12.5.6.4 基础api（编码入库后讲解操作）

![图片-157](images/图片-157.jpeg)

##### 12.5.6.4.1 验证结果

![图片-158](images/图片-158.jpeg)

## 12.6 知识谱图

![图片-159](images/图片-159.jpeg)

# 13 RAG（Retrieval Augmented Generation）

![图片-160](images/图片-160.png)

## 13.1 RAG (Retrieval-Augmented Generation) 检索增强生成

## 13.2 需求

### 13.2.1 AI智能运维助手，通过提供的错误编码，给出异常解释辅助运维人员更好的定位问题和维护系统

### 13.2.2 SpringAI+阿里百炼嵌入模型text-embedding-v3+向量数据库RedisStack+DeepSeek来实现RAG功能。

## 13.3 LLM的缺陷

### 13.3.1 LLM的知识不是实时的，不具备知识更新.

### 13.3.2 LLM可能不知道你私有的领域/业务知识.

### 13.3.3 LLM有时会在回答中生成看似合理但实际上是错误的信息

## 13.4 是什么

### 13.4.1 官网

#### 13.4.1.1 RAG (Retrieval-Augmented Generation)

##### 13.4.1.1.1 RAG

![图片-161](images/图片-161.jpeg)

LLM 的知识仅限于它所接受的训练数据。如果你想让一个 LLM 了解特定领域的知识或专有数据，你可以

##### 13.4.1.1.2 What is RAG

![图片-162](images/图片-162.jpeg)

![图片-163](images/图片-163.jpeg)

幻觉？？？

###### 13.4.1.1.2.1 幻觉

###### 13.4.1.1.2.1.1 已读乱回

###### 13.4.1.1.2.1.2 已读不回

###### 13.4.1.1.2.1.3 似是而非

#### 13.4.1.2 springai

##### 13.4.1.2.1 https://docs.spring.io/spring-ai/reference/api/retrieval-augmented-generation.html

#### 13.4.1.3 springai alibaba

##### 13.4.1.3.1 文档检索 (Document Retriever)

###### 13.4.1.3.1.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/retriever/?spm=5176.29160081.0.0.2856aa5cXggpMJ

### 13.4.2 核心设计理念

#### 13.4.2.1 RAG技术就像给AI大模型装上了「实时百科大脑」，为了让大模型获取足够的上下文，以便获得更加广泛的信息源，通过先查资料后回答的机制，让AI摆脱传统模型的”知识遗忘和幻觉回复”困境

### 13.4.3 一句话

#### 13.4.3.1 类似考试时有不懂的，给你准备了小抄，对大模型知识盲区的一种补充

## 13.5 能干嘛

### 13.5.1 通过引入外部知识源来增强LLM的输出能力，传统的LLM通常基于其训练数据生成响应，但这些数据可能过时或不够全面。RAG允许模型在生成答案之前，从特定的知识库中检索相关信息，从而提供更准确和上下文相关的回答

## 13.6 怎么玩

![图片-164](images/图片-164.png)

### 13.6.1 RAG 流程分为两个不同的阶段：索引和检索

#### 13.6.1.1 Index

![图片-165](images/图片-165.jpeg)

![图片-166](images/图片-166.jpeg)

#### 13.6.1.2 Retrieval

![图片-167](images/图片-167.jpeg)

![图片-168](images/图片-168.jpeg)

## 13.7 开发步骤

### 13.7.1 需求

#### 13.7.1.1 AI智能运维助手，通过提供的错误编码，给出异常解释辅助运维人员更好的定位问题和维护系统

#### 13.7.1.2 SpringAI+阿里百炼嵌入模型text-embedding-v3+向量数据库RedisStack+DeepSeek来实现RAG功能。

### 13.7.2 建Module

#### 13.7.2.1 SAA-12RAG4AiOps

### 13.7.3 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-12RAG4AiOps</artifactId>


    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!-- 添加 Redis 向量数据库依赖 -->
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-vector-store-redis</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

### 13.7.4 写YML

```properties
server.port=8012

# 设置全局编码格式
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-12RAG4AiDatabase

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
spring.ai.dashscope.chat.options.model=deepseek-r1
spring.ai.dashscope.embedding.options.model=text-embedding-v3


# =======Redis Stack==========
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.username=default
spring.data.redis.password=
spring.ai.vectorstore.redis.initialize-schema=true
spring.ai.vectorstore.redis.index-name=atguigu-index
spring.ai.vectorstore.redis.prefix=atguigu-prefix
```

#### 13.7.4.1 阿里云百炼平台向量大模型

![图片-169](images/图片-169.jpeg)

##### 13.7.4.1.1 text-embedding-v3

#### 13.7.4.2 配置参考信息来源和知识出处

![图片-170](images/图片-170.gif)

##### 13.7.4.2.1 https://docs.spring.io/spring-ai/reference/api/vectordbs/redis.html

### 13.7.5 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa12Rag4AiOpsApplication
{

    public static void main(String[] args)
    {

        SpringApplication.run(Saa12Rag4AiOpsApplication.class, args);
    }
}
```

### 13.7.6 业务类

#### 13.7.6.1 提供ErrorCode脚本让他存入向量数据库RedisStack，形成文档知识库

##### 13.7.6.1.1 ops.txt

```text
00000 系统OK正确执行后的返回
A0001 用户端错误一级宏观错误码
A0100 用户注册错误二级宏观错误码
B1111 支付接口超时
C2222 Kafka消息解压严重
```

#### 13.7.6.2 V1

##### 13.7.6.2.1 SpringAI源代码接口

###### 13.7.6.2.1.1 VectorStore

![图片-171](images/图片-171.jpeg)

##### 13.7.6.2.2 用redis作为向量存储

###### 13.7.6.2.2.1 安装 redis-stack-server

###### 13.7.6.2.2.1.1 docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server

###### 13.7.6.2.2.2 新增

![图片-172](images/图片-172.jpeg)

##### 13.7.6.2.3 配置类

###### 13.7.6.2.3.1 配置类LLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatModel;
import com.alibaba.cloud.ai.dashscope.chat.DashScopeChatOptions;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.ChatOptions;
import org.springframework.ai.rag.advisor.RetrievalAugmentationAdvisor;
import org.springframework.ai.rag.retrieval.search.VectorStoreDocumentRetriever;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-25 18:53
 * @Description ChatModel+ChatClient+多模型共存
 */
@Configuration
public class SaaLLMConfig
{
    // 模型名称常量定义
    private final String DEEPSEEK_MODEL = "deepseek-v3";
    private final String QWEN_MODEL = "qwen-plus";

    @Bean(name = "deepseek")
    public ChatModel deepSeek()
    {
        return DashScopeChatModel.builder()
                        .dashScopeApi(DashScopeApi.builder()
                                    .apiKey(System.getenv("aliQwen-api"))
                                .build())
                .defaultOptions(
                        DashScopeChatOptions.builder().withModel(DEEPSEEK_MODEL).build()
                )
                .build();
    }

    @Bean(name = "qwen")
    public ChatModel qwen()
    {
        return DashScopeChatModel.builder().dashScopeApi(DashScopeApi.builder()
                        .apiKey(System.getenv("aliQwen-api"))
                        .build())
                .defaultOptions(
                        DashScopeChatOptions.builder()
                                .withModel(QWEN_MODEL)
                                .build()
                )
                .build();
    }

    @Bean(name = "deepseekChatClient")
    public ChatClient deepseekChatClient(@Qualifier("deepseek") ChatModel deepSeek)
    {
        return ChatClient.builder(deepSeek)
                .defaultOptions(ChatOptions.builder()
                        .model(DEEPSEEK_MODEL)
                        .build())
                .build();
    }


    @Bean(name = "qwenChatClient")
    public ChatClient qwenChatClient(@Qualifier("qwen") ChatModel qwen)
    {
        return ChatClient.builder(qwen)
                .defaultOptions(ChatOptions.builder()
                        .model(QWEN_MODEL)
                        .build())
                .build();
    }
}
```

###### 13.7.6.2.3.2 InitVectorDatabaseConfig(第一版)

```java
package com.atguigu.study.config;

import cn.hutool.crypto.SecureUtil;
import jakarta.annotation.PostConstruct;
import org.springframework.ai.document.Document;
import org.springframework.ai.reader.TextReader;
import org.springframework.ai.transformer.splitter.TokenTextSplitter;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.Resource;
import org.springframework.data.redis.core.RedisTemplate;

import java.nio.charset.Charset;
import java.util.List;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-30 12:16
 * @Description TODO
 */
@Configuration
public class InitVectorDatabaseConfig
{
    @Autowired
    private VectorStore vectorStore;

    @Value("classpath:ops.txt")
    private Resource sqlFile;

    @PostConstruct
    public void init()
    {
        // 1.读取文件
        TextReader textReader = new TextReader(sqlFile);
        textReader.setCharset(Charset.defaultCharset());
        // 2.文件转换成向量（分词）
        List<Document> list = new TokenTextSplitter().transform(textReader.read());

        // 3.写入向量数据库（Redis）,无法去重复版
        vectorStore.add(list);
}
```

##### 13.7.6.2.4 Controller

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.rag.advisor.RetrievalAugmentationAdvisor;
import org.springframework.ai.rag.retrieval.search.VectorStoreDocumentRetriever;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-30 12:21
 * @Description TODO
 */
@RestController
public class RagController
{
    @Resource(name = "qwenChatClient")
    private ChatClient chatClient;
    @Resource
    private VectorStore vectorStore;

    /**
     * http://localhost:8012/rag4aiops?msg=00000
     * http://localhost:8012/rag4aiops?msg=C2222
     * @param msg
     * @return
     */
    @GetMapping("/rag4aiops")
    public Flux<String> rag(String msg)
    {
        String systemInfo = """
                你是一个运维工程师,按照给出的编码给出对应故障解释,否则回复找不到信息。
                """;

        RetrievalAugmentationAdvisor advisor = RetrievalAugmentationAdvisor.builder()
                .documentRetriever(
                        VectorStoreDocumentRetriever.builder()
                                .vectorStore(vectorStore)
                                .build()
                )
                .build();

        return chatClient.prompt()
                .system(systemInfo)
                .user(msg)
                .advisors(advisor) // RAG功能,向量数据库查询
                .stream()
                .content();
    }
}
```

##### 13.7.6.2.5 测试

###### 13.7.6.2.5.1 http://localhost:8012/rag4aiops?msg=00000

##### 13.7.6.2.6 其它问题

###### 13.7.6.2.6.1 重启下微服务try-try

###### 13.7.6.2.6.1.1 重复数据写入问题需考虑， 不然每次重启都要新增

![图片-173](images/图片-173.jpeg)

#### 13.7.6.3 V2

##### 13.7.6.3.1 向量数据库去重问题解决

###### 13.7.6.3.1.1 使用RedisSetNX去重

###### 13.7.6.3.1.1.1 RedisConfig

```java
package com.zzyy.study.config;

import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

/**
 * @auther zzyy
 * @create 2024-03-07 10:45
 */
@Configuration
@Slf4j
public class RedisConfig
{
    /**
     * RedisTemplate配置
     * redis序列化的工具配置类，下面这个请一定开启配置
     * 127.0.0.1:6379> keys *
     * 1) "ord:102"  序列化过
     * 2) "\xac\xed\x00\x05t\x00\aord:102"   野生，没有序列化过
     * this.redisTemplate.opsForValue(); //提供了操作string类型的所有方法
     * this.redisTemplate.opsForList(); // 提供了操作list类型的所有方法
     * this.redisTemplate.opsForSet(); //提供了操作set的所有方法
     * this.redisTemplate.opsForHash(); //提供了操作hash表的所有方法
     * this.redisTemplate.opsForZSet(); //提供了操作zset的所有方法
     * @param redisConnectionFactor
     * @return
     */
    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory redisConnectionFactor)
    {
        RedisTemplate<String,Object> redisTemplate = new RedisTemplate<>();

        redisTemplate.setConnectionFactory(redisConnectionFactor);
        //设置key序列化方式string
        redisTemplate.setKeySerializer(new StringRedisSerializer());
        //设置value的序列化方式json，使用GenericJackson2JsonRedisSerializer替换默认序列化
        redisTemplate.setValueSerializer(new GenericJackson2JsonRedisSerializer());

        redisTemplate.setHashKeySerializer(new StringRedisSerializer());
        redisTemplate.setHashValueSerializer(new GenericJackson2JsonRedisSerializer());

        redisTemplate.afterPropertiesSet();

        return redisTemplate;
    }
}
```

###### 13.7.6.3.1.1.2 InitVectorDatabaseConfig(第二版)

```java
package com.atguigu.study.config;

import cn.hutool.crypto.SecureUtil;
import jakarta.annotation.PostConstruct;
import org.springframework.ai.document.Document;
import org.springframework.ai.reader.TextReader;
import org.springframework.ai.transformer.splitter.TokenTextSplitter;
import org.springframework.ai.vectorstore.AbstractVectorStoreBuilder;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.Resource;
import org.springframework.data.redis.core.RedisTemplate;

import java.nio.charset.Charset;
import java.util.List;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-30 12:16
 * @Description TODO
 */
@Configuration
public class InitVectorDatabaseConfig
{
    @Autowired
    private VectorStore vectorStore;
    @Autowired
    private RedisTemplate<String,String> redisTemplate;

    @Value("classpath:ops.txt")
    private Resource opsFile;

    @PostConstruct
    public void init()
    {
        //1 读取文件
        TextReader textReader = new TextReader(opsFile);
        textReader.setCharset(Charset.defaultCharset());

        //2 文件转换为向量(开启分词)
        List<Document> list = new TokenTextSplitter().transform(textReader.read());

        //3 写入向量数据库RedisStack
        //vectorStore.add(list);

        // 解决上面第3步，向量数据重复问题，使用redis setnx命令处理

        //4 去重复版本

        String sourceMetadata = (String)textReader.getCustomMetadata().get("source");

        String textHash = SecureUtil.md5(sourceMetadata);
        String redisKey = "vector-xxx:" + textHash;

        // 判断是否存入过,redisKey如果可以成功插入表示以前没有过，可以假如向量数据
        Boolean retFlag = redisTemplate.opsForValue().setIfAbsent(redisKey, "1");

        System.out.println("****retFlag : "+retFlag);

        if(Boolean.TRUE.equals(retFlag))
        {
            //键不存在，首次插入,可以保存进向量数据库
            vectorStore.add(list);
        }else {
            //键已存在，跳过或者报错
            //throw new RuntimeException("---重复操作");
            System.out.println("------向量初始化数据已经加载过，请不要重复操作");
        }
    }

}
```

###### 13.7.6.3.1.1.3 性能高+线程安全问题OK

##### 13.7.6.3.2 Controller

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.rag.advisor.RetrievalAugmentationAdvisor;
import org.springframework.ai.rag.retrieval.search.VectorStoreDocumentRetriever;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-30 12:21
 * @Description TODO
 */
@RestController
public class RagController
{
    @Resource(name = "qwenChatClient")
    private ChatClient chatClient;
    @Resource
    private VectorStore vectorStore;

    /**
     * http://localhost:8012/rag4aiops?msg=00000
     * http://localhost:8012/rag4aiops?msg=C2222
     * @param msg
     * @return
     */
    @GetMapping("/rag4aiops")
    public Flux<String> rag(String msg)
    {
        String systemInfo = """
                你是一个运维工程师,按照给出的编码给出对应故障解释,否则回复找不到信息。
                """;

        RetrievalAugmentationAdvisor advisor = RetrievalAugmentationAdvisor.builder()
                .documentRetriever(
                        VectorStoreDocumentRetriever.builder()
                                .vectorStore(vectorStore)
                                .build()
                )
                .build();

        return chatClient.prompt()
                .system(systemInfo)
                .user(msg)
                .advisors(advisor) // RAG功能,向量数据库查询
                .stream()
                .content();
    }
}
```

##### 13.7.6.3.3 找不到的ErrorCode，测试不存在的ErrorCode

# 14 Tool Calling工具调用

![图片-174](images/图片-174.png)

## 14.1 不调用如何

![图片-175](images/图片-175.jpeg)

## 14.2 是什么

### 14.2.1 官网

#### 14.2.1.1 SpringAI

##### 14.2.1.1.1 https://docs.spring.io/spring-ai/reference/api/tools.html

#### 14.2.1.2 SpringAI Alibba

![图片-176](images/图片-176.jpeg)

##### 14.2.1.2.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/tool-calling/?spm=5176.29160081.0.0.2856aa5cgvn0gm

#### 14.2.1.3 一句话

##### 14.2.1.3.1 LLM的外部utils工具类

### 14.2.2 重要提示:

#### 14.2.2.1 ToolCalling(也称为FunctionCalling)它允许大模型与一组API或工具进行交互，将 LLM 的智能与外部工具或 API无缝连接，从而增强大模型其功能。

#### 14.2.2.2 LLM本身并不执行函数,它只是指示应该调用哪个函数以及如何调用

## 14.3 能干嘛

### 14.3.1 访问实时数据

#### 14.3.1.1 不调用如何

![图片-177](images/图片-177.jpeg)

### 14.3.2 执行某种工具类/辅助类操作

#### 14.3.2.1 大语言模型(LLMs)不仅仅是文本生成的能手,它们还能触发并调用第3方函数，比如发邮件/查询微信/调用支付宝/查看顺丰快递单据号等等......

## 14.4 怎么玩

### 14.4.1 工作流程

![图片-178](images/图片-178.jpeg)

## 14.5 开发步骤

### 14.5.1 新建子模块Module

#### 14.5.1.1 SAA-13ToolCalling

### 14.5.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-13ToolCalling</artifactId>


    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

### 14.5.3 写YML

```properties
server.port=8013

# 设置全局编码格式
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-13ToolCalling

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

### 14.5.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa13ToolCallingApplication
{
    public static void main(String[] args)
    {
        SpringApplication.run(Saa13ToolCallingApplication.class, args);
    }
}
```

### 14.5.5 业务类

#### 14.5.5.1 先不使用ToolCalling

##### 14.5.5.1.1 没有配置类LLMConfig

##### 14.5.5.1.2 controller

```java
package com.atguigu.study.controller;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import jakarta.annotation.Resource;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-31 20:26
 * @Description TODO
 */
@RestController
public class NoToolCallingController
{
    @Resource
    private ChatModel chatModel;
```

```java
    @GetMapping("/notoolcall/chat")
    public Flux<String> chat(@RequestParam(name = "msg",defaultValue = "你是谁现在几点") String msg)
    {
        return chatModel.stream(msg);
    }
}
```

##### 14.5.5.1.3 测试

###### 14.5.5.1.3.1 http://localhost:8013/notoolcall/chat

![图片-179](images/图片-179.jpeg)

#### 14.5.5.2 投入使用ToolCalling

##### 14.5.5.2.1 通过ChatModel实现

###### 14.5.5.2.1.1 没有配置类LLMConfig

###### 14.5.5.2.1.2 新建Tool工具类，类似Utils工具类

###### 14.5.5.2.1.2.1 代码

```java
package com.atguigu.study.utils;

import org.springframework.ai.tool.annotation.Tool;

import java.time.LocalDateTime;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-31 20:39
 * @Description TODO
 */
public class DateTimeTools
{
    /**
     * 1.定义 function call（tool call）
     * 2. returnDirect
     *    true = tool直接返回不走大模型，直接给客户
     *    false = 拿到tool返回的结果，给大模型，最后由大模型回复
     */
    @Tool(description = "获取当前时间", returnDirect = false)
    public String getCurrentTime()
    {
        return LocalDateTime.now().toString();
    }
}
```

###### 14.5.5.2.1.2.2 工具调用直接返回

![图片-180](images/图片-180.jpeg)

###### 14.5.5.2.1.3 Controller

```java
package com.atguigu.study.controller;

import com.atguigu.study.utils.DateTimeTools;
import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.ChatOptions;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.model.tool.ToolCallingChatOptions;
import org.springframework.ai.support.ToolCallbacks;
import org.springframework.ai.tool.ToolCallback;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-31 20:40
 * @Description TODO
 */

@RestController
public class ToolCallingController
{
    @Resource
    private ChatModel chatModel;

    @GetMapping("/toolcall/chat")
    public String chat(@RequestParam(name = "msg",defaultValue = "你是谁，现在几点了") String msg)
    {
        // 1.工具注册到工具集合里
        ToolCallback[] tools = ToolCallbacks.from(new DateTimeTools());
        // 2.将工具集配置进ChatOptions对象
        ChatOptions options = ToolCallingChatOptions.builder().toolCallbacks(tools).build();
        // 3.构建提示词
        Prompt prompt = new Prompt(msg, options);
        // 4.调用大模型
        return chatModel.call(prompt).getResult().getOutput().getText();
    }
}
```

###### 14.5.5.2.1.4 测试

###### 14.5.5.2.1.4.1 http://localhost:8013/toolcall/chat

##### 14.5.5.2.2 通过ChatClient实现

###### 14.5.5.2.2.1 它本身不会自动装配，直接定义无法使用

![图片-181](images/图片-181.png)

###### 14.5.5.2.2.2 配置类LLMConfig

```java
package com.atguigu.study.config;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-31 20:47
 * @Description TODO
 */
@Configuration
public class SaaLLMConfig
{
    @Bean
    public ChatClient chatClient(ChatModel chatModel)
    {
        return ChatClient.builder(chatModel).build();
    }
}
```

###### 14.5.5.2.2.2.1 ChatClient.builder(chatModel).build()

###### 14.5.5.2.2.3 Controller

```java
package com.atguigu.study.controller;

import com.atguigu.study.utils.DateTimeTools;
import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.prompt.ChatOptions;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.model.tool.ToolCallingChatOptions;
import org.springframework.ai.support.ToolCallbacks;
import org.springframework.ai.tool.ToolCallback;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-31 20:40
 * @Description TODO
 */

@RestController
public class ToolCallingController
{
    @Resource
    private ChatModel chatModel;

    @Resource
    private ChatClient chatClient;

    @GetMapping("/toolcall/chat")
    public String chat(@RequestParam(name = "msg",defaultValue = "你是谁现在几点") String msg)
    {
        // 1.工具注册到工具集合里
        ToolCallback[] tools = ToolCallbacks.from(new DateTimeTools());
        // 2.将工具集配置进ChatOptions对象
        ChatOptions options = ToolCallingChatOptions.builder().toolCallbacks(tools).build();
        // 3.构建提示词
        Prompt prompt = new Prompt(msg, options);
        // 4.调用大模型
        return chatModel.call(prompt).getResult().getOutput().getText();
    }

    @GetMapping("/toolcall/chat2")
    public Flux<String> chat2(@RequestParam(name = "msg",defaultValue = "你是谁现在几点") String msg)
    {
        return chatClient.prompt(msg)
                .tools(new DateTimeTools())
                .stream()
                .content();
    }
}
```

###### 14.5.5.2.2.4 测试

###### 14.5.5.2.2.4.1 http://localhost:8013/toolcall/chat2

![图片-182](images/图片-182.jpeg)

###### 14.5.5.2.2.4.2 工具调用直接返回

![图片-183](images/图片-183.jpeg)

###### 14.5.5.2.2.4.2.1 @Tool(description = "获取当前时间", returnDirect = true)

![图片-184](images/图片-184.jpeg)

###### 14.5.5.2.2.4.2.2 @Tool(description = "获取当前时间", returnDirect = false)

![图片-185](images/图片-185.jpeg)

### 14.5.6 小总结

#### 14.5.6.1 新建定义一个Tool工具类

#### 14.5.6.2 ChatModel/ChatClient使用

#### 14.5.6.3 Tool Calling使用注意事项

##### 14.5.6.3.1 ToolCalling使用的前提是大模型支持functioncall才能正常调用。

# 15 MCP模型上下文协议(Model Context Protocol)

![图片-186](images/图片-186.png)

## 15.1 为什么会有MCP出现，之前痛点是什么

![图片-187](images/图片-187.jpeg)
![图片-188](images/图片-188.jpeg)

### 15.1.1 之前每个大模型(如DeepSeek、ChatGPT)需要为每个工具单独开发接口(FunctionCalling)，导致重复劳动

### 15.1.2 痛点

#### 15.1.2.1 共用

#### 15.1.2.2 数量

## 15.2 MCP入门概念

### 15.2.1 MCP自身协议官网

![图片-189](images/图片-189.jpeg)

![图片-190](images/图片-190.jpeg)

#### 15.2.1.1 https://modelcontextprotocol.io/introduction

### 15.2.2 SpringAI官网支持MCP

#### 15.2.2.1 https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html

### 15.2.3 SpringAI Aibaba官网支持MCP

#### 15.2.3.1 https://java2ai.com/docs/1.0.0.2/tutorials/basics/model-context-protocol/?spm=5176.29160081.0.0.2856aa5ccBJ7XE

### 15.2.4 是什么

#### 15.2.4.1 一句话

##### 15.2.4.1.1 Java界的SpringCloud Openfeign，只不过Openfeign是用于微服务通讯的， 而MCP用于大模型通讯的，但它们都是为了通讯获取某项数据的一种机制

### 15.2.5 能干嘛

#### 15.2.5.1 提供了一种标准化的方式来连接 LLMs 需要的上下文，MCP 就类似于一个 Agent 时代的 Type-C协议，希望能将不同来源的数据、工具、服务统一起来供大模型调用

##### 15.2.5.1.1 合久必分 分久必合

![图片-191](images/图片-191.png)

###### 15.2.5.1.1.1 分

![图片-192](images/图片-192.jpeg)

###### 15.2.5.1.1.2 合

![图片-193](images/图片-193.jpeg)

##### 15.2.5.1.2 解释

![图片-194](images/图片-194.jpeg)

##### 15.2.5.1.3 小总结

MCP 厉害的地方在于，不用重复造轮子。

过去每个软件（比如微信、Excel）都要单独给 AI 做接口，

现在 MCP 统一了标准，就像所有电器都用 USB-C 充电口，AI 一个接口就能连接所有工具

### 15.2.6 怎么玩

#### 15.2.6.1 调用上万个通用的MCP

##### 15.2.6.1.1 https://mcp.so/zh

![图片-195](images/图片-195.jpeg)

## 15.3 MCP架构知识

### 15.3.1 MCP遵循 客户端-服务器架构 包含以下几个核心部分

![图片-196](images/图片-196.jpeg)

#### 15.3.1.1 MCP 主机（MCP Hosts）：发起请求的 AI 应用程序，比如聊天机器人、AI 驱动的 IDE 等。

#### 15.3.1.2 MCP 客户端（MCP Clients）：在主机程序内部，与 MCP 服务器保持 1:1 的连接。

#### 15.3.1.3 MCP 服务器（MCP Servers）：为 MCP 客户端提供上下文、工具和提示信息。

#### 15.3.1.4 本地资源（Local Resources）：本地计算机中可供 MCP 服务器安全访问的资源，如文件、数据库。

#### 15.3.1.5 远程资源（Remote Resources）：MCP 服务器可以连接到的远程资源，如通过 API 提供的数据

### 15.3.2 在MCP通信协议中，一般有两种模式

![图片-197](images/图片-197.jpeg)

#### 15.3.2.1 STDIO(标准输入/输出)

##### 15.3.2.1.1 支持标准输入和输出流进行通信，主要用于本地集成、命令行工具等场景

#### 15.3.2.2 SSE (Server-Sent Events)

##### 15.3.2.2.1 支持使用 HTTP POST 请求进行服务器到客户端流式处理，以实现客户端到服务器的通信

#### 15.3.2.3 两者对比

![图片-198](images/图片-198.jpeg)

## 15.4 小总结

### 15.4.1 ToolCalling

#### 15.4.1.1 工具类，为了让大模型使用Util工具

### 15.4.2 RAG

#### 15.4.2.1 知识库，为了让大模型获取足够的上下文

### 15.4.3 MCP

#### 15.4.3.1 协议，为了让大模型之间的相互调用

#### 15.4.3.2 1

![图片-199](images/图片-199.jpeg)

#### 15.4.3.3 2

![图片-200](images/图片-200.jpeg)

#### 15.4.3.4 3

![图片-201](images/图片-201.jpeg)

### 15.4.4 MCP VS ToolCalling

#### 15.4.4.1 之前每个大模型(如DeepSeek、ChatGPT)需要为每个工具单独开发接口(FunctionCalling)，导致重复劳动

#### 15.4.4.2 MCP通过统一协议

##### 15.4.4.2.1 开发者只需写一次MCP服务端，所有兼容MCP协议的模型都能调用，MCP让大模型从"被动应答”变为”主动调用工具”

##### 15.4.4.2.2 我调用一个MCP服务器就等价调用一个带有多个功能的Utils工具类，自己还不用受累携带

## 15.5 本地MCP-开发步骤

### 15.5.1 MCP-Server服务端实现

#### 15.5.1.1 新建子模块Module

##### 15.5.1.1.1 SAA-14LocalMcpServer

#### 15.5.1.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>


    <artifactId>SAA-14LocalMcpServer</artifactId>


    <dependencies>
        <!--注意事项（重要）
            spring-ai-starter-mcp-server-webflux不能和<artifactId>spring-boot-starter-web</artifactId>依赖并存，
            否则会使用tomcat启动,而不是netty启动，从而导致mcpserver启动失败，但程序运行是正常的，mcp客户端连接不上。
        -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>
        <!--mcp-server-webflux-->
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

#### 15.5.1.3 写YML

```properties
server.port=8014

# 设置全局编码格式
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-14LocalMcpServer


# ====mcp-server Config=============
spring.ai.mcp.server.type=async
spring.ai.mcp.server.name=customer-define-mcp-server
spring.ai.mcp.server.version=1.0.0
```

#### 15.5.1.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa14LocalMcpServerApplication
{

    public static void main(String[] args)
    {
        SpringApplication.run(Saa14LocalMcpServerApplication.class, args);
    }

}
```

#### 15.5.1.5 业务类

##### 15.5.1.5.1 天气预报WeatherService服务类

```java
package com.atguigu.study.service;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;

import java.util.Map;

/**
 * @auther bs@126.com
 * @create 2025-07-31 21:07
 * @Description TODO
 */
@Service
public class WeatherService
{
    @Tool(description = "根据城市名称获取天气预报")
    public String getWeatherByCity(String city)
    {
        Map<String, String> map = Map.of(
                "北京", "11111降雨频繁，其中今天和后天雨势较强，部分地区有暴雨并伴强对流天气，需注意",
                "上海", "22222多云,15℃~27℃,南风3级，当前温度27℃。",
                "深圳", "333333多云40天，阴16天，雨30天，晴3天"
        );
        return map.getOrDefault(city, "抱歉：未查询到对应城市！");
    }
}
```

##### 15.5.1.5.2 ToolCallbackProvider接口配置类

```java
package com.atguigu.study.config;

import com.atguigu.study.service.WeatherService;
import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-31 21:08
 * @Description TODO
 */

@Configuration
public class McpServerConfig
{
    /**
     * 将工具方法暴露给外部 mcp client 调用
     * @param weatherService
     * @return
     */
    @Bean
    public ToolCallbackProvider weatherTools(WeatherService weatherService)
    {
        return MethodToolCallbackProvider.builder()
                .toolObjects(weatherService)
                .build();
    }
}
```

#### 15.5.1.6 自启动作为服务端等待调用即可

![图片-202](images/图片-202.jpeg)

### 15.5.2 MCP-Client客户端实现

#### 15.5.2.1 新建子模块Module

##### 15.5.2.1.1 SAA-15LocalMcpClient

#### 15.5.2.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-15LocalMcpClient</artifactId>


    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!-- 2.mcp-clent 依赖 -->
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-mcp-client</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

#### 15.5.2.3 写YML

```properties
server.port=8015

# 设置全局编码格式
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-15LocalMcpClient

# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}

# ====mcp-client Config=============
spring.ai.mcp.client.type=async
spring.ai.mcp.client.request-timeout=60s
spring.ai.mcp.client.toolcallback.enabled=true
spring.ai.mcp.client.sse.connections.mcp-server1.url=http://localhost:8014
```

#### 15.5.2.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa15LocalMcpClientApplication
{
    public static void main(String[] args)
    {
        SpringApplication.run(Saa15LocalMcpClientApplication.class, args);
    }
}
```

#### 15.5.2.5 业务类

##### 15.5.2.5.1 LLMConfig并添加tool调用

```java
package com.atguigu.study.config;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-31 20:47
 * @Description TODO
 */
@Configuration
public class SaaLLMConfig
{
    @Bean
    public ChatClient chatClient(ChatModel chatModel, ToolCallbackProvider tools)
    {
        return ChatClient.builder(chatModel)
                .defaultToolCallbacks(tools.getToolCallbacks())  //mcp协议，配置见yml文件
                .build();
    }
}
```

##### 15.5.2.5.2 controller

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-31 21:14
 * @Description TODO
 */

@RestController
public class McpClientController
{
    @Resource
    private ChatClient chatClient;//使用mcp支持

    @Resource
    private ChatModel chatModel;//没有纳入tool支持，普通调用

    // http://localhost:8015/mcpclient/chat?msg=上海
    @GetMapping("/mcpclient/chat")
    public Flux<String> chat(@RequestParam(name = "msg",defaultValue = "北京") String msg)
    {
        System.out.println("使用了mcp");
        return chatClient.prompt(msg).stream().content();
    }

    @RequestMapping("/mcpclient/chat2")
    public Flux<String> chat2(@RequestParam(name = "msg",defaultValue = "北京") String msg)
    {
        System.out.println("未使用mcp");
        return chatModel.stream(msg);
    }
}
```

### 15.5.3 MCP-Client invoke MCP-Server测试

#### 15.5.3.1 http://localhost:8015/mcpclient/chat?msg=上海

![图片-203](images/图片-203.jpeg)

##### 15.5.3.1.1 使用mcp

#### 15.5.3.2 http://localhost:8015/mcpclient/chat2?msg=上海

![图片-204](images/图片-204.jpeg)

##### 15.5.3.2.1 没有mcp支持，已读乱回

## 15.6 远程MCP增强案例-对接互联网通用MCP服务（百度地图）

### 15.6.1 调用上万个通用的MCP

#### 15.6.1.1 https://mcp.so/zh

![图片-205](images/图片-205.jpeg)

### 15.6.2 对接互联网通用MCP服务（百度地图）

#### 15.6.2.1 https://mcp.so/zh/server/baidu-map/baidu-maps

### 15.6.3 环境配置

#### 15.6.3.1 原理说明

![图片-206](images/图片-206.jpeg)

#### 15.6.3.2 下载最新版的NodeJS

##### 15.6.3.2.1 https://nodejs.org/zh-cn

#### 15.6.3.3 注册百度地图账号+申请API-key

##### 15.6.3.3.1 https://lbsyun.baidu.com/

![图片-207](images/图片-207.gif)

##### 15.6.3.3.2 1

![图片-208](images/图片-208.jpeg)

##### 15.6.3.3.3 2

![图片-209](images/图片-209.jpeg)

##### 15.6.3.3.4 3

![图片-210](images/图片-210.jpeg)

##### 15.6.3.3.5 4

![图片-211](images/图片-211.jpeg)

#### 15.6.3.4 nodejs配置编码-Typescript接入

![图片-212](images/图片-212.jpeg)

### 15.6.4 开发步骤

#### 15.6.4.1 新建子模块Module

##### 15.6.4.1.1 springAI-16chat-mcpclient-call-baidumcp

#### 15.6.4.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.zzyy.study</groupId>
        <artifactId>SpringAI-zyfanV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>springAI-16chat-mcpclient-call-baidumcp</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!-- 1.大模型依赖 -->
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-model-openai</artifactId>
        </dependency>
        <!-- 2.mcp-clent 依赖 -->
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-mcp-client</artifactId>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### 15.6.4.3 写YML

```properties
server.port=6016

# 设置全局编码格式
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=springAI-16chat-mcpclient-call-baidumcp

# ====LLM Config=============
spring.ai.openai.api-key=${aliQwen-api}
spring.ai.openai.base-url=https://dashscope.aliyuncs.com/compatible-mode
spring.ai.openai.chat.options.model=qwen-plus

# ====mcp-client Config=============
spring.ai.mcp.client.toolcallback.enabled=true
spring.ai.mcp.client.stdio.servers-configuration=classpath:/mcp-server.json
```

#### 15.6.4.4 nodejs配置编码-Typescript接入

![图片-213](images/图片-213.jpeg)

##### 15.6.4.4.1 https://mcp.so/zh/server/baidu-map/baidu-maps?tab=content#typescript%E6%8E%A5%E5%85%A5

#### 15.6.4.5 mcp-server.json

{ "mcpServers": { "baidu-map": { "command": "cmd", "args": ["/c", "npx", "-y", "@baidumap/mcp-server-baidu-map"], "env": {"BAIDU_MAP_API_KEY": "yHWFqCBXiiwVrk4psrl7IvqE7IsiBgQ6"} } } }

下面是参数解释情况

![图片-214](images/图片-214.jpeg)

![图片-215](images/图片-215.png)

#### 15.6.4.6 主启动

##### 15.6.4.6.1 启动成功后台见mcp配置

![图片-216](images/图片-216.jpeg)

#### 15.6.4.7 业务类

##### 15.6.4.7.1 LLMConfig

```java
package com.atguigu.study.config;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @auther zzyybs@126.com
 * @create 2025-07-31 20:47
 * @Description TODO
 */
@Configuration
public class SaaLLMConfig
{
    @Bean
    public ChatClient chatClient(ChatModel chatModel, ToolCallbackProvider tools)
    {
        return ChatClient.builder(chatModel)
                //mcp协议，配置见yml文件，此处只赋能给ChatClient对象
                .defaultToolCallbacks(tools.getToolCallbacks())
                .build();
    }
}
```

##### 15.6.4.7.2 controller

```java
package com.zzyy.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyy
 * @create 2025-07-19 18:55
 */
@RestController
public class McpClientCallBaiDuMcpController
{
    @Resource
    private ChatClient chatClient; //添加了MCP调用能力

    @Resource
    private ChatModel chatModel; //没有添加MCP调用能力

    /**
     * 添加了MCP调用能力
     * http://localhost:6016/mcp/chat?msg=查询北京天气
     * http://localhost:6016/mcp/chat?msg=查询61.149.121.66归属地
     * http://localhost:6016/mcp/chat?msg=查询昌平到天安门路线规划
     *
     *
     * @param msg
     * @return
     */
    @GetMapping("/mcp/chat")
    public Flux<String> chat(String msg)
    {
        return chatClient.prompt(msg).stream().content();
    }

    /**
     * 没有添加MCP调用能力
     *http://localhost:6016/mcp/chat2?msg=查询北京天气
     * @param msg
     * @return
     */
    @RequestMapping("/mcp/chat2")
    public Flux<String> chat2(String msg)
    {
        return chatModel.stream(msg);
    }
}
```

### 15.6.5 测试

#### 15.6.5.1 具备mcp能力的

##### 15.6.5.1.1 http://localhost:8016/mcp/chat?msg=查询北纬39.9042东经116.4074天气

![图片-217](images/图片-217.jpeg)

#### 15.6.5.2 不具备mcp能力的

##### 15.6.5.2.1 http://localhost:8016/mcp/chat2?msg=查询北纬39.9042东经116.4074天气

###### 15.6.5.2.1.1 结果1

![图片-218](images/图片-218.jpeg)

###### 15.6.5.2.1.2 结果2

![图片-219](images/图片-219.jpeg)

## 15.7 MCP原理+源码分析

### 15.7.1 源码获得

![图片-220](images/图片-220.jpeg)

#### 15.7.1.1 下载到本地

##### 15.7.1.1.1 npm i -g @baidumap/mcp-server-baidu-map

#### 15.7.1.2 安装到哪里

##### 15.7.1.2.1 npm config get prefix

##### 15.7.1.2.2 index.js

###### 15.7.1.2.2.1 C:\Users\阳\AppData\Roaming\npm\node_modules\@baidumap\mcp-server-baidu-map\dist

![图片-221](images/图片-221.jpeg)

### 15.7.2 原理说明

![图片-222](images/图片-222.jpeg)

# 16 SAA生态篇（部分公开）

![图片-223](images/图片-223.png)

## 16.1 阿里云百炼平台云上RAG知识库(AI智能运维)

![图片-224](images/图片-224.png)

### 16.1.1 需求说明

#### 16.1.1.1 阿里云上知识库搭建

##### 16.1.1.1.1 应用数据导入

![图片-225](images/图片-225.jpeg)

##### 16.1.1.1.2 创建知识库

![图片-226](images/图片-226.jpeg)

### 16.1.2 开发步骤

#### 16.1.2.1 新建子模块Module

##### 16.1.2.1.1 SAA-17BailianRAG

#### 16.1.2.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.atguigu.study</groupId>
        <artifactId>SpringAIAlibaba-atguiguV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>SAA-17BailianRAG</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--spring-ai-alibaba dashscope-->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

</project>
```

#### 16.1.2.3 写YML

```properties
server.port=8017

# 设置全局编码格式
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-17BailianRAG


# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

#### 16.1.2.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa17BailianRagApplication
{

    public static void main(String[] args)
    {
        SpringApplication.run(Saa17BailianRagApplication.class, args);
    }

}
```

#### 16.1.2.5 业务类

##### 16.1.2.5.1 DashScopeConfig

```java
package com.zzyy.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DashScopeConfig {

    @Value("${spring.ai.dashscope.api-key}")
    private String apiKey;

    @Bean
    public DashScopeApi dashScopeApi()
    {
        return DashScopeApi.builder()
                .apiKey(apiKey)
                .workSpaceId("llm-3as714s6flm80yc1")
                .build();
    }

    @Bean
    public ChatClient chatClient(ChatModel dashscopeChatModel)
    {
        return ChatClient.builder(dashscopeChatModel).build();
    }
}
```

##### 16.1.2.5.2 controller

```java
package com.zzyy.study.controller;

import com.alibaba.cloud.ai.advisor.DocumentRetrievalAdvisor;
import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import com.alibaba.cloud.ai.dashscope.rag.DashScopeDocumentRetriever;
import com.alibaba.cloud.ai.dashscope.rag.DashScopeDocumentRetrieverOptions;
import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.rag.retrieval.search.DocumentRetriever;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-08-01 16:51
 * @Description TODO
 */
@RestController
public class BailianRagController
{
    @Resource
    private ChatClient chatClient;
    @Resource
    private DashScopeApi dashScopeApi;

    /**
     * http://localhost:6018/bailian/rag/chat
     * http://localhost:6018/bailian/rag/chat?msg=A0001
     * @param msg
     * @return
     */
    @GetMapping("/bailian/rag/chat")
    public Flux<String> chat(@RequestParam(name = "msg",defaultValue = "00000错误信息") String msg)
    {
        //1 RetrieverOptions参数配置
        DashScopeDocumentRetrieverOptions documentRetrieverOptions = DashScopeDocumentRetrieverOptions.builder()
                .withIndexName("myerror") // 知识库名称
                .build();

        //2 百炼平台RAG知识库构建器
        DocumentRetriever retriever = new DashScopeDocumentRetriever(dashScopeApi,documentRetrieverOptions);

        return chatClient.prompt()
                .user(msg)
                .advisors(new DocumentRetrievalAdvisor(retriever))
                .stream()
                .content();
    }

}
```

## 16.2 阿里云百炼平台云上RAG知识库(电商智能客服案例)

![图片-227](images/图片-227.png)

### 16.2.1 需求说明

#### 16.2.1.1 阿里云上知识库搭建RAG，电商客服统一话术

### 16.2.2 开发步骤

#### 16.2.2.1 新建子模块Module

##### 16.2.2.1.1 springAI-21chat-CustomerService

#### 16.2.2.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.zzyy.study</groupId>
        <artifactId>SpringAI-zyfanV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>springAI-21chat-CustomerService</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!-- 2. SAA大模型依赖 -->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
            <version>1.0.0.2</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### 16.2.2.3 写YML

```properties
server.port=6021

# 设置全局编码格式
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=springAI-21chat-CustomerService

# ====LLM Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

#### 16.2.2.4 主启动

```java
package com.zzyy.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringAi21chatCustomerServiceApplication
{

    public static void main(String[] args)
    {
        SpringApplication.run(SpringAi21chatCustomerServiceApplication.class, args);
    }

}
```

#### 16.2.2.5 业务类

##### 16.2.2.5.1 DashSocpeConfig

```java
package com.zzyy.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DashSocpeConfig {

    @Value("${spring.ai.dashscope.api-key}")
    private String apiKey;

    @Bean
    public DashScopeApi dashScopeApi() {
        return DashScopeApi.builder()
                .apiKey(apiKey)
                .workSpaceId("llm-3as714s6flm80yc1")
                .build();
    }

    @Bean
    public ChatClient chatClient(ChatModel dashscopeChatModel) {
        return ChatClient.builder(dashscopeChatModel).build();
    }
}
```

##### 16.2.2.5.2 controller

```java
package com.zzyy.study.controller;

import com.alibaba.cloud.ai.advisor.DocumentRetrievalAdvisor;
import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import com.alibaba.cloud.ai.dashscope.rag.DashScopeDocumentRetriever;
import com.alibaba.cloud.ai.dashscope.rag.DashScopeDocumentRetrieverOptions;
import jakarta.annotation.Resource;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.rag.retrieval.search.DocumentRetriever;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-08-01 16:51
 * @Description TODO
 */
@RestController
public class AICustomerServiceController
{
    @Resource
    private ChatClient chatClient;
    @Resource
    private DashScopeApi dashScopeApi;

    /**
     * http://localhost:6021/customer/service
     * http://localhost:6021/customer/service?msg=A0001
     * @param msg
     * @return
     */
    @GetMapping("/customer/service")
    public Flux<String> service(@RequestParam(name = "msg",defaultValue = "什么时候发货") String msg)
    {
        //1 RetrieverOptions参数配置
        DashScopeDocumentRetrieverOptions documentRetrieverOptions = DashScopeDocumentRetrieverOptions.builder()
                .withIndexName("淘宝电商话术")// 百炼平台云知识库名称
                .build();

        //2 百炼平台RAG知识库构建器
        DocumentRetriever retriever = new DashScopeDocumentRetriever(dashScopeApi,documentRetrieverOptions);

        return chatClient.prompt()
                .system("你是一个电商智能客服助手，根据用户的问题去知识库查询信息，" +
                        "如果知识库查询不到信息，返回抱歉查询不到任何信息。")
                .user(msg)
                .advisors(new DocumentRetrievalAdvisor(retriever))
                .stream()
                .content();
    }

}
```

## 16.3 本地微服务调用阿里云百炼平台工作流 (AI智能菜单，今天吃什么)

![图片-228](images/图片-228.png)

### 16.3.1 美团，今天吃什么 AI智能菜单

### 16.3.2 不用阿里SAA生态

#### 16.3.2.1 开发步骤

##### 16.3.2.1.1 新建子模块Module

###### 16.3.2.1.1.1 SAA-18TodayMenu

##### 16.3.2.1.2 改POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.zzyy.study</groupId>
        <artifactId>SpringAI-zyfanV1</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>springAI-20chat-TodayMenu</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!-- 2. SAA大模型依赖 -->
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
            <version>1.0.0.2</version>
        </dependency>
        <!--hutool-->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.22</version>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.38</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <compilerArgs>
                        <arg>-parameters</arg>
                    </compilerArgs>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

##### 16.3.2.1.3 写YML

```properties
server.port=8018

# 设置全局编码格式
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=SAA-18TodayMenu


# ====SpringAIAlibaba Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
```

##### 16.3.2.1.4 主启动

```java
package com.atguigu.study;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Saa18TodayMenuApplication
{

    public static void main(String[] args)
    {
        SpringApplication.run(Saa18TodayMenuApplication.class, args);
    }

}
```

##### 16.3.2.1.5 业务类

###### 16.3.2.1.5.1 配置类LLMConfig

```java
package com.atguigu.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DashScopeConfig
{

    @Value("${spring.ai.dashscope.api-key}")
    private String apiKey;

    @Bean
    public DashScopeApi dashScopeApi() {
        return DashScopeApi.builder()
                .apiKey(apiKey)
                .build();
    }

    @Bean
    public ChatClient chatClient(ChatModel dashscopeChatModel) {
        return ChatClient.builder(dashscopeChatModel).build();
    }
}
```

###### 16.3.2.1.5.2 controller

```java
package com.atguigu.study.controller;

import jakarta.annotation.Resource;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

/**
 * @auther zzyybs@126.com
 * @create 2025-09-11 19:00
 * @Description TODO
 */

@RestController
public class MenuController
{
    @Resource
    private ChatModel chatModel;

    @GetMapping(value = "/eat")
    public Flux<String> eat(@RequestParam(name = "msg",defaultValue = "今天吃什么") String question)
    {
        String info = """
                你是一个AI厨师助手,每次随机生成三个家常菜，并且提供这些家常菜的详细做法步骤，以HTML格式返回
                字数控制在1500字以内。
                """;
        // 系统消息
        SystemMessage systemMessage = new SystemMessage(info);
        // 用户消息
        UserMessage userMessage = new UserMessage(question);

        Prompt prompt = new Prompt(userMessage, systemMessage);

        return chatModel.stream(prompt).map(response -> response.getResults().get(0).getOutput().getText());
    }
}
```

##### 16.3.2.1.6 测试

###### 16.3.2.1.6.1 http://localhost:8018/eat

![图片-229](images/图片-229.jpeg)

### 16.3.3 使用阿里SAA生态

#### 16.3.3.1 工作流配置

![图片-230](images/图片-230.jpeg)

#### 16.3.3.2 写YML

```properties
server.port=6020

# 设置全局编码格式
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
server.servlet.encoding.charset=UTF-8

spring.application.name=springAI-20chat-TodayMenu

# ====LLM Config=============
spring.ai.dashscope.api-key=${aliQwen-api}
# SAA PlatForm today's menu Agent app-id
spring.ai.dashscope.agent.options.app-id=f0a4613e6bd540c5bcd55e137e3b0e35
```

#### 16.3.3.3 业务类

##### 16.3.3.3.1 配置类LLMConfig

```java
package com.zzyy.study.config;

import com.alibaba.cloud.ai.dashscope.api.DashScopeApi;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DashScopeConfig
{

    @Value("${spring.ai.dashscope.api-key}")
    private String apiKey;

    @Bean
    public DashScopeApi dashScopeApi() {
        return DashScopeApi.builder()
                .apiKey(apiKey)
                .build();
    }

    @Bean
    public ChatClient chatClient(ChatModel dashscopeChatModel) {
        return ChatClient.builder(dashscopeChatModel).build();
    }
}
```

##### 16.3.3.3.2 controller

```java
package com.zzyy.study.controller;

import com.alibaba.cloud.ai.dashscope.agent.DashScopeAgent;
import com.alibaba.cloud.ai.dashscope.agent.DashScopeAgentOptions;
import com.alibaba.cloud.ai.dashscope.api.DashScopeAgentApi;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @auther zzyybs@126.com
 * @create 2025-08-13 19:01
 * @Description TODO
 */
@RestController
public class MenuCallAgentController
{
    // 百炼平台的appid
    @Value("${spring.ai.dashscope.agent.options.app-id}")
    private String APPID;
    // 百炼云端智能体调用对象
       private DashScopeAgent agent;
    //构造方法注入，创建百炼云端智能体对象
       public MenuCallAgentController(DashScopeAgentApi agentApi)
    {
        this.agent = new DashScopeAgent(agentApi);
    }

    /**
     * http://localhost:8018/eatAgent
     * @param topic
     * @return
     */
    @GetMapping("/eatAgent")
    public String eatAgent(@RequestParam(name = "topic",defaultValue = "今天中午吃什么") String topic)
    {
        DashScopeAgentOptions options = DashScopeAgentOptions.builder().withAppId(APPID).build();

        Prompt prompt = new Prompt(topic, options);

        return agent.call(prompt).getResult().getOutput().getText();
    }
}
```

## 16.4 智能体

![图片-231](images/图片-231.png)

### 16.4.1 是什么

#### 16.4.1.1 钢铁侠:"贾维斯是我最好的伙伴! "

![图片-232](images/图片-232.jpeg)

![图片-233](images/图片-233.jpeg)

##### 16.4.1.1.1 “智能体”是从对话工具进化为数字助手，能像人类助理一样完成端到端的复杂任务，核心突破在于主动性和环境操作能力

#### 16.4.1.2 智能体（Agent）指的是一种应用，它依靠大模型进行自主决策，在与用户进行自然语言交互的时候，根据用户问题能够自主感知环境、做出决策并执行行动的系统。它不仅仅是被动回答问题，而是像“有自主意识的程序”，能主动完成复杂任务

#### 16.4.1.3 举个栗子

##### 16.4.1.3.1 普通大模型问题提问调用：

###### 16.4.1.3.1.1 你问“上海明天天气如何？”它返回一段文字描述。

##### 16.4.1.3.2 智能体

###### 16.4.1.3.2.1 你说“如果明天下雨，提醒我带伞，并取消明天的户外会议。”它会查询天气→设定提醒→检查日历→发送会议取消邮件。

### 16.4.2 能干嘛

#### 16.4.2.1 典型应用场景

##### 16.4.2.1.1 自动化办公：智能体读取邮件、生成报告、安排会议。

##### 16.4.2.1.2 智能家居：根据你的作息自动调节灯光、空调，甚至订购物资。

##### 16.4.2.1.3 复杂问题解决：如“帮我用1万元预算策划一场50人的公司团建”，它会拆解需求、搜索场地、比价、生成方案

### 16.4.3 怎么玩

#### 16.4.3.1 阿里云百炼平台

##### 16.4.3.1.1 https://bailian.console.aliyun.com/

#### 16.4.3.2 创建智能体

![图片-234](images/图片-234.jpeg)

