# <font style="color:rgba(0, 0, 0, 0.54);">NLP题库</font>
## <font style="color:rgba(0, 0, 0, 0.87);">Pytorch</font>
---

### <font style="color:rgba(0, 0, 0, 0.87);">练习题</font>
<font style="color:rgba(0, 0, 0, 0.87);">1，标量，向量，张量分别对应几阶张量？</font>

```plain
0，1，2
```

---

<font style="color:rgba(0, 0, 0, 0.87);">2，如何使用pytorch将列表[[1, 2, 3], [3, 2, 1]]转化为张量？</font>

```plain
torch.tensor([[1, 2, 3], [3, 2, 1]])
```

---

<font style="color:rgba(0, 0, 0, 0.87);">3，如何创建一个5x6的全为0和1的张量?</font>

```plain
全为0的张量: torch.zeros([5,6])
全为1的张量: torch.ones([5, 6])
```

---

<font style="color:rgba(0, 0, 0, 0.87);">4，使用torch.rand()创建一个随机张量时, 随机数的范围是多少？</font>

```plain
[0, 1)
```

---

<font style="color:rgba(0, 0, 0, 0.87);">5，如何将tensor([1, 2, 3, 4, 5, 6])形状变换成2x3的张量？</font>

```plain
a = tensor([1, 2, 3, 4, 5, 6])
b = a.view(2, 3)
```

---

<font style="color:rgba(0, 0, 0, 0.87);">6，使用tensor的什么方法只需一次就可以将形状[4,2,3]变成[3,4,2]的张量？</font>

```plain
permute
```

---

<font style="color:rgba(0, 0, 0, 0.87);">7，设a = torch.tensor([[1, 2, 3, 4]]), b = torch.tensor([[2], [3], [4], [5]]), 计算出a.mm(b)的结果？</font>

```plain
tensor([[40]])
```

---

<font style="color:rgba(0, 0, 0, 0.87);">8，pytorch设置张量的哪个属性可以控制是否使其自动求梯度?</font>

```plain
requires_grad
```

---

<font style="color:rgba(0, 0, 0, 0.87);">9，pytorch中通过loss的哪个方法对参数进行梯度的求解？</font>

```plain
loss.backward()
```

---

<font style="color:rgba(0, 0, 0, 0.87);">10, pytorch中自定义网络的基类是什么?</font>

```plain
nn.Module
```

---

<font style="color:rgba(0, 0, 0, 0.87);">11，当模型结构比较简单，在forward函数中没有复杂操作时, 使用nn中的哪个方法构建网络模型?</font>

```plain
nn.Sequential
```

---

<font style="color:rgba(0, 0, 0, 0.87);">12，列举pytorch中常用的优化器（至少两种）?</font>

```plain
torch.optim.SGD
torch.optim.Adam
```

---

<font style="color:rgba(0, 0, 0, 0.87);">13，列举pytorch中常用的损失函数？</font>

```plain
nn.MSELoss()
nn.CrossEntropyLoss()
```

<font style="color:rgba(0, 0, 0, 0.87);">14，使用pytorch定义一个线性模型?</font>

```plain
class Lr(nn.Module):
    def __init__(self):
        super(Lr,self).__init__()
        self.linear = nn.Linear(1,1)

    def forward(self, x):
        out = self.linear(x)
        return out
```

---

<font style="color:rgba(0, 0, 0, 0.87);">15，如何使用pytorch判断GPU是否可用?</font>

```plain
torch.cuda.is_available()
```

---

<font style="color:rgba(0, 0, 0, 0.87);">16, 说出一些常见的优化算法?</font>

```plain
梯度下降算法
随机梯度下降法
小批量梯度下降
动量法
RMSProp
Adam
```

---

<font style="color:rgba(0, 0, 0, 0.87);">17，深度学习中常用的防止过拟合或加速训练方法?</font>

```plain
Dropout
Batch Normalization
```

---

<font style="color:rgba(0, 0, 0, 0.87);">18，pytorch中提供的数据集基类是什么?</font>

```plain
torch.utils.data.Dataset
```

---

## <font style="color:rgba(0, 0, 0, 0.87);">自然语言处理入门</font>
---

### <font style="color:rgba(0, 0, 0, 0.87);">练习题</font>
<font style="color:rgba(0, 0, 0, 0.87);">1，说出几个NLP领域的常见应用场景？</font>

```plain
语音助手
机器翻译
搜索引擎
智能问答
```

---

## <font style="color:rgba(0, 0, 0, 0.87);">文本预处理</font>
---

