# 三、自动化评测RAG应用的准确性

*-- 楼兰*

**章节目标：** 尝试建立RAG应用的自动化评测体系，衡量RAG应用在特定问题下的准确度。如果出现问题，快速定位问题的根因。

## 一、评估RAG应用的准确性

经过前面章节的介绍，我们使用LlamaIndex提供的一系列组件，可以非常方便的实现一个RAG应用。但是，RAG应用是不是只要实现了就可以了呢？真实的结果可能并不如你想象的那么简单。下面我们先实现一个RAG应用来看看。

在docs目录下，我提供了一份公司员工信息表。接下来，我们使用LlamaIndex来快速实现一个RAG应用，可以支持根据这份表格检索公司员工的信息。

```python
from src.config.load_key import load_key
from utils import llm,embed_model
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
import logging

logging.basicConfig(level=logging.ERROR)

Settings.llm=llm
Settings.embed_model=embed_model

documents = SimpleDirectoryReader(input_dir="./docs").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
print("问题：王芳是哪个部门的？")
response = query_engine.query("王芳是哪个部门的？")
print(response)
```

在这个案例中，我们询问“王芳是哪个部门的”，RAG应用却无法正确回答。但是，在给出的员工信息表中，王芳确实是其中的一个员工。

![员工信息表示例](images/3.png)

| 部门  | 姓名  | 上级  | 工位   | 工号  | 岗位   | 职位   | 电话          | 邮箱                      | 职责                                             |
| --- | --- | --- | ---- | --- | ---- | ---- | ----------- | ----------------------- | ---------------------------------------------- |
| 教研部 | 王芳  | 李琳  | A102 | 002 | 内容设计 | 教研专员 | 13800000002 | wangfang@educompany.com | 负责制定学科教学方案，策划教学活动，编写教案，收集学生反馈，参与课程改进会议，提供专业意见。 |

怎么排查这个问题呢？按照RAG的流程分析，我们需要先确认RAG应用在询问大语言模型之前，是否从源数据中召回了足够多的信息。在LlamaIndex中，可以很方便的获取RAG召回的参考信息。

```python
contexts = [ node.get_content() for node in response.source_nodes]
contexts
```

从召回的信息可以看到，出现这个问题的原因是因为RAG应用并没有从源数据中召回正确的相关信息。

对于这个具体的问题，我们构建的RAG应用，检索效果并不理想。而具体的原因，是从源数据中召回的信息并不多，导致大语言模型无法正确回答。由此可见，RAG应用的效果往往并不是想象中那么稳定，而且，造成效果不佳的原因也可能不止召回信息不够这一个原因。

接下来，我们将要专注于如何评估RAG应用的准确性，并在下一个章节，再集中关注如何优化RAG应用的准确性。

## 二、建立自动化评测机制

如果我们发现了RAG应用某一个具体问题回答效果不佳，那么我们可以逐步去排查RAG应用在哪个环节出现了问题，并逐步去优化。但是，通常构建RAG应用时，我们要面临的问题是无穷无尽的。我们不可能穷尽所有问题进行分析。在测试阶段就无法对RAG应用形成一个比较正确的评估。测试不充分，自然就无法形成比较靠谱的应用。

因此，对整个RAG应用进行效果评测的第一步，通常是需要构建一个自动化的评测体系。通过自动化的评测体系进行大量样本的综合分析，这样才能对RAG应用的整体效果进行合理的评估。

比如，针对之前提出的“张伟是哪个部门的”这个问题，拿到RAG应用的答案后，我们是可以通过大模型自动来判断结果是否正确。

```python
from utils import llm

def check_answer(question, answer, correct_answer):
     prompt = ("你是一个测试人员。\n"
        "下面给出了测试问题，正确答案以及回答。\n"
        "你需要根据这些信息判断回答的内容是不是回答了用户的问题。\n"
        "回复只能是：回答正确 或者 回答错误。请勿给出其他信息。\n"
        "------"
        f"问题是 {question}"
        "------"
        f"正确答案是： {correct_answer}"
       "------"
        f"回答是： {answer}"
    )
     return llm.invoke(prompt)
```

