# 第04章：LangChain 使用之 Memory

## 1. Memory 概述

### 1.1 为什么需要 Memory

大多数大模型应用程序都会提供一个会话接口，允许进行多轮对话，并表现出一定的上下文记忆能力。

![](images/Pasted%20image%2020260507225334.png)

但实际上，**模型本身并不会主动记忆上下文**，它只能基于当前输入来生成输出。

![](images/Pasted%20image%2020260507225420.png)

因此，如果我们希望应用具备“记忆能力”，就需要额外的模块来保存用户与模型之间的历史对话信息，并在下一次请求时，把这些历史信息重新传给模型。这样模型才能基于上下文生成更连贯的回答。

在 LangChain 中，这个负责保存和管理上下文的模块就叫做 **Memory（记忆）**。

---

### 1.2 什么是 Memory

Memory 是 LangChain 中用于在多轮对话中保存和管理上下文信息的组件。它可以存储的信息不仅限于文本，还可以扩展到图像、音频等内容。

它的作用是让应用“记住”用户之前说过什么，从而使对话具备上下文感知能力，为构建真正智能的链式对话系统提供基础支持。

---

### 1.3 Memory 的设计理念

![](images/Pasted%20image%2020260507225429.png)

Memory 在链中的工作流程可以概括为：

1. **输入问题**  
   用户输入当前问题，例如：`{"question": ...}`。

2. **读取历史消息**  
   从 Memory 中读取历史上下文，例如：`{"past_messages": [...]}`。

3. **构建 Prompt**  
   将历史消息与当前问题拼接，形成新的提示词（Prompt）。

4. **模型处理**  
   把构建好的 Prompt 传递给语言模型，由模型生成回答。

5. **解析输出**  
   对模型返回结果做解析，例如通过输出解析器提取：`{"answer": ...}`。

6. **写回 Memory**  
   将当前问题与模型新生成的回答一起写入 Memory，更新对话历史，供后续轮次继续使用。

### 一个链会与 Memory 交互几次？

如果一个链接入了 Memory 模块，那么在一次调用过程中，通常会与 Memory 发生 **两次交互**：

1. **读取**：
   - 接收到用户输入后，从 Memory 中查询相关历史信息。
   - 将历史信息与当前输入一起拼接到 Prompt 中，传给 LLM。

2. **写入**：
   - 在返回响应前，把本次用户输入和 LLM 输出写回 Memory。
   - 供下一次对话继续使用。

---

### 1.4 不使用 Memory 模块，如何拥有记忆

即使不借助 LangChain，我们也可以通过手动维护一个 `messages` 列表来实现“记忆能力”。

核心思路是：

- 每轮对话后，把用户消息和模型回复都追加到消息列表中；
- 下一轮调用模型时，把整个历史消息列表一并传入；
- 这样模型就能“看到”上下文，从而实现多轮对话。

### 示例：初始化模型

```python
import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

# 创建大模型实例
llm = ChatOpenAI(model="gpt-4o-mini")
```

### 示例：通过追加消息实现上下文记忆

```python
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOpenAI(model="gpt-4o-mini")


def chat_with_model(question):
    # 步骤一：初始化消息
    chat_prompt_template = ChatPromptTemplate.from_messages([
        ("system", "你是一位人工智能小助手"),
        ("human", "{question}")
    ])

    # 步骤二：定义一个循环体
    while True:
        # 步骤三：调用模型
        chain = chat_prompt_template | llm
        response = chain.invoke({"question": question})

        # 步骤四：获取模型回答
        print(f"模型回答: {response.content}")

        # 询问用户是否还有其他问题
        user_input = input("您还有其他问题想问嘛？(输入'退出'结束对话)")

        # 设置结束循环的条件
        if user_input == "退出":
            break

        # 步骤五：记录用户回答
        chat_prompt_template.messages.append(AIMessage(content=response.content))
        chat_prompt_template.messages.append(HumanMessage(content=user_input))


chat_with_model("你好")
```

### 示例对话

```text
1 > 你好
2 > 李白很白吗？
3 > 刚才我聊的诗人是谁？
4 > 他有哪些著名的诗篇
5 > 退出
```

### 小结

这种方式是最简单的一种让大模型具备上下文记忆能力的方法。

**本质上，任何记忆能力的基础，都是对历史对话记录的保存。**
即使这些历史消息不会被完整地直接使用，也需要以某种形式被存储下来。

---

## 2. 基础 Memory 模块的使用

### 2.1 Memory 模块的设计思路

如何设计 Memory 模块？可以从简单到复杂分为几个层次：

#### 层次 1：最直接的方式
保留一个完整的聊天消息列表。

#### 层次 2：简单优化
只返回最近交互的 `k` 条消息。

#### 层次 3：进一步优化
返回过去 `k` 条消息的简洁摘要。

#### 层次 4：更复杂的策略
从存储消息中提取实体，只返回与当前问题相关的实体信息。

### LangChain 的设计

针对上述不同层次的需求，LangChain 提供了一系列可以直接使用的 Memory 工具，用于存储和管理聊天消息。