### <font style="color:rgba(0, 0, 0, 0.87);">练习题</font>
<font style="color:rgba(0, 0, 0, 0.87);">1，说出文本预处理中包含的主要环节?</font>

```plain
文本处理的基本方法
文本张量表示方法
文本语料的数据分析
文本特征处理
数据增强方法
```

---

<font style="color:rgba(0, 0, 0, 0.87);">2，文本处理的基本方法有哪些？</font>

```plain
分词
词性标注
命名实体识别
```

---

<font style="color:rgba(0, 0, 0, 0.87);">3，文本张量的表示方法有哪些?</font>

```plain
one-hot编码
Word2vec
Word Embedding
```

---

<font style="color:rgba(0, 0, 0, 0.87);">4，文本语料的数据分析方法有哪些?</font>

```plain
标签数量分布
句子长度分布
词频统计与关键词词云
```

---

<font style="color:rgba(0, 0, 0, 0.87);">5，深度学习中一般的文本特征处理方法有哪些?</font>

```plain
添加n-gram特征
文本长度规范
```

---

<font style="color:rgba(0, 0, 0, 0.87);">6，常有的有效数据增强方法是什么？</font>

```plain
回译数据增强方法
```

---

<font style="color:rgba(0, 0, 0, 0.87);">7，常见的中文分词工具有哪些(至少两个)?</font>

```plain
jieba
hanlp
```

---

<font style="color:rgba(0, 0, 0, 0.87);">8，使用jieba分词工具对"人生要如何起头，改变要如何起手"进行分词?</font>

```plain
import jieba
jieba.cut("人生要如何起头，改变要如何起手")
或
jieba.lcut("人生要如何起头，改变要如何起手")
```

---

<font style="color:rgba(0, 0, 0, 0.87);">9，使用hanlp分词工具对"人生要如何起头，改变要如何起手"进行分词?</font>

```plain
import hanlp
tokenizer = hanlp.load('CTB6_CONVSEG')
tokenizer("人生要如何起头，改变要如何起手")
```

---

<font style="color:rgba(0, 0, 0, 0.87);">10, 什么是命名实体?</font>

```plain
通常我们将人名, 地名, 机构名等专有名词统称命名实体.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">11, 使用hanlp工具对'上海华安工业（集团）公司董事长谭旭光和秘书张晚霞来到美 国纽约现代艺术博物馆参观。'进行命名实体识别.</font>

```plain
import hanlp
recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)
recognizer(list('上海华安工业（集团）公司董事长谭旭光和秘书张晚霞来到美国纽约现代艺术博物馆参观。'))
```

---

<font style="color:rgba(0, 0, 0, 0.87);">12，使用hanlp工具对'President Obama is speaking at the White House'进行英文命名实体识别.</font>

```plain
import hanlp
recognizer = hanlp.load(hanlp.pretrained.ner.CONLL03_NER_BERT_BASE_UNCASED_EN))
recognizer(["President", "Obama", "is", "speaking", "at", "the", "White", "House"])
```

---

<font style="color:rgba(0, 0, 0, 0.87);">13，什么是词性标注?</font>

```plain
词性标注(Part-Of-Speech tagging, 简称POS)就是标注出一段文本中每个词汇的词性.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">14，使用jieba对"我爱北京天安门"进行词性标注.</font>

```plain
import jieba.posseg as pseg
pseg.lcut("我爱北京天安门")
```

---

<font style="color:rgba(0, 0, 0, 0.87);">15, 使用hanlp对"我爱北京天安门"进行词性标注.</font>

```plain
import hanlp
tagger = hanlp.load(hanlp.pretrained.pos.CTB5_POS_RNN_FASTTEXT_ZH)
tagger(['我', '爱', '北京', '天安门'])
```

---

<font style="color:rgba(0, 0, 0, 0.87);">16，使用hanlp对"I will not worry about it"进行词性标注.</font>

```plain
import hanlp
tagger = hanlp.load(hanlp.pretrained.pos.PTB_POS_RNN_FASTTEXT_EN)
tagger(list("I will not worry about it"))
```

---

<font style="color:rgba(0, 0, 0, 0.87);">17，什么是文本张量表示?</font>

```plain
将一段文本使用张量进行表示，其中一般将词汇为表示成向量，称作词向量，再由各个词向量按顺序组成矩阵形成文本表示.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">18, 说一说one-hot编码的劣势.</font>

```plain
完全割裂了词与词之间的联系，而且在大语料集下，每个向量的长度过大，占据大量内存.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">19，word2vec的两种训练模式是什么?</font>

```plain
CBOW(Continuous bag of words)模式
skipgram模式
```

---