```python
# 问题
question = "王芳是哪个部门的？"
# 正确答案
correct_answer = "王芳是教研部的成员"
# RAG应用给出的回答
answer = "无法确定王芳所属的部门，因为提供的信息中没有提到名为“王芳”的人员。"
check_answer(question,answer,correct_answer)
```

除了检查问题的最终结果，还需要检查RAG应用在召回信息时，是否召回了足够多的相关信息。

```python
def check_contexts(question,contexts):
    prompt = (
        "你是一个测试人员。你需要检测下面的这些参考资料是否能对回答问题提供帮助。\n"
        "回复只能是：有用 或者 无用。请勿给出其他信息。\n"
        "------"
        f"问题是： {question}"
        "------"
        f"参考资料是： {contexts}"
    )
    return llm.invoke(prompt)
```

```python
# 问题
question = "王芳是哪个部门的？"
# RAG应用给出的回答
contexts = ['收集岗位需要的专业\n技能与知识,定期评估员工的职业发展现状,协\n助制定个性化职业发展计划。\n
人\n力\n资\n源\n部\n熊\n伟\n马\n婷 F604 029\n人\n力\n资\n源\n人\n力\n资\n源\n专\n员
\n13800000029\nxiongwe\ni@educo\nmpany.co\nm\n负责公司各项资源政策的实施与执行,分析<\n力资源数据以
优化资源配置,提供决策支持,确\n保人力资源部门顺畅运作。\n行\n政\n部\n黎\n晗\n蔡\n静 G704 033 行\n政\n
行\n政\n专\n员\n13800000033\nlih@educ\nompany.c\nom\n负责采购办公设备与耗材,登记与管理公司固\n定资
产协助实施绩效考核,提供行政管理与协\n调支持,优化行政工作流程。\n行\n政\n部\n秦\n飞\n蔡\n静 G705 034 行
\n政\n行\n政\n专\n员\n13800000034\nqinf@edu\ncompany.\ncom\n维护公司档案与信息系统,负责公司通知及
公\n告的发布,组织公司活动的前期准备与后期评\n估,确保公司各项工作的顺利进行。\nIT\n部\n张\n伟\n马\n云
H802 036\nIT\n支\n撑\nIT\n专\n员\n13800000036\nzhangwei\n036@edu\ncompany.\ncom\n进行公司网络
及硬件设备的配置与维护,监控\n系统运行状态,及时处理技术问题与故障,提供\n技术支持及工具使用培训。\nIT 谢 马
IT IT xieyu@ed 支持公司软件系统的开发与更新,参与IT项目',
 '部 宇 云 H803 037 支\n撑\n专\n员\n13800000037 ucompan\ny.com\n的计划与实施,撰写技术文档与使用说
明,确保\n信息技术的安全性与有效性。\n绩\n效\n管\n理\n部\n朱\n南\n李\n飞 I901 040\n人\n力\n资\n源\n绩
\n效\n专\n员\n1380000004\nzhun@ed\nucompan\ny.com\n责制定绩效考核体系,组织绩效评估的实施与\n反馈,
撰写评估报告,分析绩效数据以提出优化\n建议,提供决策支持。\n绩\n效\n管\n理\n部\n韩\n杉\n李\n飞 1902041\n人\n力\n资\n源\n绩\n效\n专\n员\n13800000041\nhansha\nn@educo\nmpany.co\nm\n建立并维护员工
绩效档案,定期组织绩效评价\n会议,协调各部门反馈,制定考核流程与标准,\n确保绩效考核的有效执行与公正性。']
check_contexts(question,contexts)
```

通过这两个简单的方法，我们就可以构建大量的样本集，样本集中包含了最关系的问题以及预设的正确答案。然后依次拿样本集中的问题，去问询RAG应用，评估RAG应用的答案以及召回信息。这样就可以对RAG应用的准确度进行一个整体的评估。然后再根据这个评估结果，去判断是否符合应用场景的要求。

这就像人脸识别，如果识别准确度不高，那么就只能用来做一些刷脸门禁之类的场景，而不能用来做刷脸支付这类场景。