![](Pasted%20image%2020260507225508.png)

---

### 2.2 ChatMessageHistory（基础）

`ChatMessageHistory` 是一个用于存储和管理对话消息的基础类。它直接操作消息对象（如 `HumanMessage`、`AIMessage` 等），是其他 Memory 组件常用的底层存储工具。

在 API 文档中，`ChatMessageHistory` 还有一个别名类：

- `InMemoryChatMessageHistory`

导包方式：

```python
from langchain.memory import ChatMessageHistory
```

### 特点

- 它本质上是一个消息对象的“存储器”；
- 与缓冲、窗口、摘要等记忆策略无关；
- 不负责消息格式化，例如不会自动转成字符串文本。

---

### 场景 1：记忆存储

```python
# 1. 导入相关包
from langchain.memory import ChatMessageHistory

# 2. 实例化 ChatMessageHistory 对象
history = ChatMessageHistory()

# 3. 添加 UserMessage
history.add_user_message("hi!")

# 4. 添加 AIMessage
history.add_ai_message("whats up?")

# 5. 返回存储的所有消息列表
print(history.messages)
```

输出示意：

```python
[
    HumanMessage(content='hi!', additional_kwargs={}, response_metadata={}),
    AIMessage(content='whats up?', additional_kwargs={}, response_metadata={})
]
```

---

### 场景 2：对接 LLM

```python
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()

history.add_ai_message("我是一个无所不能的小智")
history.add_user_message("你好，我叫小明，请介绍一下你自己")
history.add_user_message("我是谁呢？")

print(history.messages)  # 返回 List[BaseMessage] 类型
```

继续调用模型：

```python
# 创建 LLM
llm = ChatOpenAI(model_name='gpt-4o-mini')

llm.invoke(history.messages)
```

这种方式说明：

- `ChatMessageHistory` 可以单独保存历史消息；
- 也可以直接把这些历史消息传给模型，作为上下文输入。

---

### 2.3 ConversationBufferMemory

`ConversationBufferMemory` 是一个基础的对话记忆组件，专门用于**按原始顺序完整保存对话历史**。

### 适用场景

适合：

- 对话轮次较少；
- 高度依赖完整上下文；
- 例如简单聊天机器人等场景。

### 特点

- 完整存储对话历史；
- 简单直接；
- 不做裁剪；
- 不做压缩；
- 能够与 Chains / Models 无缝集成；
- 支持两种返回格式。

### 返回格式

通过 `return_messages` 参数控制：

- `return_messages=True`：返回消息对象列表 `List[BaseMessage]`
- `return_messages=False`（默认）：返回拼接后的纯文本字符串

---

### 场景 1：入门使用

#### 示例 1

```python
from langchain.memory import ConversationBufferMemory

# 实例化 ConversationBufferMemory 对象
memory = ConversationBufferMemory()

# 保存消息到内存中
memory.save_context(
    inputs={"input": "你好，我是人类"},
    outputs={"output": "你好，我是AI助手"}
)
memory.save_context(
    inputs={"input": "很开心认识你"}, outputs={"output": "我也是"}
)

# 读取内存中消息（返回纯文本）
print(memory.load_memory_variables({}))
```

输出示意：

```python
{
    "history": "Human: 你好，我是人类\nAI: 你好，我是AI助手\nHuman: 很开心认识你\nAI: 我也是"
}
```

#### 注意

- 不管 `inputs`、`outputs` 的 key 具体叫什么，默认都会把：
  - `inputs` 视为 `Human`
  - `outputs` 视为 `AI`
- 返回结果中的默认字段名是 `history`；
- 可以通过 `ConversationBufferMemory` 的 `memory_key` 属性修改这个字段名。

---

#### 示例 2

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)

# 保存消息到内存中
memory.save_context({"input": "hi"}, {"output": "whats up"})

# 读取内存中消息（返回消息对象）
print(memory.load_memory_variables({}))

# 访问原始消息列表
print(memory.chat_memory.messages)
```

输出示意：

```python
{
    "history": [
        HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),
        AIMessage(content='whats up', additional_kwargs={}, response_metadata={})
    ]
}

[
    HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),
    AIMessage(content='whats up', additional_kwargs={}, response_metadata={})
]
```

---

### 场景 2：结合 Chain

#### 示例 1：使用 `PromptTemplate`

```python
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate

# 初始化大模型
llm = OpenAI(model="gpt-4o-mini", temperature=0)

# 创建提示
# 有两个输入键：实际输入与来自记忆类的输入
# 需确保 PromptTemplate 和 ConversationBufferMemory 中的键匹配
template = """你可以与人类对话。

当前对话: {history}

人类问题: {question}

回复:
"""

prompt = PromptTemplate.from_template(template)

# 创建 ConversationBufferMemory
memory = ConversationBufferMemory()

# 初始化链
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