<font style="color:rgba(0, 0, 0, 0.87);">20，实现word2vec常用的工具?</font>

```plain
fasttext
```

---

<font style="color:rgba(0, 0, 0, 0.87);">21，什么是word embedding？</font>

```plain
通过一定的方式将词汇映射到指定维度(一般是更高维度)的空间.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">22，进行标签数量分布统计的原因？</font>

```plain
在深度学习模型评估中, 我们一般使用ACC作为评估指标, 若想将ACC的基线定义在50%左右, 则需要我们的正负样本比例维持在1:1左右, 否则就要进行必要的数据增强或数据删减. 上图中训练和验证集正负样本都稍有不均衡, 可以进行一些数据增强.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">23，进行句子长度分布统计的原因?</font>

```plain
通过绘制句子长度分布图, 可以得知我们的语料中大部分句子长度的分布范围, 因为模型的输入要求为固定尺寸的张量，合理的长度范围对之后进行句子截断补齐(规范长度)起到关键的指导作用.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">24，绘制高频词词云的原因？</font>

```plain
根据高频形容词词云显示, 我们可以对当前语料质量进行简单评估, 同时对违反语料标签含义的词汇进行人工审查和修正, 来保证绝大多数语料符合训练标准.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">25，什么是n-gram特征?</font>

```plain
给定一段文本序列, 其中n个词或字的相邻共现特征即n-gram特征, 常用的n-gram特征是bi-gram和tri-gram特征, 分别对应n为2和3.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">26，什么是文本你长度规范及其作用?</font>

```plain
一般模型的输入需要等尺寸大小的矩阵, 因此在进入模型前需要对每条文本数值映射后的长度进行规范, 此时将根据句子长度分布分析出覆盖绝大多数文本的合理长度, 对超长文本进行截断, 对不足文本进行补齐(一般使用数字0), 这个过程就是文本长度规范.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">27，什么是回译数据增强法？</font>

```plain
回译数据增强目前是文本数据增强方面效果较好的增强方法, 一般基于google翻译接口, 将文本数据翻译成另外一种语言(一般选择小语种),之后再翻译回原语言, 即可认为得到与与原语料同标签的新语料, 新语料加入到原数据集中即可认为是对原数据集数据增强.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">28，HMM模型的作用是什么？</font>

```plain
在NLP领域, HMM用来解决文本序列标注问题. 如分词, 词性标注, 命名实体识别都可以看作是序列标注问题.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">29，CRF模型的作用是什么？</font>

```plain
CRF(Conditional Random Fields), 中文称作条件随机场, 同HMM一样, 它一般也以文本序列数据为输入, 以该序列对应的隐含序列为输出.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">30, HMM与CRF模型之间差异是什么？</font>

```plain
HMM模型存在隐马假设, 而CRF不存在, 因此HMM的计算速度要比CRF模型快很多, 适用于对预测性能要求较高的场合.
同样因为隐马假设, 当预测问题中隐含序列单元并不是只与上一个单元有关时, HMM的准确率会大大降低, 而CRF不受这样限制, 准确率明显高于HMM.
```

---

## <font style="color:rgba(0, 0, 0, 0.87);">RNN</font>
---

### <font style="color:rgba(0, 0, 0, 0.87);">练习题</font>
---

<font style="color:rgba(0, 0, 0, 0.87);">1，什么是RNN模型？</font>

```plain
RNN(Recurrent Neural Network), 中文称作循环神经网络, 它一般以序列数据为输入, 通过网络内部的结构设计有效捕捉序列之间的关系特征, 一般也是以序列形式进行输出.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">2，RNN模型的作用是什么？</font>

```plain
因为RNN结构能够很好利用序列之间的关系, 因此针对自然界具有连续性的输入序列, 如人类的语言, 语音等进行很好的处理, 广泛应用于NLP领域的各项任务, 如文本分类, 情感分析, 意图识别, 机器翻译等.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">3，按照输入和输出的结构，RNN将分为哪几个类别？</font>

```plain
N vs N - RNN
N vs 1 - RNN
1 vs N - RNN
N vs M - RNN
```

---

<font style="color:rgba(0, 0, 0, 0.87);">4, 按照RNN的内部构造，RNN将分为哪几个类别？</font>

```plain
传统RNN
LSTM
Bi-LSTM
GRU
Bi-GRU
```

---

<font style="color:rgba(0, 0, 0, 0.87);">5，传统RNN模型的内部计算公式是什么？</font>

![]()

---

<font style="color:rgba(0, 0, 0, 0.87);">6，传统RNN的优势和缺点分别是什么？</font>

```plain
由于内部结构简单, 对计算资源要求低, 相比之后我们要学习的RNN变体:LSTM和GRU模型参数总量少了很多, 在短序列任务上性能和效果都表现优异.

