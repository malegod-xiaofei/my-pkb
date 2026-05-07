# 第2课：LangChain使用之Model I/O

## 1. Model I/O 介绍

Model I/O 模块是与语言模型（LLMs）进行交互的核心组件，在整个框架中有着很重要的地位。

所谓的 Model I/O，包括输入提示（Format）、调用模型（Predict）、输出解析（Parse），分别对应着：
- **Prompt Template**
- **Model**
- **Output Parser**

简单来说，就是输入、模型处理、输出这三个步骤。

![](<images/Pasted image 20260507155753.png>)
针对每个环节，LangChain 都提供了模板和工具，可以快捷的调用各种语言模型的接口。

---

## 2. Model I/O 之调用模型

LangChain 作为一个"工具"，不提供任何 LLMs，而是依赖于第三方集成各种大模型。比如，将 OpenAI、Anthropic、Hugging Face、LLaMA、阿里 Qwen、ChatGLM 等平台的模型无缝接入到你的应用。

### 2.1 模型的不同分类方式

>简单来说，就是谁家的 API 以什么方式调用哪种类型的模型。

#### 角度1：按照模型功能的不同

- **非对话模型（LLMs、Text Model）**
- **对话模型（Chat Models）**（推荐）
- **嵌入模型（Embedding Models）**（暂不考虑）

#### 角度2：模型调用时，几个重要参数的书写位置的不同

- 硬编码：写在代码文件中
- 使用环境变量
- **使用配置文件**（推荐）

#### 角度3：具体调用的 API

- OpenAI 提供的 API
- 其他大模型自家提供的 API
- **LangChain 的统一方式调用 API**（推荐）

> **背景小知识：**
> OpenAI 的 GPT 系列模型影响了整个模型技术发展的开发范式和标准。所以无论是 Qwen、ChatGLM 等模型，它们的使用语法和函数调用逻辑基本遵循 OpenAI 定义的规范，没有太大差异。这就使得部分开源项目能够通过一个较为通用的接口来接入和使用不同的模型。

### 2.2 角度1出发：按照功能不同举例

#### 类型1：LLMs（非对话模型）

LLMs，也叫 Text Model、非对话模型，是许多语言模型应用程序的支柱。主要特点如下：

- **输入**：接受文本字符串或 PromptValue 对象
- **输出**：总是返回文本字符串
![](<images/Pasted image 20260507162950.png>)
- **适用场景**：仅需单次文本生成任务（如摘要生成、翻译、代码生成、单次问答）或接入不支持消息结构的旧模型（如部分本地部署模型）（言外之意，优先推荐 ChatModel）
- **局限性**：不支持多轮对话上下文。每次调用独立处理输入，无法自动关联历史对话（需手动拼接历史文本）；无法处理角色分工或复杂多轮对话逻辑。

**举例：**

```python
import os
import dotenv
from langchain_openai import OpenAI

dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY1")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")

###########核心代码############
llm = OpenAI()
str = llm.invoke("写一首关于春天的诗")  # 直接输入字符串
print(str)
```

**输出示例：**
```
是那拂过大地
万物复苏欣欣向荣
花开满树……
是那温阳暖
他们情也随之划
春天来了
带来新的开始
带走冬天的寒冬
带来机遇与希望
春天啊，美丽的季节
让我们开起舞步
迎接春天的到来
让快乐永远驻留……
```

#### 类型2：Chat Models（对话模型）

ChatModels，也叫聊天模型、对话模型，底层使用 LLMs。

**大言语模型调用，以 ChatModel 为主。**

主要特点如下：

- **输入**：接收消息列表 `List[BaseMessage]` 或 PromptValue，每条消息需指定角色（如 SystemMessage、HumanMessage、AIMessage）
- **输出**：总是返回带角色的消息对象（BaseMessage 子类），通常是 AIMessage
![](<images/Pasted image 20260507163050.png>)
- 原生支持多轮对话。通过消息列表维护上下文（例如：`[SystemMessage, HumanMessage, AIMessage, ...]`），模型可基于完整对话历史生成回复。
- **适用场景**：对话系统（如客服机器人、长期交互的 AI 助手）

**举例：**

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os
import dotenv

dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY1")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")

########核心代码############
chat_model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(content="我是人工智能助手，我叫小智"),
    HumanMessage(content="你好，我是小明，很高兴认识你")
]
response = chat_model.invoke(messages)  # 输入消息列表

print(type(response))  # <class 'langchain_core.messages.ai.AIMessage'>
print(response.content)
```

**输出示例：**
```
<class 'langchain_core.messages.ai.AIMessage'>
你好，小明！很高兴认识你，有什么我可以帮你的吗？
```

#### 类型3：Embedding Model（嵌入模型）

Embedding Model：也叫文本嵌入模型，这些模型将文本作为输入并返回浮点数列表，也就是 Embedding。（后面章节《07-LangChain使用之Retrieval》重点讲）
![](<images/Pasted image 20260507163107.png>)

```python
import os
import dotenv
from langchain_openai import OpenAIEmbeddings

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

#############
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

res1 = embeddings_model.embed_query('我是文档中的数据')
print(res1)
# 打印结果：[-0.004306625574827194, 0.003083756659179926, -0.013916781172156334, ....]
```

### 2.3 角度2出发：参数位置不同举例

这里以 LangChain 的 API 为准，使用对话模型，进行测试。

#### 2.3.1 模型调用的主要方法及参数

**相关方法及属性：**
- `OpenAI(...) / ChatOpenAI(...)`：创建一个模型对象（非对话类/对话类）
- `model.invoke(xxx)`：执行调用，将用户输入发送给模型
- `.content`：提取模型返回的实际文本内容

**模型调用函数使用时需初始化模型，并设置必要的参数。**

**1）必须设置的参数：**
- `base_url`：大模型 API 服务的根地址
- `api_key`：用于身份验证的密钥，由大模型服务商（如 OpenAI、百度千帆）提供
- `model/model_name`：指定要调用的具体大模型名称（如 gpt-4-turbo、ERNIE-3.5-8K 等）

**2）其他参数：**
- `temperature`：温度，控制生成文本的"随机性"，取值范围为 0~2。
  - 值越低 → 输出越确定、保守（适合事实回答）
  - 值越高 → 输出越多样、有创意（适合创意写作）
  - 通常，根据需要设置下：
    - 精确模式（0.5或更低）：生成的文本更加安全可靠，但可能缺乏创意和多样性。
    - 平衡模式（通常是0.8）：生成的文本通常既有一定的多样性，又能保持较好的连贯性和准确性。
    - 创意模式（通常是1）：生成的文本更有创意，但也更容易出现语法错误或不合逻辑的内容。
- `max_tokens`：限制生成文本的最大长度，防止输出过长。

**Token 是什么？**
- 基本单位：大模型处理文本的最小单位是 token（相当于自然语言中的词或字），输出时逐个 token 依次生成。
- 收费依据：大语言模型（LLM）通常也是以 token 的数量作为其计量（或收费）的依据。
- 1个Token ≈ 1-1.8个汉字，1个Token ≈ 3-4个英文字符
- OpenAI提供：[https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)
- 百度智能云提供：[https://console.bce.baidu.com/support/#/tokenizer](https://console.bce.baidu.com/support/#/tokenizer)

`max_tokens` 设置建议：
- 客服短回复：128-256。比如：生成一句客服回复（如"您的订单已发货，预计明天送达"）常见对话、多轮对话：512-1024
- 长内容生成：1024-4096。比如：生成一篇产品说明书（包含功能、使用方法等结构）

#### 2.3.2 模型调用推荐平台：closeai

考虑到 OpenAI 等模型在国内访问及充值的不便，大家可以使用 CloseAI 网站注册和充值，具体费用自理。
[https://www.closeai-asia.com](https://www.closeai-asia.com/)
#### 2.3.3 方式1：硬编码

直接将 API Key 和模型参数写入代码，仅适用于临时测试，存在密钥泄露风险，在生产环境不推荐。

```python
from langchain_openai import ChatOpenAI

# 硬编码 API Key 和模型参数
llm = ChatOpenAI(
    api_key="sk-xxxxxxxxx",  # 明文暴露密钥
    base_url="https://api.openai-proxy.org/v1",
    model="gpt-3.5-turbo",
)

# 调用示例
response = llm.invoke("解释神经网络原理")
print(response.content)
```

#### 2.3.4 方式2：配置环境变量

通过系统环境变量存储密钥，避免代码明文暴露。

**方式1：终端设置环境变量（临时生效）：**
```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"  # Linux/Mac
set OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"     # Windows
```

**方式2：从 PyCharm 设置**
![](<images/Pasted image 20260507163555.png>)![](<images/Pasted image 20260507163600.png>)
**举例：**
```python
import os
from langchain_openai import ChatOpenAI

