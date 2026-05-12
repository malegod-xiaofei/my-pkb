## 项目介绍

## 项目背景

随着美团业务的不断扩展，客服人员需要应对海量的用户咨询，包括订单问题、退款流程、配送异常、优惠政策等。传统的知识库客服系统依赖规则匹配，回答僵硬，难以及时覆盖最新的业务规则。

## 项目功能

为提升客户体验和客服效率，本项目基于 RAG（Retrieval-Augmented Generation，检索增强生成） 技术构建智能客服问答系统，将美团内部文档知识与大语言模型结合，实现更智能、更准确的自动化答复。

## 项目实现

## 文档收集

收集美团客服相关知识文档，例如：

- 业务手册（退款规则、订单处理流程）
- 常见问题 FAQ
- 内部客服知识库
- 实时更新的运营公告

以美团外卖常见问题为例，文档地址：[https://waimai.meituan.com/help/faq](https://waimai.meituan.com/help/faq)，我们通过playwright 工具爬虫获取页面数据并写入本地 txt 文件中。

安装依赖包

```
pip install playwright chromium
playwright install

sudo apt update && sudo apt install fonts-wqy-zenhei fonts-wqy-microhei -y
```

代码如下：

```
from playwright.sync_api import sync_playwright

def collect_faq(url):
    """
    收集指定URL页面中的FAQ内容
    
    参数:
        url (str): 目标网页URL地址
        
    返回:
        str: 提取的FAQ文本内容
    """
    
    with sync_playwright() as p:
        
        browser = p.chromium.launch(
            headless=False,
            args=['--lang=zh-CN']  
        )
        
        page = browser.new_page(
            locale='zh-CN',  
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
            ),
            extra_http_headers={
                "Accept-Language": "zh-CN,zh;q=0.9"
            }
        )
        
        page.goto(url, timeout=30_000)
        page.wait_for_load_state("networkidle")

        
        raw_text = page.locator("#faq-list").first.text_content()
        browser.close()
        return raw_text

def save_faq(cleaned_text:str, output_file:str):
    """
    将FAQ文本内容保存到指定文件
    
    参数:
        cleaned_text (str): 要保存的FAQ文本内容
        output_file (str): 输出文件路径
    """
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(f"FAQ 已保存到 {output_file}")

if __name__ == "__main__":
    cleaned_text = collect_faq(url="https://waimai.meituan.com/help/faq")
    output_file = "faq.txt"
    save_faq(cleaned_text, output_file)
```

执行结果如下：

```
在线支付问题
          
        
        
          
            Q：在线支付取消订单后钱怎么返还？
            
              订单取消后，款项会在一个工作日内，直接返还到您的美团账户余额。
            
          
        
        
          
            Q：怎么查看退款是否成功？
            
              退款会在一个工作日之内到美团账户余额，可在“账号管理——我的账号”中查看是否到账
```
## 文档处理

我们已经爬取了 FAQ 文档，接下来就需要对收集到的文档进行统一处理，内容包括：

- 文本清洗（去除 HTML 标签、无关字符）
- 分段切分（按规则或语义将文档拆分成小片段，便于检索）
- 元数据标注（来源、时间、业务类别等）。

代码如下：

```
import re
import json
from pathlib import Path
from datetime import datetime, timezone

def clean_text(text: str) -> str:
    """
    清洗文本内容，去除HTML标签和多余空格及无效字符。

    参数:
        text (str): 需要清洗的原始文本。

    返回:
        str: 清洗后的文本内容。
    """
    
    text = re.sub(r"<.*?>", "", text)
    
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)

def split_faq(text: str):
    """
    根据 Q/A 规则将FAQ文本切分为问题和答案对。

    参数:
        text (str): 包含FAQ内容的文本字符串。

    返回:
        list[dict]: 每个元素是一个包含"question"和"answer"键的字典。
    """
    
    parts = re.split(r"(?:^|\n)Q[:：]", text)
    qa_pairs = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        
        lines = part.splitlines()
        question = lines[0]
        answer = "\n".join(lines[1:]) if len(lines) > 1 else ""
        qa_pairs.append({
            "question": question,
            "answer": answer
        })
    return qa_pairs

def process_faq(input_file: str, output_file: str, source_url: str, category="FAQ"):
    """
    处理FAQ文本文件，清洗、分割并添加元数据后保存为JSON格式。

    参数:
        input_file (str): 输入的原始FAQ文本文件路径。
        output_file (str): 输出处理后的JSON文件路径。
        source_url (str): 数据来源URL。
        category (str): FAQ分类，默认为"FAQ"。

    返回:
        None
    """
    raw_text = Path(input_file).read_text(encoding="utf-8")
    cleaned_text = clean_text(raw_text)
    qa_pairs = split_faq(cleaned_text)

    
    now = datetime.now(timezone.utc).isoformat()
    processed = []
    for qa in qa_pairs:
        processed.append({
            "question": qa["question"],
            "answer": qa["answer"],
            "metadata": {
                "source": source_url,
                "category": category,
                "crawl_time": now
            }
        })

    Path(output_file).write_text(
        json.dumps(processed, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"✅ 已处理 {len(processed)} 条 FAQ，结果保存到 {output_file}")

if __name__ == "__main__":
    process_faq(
        input_file="faq.txt",
        output_file="faq_processed.json",
        source_url="https://waimai.meituan.com/help/faq",
        category="支付问题"
    )
```

执行后的效果如下

```
[
  {
    "question": "在线支付问题",
    "answer": "",
    "metadata": {
      "source": "https://waimai.meituan.com/help/faq",
      "category": "支付问题",
      "crawl_time": "2025-09-04T02:38:28.261319+00:00"
    }
  },
  {
    "question": "在线支付取消订单后钱怎么返还？",
    "answer": "订单取消后，款项会在一个工作日内，直接返还到您的美团账户余额。",
    "metadata": {
      "source": "https://waimai.meituan.com/help/faq",
      "category": "支付问题",
      "crawl_time": "2025-09-04T02:38:28.261319+00:00"
    }
  },
  {
```
## 文档数据向量化

我们将 FAQ 数据格式化成 json 数据后，接下来就要转成向量数据并存储到向量数据库中，此处以 redis 为例，操作内容包括：

- 使用 **向量化模型（Embedding Model，如 BGE、OpenAI Embedding）** 将文档片段转换为向量表示。
- 存储至向量数据库（如 Milvus、Weaviate、Redis Vector、Faiss），支持高效的相似度搜索。

代码如下

```
import os
import json
import dotenv
import dashscope
import redis
import numpy as np
from http import HTTPStatus
from redis.commands.search.field import TextField, VectorField
from redis.commands.search.index_definition import IndexDefinition



dotenv.load_dotenv()

dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")


INDEX_NAME = "faq_index"
VECTOR_DIM = 1024
DISTANCE_METRIC = "COSINE"


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    password=None,
    decode_responses=False
)


def create_index():
    """
    创建 Redis 向量搜索索引。
    
    如果索引已存在，则跳过创建并提示信息；
    否则根据预定义的字段结构创建一个新的索引，用于支持 FAQ 的文本与向量混合检索。
    """
    try:
        redis_client.ft(INDEX_NAME).info()
        print("✅ 索引已存在")
    except Exception:
        redis_client.ft(INDEX_NAME).create_index(
            [
                TextField("question"),
                TextField("answer"),
                TextField("source"),
                TextField("category"),
                TextField("crawl_time"),
                VectorField(
                    "embedding",
                    "HNSW",
                    {"TYPE": "FLOAT32", "DIM": VECTOR_DIM, "DISTANCE_METRIC": DISTANCE_METRIC}
                )
            ],
            definition=IndexDefinition(prefix=["faq:"])
        )
        print("✅ 已创建向量索引")


def insert_faq(doc: dict):
    """
    将单条 FAQ 数据插入 Redis，并生成对应的文本嵌入向量。

    参数:
        doc (dict): 包含问题、答案及元数据的字典。
            - question (str): 问题内容
            - answer (str): 回答内容
            - metadata (dict): 元数据，包括 source, category, crawl_time 等字段

    返回值:
        无返回值。结果通过打印输出表示操作是否成功。
    """
    
    text_for_embedding = doc["question"] + " " + doc["answer"]

    
    resp = dashscope.MultiModalEmbedding.call(
        model="multimodal-embedding-v1",
        input=[{"text": text_for_embedding}]
    )

    if resp.status_code == HTTPStatus.OK:
        
        embedding = resp.output["embeddings"][0]["embedding"]
        vector = np.array(embedding, dtype=np.float32).tobytes()

        
        key = f"faq:{resp.request_id}"
        
        redis_client.hset(key, mapping={
            "question": doc["question"],
            "answer": doc["answer"],
            "source": doc["metadata"]["source"],
            "category": doc["metadata"]["category"],
            "crawl_time": doc["metadata"]["crawl_time"],
            "embedding": vector
        })
        print(f"✅ 已写入 Redis, key={key}")
    else:
        print(f"❌ Embedding 调用失败: {resp.code}, {resp.message}")


def insert_from_file(file_path="faq_processed.json"):
    """
    从指定 JSON 文件中读取 FAQ 数据并逐条插入 Redis。

    参数:
        file_path (str): JSON 格式的 FAQ 数据文件路径，默认为 "faq_processed.json"

    返回值:
        无返回值。每条数据插入后会打印状态信息。
    """
    with open(file_path, "r", encoding="utf-8") as f:
        docs = json.load(f)

    for doc in docs:
        insert_faq(doc)

if __name__ == "__main__":
    
    create_index()
    insert_from_file("faq_processed.json")
```

查看 redis 数据内容

![](images/图片23.jpeg)

## 文档数据相似性检索

文档向量数据写入数据库后，接下来就是测试验证召回数据准确性，主要内容包括：

- 用户提问后，将问题转换为向量，与向量数据库中的文档进行相似性匹配。
- 召回与问题最相关的文档片段（如退款流程、配送延误规则），并返回给上层系统。

代码如下：

```
import os
import dotenv
import dashscope
import redis
import numpy as np
from http import HTTPStatus
from redis.commands.search.query import Query



dotenv.load_dotenv()

dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")


INDEX_NAME = "faq_index"

VECTOR_DIM = 1024

TOP_K = 3


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    password=None,
    decode_responses=False
)


def embed_question(question: str):
    """
    使用 DashScope 的多模态嵌入模型将文本问题转换为向量表示。

    参数:
        question (str): 需要转换为向量的文本问题。

    返回:
        bytes: 问题对应的向量表示（以字节形式返回）。

    异常:
        RuntimeError: 如果调用嵌入服务失败，则抛出运行时错误。
    """
    resp = dashscope.MultiModalEmbedding.call(
        model="multimodal-embedding-v1",
        input=[{"text": question}]
    )
    if resp.status_code == HTTPStatus.OK:
        embedding = resp.output["embeddings"][0]["embedding"]
        return np.array(embedding, dtype=np.float32).tobytes()
    else:
        raise RuntimeError(f"❌ Embedding 调用失败: {resp.code}, {resp.message}")


def search_faq(question: str, top_k=TOP_K):
    """
    根据用户输入的问题，在 Redis 中进行向量相似度搜索，返回最相关的 FAQ 条目。

    参数:
        question (str): 用户提出的问题。
        top_k (int): 返回最相似的前 K 条结果，默认值为 TOP_K。
    """
    
    q_vector = embed_question(question)

    
    query = (
        Query(f"*=>[KNN {top_k} @embedding $vec AS score]")
        .sort_by("score")
        .return_fields("question", "answer", "source", "category", "crawl_time", "score")
        .dialect(2)
    )

    
    results = redis_client.ft(INDEX_NAME).search(query, query_params={"vec": q_vector})

    print(f"\n🔎 用户问题: {question}")
    print(f"📊 召回 {len(results.docs)} 条结果\n")

    
    for i, doc in enumerate(results.docs, start=1):
        print(f"--- Top {i} ---")
        print(f"相似度分数: {doc.score}")
        print(f"Q: {doc.question}")
        print(f"A: {doc.answer}")
        print(f"来源: {doc.source}")
        print(f"类别: {doc.category}")
        print(f"时间: {doc.crawl_time}")
        print()


if __name__ == "__main__":
    
    test_question = "为什么会出现无法下单的情况？"
    search_faq(test_question, top_k=3)
```

执行结果如下

```
🔎 用户问题: 为什么会出现无法下单的情况？
📊 召回 3 条结果

--- Top 1 ---
相似度分数: 0.114289164543
Q: 为什么会出现无法下单的情况？
A: 无法下单有很多情况，可能是菜品售完、餐厅不在营业时间等，请查看无法下单时给的提示。
来源: https://waimai.meituan.com/help/faq
类别: 支付问题
时间: 2025-09-04T02:38:28.261319+00:00

--- Top 2 ---
相似度分数: 0.13062286377
Q: 刚下单发现信息填错了怎么办？
A: 如果商家尚未接单，您可以自主取消订单；如果商家已经接单，您可以电话联系商家后由对方取消订单。然后重新下一单。
来源: https://waimai.meituan.com/help/faq
类别: 支付问题
时间: 2025-09-04T02:38:28.261319+00:00

--- Top 3 ---
相似度分数: 0.138350009918
Q: 为什么提示下单次数过多，已无法下单？
A: 同一手机号在同一设备上一天最多可以成功提交7次订单（在线支付以完成支付为准，货到付款以提交订单为准）。
其他问题
来源: https://waimai.meituan.com/help/faq
类别: 支付问题
时间: 2025-09-04T02:38:28.261319+00:00
```

## 构建提示词

- 把 **用户问题** + **检索召回的上下文** 拼接成一个高质量的 Prompt 送给大模型。
- 提示词示例：

```
你是一个智能问答助手，请仅根据提供的文档片段回答用户问题。
如果文档片段中没有相关内容，请回答“未找到相关信息”。

用户问题：
取消订单后多久能收到退款？

可用文档片段：
【文档片段1】
Q: 在线支付取消订单后钱怎么返还？
A: 订单取消后，款项会在一个工作日内，直接返还到您的美团账户余额。

【文档片段2】
Q: 怎么查看退款是否成功？
A: 退款会在一个工作日之内到美团账户余额，可在“账号管理——我的账号”中查看是否到账。

请基于以上信息，生成简洁明了的回答：
```

提示词代码如下：

```
import os
import dotenv
import dashscope
import redis
import numpy as np
from http import HTTPStatus
from redis.commands.search.query import Query



dotenv.load_dotenv()

dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")


INDEX_NAME = "faq_index"

VECTOR_DIM = 1024

TOP_K = 3


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    password=None,
    decode_responses=False
)


def embed_question(question: str):
    """
    使用 DashScope 的多模态嵌入模型将文本问题转换为向量表示。

    参数:
        question (str): 用户输入的问题文本。

    返回:
        bytes: 问题对应的向量表示（以字节形式存储）。

    异常:
        RuntimeError: 当调用嵌入服务失败时抛出异常。
    """
    resp = dashscope.MultiModalEmbedding.call(
        model="multimodal-embedding-v1",
        input=[{"text": question}]
    )
    if resp.status_code == HTTPStatus.OK:
        embedding = resp.output["embeddings"][0]["embedding"]
        return np.array(embedding, dtype=np.float32).tobytes()
    else:
        raise RuntimeError(f"❌ Embedding 调用失败: {resp.code}, {resp.message}")


def search_faq(question: str, top_k=TOP_K):
    """
    在 Redis 中基于向量相似度搜索与用户问题最相关的 FAQ 文档。

    参数:
        question (str): 用户提出的问题。
        top_k (int): 返回最相似的前 K 个文档，默认使用 TOP_K 常量。

    返回:
        list: 包含匹配文档对象的列表，每个对象包含字段如 question、answer、source 等。
    """
    q_vector = embed_question(question)

    
    query = (
        Query(f"*=>[KNN {top_k} @embedding $vec AS score]")
        .sort_by("score")
        .return_fields("question", "answer", "source", "category", "crawl_time", "score")
        .dialect(2)
    )

    
    results = redis_client.ft(INDEX_NAME).search(query, query_params={"vec": q_vector})
    return results.docs


def build_prompt(user_question: str, retrieved_docs, top_k=TOP_K) -> str:
    """
    根据用户问题和检索到的相关文档构建用于大模型推理的 Prompt。

    参数:
        user_question (str): 用户提出的问题。
        retrieved_docs (list): 检索到的相关文档列表。
        top_k (int): 使用的文档数量上限，默认为 TOP_K。

    返回:
        str: 构建完成的 Prompt 字符串。
    """
    context_parts = []
    for i, doc in enumerate(retrieved_docs[:top_k], start=1):
        context_parts.append(
            f"【文档片段{i}】\nQ: {doc.question}\nA: {doc.answer}"
        )
    context_text = "\n\n".join(context_parts)

    prompt = f"""
你是一个智能问答助手，请仅根据提供的文档片段回答用户问题。
如果文档片段中没有相关内容，请回答“未找到相关信息”。

用户问题：
{user_question}

可用文档片段：
{context_text}

请基于以上信息，生成简洁明了的回答：
"""
    return prompt.strip()


if __name__ == "__main__":
    
    while True:
        user_question = input("\n请输入问题（输入 exit 退出）：")
        if user_question.lower() in ["exit", "quit"]:
            break

        docs = search_faq(user_question, top_k=TOP_K)
        if not docs:
            print("⚠️ 未检索到相关文档")
            continue

        prompt = build_prompt(user_question, docs)
        print("\n===== 构建的 Prompt =====\n")
        print(prompt)
        print("\n=========================\n")
```

执行结果如下

```
请输入问题（输入 exit 退出）：为什么会出现无法下单的情况

===== 构建的 Prompt =====

你是一个智能问答助手，请仅根据提供的文档片段回答用户问题。
如果文档片段中没有相关内容，请回答“未找到相关信息”。

用户问题：
为什么会出现无法下单的情况

可用文档片段：
【文档片段1】
Q: 为什么会出现无法下单的情况？
A: 无法下单有很多情况，可能是菜品售完、餐厅不在营业时间等，请查看无法下单时给的提示。

【文档片段2】
Q: 刚下单发现信息填错了怎么办？
A: 如果商家尚未接单，您可以自主取消订单；如果商家已经接单，您可以电话联系商家后由对方取消订单。然后重新下一单。

【文档片段3】
Q: 为什么提示下单次数过多，已无法下单？
A: 同一手机号在同一设备上一天最多可以成功提交7次订单（在线支付以完成支付为准，货到付款以提交订单为准）。
其他问题

请基于以上信息，生成简洁明了的回答：

=========================


请输入问题（输入 exit 退出）：exit
```

## 大语言模型生成结果

提示词构建完成验证无误后，接下来调用大模型对结果进行回答既可

- 调用大语言模型（如 DeepSeek、ChatGPT、通义千问等）生成自然语言回答。

代码如下：

```
import os
import dotenv
import dashscope
import redis
import numpy as np
from http import HTTPStatus
from redis.commands.search.query import Query
from openai import OpenAI


dotenv.load_dotenv()
dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")

INDEX_NAME = "faq_index"
VECTOR_DIM = 1024
TOP_K = 3

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    password=None,
    decode_responses=False
)


client = OpenAI(
    api_key=os.getenv("BAILIAN_API_KEY"),
    base_url=os.getenv("BAILIAN_BASE_URL")
)


def embed_question(question: str):
    resp = dashscope.MultiModalEmbedding.call(
        model="multimodal-embedding-v1",
        input=[{"text": question}]
    )
    if resp.status_code == HTTPStatus.OK:
        embedding = resp.output["embeddings"][0]["embedding"]
        return np.array(embedding, dtype=np.float32).tobytes()
    else:
        raise RuntimeError(f"❌ Embedding 调用失败: {resp.code}, {resp.message}")


def search_faq(question: str, top_k=TOP_K):
    q_vector = embed_question(question)

    query = (
        Query(f"*=>[KNN {top_k} @embedding $vec AS score]")
        .sort_by("score")
        .return_fields("question", "answer", "source", "category", "crawl_time", "score")
        .dialect(2)
    )

    results = redis_client.ft(INDEX_NAME).search(query, query_params={"vec": q_vector})
    return results.docs


def build_prompt(user_question: str, retrieved_docs, top_k=TOP_K) -> str:
    context_parts = []
    for i, doc in enumerate(retrieved_docs[:top_k], start=1):
        context_parts.append(
            f"【文档片段{i}】\nQ: {doc.question}\nA: {doc.answer}"
        )
    context_text = "\n\n".join(context_parts)

    prompt = f"""
    你是一个智能问答助手，请仅根据提供的文档片段回答用户问题。
    如果文档片段中没有相关内容，请回答“未找到相关信息”。
    
    用户问题：
    {user_question}
    
    可用文档片段：
    {context_text}
    
    请基于以上信息，生成简洁明了的回答：
    """
    return prompt.strip()


def ask_llm(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",  
        messages=[{"role": "user", "content": prompt}]
    )

    
    return completion.choices[0].message.content


if __name__ == "__main__":
    while True:
        user_question = input("\n请输入问题（输入 exit 退出）：")
        if user_question.lower() in ["exit", "quit"]:
            break

        docs = search_faq(user_question, top_k=TOP_K)
        if not docs:
            print("⚠️ 未检索到相关文档")
            continue

        prompt = build_prompt(user_question, docs)
        
        
        

        answer = ask_llm(prompt)
        print("💡 大模型回答：")
        print(answer)
```

执行结果如下

```
请输入问题（输入 exit 退出）：为什么会出现无法下单的情况
💡 大模型回答：
无法下单的情况可能是由于菜品售完、餐厅不在营业时间等原因。请查看下单时的提示信息以获取具体原因。
```

向量数据库存储与检索

RAG优化

项目介绍

项目背景

项目功能

项目实现

文档收集

文档处理

文档数据向量化

文档数据相似性检索

构建提示词

大语言模型生成结果