传统RNN在解决长序列之间的关联时, 通过实践，证明经典RNN表现很差, 原因是在进行反向传播的时候, 过长的序列导致梯度的计算异常, 发生梯度消失或爆炸.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">7, 什么是梯度消失或爆炸？</font>

```plain
根据反向传播算法和链式法则, w的初始值往往小于1，梯度会在计算过程中变得非常非常小, 这种现象称作梯度消失. 反之, 如果我们人为的增大w的值, 使其大于1, 那么连乘够就可能造成梯度过大, 称作梯度爆炸.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">8，梯度消失或爆炸的危害是什么？</font>

```plain
如果在训练过程中发生了梯度消失，权重无法被更新，最终导致训练失败; 梯度爆炸所带来的梯度过大，大幅度更新网络参数，在极端情况下，结果会溢出（NaN值）.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">9, LSTM（Long Short-Term Memory）的四个内部核心结构？</font>

```plain
遗忘门
输入门
细胞状态
输出门
```

---

<font style="color:rgba(0, 0, 0, 0.87);">10，LSTM中输出门的计算公式是什么？</font>

![]()

---

<font style="color:rgba(0, 0, 0, 0.87);">11，LSTM中细胞状态更新的计算公式是什么？</font>

![]()

---

<font style="color:rgba(0, 0, 0, 0.87);">12，LSTM中输入门的计算公式是什么？</font>

![]()

---

<font style="color:rgba(0, 0, 0, 0.87);">13，LSTM中遗忘门的计算公式是什么？</font>

![]()

---

<font style="color:rgba(0, 0, 0, 0.87);">14，GRU的内部核心结构是什么？</font>

```plain
更新门
重置门
```

---

<font style="color:rgba(0, 0, 0, 0.87);">15，GRU的内部结构公式是什么？</font>

![]()

---

<font style="color:rgba(0, 0, 0, 0.87);">16，GRU的优势和缺点是什么？</font>

```plain
GRU和LSTM作用相同, 在捕捉长序列语义关联时, 能有效抑制梯度消失或爆炸, 效果都优于传统RNN且计算复杂度相比LSTM要小.

GRU仍然不能完全解决梯度消失问题, 同时其作用RNN的变体, 有着RNN结构本身的一大弊端, 即不可并行计算, 这在数据量和模型体量逐步增大的未来, 是RNN发展的关键瓶颈.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">17，什么是注意力机制？</font>

```plain
注意力机制是注意力计算规则能够应用的深度学习网络的载体, 同时包括一些必要的全连接层以及相关张量处理, 使其与应用网络融为一体. 使自注意力计算规则的注意力机制称为自注意力机制.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">18，注意力机制的作用是什么？</font>

```plain
在解码器端的注意力机制: 能够根据模型目标有效的聚焦编码器的输出结果, 当其作为解码器的输入时提升效果. 改善以往编码器输出是单一定长张量, 无法存储过多信息的情况.
在编码器端的注意力机制: 主要解决表征问题, 相当于特征提取过程, 得到输入的注意力表示. 一般使用自注意力(self-attention).
```

---

<font style="color:rgba(0, 0, 0, 0.87);">19，实现基于注意力计算规则</font>![]()<font style="color:rgba(0, 0, 0, 0.87);">的Attention类.</font>

```plain
import torch
import torch.nn as nn
import torch.nn.functional as F

class Attn(nn.Module):
    def __init__(self, query_size, key_size, value_size1, value_size2, output_size):
        """初始化函数中的参数有5个, query_size代表query的最后一维大小
           key_size代表key的最后一维大小, value_size1代表value的导数第二维大小, 
           value = (1, value_size1, value_size2)
           value_size2代表value的倒数第一维大小, output_size输出的最后一维大小"""
        super(Attn, self).__init__()
        # 将以下参数传入类中
        self.query_size = query_size
        self.key_size = key_size
        self.value_size1 = value_size1
        self.value_size2 = value_size2
        self.output_size = output_size

        # 初始化注意力机制实现第一步中需要的线性层.
        self.attn = nn.Linear(self.query_size + self.key_size, value_size1)

        # 初始化注意力机制实现第三步中需要的线性层.
        self.attn_combine = nn.Linear(self.query_size + value_size2, output_size)


    def forward(self, Q, K, V):
        """forward函数的输入参数有三个, 分别是Q, K, V, 根据模型训练常识, 输入给Attion机制的
           张量一般情况都是三维张量, 因此这里也假设Q, K, V都是三维张量"""

        # 第一步, 按照计算规则进行计算, 
        # 我们采用常见的第一种计算规则
        # 将Q，K进行纵轴拼接, 做一次线性变化, 最后使用softmax处理获得结果
        attn_weights = F.softmax(
            self.attn(torch.cat((Q[0], K[0]), 1)), dim=1)

        # 然后进行第一步的后半部分, 将得到的权重矩阵与V做矩阵乘法计算, 
        # 当二者都是三维张量且第一维代表为batch条数时, 则做bmm运算
        attn_applied = torch.bmm(attn_weights.unsqueeze(0), V)

        # 之后进行第二步, 通过取[0]是用来降维, 根据第一步采用的计算方法, 
        # 需要将Q与第一步的计算结果再进行拼接
        output = torch.cat((Q[0], attn_applied[0]), 1)

        # 最后是第三步, 使用线性层作用在第三步的结果上做一个线性变换并扩展维度，得到输出
        # 因为要保证输出也是三维张量, 因此使用unsqueeze(0)扩展维度
        output = self.attn_combine(output).unsqueeze(0)
        return output, attn_weights
```