# 从环境变量读取密钥
llm = ChatOpenAI(
    api_key=os.environ["OPENAI_API_KEY"],  # 动态获取
    base_url=os.environ["OPENAI_BASE_URL"],
    model="gpt-4o-mini",
)

response = llm.invoke("LangChain 是什么？")
print(response.content)
```
```python
输出：略
```
- 优点：密钥与代码分离，适合单机开发
- 缺点：切换终端或文件后，变量失效，需重新设置。

#### 2.3.5 方式3：使用 .env 配置文件（推荐）

使用 `python-dotenv` 加载本地配置文件，支持多环境管理（开发/生产）。

**1）安装依赖：**
```bash
pip install python-dotenv
# 或者
conda install python-dotenv
```

**2）创建 .env 文件（项目根目录）：**
```
OPENAI_API_KEY="sk-xxxxxxxxx"  # 需填写自己的API KEY
OPENAI_BASE_URL="https://api.openai-proxy.org/v1"
```

**3）举例：**

**方式1：**
```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()  # 自动加载 .env 文件

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # 安全读取
    base_url=os.getenv("OPENAI_BASE_URL"),
    model="gpt-4o-mini",
    temperature=0.7,
)

response = llm.invoke("RAG 技术的核心流程")
print(response.content)
```

**方式2：给 os 内部的环境变量赋值：**
```python
from langchain_openai import ChatOpenAI
import dotenv
dotenv.load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY1")
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_BASE_URL")

text = "猫王是猫吗？"

chat_model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=300,
)
response = chat_model.invoke(text)
print(type(response))
print(response.content)
```

**核心优势：**
- 配置文件可加入 `.gitignore` 避免泄露
- 结合 LangChain 可扩展其他模型（如 DeepSeek、阿里云）
- 生产环境推荐

 **小结：**

| 方式        | 安全性  | 持久性   | 适用场景      |
| --------- | ---- | ----- | --------- |
| 硬编码       | ⚠ 低  | ❌ 临时  | 本地快速测试    |
| 环境变量      | ✅ 中  | ⚠ 会话级 | 短期开发调试    |
| .env 配置文件 | ✅✅ 高 | ✅ 永久  | 生产环境、团队协作 |

以上3种方式，适合于所有的 LLM 的获取。

### 2.4 角度3出发：各平台 API 的调用举例（了解）

#### 2.4.1 OpenAI 官方 API
考虑到OpenAI在国内访问及充值的不便，我们仍然使用CloseAI网站（[https://www.closeai-asia.com](https://www.closeai-asia.com)）注册和充值，具体费用自理。
**调用非对话模型：**
```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-zD4CB2Qe7G2Dp6veCfPRSxeDx9fQPxCUIfOFAk20ETV5B2VA",  # 填写自己的api-key
    base_url="https://api.openai-proxy.org/v1"
)

# 调用Completion接口
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",  # 非对话模型
    prompt="请将以下英文翻译成中文：\n'Artificial intelligence will reshape the future.'",
    max_tokens=100,  # 生成文本最大长度
    temperature=0.7,  # 控制随机性
)
# 提取结果
print(response.choices[0].text.strip())
```

**调用对话模型（写法1）：**
```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-zD4CB2Qe7G2Dp6veCfPRSxeDx9fQPxCUIfOFAk20ETV5B2VA",
    base_url="https://api.openai-proxy.org/v1"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # 对话模型
    messages=[
        {"role": "system", "content": "你是一个乐于助人的智能AI小助手"},
        {"role": "user", "content": "你好，请你介绍一下你自己"}
    ],
    max_tokens=150,
    temperature=0.5
)

print(completion.choices[0].message)
```
```python
ChatCompletionMessage(content=你好，我是⼀个智能AI助⼿，可以回答各种问题、提供信息
和建议。⽆论是⽇常⽣活中的疑问，还是学习⼯', refusal=None, role=8assistant8, annotations=None, audio=None, function_call=None, tool_calls=None)
```
**调用对话模型（写法2）：**
```python
from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY1")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "我是一位乐于助人的AI智能小助手"},
        {"role": "user", "content": "你好，请你介绍一下你自己。"}
    ]
)

print(response.choices[0])
```

#### 2.4.2 百度千帆平台

开发参考文档[https://cloud.baidu.com/doc/qianfan-docs/s/Mm8r1mejk](https://cloud.baidu.com/doc/qianfan-docs/s/Mm8r1mejk)
获取 API Key 和 App ID
创建API Key：[https://console.bce.baidu.com/qianfan/ais/console/apiKey](https://console.bce.baidu.com/qianfan/ais/console/apiKey)
创建App ID：[https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/applicatio](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application/v2) [n/v2](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application/v2)
**代码举例：**
```python
from openai import OpenAI

client = OpenAI(
    api_key="bce-v3/ALTAK-KZke********/f1d6ee*************",  # 千帆bearer token
    base_url="https://qianfan.baidubce.com/v2",  # 千帆域名
    default_headers={"appid": "app-MuYR79q6"}   # 用户在千帆上的appid，非必传
)

completion = client.chat.completions.create(
    model="ernie-4.0-turbo-8k",  # 预置服务请查看模型列表，定制服务请填入API地址
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Hello！'}
    ]
)

print(completion.choices[0].message)
```

#### 2.4.3 阿里云百炼平台

注册并提前开通百炼平台账号并申请 API KEY。
![](<images/Pasted image 20260507164636.png>)
**对应的配置文件：**
```
DASHSCOPE_API_KEY="sk-f1a87324#####e6a819a482"  # 使用自己的api key
DASHSCOPE_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
```
**模型的调用：**
参考具体模型的代码示例。这里以DeepSeek为例：
![](<images/Pasted image 20260507164652.png>)
**举例1：通过 OpenAI SDK：**
```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="deepseek-r1",  # 此处以 deepseek-r1 为例，可按需更换模型名称。
    messages=[
        {'role': 'user', 'content': '9.9和9.11谁大'}
    ]
)

# 通过reasoning_content字段打印思考过程
print("思考过程：")
print(completion.choices[0].message.reasoning_content)

# 通过content字段打印最终答案
print("最终答案：")
print(completion.choices[0].message.content)
```

**举例2：通过 DashScope SDK：**
```python
pip install dashscope
```

```python
import dashscope

messages = [
    {'role': 'user', 'content': '你是谁？'}
]

response = dashscope.Generation.call(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    model="deepseek-r1",  # 此处以 deepseek-r1 为例，可按需更换模型名称。
    messages=messages,
    # result_format参数不可以设置为"text"。
    result_format='message'
)

print("=" * 20 + "思考过程" + "=" * 20)
print(response.output.choices[0].message.reasoning_content)
print("=" * 20 + "最终答案" + "=" * 20)
print(response.output.choices[0].message.content)
```

#### 2.4.4 智谱的GLM

注册智谱模型并获取 API Key。
[https://www.bigmodel.cn/usercenter/proj-mgmt/apikeys](https://www.bigmodel.cn/usercenter/proj-mgmt/apikeys)
![](<images/Pasted image 20260507164836.png>)
![](<images/Pasted image 20260507164842.png>)
**配置文件：**
```
ZHIPUAI_API_KEY="63a0f275b3a9###############rA4Y8daGaLydxQ"
```
**查看《开发文档》**
![](<images/Pasted image 20260507164859.png>)
![](<images/Pasted image 20260507164931.png>)
或者选择如下《参考文档》皆可：
[https://www.bigmodel.cn/dev/api/normal-model/glm-4](https://www.bigmodel.cn/dev/api/normal-model/glm-4)
![](<images/Pasted image 20260507164958.png>)
**举例1：使用 OpenAI SDK：**
```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("ZHIPUAI_API_KEY"),
    base_url=os.getenv("ZHIPUAI_URL")
)

completion = client.chat.completions.create(
    model="glm-4-air-250414",
    messages=[
        {"role": "system", "content": "你是一个聪明且富有创造力的小说作家"},
        {"role": "user", "content": "请你作为童话故事大王，写一篇短篇童话故事，故事的主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。"}
    ],
)