# 提问
res1 = chain.invoke({"question": "我的名字叫Tom"})
print(res1)
```

第一次调用结果示意：

```python
{
    "question": "我的名字叫Tom",
    "history": "",
    "text": "你好，Tom！很高兴认识你。你今天过得怎么样？有什么我可以帮助你的吗？"
}
```

继续调用：

```python
res = chain.invoke({"question": "我的名字是什么?"})
print(res)
```

第二次调用结果示意：

```python
{
    "question": "我的名字是什么?",
    "history": "Human: 我的名字叫Tom\nAI: 你好，Tom！很高兴认识你。你今天过得怎么样？有什么我可以帮助你的吗？",
    "text": "你的名字是Tom。你今天过得怎么样？有什么我可以帮助你的吗？"
}
```

这个例子说明：

- 第一次提问时，`history` 为空；
- 第二次提问时，模型已经可以读取上一轮对话；
- `ConversationBufferMemory` 自动完成了上下文的存取。

---

#### 示例 2：通过 `memory_key` 修改变量名

```python
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate

# 初始化大模型
llm = OpenAI(model="gpt-4o-mini", temperature=0)

# 创建提示
# 有两个输入键：实际输入与来自记忆类的输入
# 需确保 PromptTemplate 和 ConversationBufferMemory 中的键匹配
template = """你可以与人类对话。

当前对话: {chat_history}

人类问题: {question}

回复:
"""

prompt = PromptTemplate.from_template(template)

# 创建 ConversationBufferMemory
memory = ConversationBufferMemory(memory_key="chat_history")

# 初始化链
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

# 提问
res1 = chain.invoke({"question": "我的名字叫Tom"})
print(str(res1) + "\n")

res = chain.invoke({"question": "我的名字是什么?"})
print(res)
```

输出示意：

```python
{
    "question": "我的名字叫Tom",
    "chat_history": "",
    "text": "你好，Tom！很高兴认识你。有什么我可以帮助你的吗？"
}

{
    "question": "我的名字是什么?",
    "chat_history": "Human: 我的名字叫Tom\nAI: 你好，Tom！很高兴认识你。有什么我可以帮助你的吗？",
    "text": "你的名字是Tom。很高兴再次见到你！有什么我可以帮助你的吗？"
}
```

### 使用说明补充

创建带 Memory 功能的 `LLMChain` 时，并不能像普通 LCEL 那样完全统一地使用管道写法；同样，`LLMChain` 也不能直接再通过管道去接 `StrOutputParser`。这也是很多人觉得当前 Memory 模块相对更像 Beta 形态的原因之一。

---

#### 示例 3：使用 `ChatPromptTemplate` 和 `return_messages`

```python
from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 创建 LLM
llm = ChatOpenAI(model_name='gpt-4o-mini')

# 创建 Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个与人类对话的机器人。"),
    MessagesPlaceholder(variable_name='history'),
    ("human", "问题：{question}")
])

# 创建 Memory
memory = ConversationBufferMemory(return_messages=True)

# 创建 LLMChain
llm_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)

# 调用 LLMChain
res1 = llm_chain.invoke({"question": "中国首都在哪里？"})
print(res1, end="\n\n")

res2 = llm_chain.invoke({"question": "我刚刚问了什么"})
print(res2)
```

输出示意：

```python
{
    "question": "中国首都在哪里？",
    "history": [
        HumanMessage(content='中国首都在哪里？', additional_kwargs={}, response_metadata={}),
        AIMessage(content='中国的首都是北京市。', additional_kwargs={}, response_metadata={})
    ],
    "text": "中国的首都是北京市。"
}

{
    "question": "我刚刚问了什么",
    "history": [
        HumanMessage(content='中国首都在哪里？', additional_kwargs={}, response_metadata={}),
        AIMessage(content='中国的首都是北京市。', additional_kwargs={}, response_metadata={}),
        HumanMessage(content='我刚刚问了什么', additional_kwargs={}, response_metadata={}),
        AIMessage(content='你刚刚问了中国的首都在哪里。', additional_kwargs={}, response_metadata={})
    ],
    "text": "你刚刚问了中国的首都在哪里。"
}
```

### `PromptTemplate` 与 `ChatPromptTemplate` 对比

| 特性 | 普通 `PromptTemplate` | `ChatPromptTemplate` |
|---|---|---|
| 历史存储时机 | 仅执行后存储 | 执行前存储用户输入 + 执行后存储输出 |
| 首次调用显示 | 仅显示问题，历史仍为空字符串 | 显示完整问答对 |
| 内部消息类型 | 拼接字符串 | `List[BaseMessage]` |

### 注意

我们观察到的现象并不是 bug，而是 LangChain 为了保障对话一致性所做的刻意设计：

1. 用户提问后，系统应立即“记住”该问题；
2. AI 回答后，该响应也应立刻加入上下文；
3. 返回给客户端的结果应当体现最新状态。

---

### 2.4 ConversationChain

`ConversationChain` 本质上是对 `ConversationBufferMemory` 和 `LLMChain` 的进一步封装，并提供了一套默认的 Prompt 模板，从而简化了初始化流程。

换句话说，它就是一个更方便的“开箱即用版对话链”。

#### 示例 1：使用自定义 `PromptTemplate`

```python
from langchain.chains.conversation.base import ConversationChain
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

# 初始化大模型
llm = ChatOpenAI(model="gpt-4o-mini")

