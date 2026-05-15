# 第03章：LangChain使用之 Chains

## 1. Chains 的基本使用

### 1.1 Chain 的基本概念

Chain（链）用于将多个组件连接起来，形成可复用的工作流，以完成更复杂的任务。常见可组合组件包括：

- Prompt Template（提示模板）
- LLM / ChatModel
- Output Parser（输出解析器）
- Memory（记忆）
- Tool（工具）

它的核心思想是：**通过组合多个模块化单元，实现比单一组件更强大的能力**。例如：

- 将 LLM 与 Prompt Template 结合
- 将 LLM 与输出解析器结合
- 将 LLM 与外部数据结合，用于问答
- 将 LLM 与长期记忆结合，用于多轮对话
- 将多个 LLM 串联，让上一个模型的输出成为下一个模型的输入

### 1.2 LCEL 及其基本构成

使用 LCEL，可以构造出结构最简单的 Chain。

**LCEL**（LangChain Expression Language，LangChain 表达式语言）是一种声明式方法，可以轻松地将多个组件链接成 AI 工作流。它通过 Python 原生操作符（如管道符 `|`）将组件连接成可执行流程，从而显著简化 AI 应用开发。

LCEL 的基本构成：

- Prompt
- Model
- OutputParser

即：

```python
# 用户输入先传给提示模板，
# 提示模板输出再传给模型，
# 最后模型输出交给输出解析器。
chain = prompt | model | output_parser

chain.invoke({"input": "What's your name?"})
```

三个组成部分的含义如下：

- **Prompt**：`BasePromptTemplate` 的实例，接收模板变量字典并生成 `PromptValue`
- **Model**：接收 `PromptValue`，如果是 `ChatModel`，通常输出 `BaseMessage`
- **OutputParser**：接收模型输出，将字符串或 `BaseMessage` 解析成需要的结果

其中：

- `chain`：可以使用 `|` 运算符将多个组件串联成一个 Chain
- `invoke()`：LCEL 对象统一的调用入口
- 常见调用方式：`invoke` / `batch` / `stream`

`|` 符号类似 shell 里的管道操作符：将前一个组件的输出作为后一个组件的输入，从而形成完整的 AI 工作流。

### 1.3 Runnable

Runnable 是 LangChain 定义的一个抽象协议（Protocol），它要求所有 LCEL 组件实现统一的标准方法：

```python
class Runnable(Protocol):
    def invoke(self, input: Any) -> Any: ...
    def batch(self, inputs: List[Any]) -> List[Any]: ...
    def stream(self, input: Any) -> Iterator[Any]: ...
    # 还有其他方法，如 ainvoke（异步）等
```

任何实现了这些方法的对象，都可以视为 LCEL 兼容组件，例如：

- 聊天模型
- 提示词模板
- 输出解析器
- 检索器
- 代理（智能体）

#### 为什么需要统一调用方式？

传统方式中，不同组件的调用接口往往不同：

- 提示词渲染：`.format()`
- 模型调用：`.generate()`
- 解析器解析：`.parse()`
- 工具调用：`.run()`

传统写法：

```python
prompt_text = prompt.format(topic="猫")
model_out = model.generate(prompt_text)
result = parser.parse(model_out)
```

痛点在于：**每个组件调用方式不同，组合时需要手动适配。**

LCEL 的解决方案是通过 `Runnable` 协议统一调用方式：

```python
# 分步调用
prompt_text = prompt.invoke({"topic": "猫"})
model_out = model.invoke(prompt_text)
result = parser.invoke(model_out)

# LCEL 管道式写法
chain = prompt | model | parser
result = chain.invoke({"topic": "猫"})
```

优点：

- **一致性**：无论组件功能多复杂，调用方式都一致
- **组合性**：`|` 运算符会自动处理类型匹配和中间结果传递

### 1.4 使用举例

#### 举例 1：不使用 Chain

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
import dotenv

dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY1")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")

chat_model = ChatOpenAI(model="gpt-4o-mini")

prompt_template = PromptTemplate.from_template(
    template="给我讲一个关于{topic}话题的简短笑话"
)

parser = StrOutputParser()