print(completion.choices[0].message)
```

**举例2：使用 Langchain SDK：**
```python
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4-air-250414",
    openai_api_key=os.getenv("ZHIPUAI_API_KEY"),
    openai_api_base=os.getenv("ZHIPUAI_URL"),
)
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a nice chatbot having a conversation with a human."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)
conversation.invoke({"question": "给我讲个冷笑话"})
```

**举例3：参考 langchain 的文档**
[https://imooc-langchain.shortvar.com/docs/integrations/chat/zhipuai/](https://imooc-langchain.shortvar.com/docs/integrations/chat/zhipuai/)
**安装包：**
```bash
pip install langchain-community
pip install pyjwt
```

```python
import dotenv
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# 智谱大模型：参考langchain的大模型

dotenv.load_dotenv()

import os
os.environ["ZHIPUAI_API_KEY"] = os.getenv("ZHIPUAI_API_KEY")

chat = ChatZhipuAI(
    model="glm-4",
    temperature=0.5,
)

messages = [
    AIMessage(content="哈哈~"),
    SystemMessage(content="你是一个诗人"),
    HumanMessage(content="写一首关于AI的七言绝句"),
]

response = chat.invoke(messages)
print(response.content)  # 显示 AI 生成的诗
```

```python
智能助⼿显神通，
万物互联慧眼中。
编码世界藏诗意，
共融未来路⽆穷。
```
#### 2.4.5 硅基流动平台
官网：[https://www.siliconflow.cn/](https://www.siliconflow.cn/)
**申请API Key：**
![](<images/Pasted image 20260507165149.png>)
参考文档：[https://docs.siliconflow.cn/cn/userguide/quickstart](https://docs.siliconflow.cn/cn/userguide/quickstart)

**代码举例（流式输出）：**
```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("SILICON_API_KEY"),
    base_url="https://api.siliconflow.cn/v1"
)
response = client.chat.completions.create(
    model='Pro/deepseek-ai/DeepSeek-R1',
    messages=[
        {'role': 'user',
         'content': "推理模型会给市场带来哪些新的机会"}
    ],
    stream=True
)

for chunk in response:
    if not chunk.choices:
        continue
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
    if chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end="", flush=True)