template = """以下是人类与AI之间的友好对话描述。AI表现得很健谈，并提供了大量来自其上下文的具体细节。
如果AI不知道问题的答案，它会真诚地表示不知道。

当前对话：
{history}
Human: {input}
AI:"""

prompt = PromptTemplate.from_template(template)

chain = ConversationChain(llm=llm, prompt=prompt, verbose=True)

chain.invoke({"input": "你好，你的名字叫小智"})
chain.invoke({"input": "你好，你叫什么名字？"})
```

输出示意：

```python
{
    "input": "你好，你的名字叫小智",
    "history": "",
    "response": "你好！是的，我叫小智。很高兴和你聊聊！你想讨论些什么呢？"
}

{
    "input": "你好，你叫什么名字？",
    "history": "Human: 你好，你的名字叫小智\nAI: 你好！是的，我叫小智。很高兴和你聊聊！你想讨论些什么呢？",
    "response": "你好！我叫小智。很高兴见到你！有什么想聊的话题吗？"
}
```

> 注意：`ConversationChain` 中默认的输入键名必须是 `input`，否则会报错。

---

#### 示例 2：使用内置默认 Prompt 模板

`ConversationChain` 内置的默认模板本身就包含 `input` 和 `history` 两个变量，因此可以直接使用。

```python
from langchain_openai import ChatOpenAI
from langchain.chains.conversation.base import ConversationChain

# 初始化大语言模型
llm = ChatOpenAI(model="gpt-4o-mini")

# 初始化对话链
conv_chain = ConversationChain(llm=llm)

# 进行对话
result1 = conv_chain.invoke(input="小明有1只猫")
result2 = conv_chain.invoke(input="小刚有2只狗")
result3 = conv_chain.invoke(input="小明和小刚一共有几只宠物?")

print(result3)
```

输出示意：

```text
小明有一只猫，小刚有两只狗，所以他们一共有三只宠物。
```

---

### 2.5 ConversationBufferWindowMemory

在了解了 `ConversationBufferMemory` 之后，我们知道它会不断把所有历史对话追加到 `history` 中，这样虽然能保留完整上下文，但也会带来两个明显问题：

1. 内存占用越来越大；
2. 消耗的 token 越来越多；
3. 还会受到模型最大上下文窗口的限制。

而很多很早之前的对话，其实对当前问题已经没有价值了。

LangChain 给出的解决方案就是：`ConversationBufferWindowMemory`。

它只保留最近 `K` 轮交互，从而让上下文窗口始终保持在一个可控范围内。

### 特点

- 适合长对话场景；
- 与 Chains / Models 无缝集成；
- 支持两种返回格式；
- 可以只关注最近若干轮对话。

### 返回格式

通过 `return_messages` 参数控制：

- `return_messages=True`：返回消息对象列表；
- `return_messages=False`（默认）：返回拼接的纯文本字符串。

---

#### 场景 1：入门使用

##### 示例 1

```python
from langchain.memory import ConversationBufferWindowMemory

# 实例化对象，设定窗口阈值
memory = ConversationBufferWindowMemory(k=2)

# 保存消息
memory.save_context({"input": "你好"}, {"output": "怎么了"})
memory.save_context({"input": "你是谁"}, {"output": "我是AI助手"})
memory.save_context({"input": "你的生日是哪天？"}, {"output": "我不清楚"})

# 读取消息
print(memory.load_memory_variables({}))
```

输出示意：

```python
{
    "history": "Human: 你是谁\nAI: 我是AI助手\nHuman: 你的生日是哪天？\nAI: 我不清楚"
}
```

可以看到，最早的一轮“你好 / 怎么了”已经被窗口裁掉了。

---

##### 示例 2：配合聊天模型使用

```python
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=2, return_messages=True)

memory.save_context({"input": "你好"}, {"output": "怎么了"})
memory.save_context({"input": "你是谁"}, {"output": "我是AI助手小智"})
memory.save_context(
    {"input": "初次对话，你能介绍一下你自己吗？"},
    {"output": "当然可以了。我是一个无所不能的小智。"}
)

print(memory.load_memory_variables({}))
```

输出示意：

```python
{
    "history": [
        HumanMessage(content='你是谁', additional_kwargs={}, response_metadata={}),
        AIMessage(content='我是AI助手小智', additional_kwargs={}, response_metadata={}),
        HumanMessage(content='初次对话，你能介绍一下你自己吗？', additional_kwargs={}, response_metadata={}),
        AIMessage(content='当然可以了。我是一个无所不能的小智。', additional_kwargs={}, response_metadata={})
    ]
}
```

---

#### 场景 2：结合 Chain

```python
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts.prompt import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI

template = """以下是人类与AI之间的友好对话描述。AI表现得很健谈，并提供了大量来自其上下文的具体细节。
如果AI不知道问题的答案，它会表示不知道。

当前对话：
{history}
Human: {question}
AI:"""

prompt_template = PromptTemplate.from_template(template)
llm = ChatOpenAI(model="gpt-4o-mini")
memory = ConversationBufferWindowMemory(k=1)

