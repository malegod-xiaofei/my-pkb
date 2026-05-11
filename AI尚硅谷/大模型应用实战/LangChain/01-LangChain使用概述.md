# 1、介绍LangChain
![](images/1777389693211-f37e8b41-1cf6-41f1-8977-94489658be30.png)
## 1.1 什么是LangChain

LangChain是2022年10月，由哈佛大学的Harrison Chase（哈里森·蔡斯）发起研发的一个开源框架，用于开发由大语言模型（LLMs）驱动的应用程序。

比如，搭建“智能体”（Agent）、问答系统（QA）、对话机器人、文档搜索系统、企业私有知识库等。

**LangChain在Github上的热度变化**

![](images/1777389712868-da2d3749-f777-40ba-8971-133cde0a58d0.png)

LangChain在Github上的star


![](images/1777389717667-26b9359f-e920-4bba-b109-2da46d7872df.png)

[https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)

**简单概括**

LangChain ≠ LLMs

LangChain 之于 LLMs，类似 Spring 之于 Java

LangChain 之于 LLMs，类似 Django、Flask 之于 Python

>顾名思义，LangChain中的“Lang”是指language，即⼤语⾔模型，“Chain”即“链”，也就是将⼤模型与外部数据&各种组件连接成链，以此构建AI应⽤程序。

**大模型相关的岗位**

![](images/1777389884233-5186dbb9-d6ee-4bf4-830a-85040d87cdcb.png)

应用开发是大模型最值得关注的方向：应用为王！

学习LangChain框架，高效开发大模型应用

## 1.2 有哪些大模型应用开发框架呢？

截止到2025年7月26日，GitHub统计数据：

![](images/1777389963248-3cf3b227-fc85-4995-825a-92840f66b057.png)

+ LangChain：这些工具里出现最早、最成熟的，适合复杂任务分解和单智能体应用
+ LlamaIndex：专注于高效的索引和检索，适合 RAG 场景。（注意不是Meta开发的）
+ LangChain4J：LangChain还出了Java、JavaScript（LangChain.js）两个语言的版本，LangChain4j的功能略少于LangChain，但是主要的核心功能都是有的
+ SpringAI/SpringAI Alibaba：有待进一步成熟，此外只是简单的对于一些接口进行了封装
+ SemanticKernel：也称为sk，微软推出的，对于C#同学来说，那就是5颗星

## 1.3 为什么需要LangChain？

**问题1：LLM用的好好的，干嘛还需要LangChain？**

在大语言模型（LLM）如 ChatGPT、Claude、DeepSeek 等快速发展的今天，开发者不仅希望能“使用”这些模型，还希望能将它们灵活集成到自己的应用中，实现更强大的对话能力、检索增强生成（RAG）、工具调用（Tool Calling）、多轮推理等功能。

![](images/1777390027000-56d87126-3b56-4d93-b13b-43a4c5068295.png)

LangChain 为更方便解决这些问题，而生的。比如：大模型默认不能联网，如果需要联网，用langchain。

**问题2：我们可以使用GPT 或GLM4 等模型的API进行开发，为何需要LangChain这样的框架？**

不使用LangChain，确实可以使用GPT 或GLM4 等模型的API进行开发。比如，搭建“智能体”（Agent）、问答系统、对话机器人等复杂的 LLM 应用。

但使用LangChain的好处：

+ 简化开发难度：更简单、更高效、效果更好
+ 学习成本更低：不同模型的API不同，调用方式也有区别，切换模型时学习成本高。使用LangChain，可以以统一、规范的方式进行调用，有更好的移植性。
+ 现成的链式组装：LangChain提供了一些现成的链式组装，用于完成特定的高级任务。让复杂的逻辑变得结构化、易组合、易扩展


![](images/1777390068374-3a19de03-6631-4da7-867a-9e769744dbdf.png)

**问题3：LangChain 提供了哪些功能呢？**

LangChain 是一个帮助你构建 LLM 应用的全套工具集。这里涉及到prompt 构建、LLM 接入、记忆管理、工具调用、RAG、智能体开发等模块。

学习 LangChain 最好的⽅式就是做项⽬。

## 1.4 LangChain的使用场景
学完LangChain，如下类型的项目，大家都可以实现：

| 项目名称 | 技术点 | 难度 |
| --- | --- | --- |
| 文档问答助手 | Prompt + Embedding + RetrievalQA | ⭐⭐ |
| 智能日程规划助手 | Agent + Tool + Memory | ⭐⭐⭐ |
| LLM+数据库问答 | SQLDatabaseToolkit + Agent | ⭐⭐⭐⭐ |
| 多模型路由对话系统 | RouterChain + 多 LLM | ⭐⭐⭐⭐ |
| 互联网智能客服 | ConversationChain + RAG +Agent | ⭐⭐⭐⭐⭐ |
| 企业知识库助手（RAG + 本地模型） | VectorDB + LLM + Streamlit | ⭐⭐⭐⭐⭐ |


比如：医院智能助手
![](images/1777390232416-f7a8fdad-4de3-4fb3-a6fc-456e05334fb7.png)

比如：万象知识库
![](images/1777390239275-b7abb900-56e0-4de2-9ba3-7b035f42470a.png)

比如：京东助手


![](images/1777390245066-ba209568-e777-4e9b-85d8-835e13249cb4.png)

LangChain的位置：
![](images/1777390251783-811edb2d-a436-41f2-986e-f2ff60dedf18.png)

## 1.5 LangChain资料介绍