```

**或者：**
![](<images/Pasted image 20260507165232.png>)
![](<images/Pasted image 20260507165236.png>)

```python
import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "deepseek-ai/DeepSeek-R1",  # 填写你选择的大模型
    "messages": [
        {
            "role": "user",
            "content": "1 +2 * 3 = ？"
        }
    ]
}
headers = {
    "Authorization": "Bearer sk-auciaxqpz.....zepozralhwleyrdoyjani",  # 填写你的api-key
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

### 2.5 如何选择合适的大模型

#### 2.5.1 有没有最好的大模型

凡是问"哪个大模型最好？"的，都是不懂的。

不妨反问：「无论做什么，有都表现最好的员工吗？」

**划重点：没有最好的大模型，只有最适合的大模型**

基础模型选型，合规和安全是首要考量因素。

**为什么不要依赖榜单**
- 榜单已被应试教育污染，还算值得相信的榜单：[LMSYS Chatbot Arena Leaderboard](https://lmarena.ai/leaderboard)
- 榜单体现的是整体能力，放到一份具体事情上，排名低的可能反倒更好
- 榜单体现不出成本差异
- 本课程主要以 OpenAI 为例展开后续的课程。因为：
  1. OpenAI 最流行，即便是国内也是最多
  2. OpenAI 最先进。别的模型有的能力，OpenAI 一定都有。OpenAI 有的，别的模型不一定有。
  3. 其他模型都在追赶和模仿 OpenAI（gpt-4o-mini）
- 学会 OpenAI，其他模型触类旁通。反之，不行。

#### 2.5.2 小结：获取大模型的标准方式

后续的各种模型测试，都基于如下的模型展开：

**非对话模型：**
```python
import os
import dotenv
from langchain_openai import OpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

llm = OpenAI()  # 非对话模型
```

**对话模型：**
```python
import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

chat_model = ChatOpenAI(  # 对话模型
    model="gpt-4o-mini",
    # max_tokens=512,
)
```

**对应的配置文件：**
```
OPENAI_API_KEY="sk-xxxxxx"   # 从CloseAI平台，注册自己的账号，并获取API KEY
OPENAI_BASE_URL="https://api.openai-proxy.org/v1"
```

---

## 3. Model I/O 之调用模型（消息与调用方法）

### 3.1 关于对话模型的 Message（消息）

聊天模型，除了将字符串作为输入外，还可以使用聊天消息作为输入，并返回聊天消息作为输出。

LangChain 有一些内置的消息类型：

- 🔥 **SystemMessage**：规定 AI 行为规则或背景信息。比如规定 AI 的初始状态、行为模式或对话的总体目标。比如"作为一个代码专家"，或者"返回 Json 格式"。通常作为输入消息序列中的第一个传递。
- 🔥 **HumanMessage**：表示来自用户输入。比如"实现一个快速排序方法"
- **AIMessage**：存储 AI 回复的内容。这可以是文本，也可以是调用工具的请求
- **ChatMessage**：可以自定义角色的通用消息类型
- **FunctionMessage/ToolMessage**：函数调用/工具消息，用于函数调用结果的消息类型

> **注意：**
> FunctionMessage 和 ToolMessage 分别是在函数调用和工具调用场景下才会用的特殊消息类型，HumanMessage、AIMessage 和 SystemMessage 才是最常用的消息类型。

**举例1：**
```python
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="你是一位乐于助人的智能小助手"),
    HumanMessage(content="你好，请你介绍一下你自己"),
]

print(messages)
```

**举例2：**
```python
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

messages = [
    SystemMessage(content=["你是一个数学家,会回答数学问题", "每次你都能给出详细的答案"]),
    HumanMessage(content="1 + 2 * 3 = ?"),
    AIMessage(content="1 + 2 * 3 的结果是7"),
]

print(messages)
```

**举例4：创建不同类型的消息：**
```python
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ChatMessage
)

system_message = SystemMessage(content="你是一个专业的数据科学家")
human_message = HumanMessage(content="解释一下随机森林算法")
ai_message = AIMessage(content="随机森林是一种集成学习方法..")
custom_message = ChatMessage(role="analyst", content="补充一点关于超参数调优的信息")

print(system_message.content)
print(human_message.content)
print(ai_message.content)
print(custom_message.content)
```

**举例5：结合大模型使用：**
```python
import os
from langchain_core.messages import SystemMessage, HumanMessage
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

chat_model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(content="你是一个擅长人工智能相关科学的专家"),
    HumanMessage(content="请解释一下什么是机器学习？")
]

response = chat_model.invoke(messages)
print(response.content)
print(type(response))  # <class 'langchain_core.messages.ai.AIMessage'>
```

### 3.2 关于多轮对话与上下文记忆

**前提：获取大模型**
```python
import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

chat_model = ChatOpenAI(model="gpt-4o-mini")
```

**测试1：两次独立调用，无上下文：**
```python
from langchain_core.messages import SystemMessage, HumanMessage

sys_message = SystemMessage(content="我是一个人工智能的助手，我的名字叫小智")
human_message = HumanMessage(content="猫王是一只猫吗？")

messages = [sys_message, human_message]
response = chat_model.invoke(messages)
print(response.content)

# 第二次调用没有上下文，无法知道"小智"
response1 = chat_model.invoke("你叫什么名字？")
print(response1.content)
```

**测试5：手动维护对话历史（实现多轮对话）：**
```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

messages = [
    SystemMessage(content="我是一个人工智能助手，我的名字叫小智"),
    HumanMessage(content="人工智能英文怎么说？"),
    AIMessage(content="AI"),
    HumanMessage(content="你叫什么名字"),
]

# 手动传入历史对话，模型可以正确记住上下文
chat_model.invoke(messages)
```

### 3.3 关于模型调用的方法

为了尽可能简化自定义链的创建，我们实现了一个协议。许多 LangChain 组件实现了 **Runnable** 协议，包括聊天模型、提示词模板、输出解析器、检索器、代理智能体等。

**Runnable 定义的公共调用方法：**
- `invoke`：处理单条输入，等待 LLM 完全推理完成后再返回调用结果
- `stream`：流式响应，逐字输出 LLM 的响应结果
- `batch`：处理批量输入

**异步方法：**
- `astream`：异步流式响应
- `ainvoke`：异步处理单条输入
- `abatch`：异步处理批量输入
- `astream_log`：异步流式返回中间步骤，以及最终响应
- `astream_events`：（测试版）异步流式返回链中发生的事件

#### 3.3.1 流式输出与非流式输出

**非流式输出**：Langchain 与 LLM 交互时的默认行为。系统等待模型生成完整响应后，一次性返回全部结果。适合问答、摘要、信息抽取类任务。

**流式输出**：用户不再等待完整答案，模型逐个 token 地实时返回内容。适合构建聊天机器人、写作助手等强调"实时反馈"的应用。Langchain 中通过设置 `streaming=True` 来启用。

**非流式输出举例：**
```python
import os
import dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

chat_model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(content="你是一位乐于助人的助手。你叫于老师"),
    HumanMessage(content="你是谁？")
]
response = chat_model.invoke(messages)
print(response.content)
```

**流式输出举例：**
```python
import os
import dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

chat_model = ChatOpenAI(
    model="gpt-4o-mini",
    streaming=True  # 启用流式输出
)

messages = [HumanMessage(content="你好，请介绍一下自己")]

print("开始流式输出：")
for chunk in chat_model.stream(messages):
    print(chunk.content, end="", flush=True)

print("\n流式输出结束")
```

#### 3.3.2 批量调用

```python
import os
import dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

chat_model = ChatOpenAI(model="gpt-4o-mini")

messages1 = [SystemMessage(content="你是一位乐于助人的智能小助手"),
             HumanMessage(content="请帮我介绍一下什么是机器学习")]

messages2 = [SystemMessage(content="你是一位乐于助人的智能小助手"),
             HumanMessage(content="请帮我介绍一下什么是AIGC")]

messages3 = [SystemMessage(content="你是一位乐于助人的智能小助手"),
             HumanMessage(content="请帮我介绍一下什么是大模型技术")]

messages = [messages1, messages2, messages3]

# 调用batch
response = chat_model.batch(messages)
print(response)
```

#### 3.3.3 同步调用与异步调用（了解）

**同步调用：**

之前的 `llm.invoke(...)` 本质上是一个同步调用。每个操作依次执行，总执行时间是各操作时间之和。

```python
import time

def perform_other_tasks():
    for i in range(5):
        print(f"执行其他任务 {i + 1}")
        time.sleep(1)

def main():
    start_time = time.time()
    call_model()
    perform_other_tasks()
    total_time = time.time() - start_time
    return f"总共耗时：{total_time}"

print(main())
```

**异步调用：**

允许程序在等待某些操作完成时继续执行其他任务，可以显著提高程序的效率和响应性。

**写法1（适合 Jupyter Notebook）：**
```python
import asyncio
import time

async def async_call(llm):
    await asyncio.sleep(5)
    print("异步调用完成")

async def perform_other_tasks():
    await asyncio.sleep(5)
    print("其他任务完成")

async def run_async_tasks():
    start_time = time.time()
    await asyncio.gather(
        async_call(None),
        perform_other_tasks()
    )
    return f"总共耗时：{time.time() - start_time}"

# 在Jupyter单元格中直接调用
result = await run_async_tasks()
print(result)
```

**写法2（不适合 Jupyter Notebook）：**
```python
if __name__ == "__main__":
    result = asyncio.run(run_async_tasks())
    print(result)
```

**异步调用 ainvoke 举例（不能在 Jupyter Notebook 中测试）：**
```python
import asyncio, os, time, dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")
chat_model = ChatOpenAI(model="gpt-4o-mini")

def sync_test():
    messages1 = [SystemMessage(content="你是一位乐于助人的智能小助手"),
                 HumanMessage(content="请帮我介绍一下什么是机器学习")]
    start_time = time.time()
    response = chat_model.invoke(messages1)
    print(f"同步调用耗时：{time.time() - start_time:.2f}秒")
    return response

async def async_test():
    messages1 = [SystemMessage(content="你是一位乐于助人的智能小助手"),
                 HumanMessage(content="请帮我介绍一下什么是机器学习")]
    start_time = time.time()
    response = await chat_model.ainvoke(messages1)
    print(f"异步调用耗时：{time.time() - start_time:.2f}秒")
    return response

if __name__ == "__main__":
    sync_test()

    async def run_concurrent():
        tasks = [async_test() for _ in range(3)]
        return await asyncio.gather(*tasks)

    start = time.time()
    asyncio.run(run_concurrent())
    print(f"\n3个并发异步调用总耗时: {time.time() - start:.2f}秒")
```

---

## 4. Model I/O 之 Prompt Template

Prompt Template，通过模板管理大模型的输入。

### 4.1 介绍与分类

Prompt Template 是 LangChain 中的一个概念，接收用户输入，返回一个传递给 LLM 的信息（即提示词 prompt）。

在应用开发中，固定的提示词限制了模型的灵活性和适用范围。所以，prompt template 是一个模板化的字符串，你可以将变量插入到模板中，从而创建出不同的提示。调用时：
- 以字典作为输入，其中每个键代表要填充的提示模板中的变量
- 输出一个 PromptValue。这个 PromptValue 可以传递给 LLM 或 ChatModel，并且还可以转换为字符串或消息列表

**有几种不同类型的提示模板：**
- **PromptTemplate**：LLM 提示模板，用于生成字符串提示。它使用 Python 的字符串来模板提示
- **ChatPromptTemplate**：聊天提示模板，用于组合各种角色的消息模板，传入聊天模型
- **XxxMessagePromptTemplate**：消息模板，包括：SystemMessagePromptTemplate、HumanMessagePromptTemplate、AIMessagePromptTemplate、ChatMessagePromptTemplate
- **FewShotPromptTemplate**：样本提示词模板，通过示例来教模型如何回答
- **PipelinePrompt**：管道提示词模板，用于把几个提示词组合在一起使用
- **自定义模板**：允许基于其它模板类来定制自己的提示词模板

**模板导入：**
```python
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts import (
    ChatMessagePromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
```

### 4.2 复习：str.format()

Python 的 `str.format()` 方法是一种字符串格式化的手段，允许在字符串中插入变量。在 LangChain 的默认设置下，PromptTemplate 使用 Python 的 `str.format()` 方法进行模板化。

```python
# 带有位置参数
info = "Name: {0}, Age: {1}".format("Jerry", 25)
print(info)  # Name: Jerry, Age: 25

# 带有关键字参数
info = "Name: {name}, Age: {age}".format(name="Tom", age=25)
print(info)  # Name: Tom, Age: 25

# 使用字典解包
person = {"name": "David", "age": 40}
info = "Name: {name}, Age: {age}".format(**person)
print(info)  # Name: David, Age: 40
```

### 4.3 具体使用：PromptTemplate

#### 4.3.1 使用说明

PromptTemplate 类，用于快速构建包含变量的提示词模板，并通过传入不同的参数值生成自定义的提示词。

**主要参数：**
- `template`：定义提示词模板的字符串，包含文本和变量占位符（如 `{name}`）
- `input_variables`：列表，指定模板中使用的变量名称
- `partial_variables`：字典，用于定义模板中一些固定的变量，不需要每次调用时被替换

**函数：**
- `format()`：给 `input_variables` 变量赋值，并返回提示词

#### 4.3.2 两种实例化方式

**方式1：使用构造方法：**
```python
from langchain.prompts import PromptTemplate

template = PromptTemplate(
    template="请简要描述{topic}的应用",
    input_variables=["topic"]
)

prompt_1 = template.format(topic="机器学习")
prompt_2 = template.format(topic="自然语言处理")

print("提示词:", prompt_1)
print("提示词:", prompt_2)
```

**举例2（多变量）：**
```python
template = PromptTemplate(
    template="请评价{product}的优缺点，包括{aspect1}和{aspect2}",
    input_variables=["product", "aspect1", "aspect2"]
)

prompt_1 = template.format(product="智能手机", aspect1="电池续航", aspect2="拍照质量")
prompt_2 = template.format(product="笔记本电脑", aspect1="处理速度", aspect2="便携性")
```

**方式2：调用 `from_template()`：**
```python
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "请给我一个关于{topic}的{type}解释"
)

prompt = prompt_template.format(type="详细", topic="量子力学")
print(prompt)  # 请给我一个关于量子力学的详细解释
```

#### 4.3.3 两种新的结构形式

**形式1：部分提示词模版**

**方式1：`partial_variables`：**
```python
from langchain.prompts import PromptTemplate

template2 = PromptTemplate(
    template="{foo}{bar}",
    input_variables=["foo", "bar"],
    partial_variables={"foo": "hello"}
)
prompt2 = template2.format(bar="world")
print(prompt2)  # helloworld
```

**方式2：`.partial()` 方法：**
```python
template1 = PromptTemplate(
    template="{foo}{bar}",
    input_variables=["foo", "bar"]
)
partial_template1 = template1.partial(foo="hello")
prompt1 = partial_template1.format(bar="world")
print(prompt1)  # helloworld
```

**举例3：**
```python
prompt_template = PromptTemplate.from_template(
    template="请评价{product}的优缺点，包括{aspect1}和{aspect2}",
    partial_variables={"aspect1": "电池", "aspect2": "屏幕"}
)
prompt = prompt_template.format(product="笔记本电脑")
print(prompt)  # 请评价笔记本电脑的优缺点，包括电池和屏幕
```

**形式2：组合提示词（了解）：**
```python
from langchain_core.prompts import PromptTemplate

template = (
    PromptTemplate.from_template("Tell me a joke about {topic}")
    + ", make it funny"
    + "\n\nand in {language}"
)

prompt = template.format(topic="sports", language="spanish")
print(prompt)
# Tell me a joke about sports, make it funny
# and in spanish
```

#### 4.3.4 format() 与 invoke()

- `format()`：返回值为**字符串**类型
- `invoke()`：返回值为 **PromptValue** 类型

```python
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)
result = prompt_template.invoke({"adjective": "funny", "content": "chickens"})
# StringPromptValue(text='Tell me a funny joke about chickens.')
```

#### 4.3.5 结合 LLM 调用

```python
from langchain.prompts import PromptTemplate
import os, dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

llm = ChatOpenAI(model="gpt-4o-mini")

prompt_template = PromptTemplate.from_template(
    template="请评价{product}的优缺点，包括{aspect1}和{aspect2}"
)

prompt = prompt_template.format(product="电脑", aspect1="性能", aspect2="电池")
llm.invoke(prompt)
```

### 4.4 具体使用：ChatPromptTemplate

#### 4.4.1 使用说明

ChatPromptTemplate 是创建聊天消息列表的提示模板。它比普通 PromptTemplate 更适合处理多角色、多轮次的对话场景。

**特点：**
- 支持 System/Human/AI 等不同角色的消息模板
- 对话历史维护
- 参数类型：列表参数格式是 tuple 类型（role:str content:str 组合最常用）
- 元组格式：`(role: str | type, content: str | list[dict] | list[object])`
- role 是：字符串（如 "system"、"human"、"ai"）

#### 4.4.2 两种实例化方式

**方式2：调用 `from_messages()`（推荐）：**
```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个有帮助的AI机器人，你的名字是{name}"),
        ("human", "你好，最近怎么样？"),
        ("ai", "我很好，谢谢"),
        ("human", "{user_input}"),
    ]
)

messages = chat_template.invoke(input={"name": "小明", "user_input": "你叫什么名字？"})
print(messages)
```

#### 4.4.3 模板调用的几种方式

| 方法 | 返回类型 | 说明 |
|------|---------|------|
| `invoke()` | ChatPromptValue | 推荐 |
| `format()` | str | 字符串 |
| `format_messages()` | List[BaseMessage] | **针对ChatPromptTemplate推荐** |
| `format_prompt()` | ChatPromptValue | 需再调用 `.to_messages()` |

#### 4.4.4 更丰富的实例化参数类型

结论：参数是列表类型，列表的元素可以是字符串、字典、元组、消息类型、提示词模板类型、消息提示词模板类型。

**类型1：str 类型**（不推荐，默认角色为 human）
```python
chat_template = ChatPromptTemplate.from_messages([
    "Hello, {name}!"  # 等价于 ("human", "Hello, {name}!")
])
```

**类型2：dict 类型**
```python
prompt = ChatPromptTemplate.from_messages([
    {"role": "system", "content": "你是一个{role}."},
    {"role": "human", "content": ["复杂内容", {"type": "text"}]},
])
print(prompt.format_messages(role="教师"))
```

**类型3：Message 类型**
```python
from langchain_core.messages import SystemMessage, HumanMessage

chat_prompt_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="我是一个贴心的智能助手"),
    HumanMessage(content="我的问题是：人工智能英文怎么说？")
])
messages = chat_prompt_template.format_messages()
print(messages)
```

**类型4：BaseChatPromptTemplate 类型**（嵌套 ChatPromptTemplate）
```python
nested1 = ChatPromptTemplate.from_messages([("system", "我是一个人工智能助手")])
nested2 = ChatPromptTemplate.from_messages([("human", "很高兴认识你")])

prompt_template = ChatPromptTemplate.from_messages([nested1, nested2])
prompt_template.format_messages()
```

**类型5：BaseMessagePromptTemplate 类型**

- **HumanMessagePromptTemplate**：预定义 `role="human"`，支持变量占位符
- **SystemMessagePromptTemplate**：类似，用于系统消息
- **AIMessagePromptTemplate**：类似，用于 AI 消息
- **ChatMessagePromptTemplate**：可以为每条消息指定任意角色

```python
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate
)

system_message_prompt = SystemMessagePromptTemplate.from_template("你是一个专家{role}")
human_message_prompt = HumanMessagePromptTemplate.from_template("给我解释{concept}，用浅显易懂的语言")

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

formatted_messages = chat_prompt.format_messages(role="物理学家", concept="相对论")
print(formatted_messages)
```

**ChatMessagePromptTemplate 举例：**
```python
from langchain_core.prompts import ChatMessagePromptTemplate

prompt = "今天我们授课的内容是{subject}"
chat_message_prompt = ChatMessagePromptTemplate.from_template(
    role="teacher", template=prompt
)
resp = chat_message_prompt.format(subject="我爱北京天安门")
print(type(resp))   # <class 'langchain_core.messages.chat.ChatMessage'>
print(resp)         # content='今天...' role='teacher'
```

#### 4.4.5 结合 LLM

```python
from langchain.prompts.chat import ChatPromptTemplate
import os, dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个数学家，你可以计算任何算式"),
    ("human", "我的问题：{question}"),
])

messages = chat_prompt.format_messages(
    question="我今年18岁，我的舅舅今年38岁，我和舅舅一共多少岁了？"
)

chat_model = ChatOpenAI(model="gpt-4o-mini")
output = chat_model.invoke(messages)
print(output.content)
# 你今年18岁，你的舅舅今年38岁。那么你和舅舅的年龄总和是：18 + 38 = 56，所以你和舅舅一共56岁。
```

#### 4.4.6 插入消息列表：MessagesPlaceholder

当你不确定消息提示模板使用什么角色，或者希望在格式化过程中插入消息列表时，可以使用 **MessagesPlaceholder**。

**使用场景**：多轮对话系统存储历史消息，以及 Agent 的中间步骤处理。

**举例1：**
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder("msgs")
])