conversation_with_summary = LLMChain(
    llm=llm,
    prompt=prompt_template,
    memory=memory,
    verbose=True,
)

response1 = conversation_with_summary.invoke({"question": "你好，我是孙小空"})
response2 = conversation_with_summary.invoke({"question": "我还有两个师弟，一个是猪小戒，一个是沙小僧"})
response3 = conversation_with_summary.invoke({"question": "我今年高考，竟然考上了1本"})
response4 = conversation_with_summary.invoke({"question": "我叫什么？"})

print(response4)
```

当 `k=1` 时，最后只保留最近一轮交互，所以模型可能无法记住最开始提到的名字。

输出示意：

```python
{
    "input": "我叫什么？",
    "history": "Human: 我今年高考，竟然考上了1本\nAI: 太棒了！恭喜你考上了1本，这真是一个了不起的成就！高考是一个重要的里程碑，你一定为了这个目标付出了很多努力。你打算选择什么专业呢？或者你对未来的大学生活有什么期待吗？",
    "text": "抱歉，我不知道你的名字。不过，我很高兴能与您进行交流！如果你愿意分享更多关于你的事情，比如你的兴趣或未来的计划，我会很乐意听！"
}
```

### 思考：如果把 `k=1` 改成 `k=3` 会怎样？

如果窗口扩大到 `k=3`，模型就能保留更多最近对话，于是有机会回忆起更早的信息：

```python
{
    "input": "我叫什么？",
    "history": "Human: 你好，我是孙小空\nAI: 你好，孙小空！很高兴和你交流。有什么我可以帮助你的吗？\nHuman: 我还有两个师弟，一个是猪小戒，一个是沙小僧\nAI: 你们的名字听起来很有趣，似乎有点像《西游记》中的角色！猪小戒和沙小僧一定也很特别。你们平时一起做些什么呢？\nHuman: 我今年高考，竟然考上了1本\nAI: 太棒了，恭喜你考上了本科！这是一个重要的里程碑，你一定为自己感到骄傲。你打算大学学什么专业呢？或者有什么特别的目标和期待吗？",
    "text": "你叫孙小空！如果我没记错的话，这个名字很有个性。你喜欢这个名字吗？"
}
```

---

## 3. 其他 Memory 模块

### 3.1 ConversationTokenBufferMemory

`ConversationTokenBufferMemory` 是一种**基于 Token 数量进行裁剪**的记忆机制。

它不是按“轮数”裁剪，而是按 token 总量来控制历史长度：

- 超过上限时，会裁掉较早的部分；
- 尽量保留最近的交流；
- 更贴近模型真实的上下文消耗方式。

### 特点

- Token 精准控制；
- 保留原始对话形式；
- 适合需要精细控制上下文长度的场景。

![](Pasted%20image%2020260507225609.png)

---

#### 示例：不同 `max_token_limit` 的差异

##### 情况 1：阈值过小

```python
from langchain.memory import ConversationTokenBufferMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

memory = ConversationTokenBufferMemory(
    llm=llm,
    max_token_limit=10
)

memory.save_context({"input": "你好吗？"}, {"output": "我很好，谢谢！"})
memory.save_context({"input": "今天天气如何？"}, {"output": "晴天，25度"})

print(memory.load_memory_variables({}))
```

输出示意：

```python
{"history": ""}
```

因为 token 限制太小，历史消息几乎都保不住。

##### 情况 2：阈值适中

```python
from langchain.memory import ConversationTokenBufferMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

memory = ConversationTokenBufferMemory(
    llm=llm,
    max_token_limit=50
)

memory.save_context({"input": "你好吗？"}, {"output": "我很好，谢谢！"})
memory.save_context({"input": "今天天气如何？"}, {"output": "晴天，25度"})

print(memory.load_memory_variables({}))
```

输出示意：

```python
{
    "history": "Human: 你好吗？\nAI: 我很好，谢谢！\nHuman: 今天天气如何？\nAI: 晴天，25度"
}
```

---

### 3.2 ConversationSummaryMemory

前面的几种方式要么保留全部历史，要么简单截断。问题在于：

- 全保留会太浪费；
- 仅按轮数或 token 截断，又可能误删重要信息。

因此 LangChain 提供了 `ConversationSummaryMemory`。

它的核心思路是：

> 不再保存完整原始对话，而是让 LLM 自动生成一份“对话摘要”，并不断更新这份摘要。

这特别适合**长对话**和**需要保留核心信息**的场景。

### 特点

- 自动生成摘要；
- 动态更新摘要内容；
- 用更少上下文保留更关键的信息。

### 原理

![](Pasted%20image%2020260507225641.png)

---

#### 场景 1：没有历史消息时，直接构造

```python
from langchain.memory import ConversationSummaryMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
memory = ConversationSummaryMemory(llm=llm)

memory.save_context({"input": "你好"}, {"output": "怎么了"})
memory.save_context({"input": "你是谁"}, {"output": "我是AI助手小智"})
memory.save_context(
    {"input": "初次对话，你能介绍一下你自己吗？"},
    {"output": "当然可以了。我是一个无所不能的小智。"}
)