但是，其实你能够想到，我们这样初步搭建起来的测试方法，其实是不太完善的。比如：

- 大模型是有幻觉问题的，对于一些似是而非的答案，他的检测结果也容易受到影响。
- 对于RAG召回的信息，并不是简单的有用和无用就能判断好坏的。如果RAG应用召回了过多的不相关的信息，即便最终检测有用，其实质量也是不高的。而目前我们都还没有考虑过这些问题。

这时候，就需要借鉴一些成熟的测试框架来进一步完善测试的方法。

## 三、使用Ragas评估RAG应用表现

这类测试框架有很多，主流的有Ragas\DeepEval\Trulens等。LlamaIndex框架自己也提供了检测功能。甚至按照LlamaIndex的设计模式，还提供了和其他主流评测框架集成的实现。这里就以Ragas为例，来介绍一下如何来评估RAG应用的准确性。

Ragas是这个领域里非常著名的一个框架，官网地址： [https://docs.ragas.io/en/stable/getstarted/](https://docs.ragas.io/en/stable/getstarted/) 。他的核心思想和我们之前的简单应用差不多，也是“让大模型来帮助你评估RAG系统”。更重要的是，Ragas设计的评估指标非常契合RAG系统的特点。Ragas提供的评测指标有很多，对于RAG应用，主要关注以下几个指标：

![Ragas 评测指标结构图](images/4.png)

### 评估RAG应用回答质量

Ragas提供了Answer Correctness指标，用于评估RAG应用的整体回答质量。使用这个指标时，需要准备以下数据：

- question：输入给RAG应用的样本问题
- groud_truth：样本问题的正确答案
- answer：RAG应用给出的回答

这里稍微需要注意下的是，由于大模型给出的答案是具有随机性的，所以，在准备answer时，通常建议多收集几次RAG应用的回答，这样评估结果会更完整一点。

接下来，就可以使用Ragas快速评估Answer Correctness指标了。

```python
# 安装ragas依赖
!pip install ragas
```

```python
from langchain_community.embeddings import DashScopeEmbeddings
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_correctness
from config.load_key import load_key

data_samples = {
    # 测试问题
    'question': [
        '王芳是哪个部门的？',
        '王芳是哪个部门的？',
        '王芳是哪个部门的？'
    ],
    # RAG应用给出的答案
    'answer': [
        '无法确定王芳所属的部门，因为提供的信息中没有提到名为“王芳”的人员。',
        '王芳是人事部门的',
        '王芳是教研部的'
    ],
    # 正确的答案
    'ground_truth':[
        '王芳是教研部的成员',
        '王芳是教研部的成员',
        '王芳是教研部的成员'
    ]
}

dataset = Dataset.from_dict(data_samples)
score = evaluate(
    dataset = dataset,
    metrics=[answer_correctness],
    llm=llm,
    embeddings=DashScopeEmbeddings(model="text-embedding-v3",dashscope_api_key=load_key("BAILIAN_API_KEY"))
)
score.to_pandas()
```

可以看到， Ragas的Answer Correctness指标准确的反应了三种回答的表现，越符合事实的answer得分越高。

不过，通常真实的answer不太会像我们这个案例一样，表现出这么多的波动。所以这些answer_correctness的综合评分能够比较客观的体现出RAG应用针对某一个问题的整体表现。

另外，在实际评测时，建议可以采用与RAG应用不同的LLM和Embedding模型，这样可以更全面的评估RAG应用的表现。

### 评估RAG应用检索召回的效果

检索召回阶段，主要使用Context precision和Context recall两个指标来评估RAG应用的召回效果。

- Context precision: precision表示检索出来的条目有多少是正确的，或者说相关的。Ragas在评估这个指标时，还会计算与正确答案相关的条目是否靠前、是否占比高。更加侧重于相关性。
- Context recall：Recall有多少正确的条目被检索出来。主要是评估contexts与groud_truth的试试一致性，侧重于事实准确度。

计算这些指标时，需要准备以下数据：

- question：输入给RAG应用的样本问题
- contexts：RAG应用返回的答案片段
- ground_truth：问题对应的真实答案
- answer：RAG应用给出的回答

```python
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import context_recall,context_precision
from utils import llm

data_samples = {
    # 测试问题
    'question': [
        '王芳是哪个部门的？',
        '王芳是哪个部门的？',
        '王芳是哪个部门的？'
    ],
    # RAG应用给出的答案
    'answer': [
        '无法确定王芳所属的部门，因为提供的信息中没有提到名为“王芳”的人员。',
        '王芳是人事部门的',
        '王芳是教研部的'
    ],
    # 正确的答案
    'ground_truth':[
        '王芳是教研部的成员',
        '王芳是教研部的成员',
        '王芳是教研部的成员'
    ],
    # RAG应用检索出的上下文
    'contexts' : [
        ['提供行政管理与协调支持，优化行政工作流程。 ', '绩效管理部 韩杉 李飞 I902 041 人力资源'],
        ['李凯 教研部主任 ', '牛顿发现了万有引力'],
        ['牛顿发现了万有引力', '王芳 教研部教研专员，他最近在负责课程研发'],
    ],
}

dataset = Dataset.from_dict(data_samples)
score = evaluate(
    dataset = dataset,
    metrics=[context_recall, context_precision],
    llm=llm)
score.to_pandas()
```

从上面的数据可以看到：

- 最后一行数据的回答是准确的
- 过程中检索到的参考资料(contexts)中包含了正确答案的观点，即王芳是教研部的。体现为context recall得分为1。
- 但是contexts中并不是每一条信息都和问题以及答案相关，比如牛顿发现了万有引力。体现为context precision得分为0.5。

### Ragas核心提示词分析

Ragas的许多评测指标也是基于大模型实现的。用户可以直接看到Ragas的很多核心提示词，也同样可以替换他的核心提示词。比如把Ragas默认的英文提示词翻译成中文，这样可以让评测结果更符合中文问答场景。

```python
from ragas.metrics import context_recall,context_precision,answer_correctness
# Ragas的默认提示词。 也可以直接替换。
print(context_recall.context_recall_prompt)
# 也可以直接替换
# context_recall.context_recall_prompt.instruction="xxx"
# context_recall.context_recall_prompt.output_format_instruction="xxx"
# context_recall.context_recall_prompt.examples="xxx"
print("=======")
print(context_precision.context_precision_prompt)
print("=======")
print(answer_correctness.correctness_prompt)
print("=======")
```

其实，如果你认真分析这些提示词，也大概能够猜想到Ragas一些核心指标的计算过程。

对于answer_correctness，他的打分过程需要用到LLM大语言模型和Embedding向量化模型。在打分时，会综合计算answer和ground_truth的语义相似度和事实准确度。

语义相似度主要是通过Embedding模型得到answer和ground_truth的文本向量，然后计算两个文本向量的相似度。向量相似度的计算方法有很多种，比如余弦相似度、欧式距离、曼哈顿距离等。Ragas使用的是最常用的余弦相似度。

事实准确度则会衡量answer和ground_truth在事实描述上的一些差异。在计算指标时，会把answer和ground_truth拆分成一些相对独立的观点列表，然后综合比较answer和ground_truth的这些观点列表的匹配程度。统计F1指标。

在计算context_recall和context_precision时，也会采用计算 answer_correctness 相似的方法。拆分成一些观点，再来计算匹配程度。

如果你对ragas的具体实现感兴趣，可以尝试去研读Ragas的源码。

## 四、总结

对大模型的能力进行合理的评估，这是深度使用大模型必须要走的一个过程。这一章节介绍了针对RAG应用，构建自动化评测体系的基础思路，也演示了如何通过Ragas构建更专业的评测体系。这些评测的经验，都是行业内不可多得的宝贵财富。

对于这些评测框架，我们也只介绍了一些简单的实现。实际上，Ragas除了构建RAG的相关指标外，针对其他大模型的应用场景也构建了非常多的指标。比如针对机器翻译、文本摘要、NL2SQL(自然语言转换成SQL)、Agent等场景，也有非常多的指标。

另外像LlamaIndex、Trulens、Deepeval等其他的大模型评测框架也都从同的角度提供了对大模型进行评测的思路和实现。
