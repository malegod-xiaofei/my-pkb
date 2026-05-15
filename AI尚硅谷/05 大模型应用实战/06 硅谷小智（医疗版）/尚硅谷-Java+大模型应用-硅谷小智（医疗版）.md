# 硅谷小智（医疗版）

> 讲师：环环

## 目录

- 前置知识
- 一、LangChain4j 入门
- 二、接入其他大模型
- 三、人工智能服务 AIService
- 四、聊天记忆 Chat memory
- 五、持久化聊天记忆 Persistence
- 六、提示词 Prompt
- 七、项目实战：创建硅谷小智
- 八、Function Calling 函数调用
- 九、项目实战：优化硅谷小智
- 十、检索增强生成 RAG
- 十一、项目实战：在硅谷小智中实现 RAG
- 十二、向量模型和向量存储
- 十三、项目实战：在硅谷小智中整合向量数据库
- 十四、项目实战：改造流式输出
- 十五、项目实战：运行前端工程

---

## 前置知识

在学习本项目之前，建议先具备以下基础：

- Java 基础
- Maven
- MySQL
- SSM
- Spring Boot

---

# 一、LangChain4j 入门

## 1. 简介

LangChain4j 的目标，是简化将大语言模型（LLM, Large Language Model）集成到 Java 应用程序中的过程。

### 1.1 历史背景

- 2022 年 10 月，Harrison Chase 发布了基于 Python 的 LangChain。
- 2022 年 11 月 30 日，OpenAI 发布 ChatGPT（GPT-3.5）。
- 随后，LangChain 的 JavaScript 版本 `LangChain.js` 也发布了。
- 2023 年 11 月，Quarkus 发布 LangChain4j `0.1` 版本。
- 2025 年 2 月，发布 `1.0-Beta1`；2025 年 4 月，发布 `1.0-Beta3`。

官网：<https://docs.langchain4j.dev>

### 1.2 主要功能

LangChain4j 的核心价值主要体现在以下几个方面：

1. **统一接入大模型与向量数据库**  
   通过统一的应用程序编程接口（API），可以方便地访问主流商业和开源大语言模型，以及各类向量数据库，用于构建聊天机器人、智能助手等应用。

2. **面向 Java 生态设计**  
   借助 Spring Boot 集成能力，可以把大模型能力顺畅地接入 Java 应用。

3. **支持双向能力集成**  
   不仅可以从 Java 代码中调用大模型，也允许大模型反向调用你的 Java 代码。

4. **覆盖高级 AI 应用模式**  
   提供从提示词模板、聊天记忆、输出解析，到 AI Service、工具调用、RAG（检索增强生成）等一整套能力。

### 1.3 应用示例

#### 场景 1：构建 AI 聊天机器人

你可能希望构建一个由 AI 驱动的聊天机器人，它可以访问你的数据，并按照你的业务方式运行。

例如，客户支持机器人可以：

- 礼貌地回答客户问题
- 处理 / 更改 / 取消订单

教育助手可以：

- 解释不清楚的部分

#### 场景 2：处理非结构化数据并抽取结构化信息

你可能需要处理大量非结构化数据（如文件、网页等），并从中提取结构化信息，例如：

- 从客户评价和客服聊天记录中提取有效反馈
- 从竞争对手网站中提取有价值的信息
- 从求职者简历中提取关键信息

#### 场景 3：生成内容

你可能需要生成各类内容，例如：

- 为每位客户量身定制电子邮件
- 为应用程序 / 网站生成内容
  - 博客文章
  - 故事

#### 场景 4：转换信息

你可能需要对信息进行转换，例如：

- 总结
- 校对与改写
- 翻译

---

## 2. 创建 Spring Boot 项目

### 2.1 创建一个 Maven 项目

项目名示例：

```text
java-ai-langchain4j
```

### 2.2 添加 Spring Boot 相关依赖

在 `pom.xml` 中添加如下内容：

```xml
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <spring-boot.version>3.2.6</spring-boot.version>
    <knife4j.version>4.3.0</knife4j.version>
    <langchain4j.version>1.0.0-beta3</langchain4j.version>
    <mybatis-plus.version>3.5.11</mybatis-plus.version>
</properties>

<dependencies>
    <!-- web应用程序核心依赖 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <!-- 编写和运行测试用例 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>

    <!-- 前后端分离中的后端接口测试工具 -->
    <dependency>
        <groupId>com.github.xiaoymin</groupId>
        <artifactId>knife4j-openapi3-jakarta-spring-boot-starter</artifactId>
        <version>${knife4j.version}</version>
    </dependency>
</dependencies>

<dependencyManagement>
    <dependencies>
        <!-- 引入SpringBoot依赖管理清单 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>${spring-boot.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### 2.3 创建配置文件

在 `resources` 目录下创建 `application.properties`：

```properties
# web服务访问端口
server.port=8080
```

### 2.4 创建启动类

```java
package com.atguigu.java.ai.langchain4j;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class XiaozhiApp {

    public static void main(String[] args) {
        SpringApplication.run(XiaozhiApp.class, args);
    }
}
```

### 2.5 启动项目

启动启动类后，访问：

- <http://localhost:8080/doc.html>

用于检查程序能否正常运行。

---

## 3. 接入大模型

参考文档：<https://docs.langchain4j.dev/get-started>

### 3.1 LangChain4j 库结构

LangChain4j 采用模块化设计，主要包括：

1. `langchain4j-core`  
   定义核心抽象概念，例如聊天语言模型、嵌入存储及相关 API。

2. `langchain4j` 主模块  
   提供常用工具，例如文档加载器、聊天记忆实现，以及 AI Service 等高层能力。

3. `langchain4j-{integration}` 集成模块  
   用于对接不同的大语言模型提供商和嵌入存储。你可以独立使用这些模块；如需更多高级能力，再额外引入主模块即可。

### 3.2 添加 LangChain4j 相关依赖

```xml
<properties>
    <langchain4j.version>1.0.0-beta3</langchain4j.version>
</properties>

<dependencies>
    <!-- 基于 open-ai 标准的大模型接入：ChatGPT、DeepSeek 等 -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-open-ai</artifactId>
    </dependency>
</dependencies>