官网地址：[https://www.langchain.com/langchain](https://www.langchain.com/langchain)

官网文档：[https://python.langchain.com/docs/introduction/](https://python.langchain.com/docs/introduction/)

API文档：[https://python.langchain.com/api_reference/](https://python.langchain.com/api_reference/)

github地址：[https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)

## 1.6 架构设计
### 1.6.1 总体架构图
V0.1 版本
![](images/1777390421022-611c4347-2378-4676-b1a6-739803891f72.png)

V0.2 / V0.3 版本


![](images/1777390431972-f29a0590-3c9f-4316-8b0a-af9d90a35613.png)

图中展示了LangChain生态系统的主要组件及其分类，分为三个层次：架构(Architecture)、组件(Components)和部署(Deployment)。

版本的升级，v0.2 相较于v0.1，修改了⼤概10%-15%。功能性上差不多，主要是往稳定性（或兼

容性）、安全性上使劲了，⽀持更多的⼤模型，更安全。

### 1.6.2 内部架构详情

**结构1：LangChain**

**langchain**：构成应用程序认知架构的Chains，Agents，Retrieval strategies等

构成应⽤程序的链、智能体、RAG。

**langchain-community**：第三方集成

⽐如：Model I/O、Retrieval、Tool & Toolkit；合作伙伴包 langchain-openai，langchain-

anthropic等。

**langchain-Core**：基础抽象和LangChain表达式语言 (LCEL)

小结：LangChain，就是AI应用组装套件，封装了一堆的API。langchain框架不大，但是里面琐碎的知识点特别多。就像玩乐高，提供了很多标准化的乐高零件（比如，连接器、轮子等）

**结构2：LangGraph**

LangGraph可以看做基于LangChain的api的进一步封装，能够协调多个Chain、Agent、Tools完成更复杂的任务，实现更高级的功能。

**结构3：LangSmith**

[https://docs.smith.langchain.com/](https://docs.smith.langchain.com/)

**链路追踪**。提供了6大功能，涉及Debugging (调试)、Playground (沙盒)、Prompt Management (提示管理)、Annotation (注释)、Testing (测试)、Monitoring (监控)等。与LangChain无缝集成，帮助你从原型阶段过渡到生产阶段。 

正是因为LangSmith这样的⼯具出现，才使得LangChain意义更⼤，要不仅靠⼀些API（当然也可以不⽤，⽤原⽣的API），⽀持不住LangChain的热度。

**结构4：LangServe**

将LangChain的可运行项和链部署为REST API，使得它们可以通过网络进行调用。

Java怎么调用langchain呢？就通过这个langserve。将langchain应用包装成一个rest api，对外暴露服务。同时，支持更高的并发，稳定性更好。

**总结：LangChain当中，最有前途的两个模块就是：LangGraph，LangSmith。**

LangChain能做RAG，其它的⼀些框架也能做，而且做的也不错，⽐如LlamaIndex。所以这时候LangChain要在Agent这块发⼒，那就需要LangGraph。而LangSmith，做运维、监控。故，⼆者是LangChain⾥最有前途的。

# 2、开发前的准备工作
## 2.1 前置知识
1. Python 基础语法
+ 变量、函数、类、装饰器、上下文管理器 
+ 模块导入、包管理（推荐用 pip 或 conda） 
2. 大语言模型基础
+ 了解什么是 LLM、Token、Prompt、Embedding 
+ OpenAI API 或其他模型提供商，如 Anthropic、阿里云百炼、DeepSeek等
+ 通过浏览器或app使用过大模型（比如：豆包、DeepSeek等）

## 2.2 相关环境安装
1. 安装Python或Anaconda

LangChain基于Python开发，因此需确保系统中安装了Python。

方式1：直接下载Python安装包。推荐版本为Python 3.10及以上

Python官网：[https://www.python.org/](https://www.python.org/)

方式2：使用包管理工具（如Anaconda）进行安装。通过Anaconda可以轻松创建和管理虚拟环境，为项目提供独立的依赖空间，避免不同项目之间的依赖冲突。

具体操作见《[尚硅谷-conda使用指南.md](https://www.yuque.com/zhaoyingfei-ypwo0/ua7kgd/58b15f1ff227b3190c6965ed604f87f5)》

2. 创建虚拟环境

为了保持项目的独立性与环境的干净，建议使用虚拟环境。可以在Anaconda中创建虚拟环境。

具体操作见《[尚硅谷-conda使用指南.md](https://www.yuque.com/zhaoyingfei-ypwo0/ua7kgd/58b15f1ff227b3190c6965ed604f87f5)》

验证Python版本：在激活的虚拟环境中，输入以下命令验证Python版本是否正确：

```plain
python --version
```

3. 如何下载安装包

比如：安装langchain包

**方式1：使用pip指令**

基础指令

```bash
# 安装包（默认最新版）
pip install langchain

# 指定版本
pip install langchain==0.3.7

# 批量安装（空格分隔）
pip install langchain requests numpy

# 升级包
pip install --upgrade langchain

# 卸载包
pip uninstall langchain

# 查看已安装包
pip list
```

高级操作

```bash
# 国内镜像加速 （解决下载慢）  -i：指定镜像源
pip install -i https://mirrors.aliyun.com/pypi/simple/ langchain

# 从本地/URL安装：
pip install ./local_package.whl
pip install https://github.com/user/repo/archive/main.zip
```

**方式2：使用conda指令**

```bash
# 安装包（默认仓库）
conda install langchain

# 指定频道（如 conda-forge）


conda install -c conda-forge langchain==0.3.7

# 更新包
conda update langchain

# 卸载包
conda uninstall langchain

# 查看已安装包
conda list
```

```bash
-c：是--channel的缩写，conda⽤于指定包的安装来源渠道。
conda-forge：该源⽐官⽅默认渠道更新更快、包更全
```

建议：二者最好不好混用，推荐先conda装基础包，后 pip补充的顺序。

```bash
# 检查包来源
conda list   # conda 安装的包显示频道，pip安装的显示 pypi
```


![](images/1777391152999-2bae53eb-9e53-425d-8bc2-bd46364771ca.png)

4. PyCharm开发环境

PyCharm作为专业的Python IDE，具有强大的代码编辑、调试和版本控制功能。


![](images/1777391313258-268fcdea-e6f6-45d0-b868-01ba74ebc991.png)

创建新的工程，并设置Python解释器（选择Anaconda环境）。

```bash
import langchain

print(langchain.__version__)  # 0.3.25
import openai
print(openai.__version__)  # 1.81.0
import sys

#查看python的版本
print(sys.version)  # 3.10.17 | packaged by conda-forge | (main, Apr 10 2025, 22:06:35) [MSC v.1943 64 bit (AMD64)]
```

# 3、大模型应用开发
大模型应用技术特点：门槛低，天花板高。

## 3.1 基于RAG架构的开发
背景：

+ 大模型的知识冻结
+ 大模型幻觉

而RAG就可以非常精准的解决这两个问题。

举例：

LLM在考试的时候面对陌生的领域，答复能力有限，然后就准备放飞自我了。而此时RAG给了一些提示和思路，让LLM懂了开始往这个提示的方向做，最终考试的正确率从60%到了90%！


![](images/1777391368759-245f6b9a-fce8-45ad-9e24-651360e080cf.png)

**何为RAG？**

Retrieval-Augmented Generation（检索增强生成）
![](images/1777391394376-953dec47-6ef0-446a-b05e-c62e5de2a5a7.png)

检索-增强-⽣成过程：检索可以理解为第10步，增强理解为第12步（这⾥的提⽰词包含检索到的数据），⽣成理解为第15步。

类似的细节图：


![](images/1777391594392-864ef91c-8caf-4e9e-810c-3c02ad5956fc.png)

强调一下难点的步骤：
![](images/1777391609260-6073cd28-c7bd-4e97-8e61-4d65024c7698.png)

这些过程中的难点：1、文件解析 2、文件切割  3、知识检索   4、知识重排序

**Reranker的使用场景：**

+ 适合：追求回答高精度和高相关性的场景中特别适合使用 Reranker，例如专业知识库或者客服系统等应用。
+ 不适合：引入reranker会增加召回时间，增加检索延迟。服务对响应时间要求高时，使用reranker可能不合适。

**这里有三个位置涉及到大模型的使用：**

+ 第3步向量化时，需要使用EmbeddingModels。
+ 第7步重排序时，需要使用RerankModels。
+ 第9步生成答案时，需要使用LLM。

## 3.2 基于Agent架构的开发
充分利用 LLM 的推理决策能力，通过增加**规划**、**记忆**和**工具**调用的能力，构造一个能够独立思考、逐步完成给定目标的智能体。

举例：传统的程序 vs Agent（智能体）


![](images/1777391672074-fefd0757-a0b6-4d0e-acff-9bd96add697e.png)

OpenAI的元老翁丽莲(Lilian Weng)于2023年6月在个人博客首次提出了现代AI Agent架构。 
![](images/1777391678152-a0c63b75-ad14-4cc3-952d-d188dbe38bb4.png)
![](images/1777391681538-12156330-c0ee-428e-86a9-3d9ddc3b91d9.png)

一个数学公式来表示：

**Agent = LLM + Memory + Tools + Planning +  Action**

⽐如，打⻋到西藏玩。

+ ⼤脑中枢：规划⾏程的你
+ 规划：步骤1：规划打⻋路线，步骤2：定饭店、酒店，。。。
+ 调⽤⼯具：调⽤MCP或FunctionCalling等API，滴滴打⻋、携程、美团订酒店饭店记忆能⼒：沟通时，要知道上下⽂。⽐如定酒店得知道是西藏路上的酒店，不能聊着聊着忘了最初的⽬的。
+ 能够执⾏上述操作。说走就走，不能纸上谈兵。

智能体核心要素被细化为以下模块：

1. **大模型（LLM）作为“大脑”**：提供推理、规划和知识理解能力，是AI Agent的决策中枢。

⼤脑主要由⼀个⼤型语⾔模型 LLM 组成，承担着信息处理和决策等功能， 并可以呈现推理和规划

的过程，能很好地应对未知任务。

2. **记忆（Memory） **

记忆机制能让智能体在处理重复⼯作时调⽤以前的经验，从而避免⽤⼾进⾏⼤量重复交互。

+ **短期记忆**：存储单次对话周期的上下文信息，属于临时信息存储机制。受限于模型的上下文窗口长度。 
![](images/1777391766839-7cb481a1-ca0d-405d-9b40-34e68e715d7f.png)

ChatGPT：⽀持约8k token的上下⽂

GPT4：⽀持约32k token的上下⽂

最新的很多⼤模型：都⽀持100万、1000万 token的上下⽂ （相当于2000万字⽂本或20小时

视频）

⼀般情况下模型中 token 和字数的换算⽐例⼤致如下：

+ 1 个英⽂字符 ≈ 0.3 个 token。
+ 1 个中⽂字符 ≈ 0.6 个 token。
+ 长期记忆：可以横跨多个任务或时间周期，可存储并调用核心知识，非即时任务。
    - 长期记忆，可以通过模型**参数微调（固化知识）**、**知识图谱（结构化语义网络）**或**向量数据库（相似性检索）**方式实现。
3. 工具使用（Tool Use）：调用外部工具（如API、数据库）扩展能力边界。
![](images/1777391868247-d47103f8-b301-4e75-b573-06a37a10270c.png)
4. 规划决策（Planning）：通过任务分解、反思与自省框架实现复杂任务处理。例如，利用思维链（Chain of Thought）将目标拆解为子任务，并通过反馈优化策略。


![](images/1777391872903-105f987e-1005-4a7c-b2eb-6912668447f3.png)
![](images/1777391895463-d5b235ff-efd7-4812-8ce4-c9915fad5fba.png)

5. 行动（Action）：实际执行决策的模块，涵盖软件接口操作（如自动订票）和物理交互（如机器人执行搬运）。比如：检索、推理、编程等。

智能体会形成完整的计划流程。例如先读取以前⼯作的经验和记忆，之后规划⼦⽬标并使⽤相应⼯

具去处理问题，最后输出给⽤⼾并完成反思。 

## 3.3 大模型应用开发的4个场景
**场景1：纯 Prompt**

Prompt是操作大模型的唯一接口

当人看：你说一句，ta回一句，你再说一句，ta再回一句...

 
![](images/1777391932082-0b263bfe-b9fe-4fc3-bdf0-d8f66b57ea7a.png)

**场景2：Agent + Function Calling**

+ Agent：AI 主动提要求
+ Function Calling：需要对接外部系统时，AI 要求执行某个函数
+ 当人看：你问 ta「我明天去杭州出差，要带伞吗？」，ta 让你先看天气预报，你看了告诉ta，ta 再告诉你要不要带伞


![](images/1777391951697-3e8a53be-32e4-47c3-b742-4d6d7bdee778.png)

**场景3：RAG (Retrieval-Augmented Generation)**

RAG：需要补充领域知识时使用

+ Embeddings：把文字转换为更易于相似度计算的编码。这种编码叫向量
+ 向量数据库：把向量存起来，方便查找
+ 向量搜索：根据输入向量，找到最相似的向量

举例：考试答题时，到书上找相关内容，再结合题目组成答案
![](images/1777392001829-c26d8eac-3cae-4655-97be-6ccc0a9cadb9.png)

这个在智能客服上用的最广泛。

**场景4：Fine-tuning(精调/微调)**

举例：努力学习考试内容，长期记住，活学活用。
![](images/1777392011118-7c9f6ed1-f3a8-4a2d-be6c-3fbba9aed0c8.png)

特点：成本最高；在前面的方式解决不了问题的情况下，再使用。

如何选择

面对一个需求，如何开始，如何选择技术方案？下面是个常用思路：
![](images/1777392029277-e048fef5-fb0d-4edf-b67b-862f4a41c90f.png)

注意：其中最容易被忽略的，是准备测试数据

**下面，我们重点介绍下大模型应用的开发两类：基于RAG的架构，基于Agent的架构。**

# 4、LangChain的核心组件
学习Langchain最简单直接的方法就是阅读官方文档。

[https://python.langchain.com/v0.1/docs/modules/](https://python.langchain.com/v0.1/docs/modules/)

通过文档目录我们可以看到，Langchain构成的核心组件。
![](images/1777392067664-6d347484-ecf2-4ade-b53d-8d6156a966af.png)

两个红框内容是核⼼。中间的Integrations：集成各种⼯具或云平台。

## 4.1 一个问题引发的思考
**如果要组织一个AI应用，开发者一般需要什么？**

第1，提示词模板的构建，不仅仅只包含用户输入。

第2，模型调用与返回，参数设置，返回内容的格式化输出。

第3，知识库查询，这里会包含文档加载，切割，以及转化为词嵌入（Embedding）向量。第4，其他第三方工具调用，一般包含天气查询、Google搜索、一些自定义的接口能力调用。

第5，记忆获取，每一个对话都有上下文，在开启对话之前总得获取到之前的上下文吧？

## 4.2 核心组件的概述
LangChain的核心组件涉及六大模块，这六大模块提供了一个全面且强大的框架，使开发者能够创建复杂、高效且用户友好的基于大模型的应用。
![](images/1777392102535-18c2994f-63b1-4871-893b-985de0ca46af.png)

## 4.3 核心组件的说明
**核心组件1：Model I/O**

这个模块使⽤最多，也最简单

Model I/O：标准化各个大模型的输入和输出，包含输入模版，模型本身和格式化输出。以下是使用语言模型从输入到输出的基本流程。
![](images/1777392116686-5775e808-8d8f-45d8-a93c-f302c4a29566.png)

以下是对每一块的总结：

+ Format(格式化)：即指代Prompts Template，通过模板管理大模型的输入。将原始数据格式化成模型可以处理的形式，插入到一个模板问题中，然后送入模型进行处理。
+ Predict(预测)：即指代Models，使用通用接口调用不同的大语言模型。接受被送进来的问题，然后基于这个问题进行预测或生成回答。
+ Parse(生成)：即指代Output Parser 部分，用来从模型的推理中提取信息，并按照预先设定好的模版来规范化输出。比如，格式化成一个结构化的JSON对象。

**核心组件2：Chains**

Chain："链条"，用于将多个模块串联起来组成一个完整的流程，是 LangChain 框架中最重要的模块。

例如，一个 Chain 可能包括一个 Prompt 模板、一个语言模型和一个输出解析器，它们一起工作以处理用户输入、生成响应并处理输出。

**常见的Chain类型：**

+ LLMChain：最基础的模型调用链 
+ SequentialChain：多个链串联执行 
+ RouterChain：自动分析用户的需求，引导到最适合的链
+ RetrievalQA：结合向量数据库进行问答的链

**核心组件3：Memory**

+ Memory：记忆模块，用于保存对话历史或上下文信息，以便在后续对话中使用。
+ 常见的 Memory 类型：
+ ConversationBufferMemory：保存完整的对话历史
+ ConversationSummaryMemory：保存对话内容的精简摘要（适合长对话） 
+ ConversationSummaryBufferMemory：混合型记忆机制，兼具上面两个类型的特点
+ VectorStoreRetrieverMemory：保存对话历史存储在向量数据库中

**核心组件4：Agents**

Agents，对应着智能体，是 LangChain 的高阶能力，它可以自主选择工具并规划执行步骤。

**Agent 的关键组成：**

+ AgentType：定义决策逻辑的工作流模式
+ Tool：是一些内置的功能模块，如API调用、搜索引擎、文本处理、数据查询等工具。Agents通过这些工具来执行特定的功能。
+ AgentExecutor：用来运行智能体并执行其决策的工具，负责协调智能体的决策和实际的工具执行。

⽬前最热⻔的智能体开发实践，未来能够真正实现通⽤⼈⼯智能的落地⽅案。

这⾥的Agent，就会涉及到前⾯讲的memory，以及tools。

**核心组件5：Retrieval**

Retrieval：对应着RAG，检索外部数据，然后在执行生成步骤时将其传递到 LLM。步骤包括文档加载、切割、Embedding等
![](images/1777392190574-1910a6b3-ab3b-44b8-af1d-ce0de1c8eb3d.png)

+ Source：数据源，即大模型可以识别的多种类型的数据：视频、图片、文本、代码、文档等。
+ Load：负责将来自不同数据源的非结构化数据，加载为文档(Document)对象
+ Transform：负责对加载的文档进行转换和处理，比如将文本拆分为具有语义意义的小块。
+ Embed：将文本编码为向量的能力。一种用于嵌入文档，另一种用于嵌入查询
+ Store：将向量化后的数据进行存储
+ Retrieve：从大规模文本库中检索和查询相关的文本段落

绿⾊的是⼊库存储前的操作。

**核心组件6：Callbacks**

Callbacks：回调机制，允许连接到 LLM 应用程序的各个阶段，可以监控和分析LangChain的运行情况，比如日志记录、监控、流传输等，以优化性能。

回调函数，对于程序员们应该都不陌⽣。这个函数允许我们在LLM的各个阶段使⽤各种各样的“钩⼦”，从而达实现⽇志的记录、监控以及流式传输等功能。

## 4.4 小结
+ Model I/O模块：使用最多，也最简单
+ Chains 模块： 最重要的模块
+ Retrieval模块、Agents模块：大模型的主要落地场景

在这个基础上，其它组件要么是它们的辅助，要么只是完成常规应用程序的任务。

辅助：⽐如，向量数据库的分块和嵌⼊，⽤于追踪、观测的Callbacks

任务：⽐如，Tools，Memory


![](images/1777392227150-268d844e-dbf9-4a17-8151-ce29cca50c33.png)

我们要做的就是⼀个⼀个module去攻破，最后将他们融会贯通，也就成为⼀名合格的LangChain

学习者了。

# 5、LangChain的helloworld
注意：⼤家如果想演⽰如下代码的话，需要准备两个前提：

① 安装必要的库和插件

② 参考后续《02-LangChain使⽤之Model IO》的2.3.2小结，配置好.env配置⽂件

建议：如下的helloworld⼤家看看即可，从下⼀章开始展开讲解

## 5.1 获取大模型
```python
#导入 dotenv 库的 load_dotenv 函数，用于加载环境变量文件（.env）中的配置
import dotenv
from langchain_openai import ChatOpenAI
import os

dotenv.load_dotenv()  #加载当前目录下的 .env 文件

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")


os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

# 创建大模型实例
llm = ChatOpenAI(model="gpt-4o-mini")  # 默认使用 gpt-3.5-turbo

# 直接提供问题，并调用llm
response = llm.invoke("什么是大模型？")
print(response)
```

```plain
content=8⼤模型（Large Model）通常是指在深度学习和机器学习领域中，拥有⼤量参数和复杂结构的模型。这些模型可以处理复杂的数据集，进⾏⾼级的任务，如⾃然语⾔处理、图像识别、⽣成对抗⽹络等。以下是⼀些关于⼤模型的关键点：\n\n1. 参数量：⼤模型通常具备数亿甚⾄数千亿个参数，这使得它们能够学习到更加丰富的特征和关系。\n\n2. 计算需求：由于其庞⼤的规模，⼤模型通常需要⾼性能的计算资源，例如GPU或TPU，以及⻓时间的训练过程。\n\n3. 数据需求：训练⼤模型通常需要⼤量的数据，以确保模型能够在各种情况下进⾏有效的学习和泛化。\n\n4. 应⽤⼴泛：⼤模型在许多领域都有应⽤，包括语⾔模型（如GPT-3、BERT等）、图像处理（如卷积神经⽹络）以及⽣成模型（如GAN）。\n\n5. 转移学习：许多⼤模型允许通过转移学习的⽅式进⾏微调，使得它们能够在特定任务上表现良好，而⽆需从头开始训练。\n\n⼤模型的出现⼤⼤推动了⼈⼯智能的发展，使得许多复杂的任务变得可⾏，并且在多个领域取得了显著的成果。' additional_kwargs={8refusal8: None} response_metadata={8token_usage8: 
{8completion_tokens8: 289, 8prompt_tokens8: 12, 8total_tokens8: 301, 
8completion_tokens_details8: {8accepted_prediction_tokens8: 0, 8audio_tokens8: 0, 
8reasoning_tokens8: 0, 8rejected_prediction_tokens8: 0}, 8prompt_tokens_details8: {8audio_tokens8: 0, 8cached_tokens8: 0}}, 8model_name8: 8gpt-4o-mini-2024-07-188, 
8system_fingerprint8: 8fp_efad92c60b8, 8id8: 8chatcmpl-BxO81Kq8FpSQgLyTikWfGzOlry2MF8, 
8service_tier8: None, 8finish_reason8: 8stop8, 8logprobs8: None} id=8run--134748c7-8c54-4784-8781-6ea143086285-08 usage_metadata={8input_tokens8: 12, 8output_tokens8: 289, 
8total_tokens8: 301, 8input_token_details8: {8audio8: 0, 8cache_read8: 0}, 
8output_token_details8: {8audio8: 0, 8reasoning8: 0}}
```

其中，需要在当前工程下提供.env文件，文件中提供如下信息：

```plain
OPENAI_API_KEY1="sk-cvUm8OddQbly.............AGgIHTm9kMH7Bf226G2"  #你自己的密钥
OPENAI_BASE_URL="https://api.openai-proxy.org/v1"                  #url是固定值，统一写成这样
```

密钥来自于：[https://www.closeai-asia.com/](https://www.closeai-asia.com/)

## 5.2 使用提示词模板
我们也可以创建prompt template, 并引入一些变量到prompt template中，这样在应用的时候更加灵活。

```python
from langchain_core.prompts import ChatPromptTemplate

# 需要注意的一点是，这里需要指明具体的role，在这里是system和用户
prompt = ChatPromptTemplate.from_messages([
("system", "你是世界级的技术文档编写者"),
("user", "{input}")  # {input}为变量
])

# 我们可以把prompt和具体llm的调用和在一起。
chain = prompt | llm 
message = chain.invoke({"input": "大模型中的LangChain是什么?"}) 12 	print(message)

# print(type(message))
```

```python
LangChain是一个开源框架，旨在简化和增强大语言模型（如GPT-3、GPT-4 等）的开发与应用。它为开发者提供了一套工具和组件，使得在不同的用例中利用语言模型变得更加高效和灵活。LangChain 的全名是“Language Chain”，意在强调它将多个处理步骤或组件串联在一起，形成一个完整的处理链，以便更好地利用语言模型的能力。

### LangChain 的主要特性包括：

1. **组件化设计**：LangChain 提供了高度模块化的组件，允许开发者根据需要组合和扩展不同	的功能，比如文本生成、数据提取、工具调用等。

2. **链式调用**：可以将多个操作串联在一起，例如先生成文本，然后对生成的内容进行解析或处	理，使得工作流程更加流畅。

3. **多种后端支持**：LangChain 支持多种语言模型和生成后端，方便开发者在不同的平台和环	境下进行开发。

4. **集成外部工具**：LangChain 允许与外部API、数据库和其他工具集成，使得模型可以利用外	部数据源和功能，增强其智能性和实用性。

5. **可扩展性**：开发者可以通过自定义组件和方法，扩展 LangChain 的功能，以适应特定的业	务需求。

### 应用场景：

- **对话系统**：构建更智能的聊天机器人，能够理解上下文并进行多轮对话。
- **内容生成**：生成文章、故事、产品描述等多种内容，并对其进行编辑和优化。
- **数据提取和处理**：从大量文本中提取关键信息，并将其结构化。
- **知识库查询**：结合语言模型与知识库，提供深度的知识查询和推荐。

总之，LangChain 作为大模型应用的一个助手工具，提升了开发者的生产力，使得他们可以更专	注于构建创新的应用，而不是陷入底层实现的复杂性中。



# <class 'langchain_core.messages.ai.AIMessage'>
```

## 5.3 使用输出解析器
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser 4
# 初始化模型
llm = ChatOpenAI(model="gpt-4o-mini")

# 创建提示模板
prompt = ChatPromptTemplate.from_messages([
 ("system", "你是世界级的技术文档编写者。"),
 ("user", "{input}")
])

# 使用输出解析器
# output_parser = StrOutputParser()
output_parser = JsonOutputParser()

# 将其添加到上一个链中
# chain = prompt | llm
chain = prompt | llm | output_parser

# 调用它并提出同样的问题。答案是一个字符串，而不是ChatMessage
# chain.invoke({"input": "LangChain是什么?"}) 
chain.invoke({"input": "LangChain是什么? 用JSON格式回复，问题用question，回答用answer"})
```

```python
{8question8: 8LangChain是什么?',
8answer8: 8LangChain是⼀个开源框架，⽤于构建与⼤型语⾔模型（LLMs）交互的应⽤程序。它
提供了⼀个灵活的⼯具集，允许开发⼈员创建具有复杂推理能⼒、链式任务处理和上下⽂管理的智
能应⽤。LangChain⽀持多种数据源和组件，可以帮助开发者在各种环境中更⾼效地利⽤语⾔模
型。'}
```

或

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
# 初始化模型
llm = ChatOpenAI(model="gpt-4o-mini")

# 创建提示模板
prompt = ChatPromptTemplate.from_messages([ 
 ("system", "你是世界级的技术文档编写者。输出格式要求：{format_instructions}"),
  ("user", "{input}")
])

# 使用输出解析器


# output_parser = StrOutputParser()
output_parser = JsonOutputParser()

# 将其添加到上一个链中
# chain = prompt | llm
chain = prompt | llm | output_parser

# 调用它并提出同样的问题。答案是一个字符串，而不是ChatMessage
# chain.invoke({"input": "LangChain是什么?"})
chain.invoke({"input": "LangChain是什么? ","format_instructions":output_parser.get_format_instructions()})
```

```python
{8LangChain8: {8description8: 8LangChain是⼀个开源的框架，⽤于构建基于语⾔模型的应⽤程
序。它旨在将不同的语⾔模型、数据源和⼯具结合起来，以便于开发者创建复杂的应⽤。',
8key_features8: ['模块化设计：⽀持将不同的组件组合在⼀起，如语⾔模型、数据处理和外部
API。',
'⽀持多种语⾔模型：兼容不同类型的语⾔模型，如OpenAI的GPT系列、BERT等。',
'内置数据连接：可以与多种数据源进⾏集成，例如数据库、⽂件和外部API。',
'灵活的⼯作流管理：提供了多种⽅法来定义和管理任务的执⾏流程。',
'社区⽀持：拥有活跃的社区，提供⽂档、⽰例和⽀持。',
'可扩展性：允许开发者根据需求定制和扩展功能。'],
8use_cases8: ['聊天机器⼈开发', '⽂本⽣成和摘要', '内容推荐系统', '⾃然语⾔理解任务', '⾃动化⼯作流处理'],
8getting_started8: {8installation8: '使⽤pip安装：pip install langchain8,
8documentation_link8: 'https://langchain.readthedocs.io/en/latest/'}}}
```

## 5.4 使用向量存储
使用一个简单的本地向量存储 FAISS，首先需要安装它

```python
pip install faiss-cpu
#或者
conda install faiss-cpu
pip install langchain_community==0.3.7
#或者
conda install langchain_community==0.3.7
# 导入和使用 WebBaseLoader
from langchain_community.document_loaders import WebBaseLoader
import bs4

loader = WebBaseLoader( 
 web_path="https://www.gov.cn/xinwen/2020-06/01/content_5516649.htm", 
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(id="UCAP-CONTENT"))
    )
docs = loader.load()
# print(docs)

# 对于嵌入模型，这里通过 API调用


from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002") 16

from langchain_community.vectorstores import FAISS 
from langchain_text_splitters import RecursiveCharacterTextSplitter 20
# 使用分割器分割文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.split_documents(docs)
print(len(documents)) 
# 向量存储  embeddings 会将 documents 中的每个文本片段转换为向量，并将这些向量存储在 FAISS 
向量数据库中
vector = FAISS.from_documents(documents, embeddings)
248
```

## 5.5 RAG(检索增强生成)
基于外部知识，增强大模型回复

```python
from langchain_core.prompts import PromptTemplate

retriever = vector.as_retriever()
retriever.search_kwargs = {"k": 3}
docs = retriever.invoke("建设用地使用权是什么？")

# for i,doc in enumerate(docs):
#     print(f"⭐第{i+1}条规定：")
#     print(doc)





# 6.定义提示词模版
prompt_template = """
你是一个问答机器人。
你的任务是根据下述给定的已知信息回答用户问题。
确保你的回复完全依据下述已知信息。不要编造答案。
如果下述已知信息不足以回答用户的问题，请直接回复"我无法回答您的问题"。

已知信息:
{info}


用户问：
{question}




请用中文回答用户问题。
"""
# 7.得到提示词模版对象
template = PromptTemplate.from_template(prompt_template)

# 8.得到提示词对象
prompt = template.format(info=docs, question='建设用地使用权是什么？')

## 9. 调用LLM
response = llm.invoke(prompt)
print(response.content)
```

建设⽤地使⽤权是指在法律规定的范围内，建设⽤地使⽤权⼈对特定⼟地的使⽤、建造建筑物及其

他设施的权利。根据相关法律规定，建设⽤地使⽤权可以通过出让或划拨等⽅式设⽴，并应当符合

资源节约、⽣态环境保护及⼟地⽤途的规定。建设⽤地使⽤权⼈有权转让、出资、赠与或抵押其使

⽤权，但需遵循法律规定和合同约定。

## 5.6 使用Agent
```python
from langchain.tools.retriever import create_retriever_tool

# 检索器工具
retriever_tool = create_retriever_tool(
 retriever,
 "CivilCodeRetriever", 
 "搜索有关中华人民共和国民法典的信息。关于中华人民共和国民法典的任何问题，您必须使用此工	具!",
)

tools = [retriever_tool]

from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

# https://smith.langchain.com/hub
prompt = hub.pull("hwchase17/openai-functions-agent")

agent = create_openai_functions_agent(llm, tools, prompt) 
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) 21
# 运行代理
agent_executor.invoke({"input": "建设用地使用权是什么"})
```

```python
> Entering new AgentExecutor chain...

Invoking: `CivilCodeRetriever` with `{'query': '建设用地使用权'}`


> Entering new AgentExecutor chain...

Invoking: `CivilCodeRetriever` with `{'query': '建设用地使用权'}`


第三百四十五条 建设用地使用权可以在土地的地表、地上或者地下分别设立。
第三百四十六条 设立建设用地使用权，应当符合节约资源、保护生态环境的要求，遵守法律、	行政法规关于土地用途的规定，不得损害已经设立的用益物权。
第三百四十七条 设立建设用地使用权，可以采取出让或者划拨等方式。

工业、商业、旅游、娱乐和商品住宅等经营性用地以及同一土地有两个以上意向用地者的，应当采取招标、拍卖等公开竞价的方式出让。
严格限制以划拨方式设立建设用地使用权。
第三百四十八条 通过招标、拍卖、协议等出让方式设立建设用地使用权的，当事人应当采用书	面形式订立建设用地使用权出让合同。
建设用地使用权出让合同一般包括下列条款：
（一）当事人的名称和住所；
（二）土地界址、面积等；
（三）建筑物、构筑物及其附属设施占用的空间；
（四）土地用途、规划条件；
（五）建设用地使用权期限；
（六）出让金等费用及其支付方式；
（七）解决争议的方法。
第三百四十九条 设立建设用地使用权的，应当向登记机构申请建设用地使用权登记。建设用地	使用权自登记时设立。登记机构应当向建设用地使用权人发放权属证书。

第三百五十条 建设用地使用权人应当合理利用土地，不得改变土地用途；需要改变土地用途	的，应当依法经有关行政主管部门批准。
第三百五十一条 建设用地使用权人应当依照法律规定以及合同约定支付出让金等费用。29	第三百五十二条 建设用地使用权人建造的建筑物、构筑物及其附属设施的所有权属于建设用地	使用权人，但是有相反证据证明的除外。
第三百五十三条 建设用地使用权人有权将建设用地使用权转让、互换、出资、赠与或者抵押，	但是法律另有规定的除外。
第三百五十四条 建设用地使用权转让、互换、出资、赠与或者抵押的，当事人应当采用书面形	式订立相应的合同。使用期限由当事人约定，但是不得超过建设用地使用权的剩余期限。
第三百五十五条 建设用地使用权转让、互换、出资或者赠与的，应当向登记机构申请变更登	记。
第三百五十六条 建设用地使用权转让、互换、出资或者赠与的，附着于该土地上的建筑物、构	筑物及其附属设施一并处分。
第三百五十七条 建筑物、构筑物及其附属设施转让、互换、出资或者赠与的，该建筑物、构筑	物及其附属设施占用范围内的建设用地使用权一并处分。

第三百五十八条 建设用地使用权期限届满前，因公共利益需要提前收回该土地的，应当依据本	法第二百四十三条的规定对该土地上的房屋以及其他不动产给予补偿，并退还相应的出让金。
第三百五十九条 住宅建设用地使用权期限届满的，自动续期。续期费用的缴纳或者减免，依照	法律、行政法规的规定办理。
非住宅建设用地使用权期限届满后的续期，依照法律规定办理。该土地上的房屋以及其他不动产	的归属，有约定的，按照约定；没有约定或者约定不明确的，依照法律、行政法规的规定办理。39	第三百六十条 建设用地使用权消灭的，出让人应当及时办理注销登记。登记机构应当收回权属	证书。
第三百六十一条 集体所有的土地作为建设用地的，应当依照土地管理的法律规定办理。
第十三章 宅基地使用权
第三百六十二条 宅基地使用权人依法对集体所有的土地享有占有和使用的权利，有权依法利用	该土地建造住宅及其附属设施。
第三百六十三条 宅基地使用权的取得、行使和转让，适用土地管理的法律和国家有关规定。
> Entering new AgentExecutor chain...

Invoking: `CivilCodeRetriever` with `{'query': '建设用地使用权'}`


第三百四十五条 建设用地使用权可以在土地的地表、地上或者地下分别设立。
第三百四十六条 设立建设用地使用权，应当符合节约资源、保护生态环境的要求，遵守法律、	行政法规关于土地用途的规定，不得损害已经设立的用益物权。
第三百四十七条 设立建设用地使用权，可以采取出让或者划拨等方式。
 


工业、商业、旅游、娱乐和商品住宅等经营性用地以及同一土地有两个以上意向用地者的，应当采取招标、拍卖等公开竞价的方式出让。
严格限制以划拨方式设立建设用地使用权。
第三百四十八条 通过招标、拍卖、协议等出让方式设立建设用地使用权的，当事人应当采用书	面形式订立建设用地使用权出让合同。
建设用地使用权出让合同一般包括下列条款：
（一）当事人的名称和住所；
（二）土地界址、面积等；
（三）建筑物、构筑物及其附属设施占用的空间；
（四）土地用途、规划条件；
（五）建设用地使用权期限；
（六）出让金等费用及其支付方式；
（七）解决争议的方法。
第三百四十九条 设立建设用地使用权的，应当向登记机构申请建设用地使用权登记。建设用地	使用权自登记时设立。登记机构应当向建设用地使用权人发放权属证书。

第三百五十条 建设用地使用权人应当合理利用土地，不得改变土地用途；需要改变土地用途	的，应当依法经有关行政主管部门批准。
第三百五十一条 建设用地使用权人应当依照法律规定以及合同约定支付出让金等费用。67	第三百五十二条 建设用地使用权人建造的建筑物、构筑物及其附属设施的所有权属于建设用地	使用权人，但是有相反证据证明的除外。
第三百五十三条 建设用地使用权人有权将建设用地使用权转让、互换、出资、赠与或者抵押，	但是法律另有规定的除外。
第三百五十四条 建设用地使用权转让、互换、出资、赠与或者抵押的，当事人应当采用书面形	式订立相应的合同。使用期限由当事人约定，但是不得超过建设用地使用权的剩余期限。
第三百五十五条 建设用地使用权转让、互换、出资或者赠与的，应当向登记机构申请变更登	记。
第三百五十六条 建设用地使用权转让、互换、出资或者赠与的，附着于该土地上的建筑物、构	筑物及其附属设施一并处分。
第三百五十七条 建筑物、构筑物及其附属设施转让、互换、出资或者赠与的，该建筑物、构筑	物及其附属设施占用范围内的建设用地使用权一并处分。

第三百五十八条 建设用地使用权期限届满前，因公共利益需要提前收回该土地的，应当依据本	法第二百四十三条的规定对该土地上的房屋以及其他不动产给予补偿，并退还相应的出让金。75	第三百五十九条 住宅建设用地使用权期限届满的，自动续期。续期费用的缴纳或者减免，依照	法律、行政法规的规定办理。
非住宅建设用地使用权期限届满后的续期，依照法律规定办理。该土地上的房屋以及其他不动产	的归属，有约定的，按照约定；没有约定或者约定不明确的，依照法律、行政法规的规定办理。77	第三百六十条 建设用地使用权消灭的，出让人应当及时办理注销登记。登记机构应当收回权属	证书。
第三百六十一条 集体所有的土地作为建设用地的，应当依照土地管理的法律规定办理。
第十三章 宅基地使用权
第三百六十二条 宅基地使用权人依法对集体所有的土地享有占有和使用的权利，有权依法利用	该土地建造住宅及其附属设施。
第三百六十三条 宅基地使用权的取得、行使和转让，适用土地管理的法律和国家有关规定。82	第三百六十四条 宅基地因自然灾害等原因灭失的，宅基地使用权消灭。对失去宅基地的村民，	应当依法重新分配宅基地。建设用地使用权是指在中华人民共和国法律框架下，个人或单位依法	享有的对特定建设用地进行开发、建设和利用的权利。

根据《中华人民共和国民法典》，建设用地使用权的相关规定主要包括以下几个方面：

1. **设立与形式**：建设用地使用权可以通过出让或划拨等方式设立，通常需要通过招标、拍卖等	公开方式进行。

 

2. **合同与登记**：设立建设用地使用权时，需要书面订立相关合同，并向登记机构申请登记。只有登记后，建设用地使用权才正式成立，并会获得权属证书。

3. **权利与义务**：建设用地使用权人有权合理利用土地，但不得随意改变土地用途，任何用途的	改变都需获得相关主管部门的批准。此外，建设用地使用权人应按照合同约定支付出让金等费	用。

4. **转让与变更**：建设用地使用权可以进行转让、互换、出资、赠与或抵押，但必须遵循法律规	定，并进行相应的登记。

5. **期满续期**：住宅建设用地使用权在期满后会自动续期，而非住宅建设用地的续期需依照法律	规定办理。

这些规定旨在确保土地资源的合理利用与保护，同时维护用地权利人的合法权益。

> Finished chain.
{'input': '建设用地使用权是什么', 
 'output': '建设用地使用权是指在中华人民共和国法律框架下，个人或单位依法享有的对特定建设	用地进行开发、建设和利用的权利。\n\n根据《中华人民共和国民法典》，建设用地使用权的相关	规定主要包括以下几个方面：\n\n1. **设立与形式**：建设用地使用权可以通过出让或划拨等方式	设立，通常需要通过招标、拍卖等公开方式进行。\n\n2. **合同与登记**：设立建设用地使用权	时，需要书面订立相关合同，并向登记机构申请登记。只有登记后，建设用地使用权才正式成立，	并会获得权属证书。\n\n3. **权利与义务**：建设用地使用权人有权合理利用土地，但不得随意改	变土地用途，任何用途的改变都需获得相关主管部门的批准。此外，建设用地使用权人应按照合同	约定支付出让金等费用。\n\n4. **转让与变更**：建设用地使用权可以进行转让、互换、出资、赠	与或抵押，但必须遵循法律规定，并进行相应的登记。\n\n5. **期满续期**：住宅建设用地使用权	在期满后会自动续期，而非住宅建设用地的续期需依照法律规定办理。\n\n这些规定旨在确保土地	资源的合理利用与保护，同时维护用地权利人的合法权益。'}

```