prompt_value = prompt_template.invoke({"topic": "冰淇淋"})
result = chat_model.invoke(prompt_value)
out_put = parser.invoke(result)

print(out_put)
print(type(out_put))
```

输出示例：

```text
当然可以！这是一个关于冰淇淋的小笑话：
为什么冰淇淋总是很开心？
因为它总是能被“吃”到快乐的地方！
<class 'str'>
```

#### 举例 2：使用 Chain

将提示模板、模型、解析器链接在一起：

```python
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
chat_model = ChatOpenAI(model="gpt-4o-mini")

prompt_template = PromptTemplate.from_template(
    template="给我讲一个关于{topic}话题的简短笑话"
)

parser = StrOutputParser()
chain = prompt_template | chat_model | parser

out_put = chain.invoke({"topic": "ice cream"})
print(out_put)
print(type(out_put))
```

![697](Pasted%20image%2020260507222516.png)

---

## 2. 传统 Chain 的使用

### 2.1 基础链：LLMChain

#### 2.1.1 使用说明

在 LCEL 出现之前，最基础也最常见的链类型就是 `LLMChain`。

它至少包含：

- 一个提示词模板（`PromptTemplate`）
- 一个语言模型（`LLM` 或聊天模型）

> 注意：`LLMChain was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use prompt | llm instead.`

特点：

- 用于单次问答
- 输入一个 Prompt，输出一个 LLM 响应
- 适合无上下文的简单任务，如翻译、摘要、分类等
- 无记忆能力，不能自动维护聊天历史

#### 2.1.2 主要步骤

1. 配置任务链：使用 `LLMChain` 类将任务与提示词结合起来
2. 执行任务链：使用 `invoke()` 等方法执行，并获取生成结果

```python
chain = LLMChain(llm=llm, prompt=prompt_template)
result = chain.invoke(...)
print(result)
```

#### 2.1.3 参数说明与示例
|                   |                                                                                     |             |            |                                                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------- | ----------- | ---------- | ------------------------------------------------------------------------------------------------------------------- |
| 参数名               | 类型                                                                                  | 默认<br><br>值 | 必<br><br>填 | 说明                                                                                                                  |
| llm               | Union[Runnable[LanguageModelInput, str], Runnable[LanguageModelInput, BaseMessage]] | -           | 是          | 要调用的语言模型                                                                                                            |
| prompt            | BasePromptTemplate                                                                  | -           | 是          | 要使用的提示对象                                                                                                            |
| verbose           | bool                                                                                | False       | 否          | 是否以详细模式运行。在详细模式下，一些中间日志将被打印到控制台。默认使用全局详细设置，可通过  <br>langchain.globals.get_verbose()访问                               |
| callback_manager  | Optional[BaseCallbackManager]                                                       | None        | 否          | 【已弃用】请改用callbacks。                                                                                                  |
| callbacks         | Callbacks                                                                           | None        | 否          | 可选的回调处理器列表或回调管理器。在调用链的生命周期中的不同阶段被调用，从on_chain_start开始，到on_chain_end或  <br>on_chain_error结束。自定义链可以选择调用额外的回调方法。详见回调文档 |
| llm_kwargs        | dict                                                                                | -           | 否          | 语言模型的关键字参数字典                                                                                                        |
| memory            | Optional[BaseMemory]                                                                | None        | 否          | 可选的记忆对象。默认为None。记忆是一个在每个链的开始和结束时被调用的类。开始时，记忆加载变量并在链中传递。结束时，它保存任何返回的变量。有许多不同类型的内存，请查看内存文档获取完整目录                      |
| metadata          | Optional[Dict[str, Any]]                                                            | None        | 否          | 与链相关联的可选元数据。默认为None。这些元数据将与调用此链的每次调用相关联，并作为参数传递给callbacks中定义的处理程  <br>序。您可以使用这些来识别链的特定实例及其用例                        |
| output_parser     | BaseLLMOutputParser                                                                 | -           | 否          | 要使用的输出解析器。默认为<br><br>StrOutputParser                                                                                |
| return_final_only | bool                                                                                | True        | 否          | 是否只返回最终解析结果。默认为True。如果为False，将返回关于生成的额外信息。                                                                          |
| tags              | Optional[List[str]]                                                                 | None        | 否          | 与链相关联的可选标签列表。默认为None。这些标签将与调用此链的每次调用相关联，并作为参数传递给callbacks中定义的处理程  <br>序。您可以使用这些来识别链的特定实例及其用例                        |

##### 示例 1

```python
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
import dotenv

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