<dependencyManagement>
    <dependencies>
        <!-- 引入 langchain4j 依赖管理清单 -->
        <dependency>
            <groupId>dev.langchain4j</groupId>
            <artifactId>langchain4j-bom</artifactId>
            <version>${langchain4j.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### 3.3 创建测试用例

接入任何一个大模型前，通常都需要先申请 `apiKey`。

如果暂时没有密钥，也可以使用 LangChain4j 提供的演示密钥。该密钥免费，但有使用配额限制，且仅支持 `gpt-4o-mini` 模型。

```java
package com.atguigu.java.ai.langchain4j;

import dev.langchain4j.model.openai.OpenAiChatModel;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class LLMTest {

    /**
     * gpt-4o-mini 语言模型接入测试
     */
    @Test
    public void testGPTDemo() {
        // 初始化模型
        OpenAiChatModel model = OpenAiChatModel.builder()
                // LangChain4j提供的代理服务器，会将演示密钥替换成真实密钥，再将请求转发给 OpenAI API
                // .baseUrl("http://langchain4j.dev/demo/openai/v1")
                // 如果 apiKey="demo"，可省略 baseUrl 配置
                .apiKey("demo")
                .modelName("gpt-4o-mini")
                .build();

        // 向模型提问
        String answer = model.chat("你好");

        // 输出结果
        System.out.println(answer);
    }
}
```

---

## 4. Spring Boot 整合

参考文档：<https://docs.langchain4j.dev/tutorials/spring-boot-integration>

### 4.1 替换依赖

将 `langchain4j-open-ai` 替换为：

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-open-ai-spring-boot-starter</artifactId>
</dependency>
```

### 4.2 配置模型参数

```properties
# langchain4j 测试模型
langchain4j.open-ai.chat-model.api-key=demo
langchain4j.open-ai.chat-model.model-name=gpt-4o

# 请求和响应日志
langchain4j.open-ai.chat-model.log-requests=true
langchain4j.open-ai.chat-model.log-responses=true

# 启用日志 debug 级别
logging.level.root=debug
```

### 4.3 创建测试用例

```java
/**
 * 整合 SpringBoot
 */
@Autowired
private OpenAiChatModel openAiChatModel;

@Test
public void testSpringBoot() {
    // 向模型提问
    String answer = openAiChatModel.chat("你好");

    // 输出结果
    System.out.println(answer);
}
```

---

# 二、接入其他大模型

## 1. 都有哪些大模型

大语言模型排行榜：<https://superclueai.com/>

### SuperCLUE 简介

SuperCLUE 是由国内 CLUE 学术社区于 2023 年 5 月推出的中文通用大模型综合性评测基准。

### 评测目的

全面评估中文大模型在以下方面的能力：

- 语义理解
- 逻辑推理
- 代码生成
- 数学、物理、社科等 50 多个学科的专业能力

它旨在回答以下问题：

- 中文大模型整体效果如何
- 不同任务下的效果差异如何
- 与国际代表性模型的差距有多大
- 与人类水平相比表现如何

### 特色优势

- 针对中文特性任务进行专项评测，如成语、诗歌、字形等
- 通过 3700 多道客观题和匿名对战机制，动态追踪国内外主流模型表现
- 覆盖 GPT-4、文心一言、通义千问等主流模型
- 保证评测的客观性与时效性

### 行业影响

作为中文领域较具影响力的评测社区，其结果被学界和产业界广泛引用。例如：

- 商汤“日日新 5.0”
- 百度文心大模型

这些模型都曾借助 SuperCLUE 验证技术突破。它也为中文大模型的发展和优化提供了重要参考。

LangChain4j 支持接入的大模型列表：  
<https://docs.langchain4j.dev/integrations/language-models/>

---

## 2. 接入 DeepSeek

### 2.1 获取开发参数

访问官网注册账号，获取 `base_url` 和 `api_key`，并完成充值：

- 官网：<https://www.deepseek.com/>

### 2.2 配置开发参数

为了 `apiKey` 的安全，建议将其配置到服务器环境变量中。变量名可自定义，例如：

```bash
DEEP_SEEK_API_KEY
```

### 2.3 配置模型参数

DeepSeek API 文档：<https://api-docs.deepseek.com/zh-cn/>

在 LangChain4j 中，DeepSeek 与 GPT 一样，使用的是 OpenAI 接口标准，因此同样可以通过 `OpenAiChatModel` 接入。

```properties
# DeepSeek
langchain4j.open-ai.chat-model.base-url=https://api.deepseek.com
langchain4j.open-ai.chat-model.api-key=${DEEP_SEEK_API_KEY}

# DeepSeek-V3
langchain4j.open-ai.chat-model.model-name=deepseek-chat

# DeepSeek-R1 推理模型
# langchain4j.open-ai.chat-model.model-name=deepseek-reasoner
```

### 2.4 测试

直接复用前面的测试用例即可。

---

## 3. Ollama 本地部署

### 3.1 为什么要本地部署

Ollama 是一个用于本地部署大模型的工具。本地部署通常有以下优势：

- **数据隐私与安全**：适合金融、医疗、法律等涉及敏感数据的行业
- **离线可用**：在网络不稳定或无法联网时，模型仍可正常运行
- **降低成本**：避免长期云服务按量计费带来的持续成本
- **部署简单**：通过简单命令即可下载并运行模型
- **灵活扩展与定制**：可进一步微调以适配垂直领域需求

### 3.2 在 Ollama 上部署 DeepSeek

官网：<https://ollama.com/>

操作步骤：

1. 下载并安装 Ollama，例如安装包：`OllamaSetup.exe`
2. 查看模型列表，选择要部署的模型：<https://ollama.com/search>
3. 执行命令运行模型：

```bash
ollama run deepseek-r1:1.5
```

如果是第一次运行，会先下载模型。

### 3.3 常用命令

> 原文此处仅保留了章节标题，未见展开内容，后续整理时若发现补充内容会继续合并。

### 3.4 引入依赖

参考文档：<https://docs.langchain4j.dev/integrations/language-models/ollama#get-started>

```xml
<!-- 接入ollama -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-ollama-spring-boot-starter</artifactId>
</dependency>
```

### 3.5 配置模型参数

```properties
# ollama
langchain4j.ollama.chat-model.base-url=http://localhost:11434
langchain4j.ollama.chat-model.model-name=deepseek-r1:1.5b
langchain4j.ollama.chat-model.log-requests=true
langchain4j.ollama.chat-model.log-responses=true
```

### 3.6 创建测试用例

```java
/**
 * ollama 接入
 */
@Autowired
private OllamaChatModel ollamaChatModel;

@Test
public void testOllama() {
    // 向模型提问
    String answer = ollamaChatModel.chat("你好");

    // 输出结果
    System.out.println(answer);
}
```

---

## 4. 接入阿里百炼平台

### 4.1 什么是阿里百炼

阿里云百炼于 2023 年 10 月推出，集成了阿里的通义系列大模型和第三方大模型，覆盖文本、图像、音视频等多种模态。

其主要优势包括：

- 集成超百款大模型 API，模型选择丰富
- 5～10 分钟即可低代码快速构建智能体
- 提供模型训练、评估与应用开发的全链路工具
- 支持在线部署与弹性扩缩容
- 新用户提供大量免费 token，降低业务落地成本

相关链接：

- 支持接入的模型列表：<https://help.aliyun.com/zh/model-studio/models>
- 模型广场：<https://bailian.console.aliyun.com/?productCode=p_efm#/model-market>

### 4.2 申请免费体验

大致流程如下：

1. 进入免费体验页面
2. 点击“免费体验”
3. 点击“开通服务”
4. 确认开通

### 4.3 配置 API Key

申请地址：  
<https://bailian.console.aliyun.com/?apiKey=1&productCode=p_efm#/api-key>

建议将 API Key 配置到环境变量中：

```bash
DASH_SCOPE_API_KEY
```

### 4.4 添加依赖

LangChain4j 参考文档：  
<https://docs.langchain4j.dev/integrations/language-models/dashscope#plain-java>

```xml
<dependencies>
    <!-- 接入阿里云百炼平台 -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-community-dashscope-spring-boot-starter</artifactId>
    </dependency>
</dependencies>

<dependencyManagement>
    <dependencies>
        <!-- 引入百炼依赖管理清单 -->
        <dependency>
            <groupId>dev.langchain4j</groupId>
            <artifactId>langchain4j-community-bom</artifactId>
            <version>${langchain4j.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### 4.5 配置模型参数

```properties
# 阿里百炼平台
langchain4j.community.dashscope.chat-model.api-key=${DASH_SCOPE_API_KEY}
langchain4j.community.dashscope.chat-model.model-name=qwen-max
```

### 4.6 测试通义千问

```java
/**
 * 通义千问大模型
 */
@Autowired
private QwenChatModel qwenChatModel;

@Test
public void testDashScopeQwen() {
    // 向模型提问
    String answer = qwenChatModel.chat("你好");

    // 输出结果
    System.out.println(answer);
}
```

### 4.7 测试通义万象

用于生成图片的测试示例：

```java
@Test
public void testDashScopeWanx() {
    WanxImageModel wanxImageModel = WanxImageModel.builder()
            .modelName("wanx2.1-t2i-plus")
            .apiKey(System.getenv("DASH_SCOPE_API_KEY"))
            .build();

    Response<Image> response = wanxImageModel.generate(
            "奇幻森林精灵：在一片弥漫着轻柔薄雾的古老森林深处，阳光透过茂密枝叶洒下金色光斑。" +
            "一位身材娇小、长着透明薄翼的精灵少女站在一朵硕大的蘑菇上。" +
            "她有着海藻般的绿色长发，发间点缀着蓝色的小花，皮肤泛着珍珠般的微光。" +
            "身上穿着由翠绿树叶和白色藤蔓编织而成的连衣裙，手中捧着一颗散发着柔和光芒的水晶球，" +
            "周围环绕着五彩斑斓的蝴蝶，脚下是铺满苔藓的地面，蘑菇和蕨类植物丛生，营造出神秘而梦幻的氛围。"
    );

    System.out.println(response.content().url());
}
```

### 4.8 测试 DeepSeek

阿里百炼平台也可以集成第三方大模型，例如 DeepSeek。  
思路是：将 `base-url` 指向百炼平台，并使用百炼平台上的模型名称与 API Key。

```properties
# 集成百炼 - DeepSeek
langchain4j.open-ai.chat-model.base-url=https://dashscope.aliyuncs.com/compatible-mode/v1
langchain4j.open-ai.chat-model.api-key=${DASH_SCOPE_API_KEY}
langchain4j.open-ai.chat-model.model-name=deepseek-v3

# 温度系数：通常在 0 ~ 1 之间。
# 值越高，输出越随机、越有创造性；值越低，输出越稳定、越保守。
langchain4j.open-ai.chat-model.temperature=0.9
```

测试时，直接复用前面的 `testSpringBoot` 用例即可。

---

# 三、人工智能服务 AIService

## 1. 什么是 AIService

AIService 通过**面向接口**和**动态代理**的方式组织程序，使高级功能的实现更加灵活。

### 1.1 链 Chain（旧版）

“链（Chain）”的概念来源于 Python 生态中的 LangChain。  
它的思路是：针对常见场景预先定义一条链，例如：

- 聊天机器人
- 检索增强生成（RAG）

链会把多个底层组件组合起来，并协调它们之间的交互。

不过，链的主要问题在于**灵活性不足**，这里不做深入展开。

### 1.2 人工智能服务 AIService

在 LangChain4j 中，通常使用 AIService 来完成更复杂的操作，由它来负责底层组件的组装。

AIService 可以处理最常见的工作：

- 为大语言模型格式化输入
- 解析大语言模型输出

同时，它还支持更多高级能力：

- 聊天记忆 `Chat memory`
- 工具调用 `Tools`
- 检索增强生成 `RAG`

---

## 2. 创建 AIService

### 2.1 引入依赖

```xml
<!-- langchain4j 高级功能 -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-spring-boot-starter</artifactId>
</dependency>
```

### 2.2 创建接口

```java
package com.atguigu.java.ai.langchain4j.assistant;

public interface Assistant {
    String chat(String userMessage);
}
```

### 2.3 测试用例

```java
@SpringBootTest
public class AIServiceTest {

    @Autowired
    private QwenChatModel qwenChatModel;

    @Test
    public void testChat() {
        // 创建 AIService
        Assistant assistant = AiServices.create(Assistant.class, qwenChatModel);

        // 调用 service 接口
        String answer = assistant.chat("Hello");
        System.out.println(answer);
    }
}
```

### 2.4 `@AiService`

也可以直接在 `Assistant` 接口上添加 `@AiService` 注解：

```java
package com.atguigu.java.ai.langchain4j.assistant;

// 因为在配置文件中同时配置了多个大语言模型，
// 所以这里需要显式指定模型的 beanName（qwenChatModel）
@AiService(wiringMode = EXPLICIT, chatModel = "qwenChatModel")
public interface Assistant {
    String chat(String userMessage);
}
```

这样在测试类中，就可以直接注入 `Assistant`：

```java
@Autowired
private Assistant assistant;

@Test
public void testAssistant() {
    String answer = assistant.chat("Hello");
    System.out.println(answer);
}
```

### 2.5 工作原理

`AiServices` 会将 `Assistant` 接口和其他组件进行组装，并通过反射机制创建一个实现该接口的代理对象。

这个代理对象的核心作用是：

- **输入转换**：例如将 `String` 转换为模型需要的 `UserMessage`
- **输出转换**：例如将模型返回的 `AiMessage` 转换为 `String`

可以简单理解为：**代理对象负责输入与输出的适配转换**。

---

# 四、聊天记忆 Chat memory

## 1. 测试对话是否有记忆

```java
package com.atguigu.java.ai.langchain4j;

@SpringBootTest
public class ChatMemoryTest {

    @Autowired
    private Assistant assistant;

    @Test
    public void testChatMemory() {
        String answer1 = assistant.chat("我是环环");
        System.out.println(answer1);

        String answer2 = assistant.chat("我是谁");
        System.out.println(answer2);
    }
}
```

从这个测试可以看出，当前这种基础接入方式下，大模型本身**并没有聊天记忆**。

## 2. 聊天记忆的简单实现

也可以通过手动拼接上下文的方式，实现简单的对话记忆：

```java
@Autowired
private QwenChatModel qwenChatModel;

@Test
public void testChatMemory2() {
    // 第一轮对话
    UserMessage userMessage1 = UserMessage.userMessage("我是环环");
    ChatResponse chatResponse1 = qwenChatModel.chat(userMessage1);
    AiMessage aiMessage1 = chatResponse1.aiMessage();

    // 输出大语言模型的回复
    System.out.println(aiMessage1.text());

    // 第二轮对话
    UserMessage userMessage2 = UserMessage.userMessage("你知道我是谁吗");
    ChatResponse chatResponse2 = qwenChatModel.chat(Arrays.asList(userMessage1, aiMessage1, userMessage2));
    AiMessage aiMessage2 = chatResponse2.aiMessage();

    // 输出大语言模型的回复
    System.out.println(aiMessage2.text());
}
```

## 3. 使用 ChatMemory 实现聊天记忆

使用 AIService 后，可以把多轮对话的复杂性封装起来，使聊天记忆的实现更加简洁：

```java
@Test
public void testChatMemory3() {
    // 创建 chatMemory
    MessageWindowChatMemory chatMemory = MessageWindowChatMemory.withMaxMessages(10);

    // 创建 AIService
    Assistant assistant = AiServices
            .builder(Assistant.class)
            .chatLanguageModel(qwenChatModel)
            .chatMemory(chatMemory)
            .build();

    // 调用 service 接口
    String answer1 = assistant.chat("我是环环");
    System.out.println(answer1);

    String answer2 = assistant.chat("我是谁");
    System.out.println(answer2);
}
```

## 4. 使用 AIService 实现聊天记忆

### 4.1 创建记忆对话智能体

当 AIService 由多个组件（如大模型、聊天记忆等）组合而成时，也可以把它理解为一个“智能体”。

```java
package com.atguigu.java.ai.langchain4j.assistant;

@AiService(
        wiringMode = EXPLICIT,
        chatModel = "qwenChatModel",
        chatMemory = "chatMemory"
)
public interface MemoryChatAssistant {
    String chat(String message);
}
```

### 4.2 配置 ChatMemory

```java
package com.atguigu.java.ai.langchain4j.config;

@Configuration
public class MemoryChatAssistantConfig {

    @Bean
    ChatMemory chatMemory() {
        // 设置聊天记忆最多保留的 message 数量
        return MessageWindowChatMemory.withMaxMessages(10);
    }
}
```

### 4.3 测试

```java
@Autowired
private MemoryChatAssistant memoryChatAssistant;

@Test
public void testChatMemory4() {
    String answer1 = memoryChatAssistant.chat("我是环环");
    System.out.println(answer1);

    String answer2 = memoryChatAssistant.chat("我是谁");
    System.out.println(answer2);
}
```

## 5. 隔离聊天记忆

在真实业务中，通常需要做到：

- 不同用户之间聊天记忆隔离
- 同一用户不同会话之间聊天记忆隔离

### 5.1 创建记忆隔离对话智能体

```java
package com.atguigu.java.ai.langchain4j.assistant;

@AiService(
        wiringMode = EXPLICIT,
        chatMemory = "chatMemory",
        chatMemoryProvider = "chatMemoryProvider"
)
public interface SeparateChatAssistant {

    /**
     * 分离聊天记录
     *
     * @param memoryId    聊天 id
     * @param userMessage 用户消息
     * @return 回复内容
     */
    String chat(@MemoryId int memoryId, @UserMessage String userMessage);
}
```

### 5.2 配置 ChatMemoryProvider

```java
package com.atguigu.java.ai.langchain4j.config;

@Configuration
public class SeparateChatAssistantConfig {

    @Bean
    ChatMemoryProvider chatMemoryProvider() {
        return memoryId -> MessageWindowChatMemory.builder()
                .id(memoryId)
                .maxMessages(10)
                .build();
    }
}
```

### 5.3 测试对话助手

可以使用不同的 `memoryId` 来验证聊天记忆是否彼此隔离：

```java
@Autowired
private SeparateChatAssistant separateChatAssistant;

@Test
public void testChatMemory5() {
    String answer1 = separateChatAssistant.chat(1, "我是环环");
    System.out.println(answer1);

    String answer2 = separateChatAssistant.chat(1, "我是谁");
    System.out.println(answer2);

    String answer3 = separateChatAssistant.chat(2, "我是谁");
    System.out.println(answer3);
}
```

---

# 五、持久化聊天记忆 Persistence

默认情况下，聊天记忆是保存在内存中的。  
如果希望持久化存储，就需要自定义聊天记忆存储类，把聊天消息保存到指定的持久化介质中。

## 1. 存储介质的选择

聊天记忆适合存到哪种数据库，需要根据**数据特点、应用场景、性能要求**综合判断。下面是几种常见方案：

### 1.1 MySQL

**特点：**

- 关系型数据库
- 支持事务
- 适合结构化数据存储与复杂查询

**适用场景：**

如果聊天记忆结构比较规整，例如包含固定字段：

- 对话 ID
- 用户 ID
- 时间戳
- 消息内容

并且需要做复杂查询与统计分析，例如：

- 按用户统计对话次数
- 按时间范围查询特定对话

那么 MySQL 是一个不错的选择。

### 1.2 Redis

**特点：**

- 支持字符串、哈希、列表等多种数据结构
- 读写速度快
- 适合快速获取最新聊天记录

**适用场景：**

适用于对读写性能要求很高、希望快速提供上下文的场景。

### 1.3 MongoDB

**特点：**

- 文档型数据库
- 以 JSON-like 文档形式存储数据
- 结构灵活，可扩展性强
- 不要求预先定义严格表结构

**适用场景：**

当聊天记忆中包含文本、图片、语音等多样化信息，或者消息结构可能经常变化时，MongoDB 更容易适应这类半结构化 / 非结构化数据。

### 1.4 Cassandra

**特点：**

- 分布式 NoSQL 数据库
- 高可扩展性、高可用性
- 适合海量时间序列相关数据

**适用场景：**

对于用户量大、聊天数据量巨大、需要分布式存储和高并发处理的大型聊天应用，Cassandra 更有优势。

---

## 2. MongoDB

### 2.1 简介

MongoDB 是一个基于文档的 NoSQL 数据库，由 MongoDB Inc. 开发。

这里的 NoSQL，指的是**非关系型数据库**。它也常被解释为 **Not Only SQL**，用来统称不同于传统关系型数据库的一类数据库系统。

MongoDB 的设计目标主要是应对以下需求：

- 大数据量
- 高性能
- 高灵活性

MongoDB 使用以下概念组织数据：

- **Database（数据库）**：存储数据的容器，类似关系型数据库中的数据库
- **Collection（集合）**：数据库中的集合，类似关系型数据库中的表
- **Document（文档）**：集合中的一条记录，类似关系型数据库中的行，以 BSON 格式存储

MongoDB 中的数据本质上由键值对组成，文档结构类似 JSON，对字段扩展十分友好，字段值中还可以嵌套：

- 其他文档
- 数组
- 文档数组

### 2.2 安装 MongoDB

文中给出的常见安装资源包括：

- 服务端：`mongodb-windows-x86_64-8.0.6-signed.msi`
- 命令行客户端：`mongosh-2.5.0-win32-x64.zip`
- 图形客户端：`mongodb-compass-1.39.3-win32-x64.exe`

下载入口：

- MongoDB Community：<https://www.mongodb.com/try/download/community>
- MongoDB Shell：<https://www.mongodb.com/try/download/shell>
- MongoDB Compass：<https://www.mongodb.com/try/download/compass>

### 2.3 使用 `mongosh`

#### 启动 MongoDB Shell

如果 MongoDB 运行在本地默认端口 `27017`，可直接输入：

```bash
mongosh
```

#### 连接远程或非默认端口实例

```bash
mongosh --host <hostname>:<port>
```

其中：

- `<hostname>`：MongoDB 服务器主机名或 IP 地址
- `<port>`：MongoDB 服务器端口号

#### 常见基础操作

```text
查看当前数据库：db
显示数据库列表：show dbs
切换到指定数据库：use <database_name>
执行查询操作：db.<collection_name>.find()
插入文档：db.<collection_name>.insertOne({ ... })
更新文档：db.<collection_name>.updateOne({ ... })
删除文档：db.<collection_name>.deleteOne({ ... })
退出 MongoDB Shell：quit() 或 exit
```

#### CRUD 示例

```javascript
// 插入文档
db.mycollection.insertOne({ name: "Alice", age: 30 })

// 查询文档
db.mycollection.find()

// 更新文档
db.mycollection.updateOne({ name: "Alice" }, { $set: { age: 31 } })

// 删除文档
db.mycollection.deleteOne({ name: "Alice" })

// 退出 MongoDB Shell
quit()
```

### 2.4 使用 MongoDB Compass

> 原文此处仅出现章节标题，暂未展开说明，后续若在文档其他位置发现补充内容，我会继续合并整理。

### 2.5 整合 Spring Boot

引入 MongoDB 依赖：

```xml
<!-- Spring Boot Starter Data MongoDB -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>
```

添加连接配置：

```properties
# MongoDB 连接配置
spring.data.mongodb.uri=mongodb://localhost:27017/chat_memory_db
```

### 2.6 CRUD 测试

创建实体类，用于映射 MongoDB 中的文档：

```java
package com.atguigu.java.ai.langchain4j.bean;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Document("chat_messages")
public class ChatMessages {

    // 唯一标识，映射到 MongoDB 文档的 _id 字段
    @Id
    private ObjectId messageId;

    // private Long messageId;
    private String content; // 存储当前聊天记录列表的 json 字符串
}
```

创建测试类：

```java
package com.atguigu.java.ai.langchain4j;

@SpringBootTest
public class MongoCrudTest {

    @Autowired
    private MongoTemplate mongoTemplate;

    /**
     * 插入文档
     */
    /*
    @Test
    public void testInsert() {
        mongoTemplate.insert(new ChatMessages(1L, "聊天记录"));
    }
    */

    /**
     * 插入文档
     */
    @Test
    public void testInsert2() {
        ChatMessages chatMessages = new ChatMessages();
        chatMessages.setContent("聊天记录列表");
        mongoTemplate.insert(chatMessages);
    }

    /**
     * 根据 id 查询文档
     */
    @Test
    public void testFindById() {
        ChatMessages chatMessages = mongoTemplate.findById(
                "6801ead733ba9c4a0d9b6c7b",
                ChatMessages.class
        );
        System.out.println(chatMessages);
    }

    /**
     * 修改文档
     */
    @Test
    public void testUpdate() {
        Criteria criteria = Criteria.where("_id").is("6801ead733ba9c4a0d9b6c7b");
        Query query = new Query(criteria);
        Update update = new Update();
        update.set("content", "新的聊天记录列表");

        // 修改或新增
        mongoTemplate.upsert(query, update, ChatMessages.class);
    }

    /**
     * 新增或修改文档
     */
    @Test
    public void testUpdate2() {
        Criteria criteria = Criteria.where("_id").is("100");
        Query query = new Query(criteria);
        Update update = new Update();
        update.set("content", "新的聊天记录列表");

        // 修改或新增
        mongoTemplate.upsert(query, update, ChatMessages.class);
    }

    /**
     * 删除文档
     */
    @Test
    public void testDelete() {
        Criteria criteria = Criteria.where("_id").is("100");
        Query query = new Query(criteria);
        mongoTemplate.remove(query, ChatMessages.class);
    }
}
```

---

## 3. 持久化聊天

### 3.1 优化实体类

为了支持根据会话 `memoryId` 持久化聊天消息，需要对实体类进行调整：

```java
package com.atguigu.java.ai.langchain4j.bean;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Document("chat_messages")
public class ChatMessages {

    // 唯一标识，映射到 MongoDB 文档的 _id 字段
    @Id
    private ObjectId id;

    private int messageId;
    private String content; // 存储当前聊天记录列表的 json 字符串
}
```

### 3.2 创建持久化类

创建一个类，实现 `ChatMemoryStore` 接口：

```java
package com.atguigu.java.ai.langchain4j.store;

@Component
public class MongoChatMemoryStore implements ChatMemoryStore {

    @Autowired
    private MongoTemplate mongoTemplate;

    @Override
    public List<ChatMessage> getMessages(Object memoryId) {
        Criteria criteria = Criteria.where("memoryId").is(memoryId);
        Query query = new Query(criteria);
        ChatMessages chatMessages = mongoTemplate.findOne(query, ChatMessages.class);
        if (chatMessages == null) {
            return new LinkedList<>();
        }
        return ChatMessageDeserializer.messagesFromJson(chatMessages.getContent());
    }

    @Override
    public void updateMessages(Object memoryId, List<ChatMessage> messages) {
        Criteria criteria = Criteria.where("memoryId").is(memoryId);
        Query query = new Query(criteria);

        Update update = new Update();
        update.set("content", ChatMessageSerializer.messagesToJson(messages));

        // 根据 query 条件能查询出文档，则修改；否则新增
        mongoTemplate.upsert(query, update, ChatMessages.class);
    }

    @Override
    public void deleteMessages(Object memoryId) {
        Criteria criteria = Criteria.where("memoryId").is(memoryId);
        Query query = new Query(criteria);
        mongoTemplate.remove(query, ChatMessages.class);
    }
}
```

然后在 `SeparateChatAssistantConfig` 中注入并配置 `MongoChatMemoryStore`：

```java
package com.atguigu.java.ai.langchain4j.config;

@Configuration
public class SeparateChatAssistantConfig {

    // 注入持久化对象
    @Autowired
    private MongoChatMemoryStore mongoChatMemoryStore;

    @Bean
    ChatMemoryProvider chatMemoryProvider() {
        return memoryId -> MessageWindowChatMemory.builder()
                .id(memoryId)
                .maxMessages(10)
                .chatMemoryStore(mongoChatMemoryStore) // 配置持久化对象
                .build();
    }
}
```

## 4. 测试

测试后可以发现，MongoDB 中已经存储了对应的会话记录。

---

# 六、提示词 Prompt

## 1. 系统提示词

`@SystemMessage` 用于设定角色，塑造 AI 助手的专业身份，并明确助手的能力范围。

### 1.1 配置 `@SystemMessage`

可以在 `SeparateChatAssistant` 类的 `chat` 方法上添加 `@SystemMessage` 注解：

```java
@SystemMessage("你是我的好朋友，请用东北话回答问题。")
String chat(@MemoryId int memoryId, @UserMessage String userMessage);
```

`@SystemMessage` 的内容会在后台转换成 `SystemMessage` 对象，并与 `UserMessage` 一起发送给大语言模型（LLM）。

补充说明：

- `SystemMessage` 的内容通常只会发送给模型一次
- 如果你修改了 `SystemMessage` 的内容，新的系统提示词会重新发送给模型
- 此时，之前的聊天记忆通常也会失效

### 1.2 测试

```java
package com.atguigu.java.ai.langchain4j;

@SpringBootTest
public class PromptTest {

    @Autowired
    private SeparateChatAssistant separateChatAssistant;

    @Test
    public void testSystemMessage() {
        String answer = separateChatAssistant.chat(3, "今天几号");
        System.out.println(answer);
    }
}
```

如果希望模型回答中包含“今天的日期”，可以在提示词中增加占位符 `{{current_date}}`：

```java
@SystemMessage("你是我的好朋友，请用东北话回答问题。今天是{{current_date}}")
String chat(@MemoryId int memoryId, @UserMessage String userMessage);
```

### 1.3 从资源中加载提示模板

`@SystemMessage` 还支持从资源文件中加载模板：

```java
@SystemMessage(fromResource = "my-prompt-template.txt")
String chat(@MemoryId int memoryId, @UserMessage String userMessage);
```

`my-prompt-template.txt` 示例：

```text
你是我的好朋友，请用东北话回答问题，回答问题的时候适当添加表情符号。
今天是 {{current_date}}。
```

---

## 2. 用户提示词模板

`@UserMessage` 用于获取用户输入。

### 2.1 配置 `@UserMessage`

可以在 `MemoryChatAssistant` 的 `chat` 方法中添加注解：

```java
@UserMessage("你是我的好朋友，请用上海话回答问题，并且添加一些表情符号。 {{it}}")
String chat(String message);
```

其中：

- `{{it}}` 表示“唯一参数”的占位符

### 2.2 测试

```java
@Autowired
private MemoryChatAssistant memoryChatAssistant;

@Test
public void testUserMessage() {
    String answer = memoryChatAssistant.chat("我是环环");
    System.out.println(answer);
}
```

---

## 3. 指定参数名称

### 3.1 配置 `@V`

`@V` 用于显式指定传递给提示模板的参数名称。

```java
@UserMessage("你是我的好朋友，请用上海话回答问题，并且添加一些表情符号。{{message}}")
String chat(@V("message") String userMessage);
```

### 3.2 多个参数的情况

如果方法参数有两个或以上，就必须使用 `@V`。

例如，在 `SeparateChatAssistant` 中新增方法 `chat2`：

```java
@UserMessage("你是我的好朋友，请用粤语回答问题。{{message}}")
String chat2(@MemoryId int memoryId, @V("message") String userMessage);
```

测试时要注意：`@UserMessage` 中的内容**每次都会与用户问题一起发送给大模型**。

```java
@Test
public void testV() {
    String answer1 = separateChatAssistant.chat2(1, "我是环环");
    System.out.println(answer1);

    String answer2 = separateChatAssistant.chat2(1, "我是谁");
    System.out.println(answer2);
}
```

### 3.3 `@SystemMessage` 和 `@V` 结合使用

也可以把 `@SystemMessage` 和 `@V` 组合起来使用。

在 `SeparateChatAssistant` 中添加方法 `chat3`：

```java
@SystemMessage(fromResource = "my-prompt-template3.txt")
String chat3(
        @MemoryId int memoryId,
        @UserMessage String userMessage,
        @V("username") String username,
        @V("age") int age
);
```

创建提示词模板 `my-prompt-template3.txt`：

```text
你是我的好朋友，我是{{username}}，我的年龄是{{age}}，请用东北话回答问题，回答问题的时候适当添加表情符号。
今天是 {{current_date}}。
```

测试：

```java
@Test
public void testUserInfo() {
    String answer = separateChatAssistant.chat3(1, "我是谁，我多大了", "翠花", 18);
    System.out.println(answer);
}
```

---

# 七、项目实战：创建硅谷小智

这一部分开始实现“硅谷小智”的基础聊天功能，主要包含：

- 聊天记忆
- 聊天记忆持久化
- 提示词模板

## 1. 创建硅谷小智

创建 `XiaozhiAgent`：

```java
package com.atguigu.java.ai.langchain4j.assistant;

import dev.langchain4j.service.*;
import dev.langchain4j.service.spring.AiService;

import static dev.langchain4j.service.spring.AiServiceWiringMode.EXPLICIT;

@AiService(
        wiringMode = EXPLICIT,
        chatModel = "qwenChatModel",
        chatMemoryProvider = "chatMemoryProviderXiaozhi"
)
public interface XiaozhiAgent {

    @SystemMessage(fromResource = "zhaozhi-prompt-template.txt")
    String chat(@MemoryId Long memoryId, @UserMessage String userMessage);
}
```

## 2. 提示词模板

`zhaozhi-prompt-template.txt` 内容整理如下：

```text
你的名字是“硅谷小智”，你是一家名为“北京协和医院”的智能客服。
你是一个训练有素的医疗顾问和医疗伴诊助手。
你态度友好、礼貌且言辞简洁。

1、请仅在用户发起第一次会话时，和用户打个招呼，并介绍你是谁。

2、作为一个训练有素的医疗顾问：
请基于当前临床实践和研究，针对患者提出的特定健康问题，提供详细、准确且实用的医疗建议。
请同时考虑可能的病因、诊断流程、治疗方案以及预防措施，并给出在不同情境下的应对策略。
对于药物治疗，请特别指明适用的药品名称、剂量和疗程。
如果需要进一步检查或就医，也请明确说明。

3、作为医疗伴诊助手，你可以回答用户就医流程中的相关问题，主要包含以下功能：
- AI 分导诊：根据患者病情和就医需求，智能推荐最合适的科室
- AI 挂号助手：智能查询是否有挂号号源服务
- AI 挂号助手：智能预约挂号服务
- AI 挂号助手：智能取消挂号服务

4、你必须遵守以下规则：
在获取挂号预约详情或取消挂号预约之前，你必须确保自己已经知晓以下信息：
- 用户姓名（必选）
- 身份证号（必选）
- 预约科室（必选）
- 预约日期（必选，格式示例：2025-04-14）
- 预约时间（必选，格式：上午 或 下午）
- 预约医生（可选）

当被问到其他领域的咨询时，要表示歉意，并说明你无法在这方面提供帮助。

5、请在回答结果中适当包含一些轻松可爱的图标和表情。

6、今天是 {{current_date}}。
```

## 3. 配置小智助手

主要目标是配置**持久化**和**记忆隔离**：

```java
package com.atguigu.java.ai.langchain4j.config;

@Configuration
public class XiaozhiAgentConfig {

    @Autowired
    private MongoChatMemoryStore mongoChatMemoryStore;

    @Bean
    ChatMemoryProvider chatMemoryProviderXiaozhi() {
        return memoryId -> MessageWindowChatMemory.builder()
                .id(memoryId)
                .maxMessages(20)
                .chatMemoryStore(mongoChatMemoryStore)
                .build();
    }
}
```

## 4. 封装对话对象

```java
package com.atguigu.java.ai.langchain4j.bean;

@Data
public class ChatForm {
    private Long memoryId; // 对话 id
    private String message; // 用户问题
}
```

## 5. 添加 Controller 方法

```java
package com.atguigu.java.ai.langchain4j.controller;

@Tag(name = "硅谷小智")
@RestController
@RequestMapping("/xiaozhi")
public class XiaozhiController {

    @Autowired
    private XiaozhiAgent xiaozhiAgent;

    @Operation(summary = "对话")
    @PostMapping("/chat")
    public String chat(@RequestBody ChatForm chatForm) {
        return xiaozhiAgent.chat(chatForm.getMemoryId(), chatForm.getMessage());
    }
}
```

## 6. 待优化

后续可以继续完善的方向有：

### 6.1 信息查询类能力

提示词中还应补充：

- 医院信息（如位置、营业时间等）
- 科室信息（有哪些科室）
- 医生信息（有哪些医生）

### 6.2 业务能力实现

需要进一步实现：

- 查询预约
- 预约挂号
- 取消预约

### 6.3 技术实现建议

- 信息查询类能力可以使用 **RAG（检索增强生成）**
- 业务操作类能力适合通过 **Function Calling（函数调用）** 实现

---

# 八、Function Calling 函数调用

Function Calling 也常被称为 **Tools（工具调用）**。

## 1. 入门案例

大语言模型本身并不擅长精确数学运算。  
如果你的业务场景中偶尔会涉及数学计算，就可以为模型提供一个“数学工具”，让模型在必要时自行判断是否调用。

### 1.1 创建工具类

使用 `@Tool` 注解的方法：

- 可以是静态方法，也可以是实例方法
- 可以具有任意可见性（`public` / `private` 等）

```java
package com.atguigu.java.ai.langchain4j.tools;

@Component
public class CalculatorTools {

    @Tool
    double sum(double a, double b) {
        System.out.println("调用加法运算");
        return a + b;
    }

    @Tool
    double squareRoot(double x) {
        System.out.println("调用平方根运算");
        return Math.sqrt(x);
    }
}
```

### 1.2 配置工具类

在 `SeparateChatAssistant` 中添加 `tools` 配置：

```java
@AiService(
        wiringMode = EXPLICIT,
        chatModel = "qwenChatModel",
        chatMemoryProvider = "chatMemoryProvider",
        tools = "calculatorTools" // 配置 tools
)
```

### 1.3 测试工具类

```java
package com.atguigu.java.ai.langchain4j;

@SpringBootTest
public class ToolsTest {

    @Autowired
    private SeparateChatAssistant separateChatAssistant;

    @Test
    public void testCalculatorTools() {
        String answer = separateChatAssistant.chat(1, "1+2等于几，475695037565的平方根是多少？");
        // 预期答案：3，689706.4865...
        System.out.println(answer);
    }
}
```

### 1.4 调用流程理解

测试后，可以在持久化消息中看到 `SYSTEM`、`USER`、`AI` 以及 `Tools` 相关消息，从而理解工具调用流程：

```text
Request:
- messages:
  - SystemMessage:
    - text: 系统定义 AI 的角色
  - UserMessage:
    - text: 用户提问
  - AiMessage:
    - toolExecutionRequests:
      - AI 根据提问信息组织参数并请求调用工具方法
  - ToolExecutionResultMessage:
    - text: 工具方法执行结果

Response:
- AiMessage:
  - text: AI 根据工具执行结果再次组织自然语言回复
```

---

## 2. `@Tool` 注解的可选字段

`@Tool` 注解有两个可选字段：

- `name`：工具名称；如果不写，默认使用方法名
- `value`：工具描述信息

虽然一些工具即使没有描述，模型也可能能理解它的用途，例如 `add(a, b)`，但通常仍建议提供**清晰且有意义的名称与描述**，以帮助模型更准确地判断：

- 是否应该调用该工具
- 应该如何组织参数调用该工具

---

## 3. `@P` 注解

方法参数也可以使用 `@P` 注解进行标注。

`@P` 包含两个字段：

- `value`：参数描述，**必填**
- `required`：参数是否必填，默认为 `true`

---

## 4. `@ToolMemoryId`

如果你的 AIService 方法中有一个参数使用了 `@MemoryId` 注解，那么在 `@Tool` 方法中也可以使用 `@ToolMemoryId` 注解接收该值。

这意味着：提供给 AIService 方法的 `memoryId`，可以自动传递给工具方法。  
如果你需要在工具中区分不同用户或不同会话，这会非常有用。

```java
package com.atguigu.java.ai.langchain4j.tools;

public class CalculatorTools {

    @Tool(name = "加法", value = "返回两个参数相加之和")
    double sum(
            @ToolMemoryId int memoryId,
            @P(value = "加数1", required = true) double a,
            @P(value = "加数2", required = true) double b
    ) {
        System.out.println("调用加法运算 " + memoryId);
        return a + b;
    }

    @Tool(name = "平方根", value = "返回给定参数的平方根")
    double squareRoot(@ToolMemoryId int memoryId, double x) {
        System.out.println("调用平方根运算 " + memoryId);
        return Math.sqrt(x);
    }
}
```

---

# 九、项目实战：优化硅谷小智

## 1. 预约业务的实现

这一部分主要实现：

- 查询订单
- 预约订单
- 取消订单

### 1.1 创建 MySQL 数据库表

```sql
CREATE DATABASE `guiguxiaozhi`;
USE `guiguxiaozhi`;

CREATE TABLE `appointment` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(50) NOT NULL,
    `id_card` VARCHAR(18) NOT NULL,
    `department` VARCHAR(50) NOT NULL,
    `date` VARCHAR(10) NOT NULL,
    `time` VARCHAR(10) NOT NULL,
    `doctor_name` VARCHAR(50) DEFAULT NULL,
    PRIMARY KEY (`id`)
);
```

### 1.2 引入依赖

```xml
<!-- Mysql Connector -->
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
</dependency>

<!-- mybatis-plus 持久层 -->
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-spring-boot3-starter</artifactId>
    <version>${mybatis-plus.version}</version>
</dependency>
```

### 1.3 配置数据库连接

`application.properties`：

```properties
# 基本数据源配置
spring.datasource.url=jdbc:mysql://localhost:3306/guiguxiaozhi?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai&useSSL=false
spring.datasource.username=root
spring.datasource.password=123456
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# 开启 SQL 日志打印
mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
```

### 1.4 创建实体类

```java
package com.atguigu.java.ai.langchain4j.entity;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Appointment {

    @TableId(type = IdType.AUTO)
    private Long id;
    private String username;
    private String idCard;
    private String department;
    private String date;
    private String time;
    private String doctorName;
}
```

### 1.5 Mapper

接口：

```java
package com.atguigu.java.ai.langchain4j.mapper;

@Mapper
public interface AppointmentMapper extends BaseMapper<Appointment> {
}
```

`resources/mapper/AppointmentMapper.xml`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.atguigu.java.ai.langchain4j.mapper.AppointmentMapper">
</mapper>
```

### 1.6 Service

接口：

```java
package com.atguigu.java.ai.langchain4j.service;

public interface AppointmentService extends IService<Appointment> {
    Appointment getOne(Appointment appointment);
}
```

实现类：

```java
package com.atguigu.java.ai.langchain4j.service.impl;

@Service
public class AppointmentServiceImpl extends ServiceImpl<AppointmentMapper, Appointment> implements AppointmentService {

    /**
     * 查询订单是否存在
     */
    @Override
    public Appointment getOne(Appointment appointment) {
        LambdaQueryWrapper<Appointment> queryWrapper = new LambdaQueryWrapper<>();
        queryWrapper.eq(Appointment::getUsername, appointment.getUsername());
        queryWrapper.eq(Appointment::getIdCard, appointment.getIdCard());
        queryWrapper.eq(Appointment::getDepartment, appointment.getDepartment());
        queryWrapper.eq(Appointment::getDate, appointment.getDate());
        queryWrapper.eq(Appointment::getTime, appointment.getTime());

        Appointment appointmentDB = baseMapper.selectOne(queryWrapper);
        return appointmentDB;
    }
}
```

### 1.7 创建测试用例

```java
package com.atguigu.java.ai.langchain4j.service;

@SpringBootTest
class AppointmentServiceTest {

    @Autowired
    private AppointmentService appointmentService;

    @Test
    void testGetOne() {
        Appointment appointment = new Appointment();
        appointment.setUsername("张三");
        appointment.setIdCard("123456789012345678");
        appointment.setDepartment("内科");
        appointment.setDate("2025-04-14");
        appointment.setTime("上午");

        Appointment appointmentDB = appointmentService.getOne(appointment);
        System.out.println(appointmentDB);
    }

    @Test
    void testSave() {
        Appointment appointment = new Appointment();
        appointment.setUsername("张三");
        appointment.setIdCard("123456789012345678");
        appointment.setDepartment("内科");
        appointment.setDate("2025-04-14");
        appointment.setTime("上午");
        appointment.setDoctorName("张医生");

        appointmentService.save(appointment);
    }

    @Test
    void testRemoveById() {
        appointmentService.removeById(1L);
    }
}
```

---

## 2. Tools

### 2.1 创建 Tools

```java
package com.atguigu.java.ai.langchain4j.tools;

import com.atguigu.java.ai.langchain4j.entity.Appointment;
import com.atguigu.java.ai.langchain4j.service.AppointmentService;
import dev.langchain4j.agent.tool.P;
import dev.langchain4j.agent.tool.Tool;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class AppointmentTools {

    @Autowired
    private AppointmentService appointmentService;

    @Tool(
            name = "预约挂号",
            value = "根据参数，先执行工具方法 queryDepartment 查询是否可预约，并直接给用户回答是否可预约，并让用户确认所有预约信息，用户确认后再进行预约。"
    )
    public String bookAppointment(Appointment appointment) {
        // 查找数据库中是否包含对应预约记录
        Appointment appointmentDB = appointmentService.getOne(appointment);
        if (appointmentDB == null) {
            appointment.setId(null); // 防止大模型幻觉设置了 id
            if (appointmentService.save(appointment)) {
                return "预约成功，并返回预约详情";
            } else {
                return "预约失败";
            }
        }
        return "您在相同的科室和时间已有预约";
    }

    @Tool(
            name = "取消预约挂号",
            value = "根据参数，查询预约是否存在，如果存在则删除预约记录并返回取消预约成功，否则返回取消预约失败"
    )
    public String cancelAppointment(Appointment appointment) {
        Appointment appointmentDB = appointmentService.getOne(appointment);
        if (appointmentDB != null) {
            if (appointmentService.removeById(appointmentDB.getId())) {
                return "取消预约成功";
            } else {
                return "取消预约失败";
            }
        }
        return "您没有预约记录，请核对预约科室和时间";
    }

    @Tool(name = "查询是否有号源", value = "根据科室名称、日期、时间和医生查询是否有号源，并返回给用户")
    public boolean queryDepartment(
            @P(value = "科室名称") String name,
            @P(value = "日期") String date,
            @P(value = "时间，可选值：上午、下午") String time,
            @P(value = "医生名称", required = false) String doctorName
    ) {
        System.out.println("查询是否有号源");
        System.out.println("科室名称：" + name);
        System.out.println("日期：" + date);
        System.out.println("时间：" + time);
        System.out.println("医生名称：" + doctorName);

        // TODO 维护医生排班信息
        // 1. 未指定医生：根据其他条件查询是否存在可预约医生
        // 2. 指定医生：判断该医生是否排班，以及当前时段是否已约满
        return true;
    }
}
```

### 2.2 配置 Tools

在 `XiaozhiAgent` 中添加 `tools` 配置：

```java
@AiService(
        wiringMode = EXPLICIT,
        chatModel = "qwenChatModel",
        chatMemoryProvider = "chatMemoryProviderXiaozhi",
        tools = "appointmentTools" // tools 配置
)
```

### 2.3 测试

可直接在 Controller 中进行测试。

---

# 十、检索增强生成 RAG

## 1. 如何让大模型回答专业领域知识

LLM 的知识范围受限于训练数据。  
如果你希望它理解某个特定领域的知识或私有数据，通常有三种思路：

- 使用 **RAG**
- 使用你的数据对 LLM 进行**微调**
- 将 **RAG 和微调结合使用**

### 1.1 微调大模型

微调，是在现有大模型基础上，使用小规模的特定任务数据进行二次训练，以便让模型更精准地处理某类任务或领域数据。

**优点：**

- 一次会话通常只需一次模型调用
- 响应速度快
- 在特定任务上的准确性和风格一致性更高

**缺点：**

- 知识更新不及时
- 训练成本较高
- 训练周期较长

**适用场景：**

适合知识库稳定、对生成准确性和风格要求高的场景，例如：

- 文学创作
- 专业文档生成
- 对上下文理解要求较高的专用任务

### 1.2 RAG

RAG，全称 **Retrieval-Augmented Generation（检索增强生成）**。

它的核心思路是：在把原始问题发送给大模型之前，先从外部知识库中检索相关信息，再把“用户问题 + 检索结果”一起交给模型生成答案。

这样，模型就能够借助外部知识库来回答特定领域的问题。

**优点：**

- 数据保存在外部知识库中，可实时更新
- 不依赖重新训练模型
- 成本相对更低

**缺点：**

- 一般需要两步：先查知识库，再查大模型
- 性能通常不如直接微调模型

**适用场景：**

适用于知识规模大且更新频繁的场景，例如：

- 企业客服
- 实时新闻问答
- 法律 / 医疗等需要新知识的领域问答

### 1.3 RAG 常用方法

常见检索方法包括：

1. **全文（关键词）搜索**  
   通过关键词与文档内容进行匹配，并根据频率、相关性排序。

2. **向量搜索（语义搜索）**  
   先通过嵌入模型把文本转成向量，再根据查询向量与文档向量之间的相似度进行检索。

3. **混合搜索**  
   将全文搜索与向量搜索结合，往往能得到更好的检索效果。

---

## 2. 向量搜索 Vector Search

### 2.1 向量 Vectors

可以把向量理解为空间中从一个点移动到另一个点的“方向 + 距离”。

例如：

- 向量 `a`：从 `(100, 50)` 到 `(-50, -50)`
- 向量 `b`：从 `(0, 0)` 到 `(100, -50)`

很多时候，我们更关心从原点出发的表示形式，因此可以把 `b` 简化理解为向量 `(100, -50)`。

进一步的问题是：如何把“文本”这类非数值对象，也表示成向量？

### 2.2 维度 Dimensions

在二维空间中，向量有 `x` 和 `y` 两个坐标；在更高维空间中，则会有 `x、y、z ...` 等更多维度。

这些维度，本质上是描述对象不同特征的坐标轴。

例如，在“交通工具”数据集中，可以定义如下维度：

- 轮子数量
- 是否有发动机
- 是否可以在地上行驶
- 最大乘客数

这样，汽车 `Car` 可以表示为：

```text
(4, yes, yes, 5)
```

若把布尔值映射成数值，也可以写成：

```text
(4, 1, 1, 5)
```

维度越多、特征越细，通常对事物的描述也越精确。

### 2.3 相似度 Similarity

如果用户搜索“轿车 Car”，你希望能够找到与“汽车 automobile”或“车辆 vehicle”语义接近的内容，这就是向量搜索的目标。

但问题在于：**如何定义“最相似”？**

一个向量既有：

- 长度
- 方向

在很多语义检索任务中，方向往往比长度更重要，因此通常不会只看“向量长度”来判断相似度。

### 2.4 相似度测量 Measures of Similarity

常见的向量相似度 / 距离计算方法有：

- 欧几里得距离（Euclidean distance）
- 曼哈顿距离（Manhattan distance）
- 点积（Dot product）
- 余弦相似度（Cosine similarity）

---

## 3. RAG 的过程

RAG 通常包含两个核心阶段：

- 索引阶段
- 检索阶段

### 3.1 索引阶段

在索引阶段，需要对知识库文档进行预处理，以便后续高效检索。

典型流程如下：

```text
加载知识库文档
=> 将文档文本分段
=> 使用向量模型将文本片段转换为向量
=> 将向量写入向量数据库
```

为什么要进行文本分段？

- LLM 的上下文窗口有限，整个知识库无法直接全部塞入
- 输入信息越多，处理时间与成本越高
- 无关信息过多会干扰模型，并增加幻觉概率

因此，通常需要把知识库拆成更小、更清晰、更适合检索的片段。

### 3.2 检索阶段

检索阶段的典型流程如下：

```text
将用户问题转换为向量
=> 在向量数据库中执行相似度匹配
=> 将用户问题与匹配出的相关内容一起交给 LLM 处理
```

---

## 4. 文档加载器 Document Loader

### 4.1 常见文档加载器

常见加载器包括：

- `FileSystemDocumentLoader`：文件系统文档加载器
- `ClassPathDocumentLoader`：类路径文档加载器
- `UrlDocumentLoader`：URL 文档加载器
- `AmazonS3DocumentLoader`：Amazon S3 文档加载器
- `AzureBlobStorageDocumentLoader`：Azure Blob 文档加载器
- `GitHubDocumentLoader`：GitHub 文档加载器
- `GoogleCloudStorageDocumentLoader`：Google Cloud Storage 文档加载器
- `SeleniumDocumentLoader`：Selenium 文档加载器
- `TencentCosDocumentLoader`：腾讯云 COS 文档加载器

### 4.2 测试文档加载

```java
package com.atguigu.java.ai.langchain4j;

@SpringBootTest
public class RAGTest {

    @Test
    public void testReadDocument() {
        // 使用 FileSystemDocumentLoader 读取指定目录下的知识库文档
        // 并使用默认的文档解析器 TextDocumentParser 对文档进行解析
        Document document = FileSystemDocumentLoader.loadDocument("E:/knowledge/测试.txt");
        System.out.println(document.text());
    }
}
```

其他加载方式示例：

```java
// 加载单个文档
Document document = FileSystemDocumentLoader.loadDocument("E:/knowledge/file.txt", new TextDocumentParser());

// 从一个目录中加载所有文档
List<Document> documents = FileSystemDocumentLoader.loadDocuments("E:/knowledge", new TextDocumentParser());

// 从一个目录中加载所有 .txt 文档
PathMatcher pathMatcher = FileSystems.getDefault().getPathMatcher("glob:*.txt");
List<Document> documents = FileSystemDocumentLoader.loadDocuments("E:/knowledge", pathMatcher, new TextDocumentParser());

// 从一个目录及其子目录中递归加载所有文档
List<Document> documents = FileSystemDocumentLoader.loadDocumentsRecursively("E:/knowledge", new TextDocumentParser());
```

---

## 5. 文档解析器 Document Parser

### 5.1 常见文档解析器

文档可以是 PDF、DOC、TXT 等多种格式，因此需要对应的文档解析器。

LangChain4j 中常见的解析器有：

- `TextDocumentParser`：解析纯文本文件，如 `TXT`、`HTML`、`MD`
- `ApachePdfBoxDocumentParser`：解析 `PDF`
- `ApachePoiDocumentParser`：解析 `DOC`、`DOCX`、`PPT`、`PPTX`、`XLS`、`XLSX`
- `ApacheTikaDocumentParser`：自动识别并解析大多数常见文件格式

如果要解析 PDF，原本的 `TextDocumentParser` 就不够用了，需要引入 `langchain4j-document-parser-apache-pdfbox`。

### 5.2 添加依赖

```xml
<!-- 解析 PDF 文档 -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-document-parser-apache-pdfbox</artifactId>
</dependency>
```

### 5.3 解析 PDF 文档

```java
/**
 * 解析 PDF
 */
@Test
public void testParsePDF() {
    Document document = FileSystemDocumentLoader.loadDocument(
            "E:/knowledge/医院信息.pdf",
            new ApachePdfBoxDocumentParser()
    );
    System.out.println(document);
}
```

---

## 6. 文档分割器 Document Splitter

### 6.1 常见文档分割器

LangChain4j 提供了多种现成的 `DocumentSplitter` 实现：

- `DocumentByParagraphSplitter`：按段落分割
- `DocumentByLineSplitter`：按行分割
- `DocumentBySentenceSplitter`：按句子分割
- `DocumentByWordSplitter`：按单词分割
- `DocumentByCharacterSplitter`：按字符分割
- `DocumentByRegexSplitter`：按正则分割
- `DocumentSplitters.recursive(...)`：递归分割

默认情况下，每个文本片段通常不会超过 `300 token`。

### 6.2 测试向量转换和向量存储

Embedding（向量）Store 的意思，可以理解为“嵌入向量存储”。  
它负责存储文本、图像等数据转换后得到的向量，并支持相似度检索。

LangChain4j 支持的向量存储列表：  
<https://docs.langchain4j.dev/integrations/embedding-stores/>

添加依赖：

```xml
<!-- 简单的 RAG 实现 -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-easy-rag</artifactId>
</dependency>
```

测试：

```java
/**
 * 加载文档并存入向量数据库
 */
@Test
public void testReadDocumentAndStore() {
    // 使用 FileSystemDocumentLoader 读取指定目录下的知识库文档
    // 并使用默认文档解析器解析（TextDocumentParser）
    Document document = FileSystemDocumentLoader.loadDocument("E:/knowledge/人工智能.md");

    // 为了简单起见，暂时使用基于内存的向量存储
    InMemoryEmbeddingStore<TextSegment> embeddingStore = new InMemoryEmbeddingStore<>();

    // ingest：
    // 1. 默认使用递归分割器，将文档切分为多个文本片段
    // 2. 使用内置轻量向量模型对文本片段向量化
    // 3. 将原始文本与向量写入 InMemoryEmbeddingStore
    EmbeddingStoreIngestor.ingest(document, embeddingStore);

    // 查看向量数据库内容
    System.out.println(embeddingStore);
}
```

### 6.3 测试文档分割

```java
/**
 * 文档分割
 */
@Test
public void testDocumentSplitter() {
    Document document = FileSystemDocumentLoader.loadDocument("E:/knowledge/人工智能.md");

    InMemoryEmbeddingStore<TextSegment> embeddingStore = new InMemoryEmbeddingStore<>();

    // 自定义文档分割器：按段落分割
    // 每个片段不超过 300 token，重叠 30 token 保证连贯性
    DocumentByParagraphSplitter documentSplitter = new DocumentByParagraphSplitter(
            300,
            30,
            new HuggingFaceTokenizer()
    );

    // 若按字符计算，可使用：
    // DocumentByParagraphSplitter documentSplitter = new DocumentByParagraphSplitter(300, 30);

    EmbeddingStoreIngestor.builder()
            .embeddingStore(embeddingStore)
            .documentSplitter(documentSplitter)
            .build()
            .ingest(document);
}
```

### 6.4 Token 和 Token 计算

参考：

- DeepSeek：`Token 用量计算 | DeepSeek API Docs`
- 阿里百炼：百炼控制台
- LangChain4j：可直接在代码中估算

```java
@Test
public void testTokenCount() {
    String text = "这是一个示例文本，用于测试 token 长度的计算。";
    UserMessage userMessage = UserMessage.userMessage(text);

    // 计算 token 长度
    // QwenTokenizer tokenizer = new QwenTokenizer(System.getenv("DASH_SCOPE_API_KEY"), "qwen-max");
    HuggingFaceTokenizer tokenizer = new HuggingFaceTokenizer();
    int count = tokenizer.estimateTokenCountInMessage(userMessage);
    System.out.println("token长度：" + count);
}
```

### 6.5 工作方式

`DocumentSplitter` 的大致工作流程如下：

1. 实例化一个文档分割器，并指定目标文本片段大小，以及可选的重叠长度（按字符或 token）
2. 分割器先把文档拆成更小单元，例如段落、句子、单词等
3. 再把这些小单元尽量组合成不超过限制的 `TextSegment`
4. 如果某个单元仍然过大，则继续递归调用更细粒度的子分割器
5. 每个 `TextSegment` 会附带唯一元数据，如 `index=0`、`index=1` ...

#### 文本片段最大大小如何选

主要考虑：

1. **模型上下文窗口**  
   片段大小必须小于模型可处理的上下文限制，并预留足够空间给提示词和用户问题。

2. **数据特点**  
   文档信息越复杂，可适当增加片段大小；如果文档结构天然较短小，则可以设得更小。

3. **检索需求**  
   - 追求更精细匹配：可使用更小片段（如 `200 ~ 300 token`）
   - 更注重完整上下文：可使用更大片段（如 `500 ~ 600 token`）

#### 重叠部分大小如何选

主要考虑：

1. **上下文连贯性**  
   文档逻辑联系越紧密，通常越需要适当的重叠。

2. **数据冗余**  
   重叠太大虽然更连贯，但也会带来更多冗余与资源浪费。

3. **模型敏感度**  
   不同模型对上下文依赖程度不同，合适的重叠值需要结合实验调整。

一个常见经验值是：

- 文本片段最大大小：`600 ~ 800 token`
- 重叠部分：`30 ~ 50 token`

当然，最终仍建议根据实际检索效果进行实验调整。

---

# 十一、项目实战：在硅谷小智中实现 RAG

## 1. 创建 `@Bean` 对象

在 `XiaozhiAgentConfig` 中添加 `ContentRetriever`：

```java
@Bean
ContentRetriever contentRetrieverXiaozhi() {
    // 读取知识库文档
    Document document1 = FileSystemDocumentLoader.loadDocument("E:/knowledge/医院信息.md");
    Document document2 = FileSystemDocumentLoader.loadDocument("E:/knowledge/科室信息.md");
    Document document3 = FileSystemDocumentLoader.loadDocument("E:/knowledge/神经内科.md");
    List<Document> documents = Arrays.asList(document1, document2, document3);

    // 使用内存向量存储
    InMemoryEmbeddingStore<TextSegment> embeddingStore = new InMemoryEmbeddingStore<>();

    // 使用默认分割器进行向量化入库
    EmbeddingStoreIngestor.ingest(documents, embeddingStore);

    // 从向量存储中检索与查询相关的内容
    return EmbeddingStoreContentRetriever.from(embeddingStore);
}
```

## 2. 添加配置

在 `XiaozhiAgent` 中增加 `contentRetriever` 配置：

```java
@AiService(
        wiringMode = EXPLICIT,
        chatModel = "qwenChatModel",
        chatMemoryProvider = "chatMemoryProviderXiaozhi",
        tools = "appointmentTools",
        contentRetriever = "contentRetrieverXiaozhi" // 配置向量检索
)
```

## 3. 修改工具的 `value` 提示

可以进一步优化工具描述，让模型在医生姓名缺失时，主动结合向量存储查找合适医生：

```java
@Tool(
    name = "预约挂号",
    value = "根据参数，先执行工具方法queryDepartment查询是否可预约，并直接给用户回答是否可预约，并让用户确认所有预约信息，用户确认后再进行预约。如果用户没有提供具体的医生姓名，请从向量存储中找到一位医生。"
)
```

## 4. 测试 RAG

可直接在 Controller 中进行联调测试。

---

# 十二、向量模型和向量存储

## 1. 向量大模型

### 1.1 介绍

通用文本向量模型参考：  
<https://help.aliyun.com/zh/model-studio/developer-reference/text-embedding-synchronous-api>

阿里百炼中的 `text-embedding-v3`：

- 属于通用文本向量模型
- 维度为 `1024`
- 一般来说，维度越高，对对象描述越细，检索精度也越高

### 1.2 模型配置

使用 `text-embedding-v3` 仍然需要 `langchain4j-community-dashscope` 依赖，而这个依赖在前文已经添加过。

配置示例：

```properties
# 集成阿里通义千问 - 通用文本向量 v3
langchain4j.community.dashscope.embedding-model.api-key=${DASH_SCOPE_API_KEY}
langchain4j.community.dashscope.embedding-model.model-name=text-embedding-v3
```

### 1.3 文本向量化

```java
package com.atguigu.java.ai.langchain4j;

@SpringBootTest
public class EmbeddingTest {

    @Autowired
    private EmbeddingModel embeddingModel;

    @Test
    public void testEmbeddingModel() {
        Response<Embedding> embed = embeddingModel.embed("你好");
        System.out.println("向量维度：" + embed.content().vector().length);
        System.out.println("向量输出：" + embed);
    }
}
```

## 2. 向量存储

### 2.1 Pinecone 简介

前面为了演示简单，我们使用了 `InMemoryEmbeddingStore`。  
但在生产环境中，通常不建议继续使用纯内存向量存储，因此这里使用 Pinecone 作为向量数据库。

Pinecone 官网：  
<https://www.pinecone.io/>

基本使用流程：

- 注册账号
- 登录控制台
- 获取 `apiKey`
- 配置到环境变量中

文中提到，默认可获得约 `2GB` 免费存储空间。

### 2.2 Pinecone 的使用

#### 得分（score）的含义

在向量检索中，查询文本会先转成向量，然后与向量库中的文档向量进行相似度计算。  
这个计算结果就是“得分（score）”。

- 得分越高：说明越相似
- 得分越低：说明相关性越弱

#### 得分的作用

1. **筛选结果**  
   可以通过设置 `minScore` 阈值过滤掉低相关结果，例如 `minScore(0.8)` 表示只保留得分大于等于 `0.8` 的结果。

2. **平衡召回率与准确率**  
   - 阈值低：召回更多，但可能夹杂低质量结果
   - 阈值高：结果更准，但可能漏掉部分相关内容

#### 示例理解

假设知识库里有很多关于水果的文档。  
如果查询“苹果的营养价值”，那么只有和该主题高度相关的文档片段，才应该在较高 `minScore` 阈值下被返回。

### 2.3 集成 Pinecone

参考文档：`Pinecone | LangChain4j`

添加依赖：

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-pinecone</artifactId>
</dependency>
```

### 2.4 配置向量存储对象

```java
package com.atguigu.java.ai.langchain4j.config;

@Configuration
public class EmbeddingStoreConfig {

    @Autowired
    private EmbeddingModel embeddingModel;

    @Bean
    public EmbeddingStore<TextSegment> embeddingStore() {
        // 创建向量存储
        EmbeddingStore<TextSegment> embeddingStore = PineconeEmbeddingStore.builder()
                .apiKey(System.getenv("PINECONE_API_KEY"))
                .index("xiaozhi-index") // 若指定索引不存在，会自动创建
                .nameSpace("xiaozhi-namespace") // 若指定命名空间不存在，也会自动创建
                .createIndex(PineconeServerlessIndexConfig.builder()
                        .cloud("AWS")
                        .region("us-east-1")
                        .dimension(embeddingModel.dimension()) // 向量维度与 embeddingModel 保持一致
                        .build())
                .build();
        return embeddingStore;
    }
}
```

### 2.5 测试向量存储

```java
@Autowired
private EmbeddingStore embeddingStore;

/**
 * 将文本转换成向量，然后存储到 Pinecone 中
 * 参考：https://docs.langchain4j.dev/tutorials/embedding-stores
 */
@Test
public void testPineconeEmbeded() {
    // 将文本转换成向量并写入向量数据库
    TextSegment segment1 = TextSegment.from("我喜欢羽毛球");
    Embedding embedding1 = embeddingModel.embed(segment1).content();
    embeddingStore.add(embedding1, segment1);

    TextSegment segment2 = TextSegment.from("今天天气很好");
    Embedding embedding2 = embeddingModel.embed(segment2).content();
    embeddingStore.add(embedding2, segment2);
}
```

## 3. 相似度匹配

接收用户问题后，可以先把问题向量化，再到 Pinecone 中做相似度搜索，找到最相似的文本片段并返回。

```java
/**
 * Pinecone 相似度匹配
 */
@Test
public void embeddingSearch() {
    // 提问，并将问题转换成向量
    Embedding queryEmbedding = embeddingModel.embed("你最喜欢的运动是什么？").content();

    // 创建搜索请求对象
    EmbeddingSearchRequest searchRequest = EmbeddingSearchRequest.builder()
            .queryEmbedding(queryEmbedding)
            .maxResults(1) // 只取最相似的一条记录
            // .minScore(0.8)
            .build();

    // 根据搜索请求进行相似度搜索
    EmbeddingSearchResult<TextSegment> searchResult = embeddingStore.search(searchRequest);

    // 获取第一条匹配结果
    EmbeddingMatch<TextSegment> embeddingMatch = searchResult.matches().get(0);

    // 输出相似度得分
    System.out.println(embeddingMatch.score());

    // 输出匹配到的文本内容
    System.out.println(embeddingMatch.embedded().text());
}
```

---

# 十三、项目实战：在硅谷小智中整合向量数据库

## 1. 上传知识库到 Pinecone

```java
@Test
public void testUploadKnowledgeLibrary() {
    // 读取知识库文档
    Document document1 = FileSystemDocumentLoader.loadDocument("E:/knowledge/医院信息.md");
    Document document2 = FileSystemDocumentLoader.loadDocument("E:/knowledge/科室信息.md");
    Document document3 = FileSystemDocumentLoader.loadDocument("E:/knowledge/神经内科.md");
    List<Document> documents = Arrays.asList(document1, document2, document3);

    // 文本向量化并写入向量数据库
    EmbeddingStoreIngestor.builder()
            .embeddingStore(embeddingStore)
            .embeddingModel(embeddingModel)
            .build()
            .ingest(documents);
}
```

## 2. 修改 `XiaozhiAgentConfig`

添加基于 Pinecone 的内容检索配置：

```java
@Autowired
private EmbeddingStore embeddingStore;

@Autowired
private EmbeddingModel embeddingModel;

@Bean
ContentRetriever contentRetrieverXiaozhiPincone() {
    return EmbeddingStoreContentRetriever.builder()
            // 设置用于生成嵌入向量的模型
            .embeddingModel(embeddingModel)
            // 指定使用的向量存储
            .embeddingStore(embeddingStore)
            // 最多返回 1 条匹配结果
            .maxResults(1)
            // 最小得分阈值
            .minScore(0.8)
            .build();
}
```

## 3. 修改 `XiaozhiAgent`

把 `contentRetriever` 配置改为 `contentRetrieverXiaozhiPincone`：

```java
@AiService(
        wiringMode = EXPLICIT,
        chatModel = "qwenChatModel",
        chatMemoryProvider = "chatMemoryProviderXiaozhi",
        tools = "appointmentTools",
        contentRetriever = "contentRetrieverXiaozhiPincone"
)
```

---

# 十四、项目实战：改造流式输出

大模型的流式输出，是指模型在生成内容时，不是等到全部结果生成完再一次性返回，而是**生成一部分就立即返回一部分**。

这样做的主要好处是：

- 用户几乎可以立即看到响应开始输出
- 可以显著降低“长时间无反馈”的等待感
- 整体交互体验更好

## 1. 添加依赖

```xml
<!-- 流式输出 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-webflux</artifactId>
</dependency>

<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-reactor</artifactId>
</dependency>
```

## 2. 配置流式输出模型

在 `application.properties` 中配置流式输出模型：

```properties
# 集成阿里通义千问 - 流式输出
langchain4j.community.dashscope.streaming-chat-model.api-key=${DASH_SCOPE_API_KEY}
langchain4j.community.dashscope.streaming-chat-model.model-name=qwen-plus
```

## 3. 编码改造

### 3.1 修改 `XiaozhiAgent`

把原来的 `chatModel` 改为：

- `streamingChatModel = "qwenStreamingChatModel"`

同时，把 `chat` 方法返回值改成 `Flux<String>`：

```java
@AiService(
        wiringMode = EXPLICIT,
        streamingChatModel = "qwenStreamingChatModel",
        chatMemoryProvider = "chatMemoryProviderXiaozhi",
        tools = "appointmentTools",
        contentRetriever = "contentRetrieverXiaozhiPincone"
)
public interface XiaozhiAgent {

    @SystemMessage(fromResource = "zhaozhi-prompt-template.txt")
    Flux<String> chat(@MemoryId Long memoryId, @UserMessage String userMessage);
}
```

### 3.2 修改 `XiaozhiController`

将 `chat` 方法的返回值也改为 `Flux<String>`，并增加 `produces` 属性：

```java
@Operation(summary = "对话")
@PostMapping(value = "/chat", produces = "text/stream;charset=utf-8")
public Flux<String> chat(@RequestBody ChatForm chatForm) {
    return xiaozhiAgent.chat(chatForm.getMemoryId(), chatForm.getMessage());
}
```

## 4. 测试

可在前端或接口调试工具中验证流式输出效果。

---

# 十五、项目实战：运行前端工程

## 1. 安装 Node.js

前端项目在开发环境下通常依赖 Node.js 运行。  
Node.js 本质上是一个基于 JavaScript 引擎的服务端运行环境。

文中示例安装包：

```text
node-v18.17.1-x64.msi
```

## 2. 配置 npm 镜像

打开命令行后，执行以下命令，将依赖下载源切换为阿里镜像：

```bash
npm config set registry https://registry.npmmirror.com
```

## 3. 运行前端项目

进入项目目录后，执行以下命令：

```bash
cd xiaozhi-ui
npm i
npm run dev
```

---

# 全文整理说明

本文档已完成从 Word 到 Markdown 的整体整理，并做了以下处理：

- 去除了正文中可见的“尚硅谷”字样
- 统一了标题层级
- 规范了代码块格式
- 拆分了原始 Word 中粘连的段落
- 优化了列表、说明性文本和章节结构

如果你后面愿意，我还可以继续做两类进一步优化：

1. **精修版排版**：统一术语、修正个别原文错字/重复标题/命名不一致问题
2. **Obsidian 友好版**：补充目录、内部跳转、Callout、美化引用块等