<font style="color:rgba(0, 0, 0, 0.87);">20，在"使用RNN模型构建人名分类器"的案例中, 哪种RNN模型表现最好, 为什么？</font>

```plain
传统RNN的模型收敛情况最好, 然后是GRU, 最后是LSTM, 这是因为: 我们当前处理的文本数据是人名, 他们的长度有限, 且长距离字母间基本无特定关联, 因此无法发挥改进模型LSTM和GRU的长距离捕捉语义关联的优势. 所以在以后的模型选用时, 要通过对任务的分析以及实验对比, 选择最适合的模型.

同时, 传统RNN复杂度最低, 耗时几乎只是后两者的一半, 然后是GRU, 最后是复杂度最高的LSTM.
```

---

## <font style="color:rgba(0, 0, 0, 0.87);">Transformer</font>
---

### <font style="color:rgba(0, 0, 0, 0.87);">练习题</font>
<font style="color:rgba(0, 0, 0, 0.87);">1，Transformer模型的作用是什么？</font>

```plain
基于seq2seq架构的transformer模型可以完成NLP领域研究的典型任务, 如机器翻译, 文本生成等. 同时又可以构建预训练语言模型，用于不同任务的迁移学习.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">2，Transformer总体架构可分为哪四个部分？</font>

```plain
输入部分
输出部分
编码器部分
解码器部分
```

---

<font style="color:rgba(0, 0, 0, 0.87);">3，Transformer的输入部分包含什么？</font>

```plain
源文本嵌入层及其位置编码器
目标文本嵌入层及其位置编码器
```

---

<font style="color:rgba(0, 0, 0, 0.87);">4，Transformer的输出部分包含什么？</font>

```plain
线性层
softmax层
```

---

<font style="color:rgba(0, 0, 0, 0.87);">5，说一说文本嵌入层的作用.</font>

```plain
无论是源文本嵌入还是目标文本嵌入，都是为了将文本中词汇的数字表示转变为向量表示, 希望在这样的高维空间捕捉词汇间的关系.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">6，什么是掩码张量?</font>

```plain
掩代表遮掩，码就是我们张量中的数值，它的尺寸不定，里面一般只有1和0的元素，代表位置被遮掩或者不被遮掩，至于是0位置被遮掩还是1位置被遮掩可以自定义，因此它的作用就是让另外一个张量中的一些数值被遮掩，也可以说被替换, 它的表现形式是一个张量.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">7，掩码张量的作用？</font>

```plain
在transformer中, 掩码张量的主要作用在应用attention时，有一些生成的attention张量中的值计算有可能已知了未来信息而得到的，未来信息被看到是因为训练时会把整个输出结果都一次性进行Embedding，但是理论上解码器的的输出却不是一次就能产生最终结果的，而是一次次通过上一次结果综合得出的，因此，未来的信息可能被提前利用. 所以，我们会进行遮掩.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">8，Transformer中的注意力计算规则是什么？</font>

![]()

---

<font style="color:rgba(0, 0, 0, 0.87);">9，什么是注意力机制？</font>

```plain
注意力机制是注意力计算规则能够应用的深度学习网络的载体, 除了注意力计算规则外, 还包括一些必要的全连接层以及相关张量处理, 使其与应用网络融为一体. 使用自注意力计算规则的注意力机制称为自注意力机制.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">10，说一说多头注意力机制的作用.</font>

```plain
这种结构设计能让每个注意力机制去优化每个词汇的不同特征部分，从而均衡同一种注意力机制可能产生的偏差，让词义拥有来自更多元的表达，实验表明可以从而提升模型效果.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">11，Transformer中前馈全连接具有几层网络？</font>