prompt_template.format_messages(msgs=[HumanMessage(content="hi!")])
# 生成 [SystemMessage("You are a helpful assistant"), HumanMessage("hi!")]
```

**举例2：存储对话历史：**
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])

prompt.format_messages(
    history=[HumanMessage(content="1+2*3 = ?"), AIMessage(content="1+2*3=7")],
    question="我刚才问题是什么？"
)
```

**举例3：**
```python
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate
)
from langchain_core.messages import SystemMessage

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("你是{role}"),
    MessagesPlaceholder(variable_name="intermediate_steps"),
    HumanMessagePromptTemplate.from_template("{query}")
])

intermediate = [
    SystemMessage(name="search", content="北京: 晴，25℃")
]
prompt.format_messages(
    role="天气预报员",
    intermediate_steps=intermediate,
    query="北京天气怎么样？"
)
```

### 4.5 具体使用：少量样本示例的提示词模板

#### 4.5.1 使用说明

在构建 prompt 时，可以通过构建一个少量示例列表去进一步格式化 prompt，这是一种简单但强大的指导生成的方式，在某些情况下可以显著提高模型性能。

少量示例提示模板可以由一组示例或一个负责从定义的集合中选择一部分示例的示例选择器构建。

- **前者**：使用 `FewShotPromptTemplate` 或 `FewShotChatMessagePromptTemplate`
- **后者**：使用 Example selectors（示例选择器）

每个示例的结构都是一个字典，其中键是输入变量，值是输入变量的值。

**体会**：zeroshot 会导致低质量回答。

#### 4.5.2 FewShotPromptTemplate 的使用

**举例1：**
```python
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate

# 1. 创建示例集合
examples = [
    {"input": "北京天气怎么样", "output": "北京帮"},
    {"input": "南京下雨吗", "output": "南京帮"},
    {"input": "武汉热吗", "output": "武汉帮"}
]

# 2. 创建 PromptTemplate 实例
example_prompt = PromptTemplate.from_template(
    template="Input: {input}\nOutput: {output}"
)

# 3. 创建 FewShotPromptTemplate 实例
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Input: {input}\nOutput:",  # 要放在示例后面的提示模板字符串
    input_variables=["input"]  # 传入的变量
)

# 4. 调用
prompt = prompt.invoke({"input": "长沙多少度"})

print("===Prompt===")
print(prompt)
```