print(memory.load_memory_variables({}))
```

输出示意：

```python
{
    "history": "The human greets the AI in Chinese by saying 'hello', and the AI responds by asking, 'What's wrong?' The human then asks, 'Who are you?' and the AI replies, 'I am AI assistant Xiao Zhi.' Additionally, the human asks for a self-introduction, and the AI describes itself as an all-capable assistant named Xiao Zhi."
}
```

---

#### 场景 2：已有历史消息时，使用 `from_messages()`

```python
from langchain.memory import ConversationSummaryMemory, ChatMessageHistory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

history = ChatMessageHistory()
history.add_user_message("你好，你是谁？")
history.add_ai_message("我是AI助手小智")

memory = ConversationSummaryMemory.from_messages(
    llm=llm,
    chat_memory=history,
)

print(memory.load_memory_variables({}))

memory.save_context(
    inputs={"human": "我的名字叫小明"},
    outputs={"AI": "很高兴认识你"}
)

print(memory.load_memory_variables({}))
print(memory.chat_memory.messages)
```

输出示意：

```python
{
    "history": "The human greets the AI and asks who it is. The AI responds that it is an AI assistant named Xiao Zhi."
}

{
    "history": "The human greets the AI and asks who it is. The AI responds that it is an AI assistant named Xiao Zhi. The human introduces themselves as Xiao Ming, and the AI expresses pleasure in meeting them."
}

[
    HumanMessage(content='你好，你是谁？', additional_kwargs={}, response_metadata={}),
    AIMessage(content='我是AI助手小智', additional_kwargs={}, response_metadata={}),
    HumanMessage(content='我的名字叫小明', additional_kwargs={}, response_metadata={}),
    AIMessage(content='很高兴认识你', additional_kwargs={}, response_metadata={})
]
```

### 小结

`ConversationSummaryMemory` 的核心价值在于：

- 原始消息仍可存在于底层历史中；
- 但真正给模型看的，是更紧凑的摘要；
- 从而在长对话里兼顾上下文质量与成本。

---

### 3.3 ConversationSummaryBufferMemory

`ConversationSummaryBufferMemory` 是一种**混合型记忆机制**。

它结合了：

- `ConversationBufferMemory`：保留最近的原始对话；
- `ConversationSummaryMemory`：把更早的内容压缩成摘要。

因此它非常适合这种场景：

> 既想保留最新几轮的完整细节，又不想让历史越来越长。

### 特点

- 保留最近若干轮原始消息；
- 较早历史会被自动摘要；
- 在“细节保真”和“成本控制”之间取得平衡。
### 原理

![](Pasted%20image%2020260507225717.png)

---

#### 场景 1：入门使用

##### 情况 1：`max_token_limit` 较小

```python
from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=40,
    return_messages=True
)

memory.save_context({"input": "你好，我的名字叫小明"}, {"output": "很高兴认识你，小明"})
memory.save_context({"input": "李白是哪个朝代的诗人"}, {"output": "李白是唐朝诗人"})
memory.save_context({"input": "唐宋八大家里有苏轼吗？"}, {"output": "有"})

print(memory.load_memory_variables({}))
print(memory.chat_memory.messages)
```

输出示意：

```python
{
    "history": [
        SystemMessage(content='The human introduces themselves as Xiao Ming, and the AI expresses pleasure in meeting them. The human then asks which dynasty the poet Li Bai belongs to.', additional_kwargs={}, response_metadata={}),
        AIMessage(content='李白是唐朝诗人', additional_kwargs={}, response_metadata={}),
        HumanMessage(content='唐宋八大家里有苏轼吗？', additional_kwargs={}, response_metadata={}),
        AIMessage(content='有', additional_kwargs={}, response_metadata={})
    ]
}
```

可以看到：较早的一部分对话已经被压缩成了一条 `SystemMessage` 摘要。

##### 情况 2：`max_token_limit` 较大

```python
from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=100,
    return_messages=True
)

memory.save_context({"input": "你好，我的名字叫小明"}, {"output": "很高兴认识你，小明"})
memory.save_context({"input": "李白是哪个朝代的诗人"}, {"output": "李白是唐朝诗人"})
memory.save_context({"input": "唐宋八大家里有苏轼吗？"}, {"output": "有"})

print(memory.load_memory_variables({}))
print(memory.chat_memory.messages)
```

输出示意：

```python
{
    "history": [
        HumanMessage(content='你好，我的名字叫小明', additional_kwargs={}, response_metadata={}),
        AIMessage(content='很高兴认识你，小明', additional_kwargs={}, response_metadata={}),
        HumanMessage(content='李白是哪个朝代的诗人', additional_kwargs={}, response_metadata={}),
        AIMessage(content='李白是唐朝诗人', additional_kwargs={}, response_metadata={}),
        HumanMessage(content='唐宋八大家里有苏轼吗？', additional_kwargs={}, response_metadata={}),
        AIMessage(content='有', additional_kwargs={}, response_metadata={})
    ]
}
```

当 token 限制更宽松时，历史消息就不需要被摘要，可以完整保留。

---

#### 场景 2：电商客服示例

```python
from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.llm import LLMChain