```plain
2
```

---

<font style="color:rgba(0, 0, 0, 0.87);">12，说一说Transformer中前馈全连接层的作用.</font>

```plain
考虑注意力机制可能对复杂过程的拟合程度不够, 通过增加两层网络来增强模型的能力.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">13，说一说Transformer中规范化层的作用.</font>

```plain
它是所有深层网络模型都需要的标准网络层，因为随着网络层数的增加，通过多层的计算后参数可能开始出现过大或过小的情况，这样可能会导致学习过程出现异常，模型可能收敛非常的慢. 因此都会在一定层数后接规范化层进行数值的规范化，使其特征数值在合理范围内.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">14，说一说Transformer中编码器层的作用.</font>

```plain
作为编码器的组成单元, 每个编码器层完成一次对输入的特征提取过程, 即编码过程.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">15，说一说Transformer中解码器层的作用.</font>

```plain
作为解码器的组成单元, 每个解码器层根据给定的输入向目标方向进行特征提取操作，即解码过程.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">16，说一说标签平滑的作用.</font>

```plain
标签平滑的作用就是小幅度的改变原有标签值的值域，因为在理论上即使是人工的标注数据也可能并非完全正确, 会受到一些外界因素的影响而产生一些微小的偏差, 因此使用标签平滑来弥补这种偏差, 减少模型对某一条规律的绝对认知, 以防止过拟合.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">17，什么是语言模型?</font>

```plain
以一个符合语言规律的序列为输入，模型将利用序列间关系等特征，输出一个在所有词汇上的概率分布.这样的模型称为语言模型.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">18，语言模型能解决哪些问题?</font>

```plain
1, 根据语言模型的定义，可以在它的基础上完成机器翻译，文本生成等任务，因为我们通过最后输出的概率分布来预测下一个词汇是什么.
2, 语言模型可以判断输入的序列是否为一句完整的话，因为我们可以根据输出的概率分布查看最大概率是否落在句子结束符上，来判断完整性.
3, 语言模型本身的训练目标是预测下一个词，因为它的特征提取部分会抽象很多语言序列之间的关系，这些关系可能同样对其他语言类任务有效果.因此可以作为预训练模型进行迁移学习.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">19，语言模型训练的评估指标一般使用什么?</font>

```plain
困惑度
```

---

<font style="color:rgba(0, 0, 0, 0.87);">20，基于Transformer模型的优势?</font>

```plain
1, Transformer能够利用分布式GPU进行并行训练，提升模型训练效率.    
2, 在分析预测更长的文本时, 捕捉间隔较长的语义关联效果更好.
```

---

## <font style="color:rgba(0, 0, 0, 0.87);">迁移学习</font>
---

### <font style="color:rgba(0, 0, 0, 0.87);">练习题</font>
---

<font style="color:rgba(0, 0, 0, 0.87);">1，fasttext的两大作用是什么？</font>

```plain
进行文本分类
训练词向量
```

---

<font style="color:rgba(0, 0, 0, 0.87);">2，fasttext工具包的优势是什么?</font>

```plain
正如它的名字, 在保持较高精度的情况下, 快速的进行训练和预测是fasttext的最大优势.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">3，文本分类的种类有哪些?</font>

```plain
二分类:
文本被分类两个类别中, 往往这两个类别是对立面, 比如: 判断一句评论是好评还是差评.
单标签多分类:
文本被分入到多个类别中, 且每条文本只能属于某一个类别(即被打上某一个标签), 比如: 输入一个人名, 判断它是来自哪个国家的人名.
多标签多分类:
文本被分人到多个类别中, 但每条文本可以属于多个类别(即被打上多个标签), 比如: 输入一段描述, 判断可能是和哪些兴趣爱好有关, 一段描述中可能即讨论了美食, 又太讨论了游戏爱好.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">4，fasttext训练文本分类模型的方法是什么?</font>

```plain
fasttext.train_supervised()
```

---

<font style="color:rgba(0, 0, 0, 0.87);">5，说出几种fasttext进行模型调优的方法?</font>

```plain
1, 对数据进行预处理
2, 修改训练轮数
3, 调整学习率
4, 添加n-gram特征
5, 修改损失计算方式
```

---

<font style="color:rgba(0, 0, 0, 0.87);">6，fasttext训练词向量的方法是什么?</font>

```plain
fasttext.train_unsupervised()
```

---

<font style="color:rgba(0, 0, 0, 0.87);">7，什么是词向量迁移？</font>

```plain
使用在大型语料库上已经进行训练完成的词向量模型.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">8，fasttext在Wikipedia语料上提供了多少中语言进行可迁移的词向量模型?</font>