**输出：**
```
===Prompt===
Input: 北京天气怎么样
Output: 北京帮

Input: 南京下雨吗
Output: 南京帮

Input: 武汉热吗
Output: 武汉帮

Input: 长沙多少度
Output:
```

**结合大模型调用：**
```python
import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

# 获取大模型
chat_model = ChatOpenAI(model="gpt-4o-mini")
```

#### 4.5.3 FewShotChatMessagePromptTemplate 的使用

除了 FewShotPromptTemplate 之外，`FewShotChatMessagePromptTemplate` 是专门为**聊天对话场景**设计的少样本（few-shot）提示模板，它继承自 FewShotPromptTemplate，但针对聊天消息的格式进行了优化。

**特点：**
- 自动将示例格式化为聊天消息（HumanMessage/AIMessage 等）
- 输出结构化聊天消息（List[BaseMessage]）
- 保留对话轮次结构

**举例1：基本结构**
```python
from langchain.prompts import (
    FewShotChatMessagePromptTemplate,
    ChatPromptTemplate
)

# 1. 示例消息格式
examples = [
    {"input": "1+1等于几？", "output": "1+1等于2"},
    {"input": "法国的首都是：", "output": "巴黎"}
]

# 2. 定义示例的消息格式提示词模板
msg_example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])

# 3. 定义 FewShotChatMessagePromptTemplate 对象
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=msg_example_prompt,
    examples=examples
)

# 4. 输出格式化后的消息
print(few_shot_prompt.format())
```

**输出：**
```
Human: 1+1等于几？
AI: 1+1等于2
Human: 法国的首都是：
AI: 巴黎
```

**举例2：**

使用方式：将原始输入和被选中的示例组在一起加入 chat 提示词模板中。
```python
# 1. 导入相关包
from langchain_core.prompts import (FewShotChatMessagePromptTemplate, ChatPromptTemplate)

# 2. 定义示例集
examples = [...]

# 3. 定义示例的消息格式提示词模板
example_prompt = ChatPromptTemplate.from_messages([
    ('human', '{input} 是多少'),
    ('ai', '{output}')
])

# 4. 定义 FewShotChatMessagePromptTemplate 对象
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,          # 示例组
    example_prompt=example_prompt,  # 示例提示词词模板
)

# 5. 输出完整提示词的消息模板
final_prompt = ChatPromptTemplate.from_messages(
    [
        ('system', '你是一个数学专家'),
        few_shot_prompt,
        ('human', '{input}'),
    ]
)

# 6. 提供大模型
import os, dotenv
from langchain_openai import ChatOpenAI
dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")
chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)
# 输出：'2⁴ 等于 16。'
```

**举例3：与前面类似**
```python
# 1. 导入相关包
from langchain_core.prompts import (FewShotChatMessagePromptTemplate, ChatPromptTemplate)

# 2. 定义示例组
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
]

# 3. 定义示例的消息格式提示词模板
example_prompt = ChatPromptTemplate.from_messages([
    ('human', 'What is {input}?'),
    ('ai', '{output}')
])

# 4. 定义 FewShotChatMessagePromptTemplate 对象
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,          # 示例组
    example_prompt=example_prompt,  # 示例提示词词模板
)

# 5. 输出完整消息
final_prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful AI Assistant'),
        few_shot_prompt,
        ('human', '{input}'),
    ]
)

# 6. 格式化完整消息
final_prompt.format_messages(input="What is 4+4?")
```

**输出：**
```python
[SystemMessage(content='You are a helpful AI Assistant'),
 HumanMessage(content='What is 2+2?'),
 AIMessage(content='4'),
 HumanMessage(content='What is 2+3?'),
 AIMessage(content='5'),
 HumanMessage(content='What is 4+4?')]
```

#### 4.5.4 Example selectors（示例选择器）

前面 FewShotPromptTemplate 的特点是，无论输入什么问题，都会包含全部示例。在实际开发中，我们可以根据当前输入，使用示例选择器，从大量候选示例中选取最相关的示例子集。

**使用的好处**：避免盲目传递所有示例，减少 token 消耗的同时，还可以提升输出效果。

**示例选择策略：**
- **语义相似选择**：通过余弦相似度等度量方式评估语义相关性，选择与输入问题最相似的 k 个示例
- **长度选择**：根据输入文本的长度，从候选示例中筛选出长度最匹配的示例，加强模型对文本结构的理解。比语义相似度计算更轻量，适合对响应速度要求高的场景
- **最大边际相关示例选择**：优先选择与输入问题语义相似的示例；同时，通过惩罚机制避免返回同质化的内容

> 余弦相似度是通过计算两个向量的夹角余弦值来衡量它们的相似性。它的值范围在 -1 到 1 之间。
> 数学表达式：余弦相似度 = (A·B) / (||A|| × ||B||)，其中 A·B 是点积，||A|| 和 ||B|| 是向量的模（长度）。

**举例1：**
```python
import os, dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector

dotenv.load_dotenv()

# 定义嵌入模型
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

embeddings_model = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

# 定义示例选择器
example_selector = SemanticSimilarityExampleSelector.from_examples(
    # 这是可供选择的示例列表
    examples,
    # 这是用于生成嵌入的嵌入类，用于衡量语义相似性
    embeddings_model,
    # 这是用于存储嵌入并进行相似性搜索的 VectorStore 类
    Chroma,
    # 这是要生成的示例数量
    k=1,
)

# 选择与输入最相似的示例
question = "璩绿路华盛顿的父亲是谁?"
selected_examples = example_selector.select_examples({"question": question})
print(f"与输入最相似的示例：{selected_examples}")
```

**举例2：结合 FewShotPromptTemplate 使用（使用 FAISS）**
```python
import os, dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

# 定义示例提示词模板
example_prompt = PromptTemplate.from_template(
    template="Input: {input}\nOutput: {output}",
)

# 创建示例集合（反义词）
examples = [
    {"input": "高兴", "output": "悲伤"},
    {"input": "高", "output": "矮"},
    {"input": "长", "output": "短"},
    {"input": "精力充沛", "output": "无精打采"},
    {"input": "阳光", "output": "阴暗"},
    {"input": "粗糙", "output": "光滑"},
    {"input": "干燥", "output": "潮湿"},
    {"input": "富裕", "output": "贫穷"},
]

# 定义嵌入模型
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# 创建语义相似性示例选择器
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    embeddings,
    FAISS,
    k=2,
)

# 定义少样本提示词模板
similar_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="给出每个词组的反义词",
    suffix="Input: {word}\nOutput:",
    input_variables=["word"],
)

response = similar_prompt.invoke({"word": "忧愁"})
print(response.text)
```

**输出：**
```
给出每个词组的反义词
Input: 高兴
Output: 悲伤
Input: 阳光
Output: 阴暗
Input: 忧愁
Output:
```

### 4.6 具体使用：PipelinePromptTemplate（了解）

用于将多个提示模板按顺序组合成处理管道，实现分阶段、模块化的提示构建。它的核心作用类似于软件开发中的管道模式（Pipeline Pattern），通过串联多个提示处理步骤，实现复杂的提示生成逻辑。

**特点：**
- 将复杂提示拆解为多个处理阶段，每个阶段使用独立的提示模板
- 前一个模板的输出作为下一个模板的输入变量

**使用场景**：解决单一超大提示模板难以维护的问题。

> 说明：PipelinePromptTemplate 在 langchain 0.3.22 版本中已标记为过时，在 langchain-core==1.0 之前不会删除它。

**举例：**
```python
from langchain_core.prompts.pipeline import PipelinePromptTemplate
from langchain_core.prompts.prompt import PromptTemplate

# 构建管道
pipeline = PipelinePromptTemplate(
    final_prompt=answer_template,
    pipeline_prompts=[
        ("analysis_result", analysis_template),
        ("retrieval_result", retrieval_template)
    ]
)

print(pipeline.format(question="量子计算的优势是什么？"))
```

**新版代码写法（手动管道替代方式）：**
```python
from langchain_core.prompts.prompt import PromptTemplate

# 阶段1：问题分析
analysis_template = PromptTemplate.from_template("""
分析这个问题：{question}
关键要素：
""")

# 逐步执行管道提示
pipeline_prompts = [
    ("analysis_result", analysis_template),
    ("retrieval_result", retrieval_template)
]

my_input = {"question": "量子计算的优势是什么？"}

for name, prompt in pipeline_prompts:
    # 调用当前提示模板并获取字符串结果
    result = prompt.invoke(my_input).to_string()
    # 将结果添加到输入字典中供下一步使用
    my_input[name] = result

# 生成最终答案
my_output = answer_template.invoke(my_input).to_string()
print(my_output)
```