# 初始化大语言模型
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    max_tokens=500
)

# 定义提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是电商客服助手，用中文友好回复用户问题。保持专业但亲切的语气。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# 创建带摘要缓冲的记忆系统
memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=400,
    memory_key="chat_history",
    return_messages=True
)

# 创建对话链
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
)

# 模拟多轮对话
dialogue = [
    ("你好，我想查询订单12345的状态", None),
    ("这个订单是上周五下的", None),
    ("我现在急着用，能加急处理吗", None),
    ("等等，我可能记错订单号了，应该是12346", None),
    ("对了，你们退货政策是怎样的", None)
]

for user_input, _ in dialogue:
    response = chain.invoke({"input": user_input})
    print(f"用户: {user_input}")
    print(f"客服: {response['text']}\n")

print(memory.load_memory_variables({}))
```

### 这个例子体现了什么？

它很好地说明了 `ConversationSummaryBufferMemory` 的实战价值：

- 早期关于订单 `12345` 的沟通，会被压缩成摘要；
- 最近关于订单 `12346` 和退货政策的对话，仍以原始消息保留；
- 这样模型既不会丢失上下文，也不会让 Prompt 无限膨胀。

---

### 3.4 ConversationEntityMemory（了解）

`ConversationEntityMemory` 是一种**基于实体（Entity）的记忆机制**。

它不会只把历史当成普通文本，而是会主动识别对话中的关键实体，并存储这些实体及其属性、关系。常见实体包括：

- 人名
- 地点
- 产品
- 药物
- 组织
- 症状
- 时间等

### 好处

它可以有效解决“长对话中的信息过载问题”：

- 冗余寒暄可以被忽略；
- 关键事实会被保留下来；
- 尤其适合必须精确保留结构化事实的场景。

### 典型应用场景

例如在医疗等高风险领域，系统必须准确识别和保存关键信息：

```python
{"input": "我头痛，血压140/90，在吃阿司匹林。"}
{"output": "建议监测血压，阿司匹林可继续服用。"}
{"input": "我对青霉素过敏。"}
{"output": "已记录您的青霉素过敏史。"}
{"input": "阿司匹林吃了三天，头痛没缓解。"}
{"output": "建议停用阿司匹林，换布洛芬试试。"}
```

#### 如果使用 `ConversationSummaryMemory`

可能得到一段自然语言摘要：

```text
患者主诉头痛和高血压（140/90），正在服用阿司匹林。患者对青霉素过敏。三天后头痛未缓解，建议更换止痛药。
```

#### 如果使用 `ConversationEntityMemory`

则更可能保留下列结构化信息：

```python
{
    "症状": "头痛",
    "血压": "140/90",
    "当前用药": "阿司匹林（无效）",
    "过敏药物": "青霉素"
}
```

### `ConversationSummaryMemory` 与 `ConversationEntityMemory` 对比

| 维度 | `ConversationSummaryMemory` | `ConversationEntityMemory` |
|---|---|---|
| 表达形式 | 自然语言摘要 | 结构化字典 / 实体存储 |
| 下游利用方式 | 需要模型自己“读懂”摘要 | 可以直接按字段查询 |
| 防错可靠性 | 较低，依赖模型注意力 | 更高，可用代码强制校验 |
| 高风险场景适配 | 一般 | 更强 |

例如：

- 如果摘要里写了“对青霉素过敏”，模型仍可能忽略；
- 但如果实体记忆中有 `过敏药物=青霉素`，就可以直接在代码层面阻止推荐相关药物。

---

#### 示例：实体记忆的基本使用

```python
from langchain.chains.conversation.base import LLMChain
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name='gpt-4o-mini', temperature=0)

memory = ConversationEntityMemory(llm=llm)

chain = LLMChain(
    llm=llm,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    memory=memory,
)

chain.invoke(input="你好，我叫蜘蛛侠。我的好朋友包括钢铁侠、美国队长和绿巨人。")
chain.invoke(input="我住在纽约。")
chain.invoke(input="我使用的装备是由斯塔克工业提供的。")

print("\n当前存储的实体信息:")
print(chain.memory.entity_store.store)

answer = chain.invoke(input="你能告诉我蜘蛛侠住在哪里以及他的好朋友有哪些吗？")
print("\nAI的回答:")
print(answer)
```

输出示意：

```python
{
    '蜘蛛侠': '蜘蛛侠是一个超级英雄，他的好朋友包括钢铁侠、美国队长和绿巨人。',
    '钢铁侠': '钢铁侠是蜘蛛侠的好朋友之一。',
    '美国队长': '美国队长是蜘蛛侠的好朋友之一。',
    '绿巨人': '绿巨人是蜘蛛侠的好朋友之一。',
    '纽约': '蜘蛛侠住在纽约。',
    '斯塔克工业': '斯塔克工业提供了蜘蛛侠使用的装备。'
}
```

回答示意：

```python
{
    "input": "你能告诉我蜘蛛侠住在哪里以及他的好朋友有哪些吗？",
    "text": "蜘蛛侠住在纽约。他的好朋友包括钢铁侠、美国队长和绿巨人。"
}
```

---

### 3.5 ConversationKGMemory（了解）

`ConversationKGMemory` 是一种**基于知识图谱（Knowledge Graph）** 的记忆机制。

它比 `ConversationEntityMemory` 更进一步：

- 不仅识别实体；
- 还会提取实体之间的关系；
- 并将其组织成知识图谱中的三元组结构。

### 特点

- 使用知识图谱结构存储信息；
- 将对话转成 `(头实体, 关系, 尾实体)` 形式；
- 支持更强的关系推理。

---

#### 示例

```bash
pip install networkx
```

```python
from langchain.memory import ConversationKGMemory
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