chat_model = ChatOpenAI(model="gpt-4o-mini")

template = "桌上有{number}个苹果，四个桃子和 3 本书，一共有几个水果?"
prompt = PromptTemplate.from_template(template)

llm_chain = LLMChain(
    llm=chat_model,
    prompt=prompt,
)

result = llm_chain.invoke({"number": 2})
print(result)
```

##### 示例 2：`verbose=True` + `ChatPromptTemplate`

```python
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

chat_template = ChatPromptTemplate.from_messages([
    ("system", "你是一位{area}领域具备丰富经验的高端技术人才"),
    ("human", "给我讲一个 {adjective} 笑话"),
])

llm = ChatOpenAI(model="gpt-4o-mini")
llm_chain = LLMChain(llm=llm, prompt=chat_template, verbose=True)
```

补充说明：除了 `invoke()`，也常见 `run()`、`predict()` 等调用方式，效果类似。

### 2.2 顺序链：SimpleSequentialChain

顺序链允许将多个链按顺序连接起来，让前一个 Chain 的输出自动作为下一个 Chain 的输入，形成流水线（Pipeline）。

顺序链有两类：

- **单输入 / 单输出**：`SimpleSequentialChain`
- **多输入 / 多输出**：`SequentialChain`

#### 2.2.1 说明

`SimpleSequentialChain` 是最简单的顺序链：

- 多个步骤串联执行
- 每个步骤都只有单一输入和单一输出
- 上一步输出会自动作为下一步输入
- 无需手动映射变量

![](Pasted%20image%2020260507222701.png)
#### 2.2.2 使用举例

##### 示例 1

第一个链负责详细解释问题，第二个链负责提炼结论。

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

chainA_template = ChatPromptTemplate.from_messages([
    ("system", "你是一位精通各领域知识的知名教授"),
    ("human", "请你尽可能详细地解释一下：{knowledge}"),
])

chainA = LLMChain(llm=llm, prompt=chainA_template, verbose=True)

chainB_template = ChatPromptTemplate.from_messages([
    ("system", "你非常善于提取文本中的重要信息，并做出简短的总结"),
    ("human", "这是针对一个提问的完整解释说明内容：{description}"),
    ("human", "请你根据上述说明，尽可能简短地输出重要结论，控制在20个字以内"),
])

chainB = LLMChain(llm=llm, prompt=chainB_template, verbose=True)

full_chain = SimpleSequentialChain(
    chains=[chainA, chainB],
    verbose=True,
)

full_chain.invoke({"input": "什么是LangChain？"})
```

关键点：

- `chains` 中传入的顺序必须正确
- 调用时统一使用 `input`
- 不再直接使用第一个链的 `{knowledge}` 或第二个链的 `{description}`

##### 示例 2

一个链先根据剧名写大纲，另一个链基于大纲生成剧评：

```python
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompt_template1 = PromptTemplate(input_variables=["title"], template=template1)
synopsis_chain = LLMChain(llm=llm, prompt=prompt_template1)
review_chain = LLMChain(llm=llm, prompt=prompt_template2)

overall_chain = SimpleSequentialChain(
    chains=[synopsis_chain, review_chain],
    verbose=True,
)

review = overall_chain.invoke("日落海滩上的悲剧")
print(review)
```

### 2.3 顺序链：SequentialChain

#### 2.3.1 说明

`SequentialChain` 是更通用的顺序链，适用于复杂流程：

- 支持多个输入变量和多个输出变量
- 允许不同子链拥有各自独立的输入 / 输出字段
- 需要显式定义变量如何从一个链传递到下一个链
- 可以支持更复杂的流程控制

![](Pasted%20image%2020260507222726.png)
#### 2.3.2 使用举例

##### 示例 1

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain, LLMChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

schainA_template = ChatPromptTemplate.from_messages([
    ("system", "你是一位精通各领域知识的知名教授"),
    ("human", "请你先尽可能详细地解释一下：{knowledge}，并且{action}"),
])