### 4.7 具体使用：自定义提示词模板（了解）

在创建 prompt 时，我们也可以按照自己的需求去创建自定义的提示模板。

**步骤：**
1. 自定义类继承提示词基类模板 `BasePromptTemplate`
2. 重写 `format`、`format_prompt`、`from_template` 方法

**举例：**
```python
# 1. 导入相关包
from typing import List, Dict, Any
from langchain.prompts import BasePromptTemplate
from langchain.prompts import PromptTemplate
from langchain.schema import PromptValue

# 2. 自定义提示词模板
class SimpleCustomPrompt(BasePromptTemplate):
    """简单自定义提示词模板"""
    template: str

    def __init__(self, template: str, **kwargs):
        # 使用 PromptTemplate 解析输入变量
        prompt = PromptTemplate.from_template(template)
        super().__init__(
            input_variables=prompt.input_variables,
            template=template,
            **kwargs
        )

    def format(self, **kwargs: Any) -> str:
        """格式化提示词"""
        return self.template.format(**kwargs)

    def format_prompt(self, **kwargs: Any) -> PromptValue:
        """实现抽象方法"""
        return PromptValue(text=self.format(**kwargs))

    @classmethod
    def from_template(cls, template: str, **kwargs) -> "SimpleCustomPrompt":
        """从模板创建实例"""
        return cls(template=template, **kwargs)

# 3. 使用自定义提示词模板
custom_prompt = SimpleCustomPrompt.from_template(
    template="请回答关于{subject}的问题：{question}"
)

# 4. 格式化提示词
formatted = custom_prompt.format(
    subject="人工智能",
    question="什么是LLM？"
)

print(formatted)
# 请回答关于人工智能的问题：什么是LLM？
```

### 4.8 从文档中加载 Prompt（了解）

一方面，将想要设定 prompt 所支持的格式保存为 JSON 或者 YAML 格式文件。另一方面，通过读取指定路径的格式化文件，获取相应的 prompt。

**目的与使用场景**：
- 为了便于共享、存储和加强对 prompt 的版本控制
- 当我们的 prompt 模板数据较大时，我们可以使用外部导入的方式进行管理和维护

#### 4.8.1 YAML 格式提示词

在 `asset` 下创建 yaml 文件：`prompt.yaml`
```yaml
_type:
  "prompt"
input_variables:
  ["name", "what"]
template:
  "请给{name}讲一个关于{what}的故事"
```

**代码：**
```python
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv

load_dotenv()

prompt = load_prompt("asset/prompt.yaml", encoding="utf-8")
print(prompt.format(name="年轻人", what="滑稽"))
# 请给年轻人讲一个关于滑稽的笑话
```

#### 4.8.2 JSON 格式提示词

在 `asset` 下创建 json 文件：`prompt.json`
```json
{
    "_type": "prompt",
    "input_variables": ["name", "what"],
    "template": "请{name}讲一个{what}的故事。"
}
```

**代码：**
```python
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv

load_dotenv()

prompt = load_prompt("asset/prompt.json", encoding="utf-8")
print(prompt.format(name="张三", what="搞笑的"))
# 请张三讲一个搞笑的的故事。
```

## 5. Model I/O 之 Output Parsers

语言模型返回的内容通常都是字符串的格式（文本格式），但在实际 AI 应用开发过程中，往往希望 model 可以返回更直观、更格式化的内容，以确保应用能够顺利进行后续的逻辑处理。此时，LangChain 提供的输出解析器就派上用场了。

**输出解析器（Output Parser）** 负责获取 LLM 的输出并将其转换为更合适的格式。这在应用开发中及其重要。

### 5.1 输出解析器的分类

LangChain 有很多不同类型的输出解析器：

| 解析器 | 说明 |
|--------|------|
| `StrOutputParser` | 字符串解析器 |
| `JsonOutputParser` | JSON 解析器，确保输出符合特定 JSON 对象格式 |
| `XMLOutputParser` | XML 解析器，允许以流行的 XML 格式从 LLM 获取结果 |
| `CommaSeparatedListOutputParser` | CSV 解析器，模型的输出以逗号分隔，以列表形式返回输出 |
| `DatetimeOutputParser` | 日期时间解析器，可用于将 LLM 输出解析为日期时间格式 |

除了上述常用的输出解析器之外，还有：
- **EnumOutputParser**：枚举解析器，将 LLM 的输出，解析为预定义的枚举值
- **StructuredOutputParser**：将非结构化文本转换为预定义格式的结构化数据（如字典）
- **OutputFixingParser**：输出修复解析器，用于自动修复格式错误的解析器，比如将返回的不符合期望格式的输出，尝试修正为正确的结构化数据（如 JSON）
- **RetryOutputParser**：重试解析器，当主解析器（如 JSONOutputParser）因格式错误无法解析 LLM 的输出时，通过调用另一个 LLM 自动修复错误，并重新尝试解析

### 5.2 具体解析器的使用

#### ① 字符串解析器 StrOutputParser

`StrOutputParser` 简单地将任何输入转换为字符串。它是一个简单的解析器，从结果中提取 content 字段。

**举例：将一个对话模型的输出结果，解析为字符串输出**
```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

chat_model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(content="将以下内容从英语翻译成中文"),
    HumanMessage(content="It's a nice day today"),
]

result = chat_model.invoke(messages)
print(type(result))    # <class 'langchain_core.messages.ai.AIMessage'>
print(result)

parser = StrOutputParser()
# 使用 parser 处理 model 返回的结果
response = parser.invoke(result)
print(type(response))  # <class 'str'>
print(response)        # 今天是个好天气。
```

#### ② JSON 解析器 JsonOutputParser

`JsonOutputParser` 即 JSON 输出解析器，是一种用于将大模型的自由文本输出转换为结构化 JSON 数据的工具。

**适合场景**：特别适用于需要严格结构化输出的场景，比如 API 调用、数据存储或下游任务处理。

**实现方式：**
- **方式1**：用户自己通过提示词指明返回 json 格式
- **方式2**：借助 JsonOutputParser 的 `get_format_instructions()`，生成格式说明，指导模型输出 JSON 结构

**举例1：**
```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

chat_model = ChatOpenAI(model="gpt-4o-mini")

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个靠谱的{role}"),
    ("human", "{question}")
])

parser = JsonOutputParser()

# 方式1：在提示词中指定返回 JSON 格式
result = chat_model.invoke(chat_prompt_template.format_messages(
    role="人工智能专家",
    question="人工智能用英文怎么说？问题用q表示，答案用a表示，返回一个JSON格式"
))
parser.invoke(result)

# 方式2：使用 chain
# chain = chat_prompt_template | chat_model | parser
# chain.invoke({"role": "人工智能专家", "question": "人工智能用英文怎么说？..."})
```

**输出：**
```python
{'q': '人工智能用英文怎么说？', 'a': 'Artificial Intelligence'}
```

**举例2：使用指定的 JSON 格式**
```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

output_parser = JsonOutputParser()
# 返回一些指令或模板，这些指令告诉系统如何解析或格式化输出数据
format_instructions = output_parser.get_format_instructions()
print(format_instructions)

# 基于此：
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

# 初始化语言模型
chat_model = ChatOpenAI(model="gpt-4o-mini")

joke_query = "告诉我一个笑话。"

# 定义 Json 解析器
parser = JsonOutputParser()

# 定义提示词模板
# 注意，提示词模板中需要部分格式化解析器的格式要求 format_instructions
prompt = PromptTemplate(
    template="回答用户的查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 使用 LCEL 语法组合一个简单的链
chain = prompt | chat_model | parser
# 执行链
output = chain.invoke({"query": "给我讲一个笑话"})
print(output)
# {'joke': '为什么海洋总是咸的？因为它有太多的"海湿的事情发送"...'}
```

#### ③ XML 解析器 XMLOutputParser

`XMLOutputParser` 将模型的自由文本输出转换为可编程处理的 XML 数据。

**如何实现**：在 PromptTemplate 中指定 XML 格式要求，让模型返回 `<tag>content</tag>` 形式的数据。

> 注意：XMLOutputParser 不会直接将模型的输出保持为原始 XML 字符串，而是会解析 XML 并转换成 Python 字典（或类似结构化的数据）。目的是为了方便程序后续处理数据，而不是单纯保留 XML 格式。