memory = ConversationKGMemory(llm=llm)

memory.save_context({"input": "向山姆问好"}, {"output": "山姆是谁"})
memory.save_context({"input": "山姆是我的朋友"}, {"output": "好的"})

print(memory.load_memory_variables({"input": "山姆是谁"}))
print(memory.get_knowledge_triplets("她最喜欢的颜色是红色"))
```

输出示意：

```python
{"history": "On 山姆: 山姆是我的朋友。"}

[
    KnowledgeTriple(subject='山姆', predicate='是', object_='我的朋友'),
    KnowledgeTriple(subject='山姆', predicate='最喜欢的颜色是', object_='红色')
]
```

---

### 3.6 VectorStoreRetrieverMemory（了解）

`VectorStoreRetrieverMemory` 是一种**基于向量检索**的高级记忆机制。

它的核心思想不是按时间顺序线性回忆历史，而是：

1. 先把历史对话向量化；
2. 存入向量数据库；
3. 每次提问时，根据语义相似度检索最相关的历史内容；
4. 再把检索结果提供给模型。

### 适用场景

这种记忆特别适合：

- 需要长期记忆；
- 对话跨度大；
- 不一定要用最近消息，而是要找“最相关”的历史事实。

### 原理

![](Pasted%20image%2020260507225807.png)

---

#### 示例

```python
import os
import dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.memory import VectorStoreRetrieverMemory, ConversationBufferMemory
from langchain_community.vectorstores import FAISS

dotenv.load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

# 先用普通 memory 存一些历史对话
memory = ConversationBufferMemory()
memory.save_context({"input": "我最喜欢的食物是披萨"}, {"output": "很高兴知道"})
memory.save_context({"Human": "我喜欢的运动是跑步"}, {"AI": "好的，我知道了"})
memory.save_context({"Human": "我最喜欢的运动是足球"}, {"AI": "好的，我知道了"})

# 定义向量嵌入模型
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

# 初始化向量数据库
vectorstore = FAISS.from_texts(memory.buffer.split("\n"), embeddings_model)

# 定义检索对象
retriever = vectorstore.as_retriever(search_kwargs=dict(k=1))

# 初始化 VectorStoreRetrieverMemory
memory = VectorStoreRetrieverMemory(retriever=retriever)

print(memory.load_memory_variables({"prompt": "我最喜欢的食物是"}))
```

输出示意：

```python
{
    "history": "Human: 我最喜欢的食物是披萨"
}
```

### 小结

这种方式的关键优势在于：

- 不必把所有历史都塞进上下文；
- 只取与当前问题最相关的那部分；
- 很适合“长期但稀疏”的记忆检索场景。

---

## 本章总结

LangChain 的 Memory 组件本质上是在解决一个问题：

> **如何让模型在多轮对话中“记住”该记住的信息，同时避免上下文无限膨胀。**

不同 Memory 的适用方向如下：

- **`ChatMessageHistory`**：最底层消息存储器；
- **`ConversationBufferMemory`**：完整保留所有对话；
- **`ConversationBufferWindowMemory`**：只保留最近 `K` 轮；
- **`ConversationTokenBufferMemory`**：按 token 数量裁剪；
- **`ConversationSummaryMemory`**：将历史压缩为摘要；
- **`ConversationSummaryBufferMemory`**：摘要 + 最近原始消息混合；
- **`ConversationEntityMemory`**：围绕实体进行结构化记忆；
- **`ConversationKGMemory`**：用知识图谱保存实体关系；
- **`VectorStoreRetrieverMemory`**：通过向量检索语义相关历史。

### 选型建议

- 如果对话很短：优先用 `ConversationBufferMemory`
- 如果对话很长但只关心最近上下文：用 `ConversationBufferWindowMemory`
- 如果希望严格控制上下文成本：用 `ConversationTokenBufferMemory`
- 如果要兼顾长期记忆与压缩：用 `ConversationSummaryMemory` 或 `ConversationSummaryBufferMemory`
- 如果业务高度依赖关键事实字段：优先考虑 `ConversationEntityMemory`
- 如果需要做关系推理：考虑 `ConversationKGMemory`
- 如果需要长期语义检索：考虑 `VectorStoreRetrieverMemory`

---

> 整理进度：`04-LangChain使用之Memory.docx` 已全部整理完成，并完整追加到本 Markdown 文件。