schainA = LLMChain(
    llm=llm,
    prompt=schainA_template,
    verbose=True,
    output_key="schainA_chains_key",
)

schainB_template = ChatPromptTemplate.from_messages([
    ("system", "你非常善于提取文本中的重要信息，并做出简短的总结"),
    ("human", "这是针对一个提问完整的解释说明内容：{schainA_chains_key}"),
    ("human", "请你根据上述说明，尽可能简短地输出重要结论，请控制在100个字以内"),
])

schainB = LLMChain(
    llm=llm,
    prompt=schainB_template,
    verbose=True,
    output_key="schainB_chains_key",
)

seq_chain = SequentialChain(
    chains=[schainA, schainB],
    input_variables=["knowledge", "action"],
    output_variables=["schainA_chains_key", "schainB_chains_key"],
    verbose=True,
)
```

##### 示例 2

这个例子展示一个四段式流程：

1. 翻译成中文
2. 对翻译结果做摘要
3. 识别摘要语言
4. 按识别出的语言生成评论

```python
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import SequentialChain

llm = ChatOpenAI(model="gpt-4o-mini")

first_prompt = PromptTemplate.from_template("把下面内容翻译成中文:\n\n{content}")
chain_one = LLMChain(llm=llm, prompt=first_prompt, verbose=True, output_key="Chinese_Review")

second_prompt = PromptTemplate.from_template("用一句话总结下面内容:\n\n{Chinese_Review}")
chain_two = LLMChain(llm=llm, prompt=second_prompt, verbose=True, output_key="Chinese_Summary")

third_prompt = PromptTemplate.from_template("下面内容是什么语言:\n\n{Chinese_Summary}")
chain_three = LLMChain(llm=llm, prompt=third_prompt, verbose=True, output_key="Language")

fourth_prompt = PromptTemplate.from_template(
    "请使用指定的语言对以下内容进行评论:\n\n内容:{Chinese_Summary}\n\n语言:{Language}"
)
chain_four = LLMChain(llm=llm, prompt=fourth_prompt, verbose=True, output_key="Comment")

overall_chain = SequentialChain(
    chains=[chain_one, chain_two, chain_three, chain_four],
    verbose=True,
    input_variables=["content"],
    output_variables=["Chinese_Review", "Chinese_Summary", "Language", "Comment"],
)
```

#### 2.3.3 顺序链使用场景

场景：**多数据源处理 / 多变量流转**。

例如根据产品名：

1. 查询数据库获取价格
2. 基于价格生成促销文案

`SimpleSequentialChain` 更适合单输入 / 单输出场景；而 `SequentialChain` 更适合多变量传递。

```python
from langchain.chains import SequentialChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

llm = ChatOpenAI(model="gpt-4o-mini")

query_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(
        "请模拟查询{product}的市场价格，直接返回一个合理的价格数字（如6999），不要包含任何其他文字或代码"
    ),
    output_key="price",
)

promo_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(
        "为{product}（售价：{price}元）创作一篇50字以内的促销文案，要求突出产品卖点"
    ),
    output_key="promo_text",
)

sequential_chain = SequentialChain(
    chains=[query_chain, promo_chain],
    verbose=True,
    input_variables=["product"],
    output_variables=["price", "promo_text"],
)
```

### 2.4 数学链：LLMMathChain（了解）

`LLMMathChain` 会先把用户问题转成数学表达式，再借助 Python 的 `numexpr` 库执行表达式，最后返回答案。

使用前需要安装：

```bash
pip install numexpr
```

示例：

```python
from langchain.chains import LLMMathChain
from langchain_openai import ChatOpenAI
import os
import dotenv

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

llm = ChatOpenAI(model="gpt-4o-mini")
llm_math = LLMMathChain.from_llm(llm)