**举例1：不使用 XMLOutputParser，通过大模型的能力，返回 xml 格式数据**
```python
# 初始化语言模型
chat_model = ChatOpenAI(model="gpt-4o-mini")

# 测试模型的 xml 解析效果
actor_query = "生成汤姆·汉克斯的简短电影作品列表"
output = chat_model.invoke(
    f"""{actor_query}请将电影附在<movie></movie>标签中。"""
)
print(output.content)
```

**举例2：体会 XMLOutputParser 的格式**
```python
from langchain_core.output_parsers import XMLOutputParser

output_parser = XMLOutputParser()
format_instructions = output_parser.get_format_instructions()
print(format_instructions)
```

**输出格式说明：**
```
The output should be formatted as a XML file.
1. Output should conform to the tags below.
2. If tags are not given, make them on your own.
3. Remember to always open and close all the tags.

As an example, for the tags ["foo", "bar", "baz"]:
1. String "<foo><bar><baz></baz></bar></foo>" is a well-formatted instance.
...
```

**举例3：XMLOutputParser 的使用**
```python
# 1. 导入相关包
from langchain_core.output_parsers import XMLOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 2. 初始化语言模型
chat_model = ChatOpenAI(model="gpt-4o-mini")

actor_query = "生成汤姆·汉克斯的简短电影作品列表"

# 4. 定义 XMLOutputParser 对象
parser = XMLOutputParser()

# 5. 定义提示词模板对象
prompt_template = PromptTemplate.from_template("{query}\n{format_instructions}")
prompt_template1 = prompt_template.partial(
    format_instructions=parser.get_format_instructions()
)

response = chat_model.invoke(prompt_template1.format(query=actor_query))
print(response.content)

# 继续：
# 方式1
response = chat_model.invoke(prompt_template1.format(query=actor_query))
result = parser.invoke(response)
print(result)
print(type(result))  # <class 'dict'>

# 方式2
# chain = prompt_template1 | chat_model | parser
# result = chain.invoke({"query": actor_query})
# print(result)
```

**举例4：与前例类似**
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import XMLOutputParser

model = ChatOpenAI(model="gpt-4o-mini")

actor_query = "生成周星驰的简化电影作品列表，按照最新的时间降序，必要时使用中文"
# 设置解析器 + 将指令注入提示模板。
parser = XMLOutputParser()
prompt = PromptTemplate(
    template="回答用户的查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser
result = chain.invoke({"query": actor_query})
print(result)
```

#### ④ 列表解析器 CommaSeparatedListOutputParser

列表解析器：利用此解析器可以将模型的文本响应转换为一个用逗号分隔的列表（`List[str]`）。

**举例1：**
```python
from langchain_core.output_parsers import CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()

# 返回一些指令或模板，这些指令告诉系统如何解析或格式化输出数据
format_instructions = output_parser.get_format_instructions()
print(format_instructions)
# Your response should be a list of comma separated values, eg: foo, bar, baz or foo,bar,baz
```

**举例2：**
```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser

# 初始化语言模型
chat_model = ChatOpenAI(model="gpt-4o-mini")

# 创建解析器
output_parser = CommaSeparatedListOutputParser()

# 创建 LangChain 提示模板
chat_prompt = PromptTemplate.from_template(
    "生成5个关于{text}的列表\n\n{format_instructions}",
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()
    }
)

# 将提示和模型合并以进行调用
chain = chat_prompt | chat_model | output_parser
res = chain.invoke({"text": "电影"})
print(res)
print(type(res))
# ['经典电影', '现代电影', '动作电影', '爱情电影', '科幻电影']
# <class 'list'>
```

**举例3：**
```python
from langchain.prompts.chat import HumanMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser

# 初始化语言模型
chat_model = ChatOpenAI(model="gpt-4o-mini")

output_parser = CommaSeparatedListOutputParser()

chat_prompt = ChatPromptTemplate.from_messages([
    ("human", "{request}\n{format_instructions}")
])

# 方式3：LCEL 链
chain = chat_prompt | chat_model | output_parser
resp = chain.invoke({
    "request": "给我5个心情",
    "format_instructions": output_parser.get_format_instructions()
})
print(resp)
print(type(resp))
# ['快乐', '忧伤', '愁怒', '安宁', '宁静']
# <class 'list'>
```

#### ⑤ 日期解析器 DatetimeOutputParser（了解）

利用此解析器可以直接将 LLM 输出解析为日期时间格式。

`get_format_instructions()` 指令为：`Write a datetime string that matches the following pattern: '%Y-%m-%dT%H:%M:%S.%fZ'`

**举例：** `2016-08-16T17:39:06.176399Z`

**举例1：**
```python
from langchain.output_parsers import DatetimeOutputParser

output_parser = DatetimeOutputParser()

format_instructions = output_parser.get_format_instructions()
print(format_instructions)
# Write a datetime string that matches the following pattern: '%Y-%m-%dT%H:%M:%S.%fZ'.
# Examples: 1563-09-27T04:28:14.640366Z, 1786-06-24T23:46:01.984421Z, ...
# Return ONLY this string, no other words!
```

**举例2：**
```python
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import DatetimeOutputParser

chat_model = ChatOpenAI(model="gpt-4o-mini")

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "{format_instructions}"),
    ("human", "{request}")
])

output_parser = DatetimeOutputParser()

# 方式2：LCEL 链
chain = chat_prompt | chat_model | output_parser
resp = chain.invoke({
    "request": "中华人民共和国是什么时候成立的",
    "format_instructions": output_parser.get_format_instructions()
})
print(resp)
print(type(resp))
# 1949-10-01 00:00:00
# <class 'datetime.datetime'>
```

## 6. LangChain 调用本地模型

### 6.1 Ollama 的介绍

Ollama 是在 GitHub 上的一个开源项目，其项目定位是：一个本地运行大模型的集成框架。目前主要针对主流的 LlaMA 架构的开源大模型设计，可以实现如 Qwen、Deepseek 等主流大模型的下载、启动和本地运行的自动化部署及推理流程。

目前作为一个非常热门的大模型托管平台，已被包括 LangChain、Taskweaver 等在内的多个热门项目高度集成。

**Ollama 官方地址**：https://ollama.com/

### 6.2 Ollama 的下载/安装

Ollama 项目支持跨平台部署，目前已兼容 Mac、Linux 和 Windows 操作系统。特别地对于 Windows 用户提供了非常直观的预览版。

![](<images/Pasted image 20260507165841.png>)

无论使用哪个操作系统，Ollama 项目的安装过程都设计得非常简单。

- **Windows 系统**：执行 `.exe` 文件安装（大约 71M 大小）
- **Linux 系统**：执行以下命令安装：
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```
  这行命令的目的是从 https://ollama.com/ 网站读取 install.sh 脚本，并立即通过 sh 执行该脚本，在安装过程中会包含以下几个主要的操作：
  1. 检查当前服务器的基础环境，如系统版本等
  2. 下载 Ollama 的二进制文件
  3. 配置系统服务，包括创建用户和用户组，添加 Ollama 的配置信息
  4. 启动 Ollama 服务

### 6.3 模型的下载/安装

访问 https://ollama.com/search 可以查看 Ollama 支持的模型。使用命令行可以下载并运行模型，例如运行 deepseek-r1:7b 模型：

```bash
ollama run deepseek-r1:7b
```

### 6.4 调用本地私有模型

**举例1：**
```python
from langchain_community.chat_models import ChatOllama
# from langchain_ollama import ChatOllama

ollama_llm = ChatOllama(model="deepseek-r1:7b")

from langchain_core.messages import HumanMessage

messages = [
    HumanMessage(content="你好，请介绍一下你自己")
]

chat_model_response = ollama_llm.invoke(messages)
print(chat_model_response.content)
# 您好！我是由中国的深度求索（DeepSeek）公司开发的智能助手——DeepSeek-R1。如您有任何问题，我会尽我所能为您提供帮助。
```

> 若 Ollama 不在本地默认端口运行，需指定 base_url，即：
> ```python
> ollama_llm = ChatOllama(
>     model="deepseek-r1:7b",
>     base_url="http://your-ip:port"  # 自定义地址
> )
> ```

**举例2：**
```python
from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

# 生成对话形式的聊天信息格式
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个有用的助手，可以将{input_language}翻译成{output_language}。"),
    ("human", "{text}"),
])

# 格式化变量输入
messages = chat_prompt.format_messages(
    input_language="中文",
    output_language="英语",
    text="我爱编程"
)

# 实例化 Ollama 启动的模型
ollama_llm = ChatOllama(model="deepseek-r1:7b")

# 执行推理
result = ollama_llm.invoke(messages)
print(result.content)
# I love programming.
```