```plain
294
```

---

<font style="color:rgba(0, 0, 0, 0.87);">9，什么是预训练模型(Pretrained model)?</font>

```plain
一般情况下预训练模型都是大型模型，具备复杂的网络结构，众多的参数量，以及在足够大的数据集下进行训练而产生的模型. 在NLP领域，预训练模型往往是语言模型，因为语言模型的训练是无监督的，可以获得大规模语料，同时语言模型又是许多典型NLP任务的基础，如机器翻译，文本生成，阅读理解等，常见的预训练模型有BERT, GPT, roBERTa, transformer-XL等.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">10，什么是微调(Fine-tuning)？</font>

```plain
根据给定的预训练模型，改变它的部分参数或者为其新增部分输出结构后，通过在小部分数据集上训练，来使整个模型更好的适应特定任务.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">11，什么是微调脚本(Fine-tuning script)？</font>

```plain
实现微调过程的代码文件。这些脚本文件中，应包括对预训练模型的调用，对微调参数的选定以及对微调结构的更改等，同时，因为微调是一个训练过程，它同样需要一些超参数的设定，以及损失函数和优化器的选取等, 因此微调脚本往往也包含了整个迁移学习的过程.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">12，说一说常见的两种迁移方式.</font>

```plain
直接使用预训练模型，进行相同任务的处理，不需要调整参数或模型结构，这些模型开箱即用。但是这种情况一般只适用于普适任务, 如：fasttest工具包中预训练的词向量模型。另外，很多预训练模型开发者为了达到开箱即用的效果，将模型结构分各个部分保存为不同的预训练模型，提供对应的加载方法来完成特定目标.
更加主流的迁移学习方式是发挥预训练模型特征抽象的能力，然后再通过微调的方式，通过训练更新小部分参数以此来适应不同的任务。这种迁移方式需要提供小部分的标注数据来进行监督学习.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">13，CoLA数据集任务类型及其评估指标?</font>

```plain
二分类任务
评估指标为: MMC(马修斯相关系数, 在正负样本分布十分不均衡的情况下使用的二分类评估指标)
```

---

<font style="color:rgba(0, 0, 0, 0.87);">14，SST-2数据集的任务类型及其评估指标?</font>

```plain
二分类任务
评估指标为: ACC
```

---

<font style="color:rgba(0, 0, 0, 0.87);">15，MRPC数据集的任务类型及其评估指标?</font>

```plain
句子对二分类任务
评估指标为: ACC和F1
```

---

<font style="color:rgba(0, 0, 0, 0.87);">16，STS-B数据集的任务类型及其评估指标?</font>

```plain
句子对多分类任务/句子对回归任务
评估指标为: Pearson-Spearman Corr
```

---

<font style="color:rgba(0, 0, 0, 0.87);">17，QQP数据集的任务类型及其评估指标？</font>

```plain
句子对二分类任务
评估指标为: ACC/F1
```

---

<font style="color:rgba(0, 0, 0, 0.87);">18，MNLI数据集的任务类型及其评估指标？</font>

```plain
句子对多分类任务
评估指标为: ACC
```

---

<font style="color:rgba(0, 0, 0, 0.87);">19，(QNLI/RTE/WNLI)数据集的任务类型及其评估指标?</font>

```plain
句子对二分类任务
评估指标为: ACC
```

---

<font style="color:rgba(0, 0, 0, 0.87);">20，说出几种当下NLP中流行的预训练模型.</font>

```plain
BERT
GPT
GPT-2
Transformer-XL
XLNet
XLM
RoBERTa
DistilBERT
ALBERT
T5
XLM-RoBERTa
```

---

<font style="color:rgba(0, 0, 0, 0.87);">21，pytorch中加载和使用预训练模型的工具是什么?</font>