res = llm_math.invoke("10 ** 3 + 100的结果是多少？")
print(res)
```

### 2.5 路由链：RouterChain（了解）

`RouterChain` 用于**动态选择下一条链**。它会先分析用户输入，再决定把请求分派到哪条子链处理。

适合场景：

- 输入类别不固定
- 不同问题需要走不同处理链
- 需要自动路由到最合适的子链
![](Pasted%20image%2020260507222821.png)
例如：

- 数学问题走数学链
- 历史问题走历史链
- 其他问题走默认链

使用时通常还需要设置一个**默认链**，用于兼容输入不满足任意路由规则的情况。
**RouterChain图示：**
![](Pasted%20image%2020260507222830.png)
### 2.6 文档链：StuffDocumentsChain（了解）

`StuffDocumentsChain` 的核心作用是：**将多个文档内容合并后一次性塞进 Prompt，再交给 LLM 处理。**

适合场景：

- 总结
- 问答
- 对比分析
- 需要模型同时看到全部文档上下文

注意：它更适合**少量 / 中等长度文档**。

示例：

```python
from langchain.chains import StuffDocumentsChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI

loader = PyPDFLoader("./asset/example/loader.pdf")

prompt_template = """对以下文字做简洁的总结:
{text}

简洁的总结:"""

prompt = PromptTemplate.from_template(prompt_template)
llm = ChatOpenAI(model="gpt-4o-mini")
llm_chain = LLMChain(llm=llm, prompt=prompt)

stuff_chain = StuffDocumentsChain(
    llm_chain=llm_chain,
    document_variable_name="text",
)

docs = loader.load()
res = stuff_chain.invoke(docs)
print(res["output_text"])
```

---

## 3. 基于 LCEL 构建的 Chains 类型

前面介绍的大多是 Legacy Chains。下面是更现代的、基于 LCEL 构建的链式能力：

- `create_sql_query_chain`
- `create_stuff_documents_chain`
- `create_openai_fn_runnable`
- `create_structured_output_runnable`
- `load_query_constructor_runnable`
- `create_history_aware_retriever`
- `create_retrieval_chain`

### 3.1 `create_sql_query_chain`

`create_sql_query_chain` 是 SQL 查询链，用于将自然语言转换成 SQL 查询语句。

这里使用 MySQL 数据库时，需要安装：

```bash
pip install pymysql
```

示例：

```python
from langchain_openai import ChatOpenAI
from langchain.chains.sql_database.query import create_sql_query_chain

llm = ChatOpenAI(model="gpt-4o-mini")
chain = create_sql_query_chain(llm=llm, db=db)

response = chain.invoke({
    "question": "一共有多少个员工？",
    "table_names_to_use": ["employees"],
})
print(response)
```

### 3.2 `create_stuff_documents_chain`（了解）

`create_stuff_documents_chain` 用于将多个文档合并成一个长文本，并一次性交给 LLM 处理。

适合场景：

- 多文档摘要
- 基于整批文档做问答
- 需要全局理解所有文档内容

示例：

```python
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document

prompt = PromptTemplate.from_template("""
如下文档{docs}中说，香蕉是什么颜色的？
""")

llm = ChatOpenAI(model="gpt-4o-mini")
chain = create_stuff_documents_chain(llm, prompt, document_variable_name="docs")

docs = [
    Document(page_content="苹果属于蔷薇科苹果属植物。"),
    Document(page_content="香蕉是白色的水果，主要产自热带地区。"),
    Document(page_content="蓝莓是蓝色的浆果。"),
]

chain.invoke({"docs": docs})
```

---

## 4. 本章小结

本章围绕 LangChain 中的 **Chains** 展开，重点包括：

- 理解 Chain 的核心思想：通过组件组合形成工作流
- 掌握 LCEL 的基础写法：`prompt | model | parser`
- 理解 `Runnable` 统一调用协议的重要性
- 熟悉传统链：`LLMChain`、`SimpleSequentialChain`、`SequentialChain`
- 了解扩展链：`LLMMathChain`、`RouterChain`、`StuffDocumentsChain`
- 认识新版 LCEL 风格链：如 `create_sql_query_chain`、`create_stuff_documents_chain`

### 选型建议

- **简单串联**：优先使用 LCEL
- **旧项目兼容**：可能仍会见到 `LLMChain`
- **单输入单输出流程**：`SimpleSequentialChain`
- **多变量复杂流程**：`SequentialChain`
- **文档整体塞入模型**：`StuffDocumentsChain` / `create_stuff_documents_chain`
- **自然语言转 SQL**：`create_sql_query_chain`