```plain
我们使用torch.hub工具进行模型的加载和使用.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">22，加载和使用预训练模型的步骤是什么？</font>

```plain
第一步: 确定需要加载的预训练模型并安装依赖包.
第二步: 加载预训练模型的映射器tokenizer.
第三步: 加载带/不带头的预训练模型.
第四步: 使用模型获得输出结果.
```

---

<font style="color:rgba(0, 0, 0, 0.87);">23，使用指定任务类型的微调脚本的步骤是什么？</font>

```plain
第一步: 下载微调脚本文件
第二步: 配置微调脚本参数
第三步: 运行并检验效果
```

---

<font style="color:rgba(0, 0, 0, 0.87);">24，通过微调脚本微调后模型的使用步骤是什么？</font>

```plain
第一步: 在https://huggingface.co/join上创建一个帐户
第二步: 在服务器终端使用transformers-cli登陆
第三步: 使用transformers-cli上传模型并查看
第四步: 使用pytorch.hub加载模型进行使用
```

---

## <font style="color:rgba(0, 0, 0, 0.87);">项目1: 智能文本分类</font>
---

### <font style="color:rgba(0, 0, 0, 0.87);">实践题</font>
<font style="color:rgba(0, 0, 0, 0.87);">1，认真学习第二章的内容, 你会发现在2.4 获取词汇集一节中, 我们只讲解了如何获取"时尚"有关的词汇集, 我们还为大家准备了"影视", "美妆", "明星"的原始数据集, 下面请参考"时尚"数据集，完成其他三类原始数据集的词汇集获取过程.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">2，根据2.5 将词汇集导入图谱的过程, 将刚刚获取的"影视", "美妆", "明星"等词汇集导入到图谱之中.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">3，认真学习第三章的内容，参考3.1 获取训练语料的过程, 将我们在目录/data/django-uwsgi/text_labeled/create_graph下, 给出的fashion, movie, star三个原始语料文件, 提取出它们正负样本. 最终在对应的目录下生成sample.csv文件.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">4，请参考3.2 进行数据分析的过程，对其他获取的训练数据(fashion, beauty, star)进行类似的数据分析, 并在对应的文件中生成三张数据分析分布图.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">5，请参考3.3 特征处理的过程，在/data/django-uwsgi/text_labeled/model_train目录下, 创建star_model_train.py, beauty_model_train.py, fashion_model_train.py三个文件, 并根据数据分析的结果写出它们的特征处理流程.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">6，请参考3.4 构建模型结构的过程，在/data/django-uwsgi/text_labeled/model_train目录下, 在star_model_train.py, beauty_model_train.py, fashion_model_train.py三个文件中构建对应的模型结构.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">7，请参考3.5 选取损失函数和优化方法, 在/data/django-uwsgi/text_labeled/model_train目录下, 在star_model_train.py, beauty_model_train.py, fashion_model_train.py三个文件中选取损失函数和优化方法.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">8，请参考3.6 进行模型训练, 在/data/django-uwsgi/text_labeled/model_train目录下, 在star_model_train.py, beauty_model_train.py, fashion_model_train.py三个文件中构建模型训练函数, 并进行训练, 得到损失以及准确率对比曲线.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">9，请参考3.7 模型保存与加载, 在/data/django-uwsgi/text_labeled/model_train目录下, 在star_model_train.py, beauty_model_train.py, fashion_model_train.py三个文件中进行模型保存与加载函数, 得到对应的h5模型.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">10，认真学习第四章的内容，参考4.1 多模型多进程训练，将star_model_train.py和fashion_model_train.py的模型训练脚本命令放到model_train_list中, 再进行一次多进程并行训练, 看看是怎样的效果.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">11，请参考4.2 多模型多线程预测, 将beauty, star, fashion中对应的h5模型转化为pb模型, 在对应的文件中生成保存模型的时间戳文件夹并使用docker启动对应的tensorflow-serving微服务, 使其运行成功.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">12，认真学习第一章和第五章的内容，参考5.1 系统联调与测试，将服务重新启动并使用测试脚本进行测试，保证新加入的模型服务能够正常运行.</font>

---

---

## <font style="color:rgba(0, 0, 0, 0.87);">项目2: 在线医生</font>
---

### <font style="color:rgba(0, 0, 0, 0.87);">实践题</font>
<font style="color:rgba(0, 0, 0, 0.87);">1，尝试使用命令"match(a) detach delete a"清空图数据库，参考4.2 结构化数据流水线, 将/data/doctor_offline/structured/noreview/目录下的csv文件导入到图数据库当中, 使其满足"疾病-症状"的节点和关系效果.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">2，参考5.3 BERT中文预训练模型, 对单条句子"人生该如何起头"使用BERT中文预训练模型进行编码.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">3，参考8.3 BERT中文预训练模型, 对句子对"人生该如何起头", "改变要如何起手"使用BERT中文预训练模型进行编码.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">4，参考5.2 训练数据集, 将命名实体审核中训练数据加载到内存中, 并取出20条进行查看.</font>

---

<font style="color:rgba(0, 0, 0, 0.87);">5，参考8.4 微调模型, 将其更改一为一个具有三层全连接的神经网络, 并使用这个微调模型进行训练，与当前的微调模型进行效果对比.</font>

  
 

