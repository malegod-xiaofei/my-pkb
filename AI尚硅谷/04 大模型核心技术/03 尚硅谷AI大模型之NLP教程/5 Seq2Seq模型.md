# 5 Seq2Seq模型

## 5.1 概述

传统的自然语言处理任务（如文本分类、序列标注）以​​静态输出​​为主，其目标是预测固定类别或标签。然而，现实中的许多应用需要模型​​动态生成新的序列​​，例如：

- ​​机器翻译​​：输入中文句子，输出对应的英文翻译。
- ​​文本摘要​​：输入长篇文章，生成简短的摘要。
- ​​问答系统​​：输入用户问题，生成自然语言回答。
- ​​对话系统​​：输入对话历史，生成连贯的下一条回复。

这些任务具有两个关键共同点：

- ​​输入和输出均为序列​​（如词、字符或子词序列）。
- ​​输入与输出序列长度动态可变​​（例如翻译任务中，中英文句子长度可能不同）。

为了解决这类问题，研究者提出了Seq2Seq（Sequence to Sequence，序列到序列）模型。

![图片89.png](images/图片89.png)

## 5.2 模型结构详解

Seq2Seq 模型由一个编码器（Encoder）和一个解码器（Decoder）构成。编码器负责提取输入序列的语义信息，并将其压缩为一个固定长度的上下文向量（Context Vector）；解码器则基于该向量，逐步生成目标序列。

![图片90.png](images/图片90.png)

### 5.2.1 编码器

编码器主要由一个循环神经网络（RNN/LSTM/GRU）构成，其任务是将输入序列的语义信息提取并压缩为一个上下文向量。

在模型处理输入序列时，循环神经网络会依次接收每个token的输入，并在每个时间步步更新隐藏状态。每个隐藏状态都携带了截止到当前位置为止的信息。随着序列推进，信息不断累积，最终会在最后一个时间步形成一个包含整句信息的隐藏状态。

这个最后的隐藏状态就会作为上下文向量（context vector），传递给解码器，用于指导后续的序列生成。

![图片91.png](images/图片91.png)

为增强编码器的理解能力，循环网络也可以采用双向结构（结合前文与后文信息）或多层结构（提取更深的语义特征）。

### 5.2.2 解码器

解码器主要也由一个循环神经网络（RNN / LSTM / GRU）构成，其任务是基于编码器传递的上下文向量，逐步生成目标序列。

![图片92.png](images/图片92.png)

在生成开始时，循环神经网络以上下文向量作为初始隐藏状态，并接收一个特殊的起始标记 `<sos>`（start of sentence）作为第一个时间步的输入，用于预测第一个 token。

随后，在每一个时间步，模型都会根据前一时刻的隐藏状态和上一步生成的 token，预测当前的输出。这种“将前一步的输出作为下一步输入”的方式被称为自回归生成（Autoregressive Generation），它确保了生成结果的连贯性。

生成过程会持续进行，直到模型生成了一个特殊的结束标记 `<eos>`（end of sentence），表示句子生成完成。

说明：起始标记和结束标记会在训练数据中显式添加，模型会在训练中学会何时开始、如何续写，以及何时结束，从而掌握完整的生成流程。

## 5.3 模型训练和推理机制

### 5.3.1 模型训练

Seq2Seq 模型的训练目标，是在给定输入序列的条件下，逐步生成完整且准确的目标序列。下面以一个中–英机器翻译样本为例，说明训练过程的各个环节。

假设某个训练样本为：

中文输入：“我喜欢你。”

英文输出：“I like you.”

#### 5.3.1.1 数据准备

为了让模型明确目标序列的起点和终点，通常在目标句前添加 `<sos>`（start of sequence），句末添加 `<eos>`（end of sequence）：

“I like you.” → “`<sos>` I like you. `<eos>`”

这两个特殊标记帮助模型学会从哪里开始生成，以及何时停止生成。

#### 5.3.1.2 前向传播

模型由编码器和解码器两部分组成：

##### 5.3.1.2.1 编码器

编码器接收源语言序列“我喜欢你。”，通过嵌入层和循环神经网络（RNN / LSTM / GRU）的逐步处理，将整句编码为上下文向量。

##### 5.3.1.2.2 解码器

解码器使用该上下文向量初始化其隐藏状态，然后逐步生成目标序列。

需要特别注意的是，训练阶段与推理阶段的解码策略是不同的：

在推理阶段，解码器采用自回归生成方式：每一步的输入是模型自己上一步的预测结果。

而在训练阶段，通常使用一种称为 Teacher Forcing 的策略，即：

解码器每一步的输入不是模型上一步的预测结果，而是目标序列中真实的前一个token。如图下图所示

![图片93.png](images/图片93.png)

这种做法带来了两个明显好处：

- 训练更快，误差不会累积；
- 梯度传播更稳定，有利于优化收敛。

#### 5.3.1.3 计算损失

解码器每一步输出一个token的概率分布，我们通过交叉熵损失函数衡量模型对真实词的预测质量。训练过程中，每一个时间步都会产生一个损失值。该样本的总损失，就是所有时间步的损失值逐步累加的结果。

![图片94.png](images/图片94.png)

#### 5.3.1.4 反向传播

在 PyTorch 中，调用 loss.backward() 即可自动完成梯度的反向传播。系统会沿时间维度展开计算图，自动完成所有参数的梯度计算，无需手动推导，实现简洁高效。

### 5.3.2 模型推理

模型推理是Seq2Seq模型在实际任务中生成目标序列的过程，通常包括以下几个环节：

#### 5.3.2.1 编码器处理

推理阶段的编码器处理流程与训练时完全一致。

输入序列会经过分词、嵌入和循环神经网络的逐步处理，最终生成一个表示整句语义的上下文向量，该向量将作为解码器的初始隐藏状态，为生成过程提供语义基础。

#### 5.3.2.2 解码器处理

解码器是推理过程的核心，其生成方式采用自回归生成（Autoregressive Generation）：每一步的输出会作为下一步的输入，逐步构造完整句子。

##### 5.3.2.2.1 自回归生成流程

第一步，解码器接收起始标记 `<sos>`，生成第一个词；

第二步，将上一步生成的词作为当前输入，再预测第二个词；

持续重复以上过程，直到模型生成 `<eos>`，或达到设定的最大生成步数。

##### 5.3.2.2.2 词选择策略

每个时间步，解码器输出的是一个词概率分布。我们需要从中选择一个具体词作为本时间步的输出，选择方式即为生成策略。常见策略包括：

- 贪心解码（Greedy Decoding）

每一步都选择概率最高的词。

优点：简单高效

缺点：容易陷入局部最优，生成不够多样。

- 束搜索（Beam Search）

每一步保留多个候选词序列（如 beam size = 3），并在扩展后选择得分最高的完整句子。

优点：全局考虑，生成质量高

缺点：计算开销大

## 5.4 案例实操（中英翻译V1.0）

### 5.4.1 需求说明

本案例的目标是实现一个简易的中→英翻译模型，输入为中文句子（如“我喜欢你。”），输出为英文翻译结果（如“I like you.”）。

### 5.4.2 需求分析

#### 5.4.2.1 数据处理

本案例使用的数据集来自，共包含 29,155 对中英文平行语句。原始文件为 TSV 格式，每行包含一对中文句子和对应的英文翻译，结构如下图所示：

![图片95.png](images/图片95.png)

在本案例中，仅使用前两列数据：中文句子作为模型输入（源语言），英文句子作为模型输出（目标语言）。

需要注意的是，输入和输出序列需要单独分词和构建词表，其中中文按照字粒度分词，英文使用分词工具。

#### 5.4.2.2 模型设计

模型采用经典的 Seq2Seq 架构，由编码器（Encoder）与解码器（Decoder）两部分构成，具体结构如下：

##### 5.4.2.2.1 编码器

编码器由两层组成：

嵌入层（Embedding Layer）：将中文 token 序列映射为稠密向量。

循环神经网络层（GRU）：为更好的提取输入序列的语义信息，采用双向GRU，最终拼接前向与后向的隐藏状态，作为上下文向量传递给解码器。

##### 5.4.2.2.2 解码器

解码器由三层组成：

嵌入层（Embedding Layer）：将目标序列中的token 转换为稠密向量。

循环神经网络层（GRU）：结合前一步的词向量和隐藏状态，生成当前的隐藏状态。

全连接层（Linear Layer）：将当前隐藏状态映射为词表大小的概率分布，用于预测下一个词。

#### 5.4.2.3 训练方案

训练策略：采用 Teacher Forcing，即每一步使用目标序列中真实的前一个词作为解码器输入。

损失函数：使用 CrossEntropyLoss。

优化器：使用 Adam 优化器进行参数更新。

#### 5.4.2.4 推理方案

推理阶段采用自回归生成策略（Autoregressive Generation）。

词选择策略使用贪心解码（Greedy Decoding）。

#### 5.4.2.5 评估方案

在机器翻译任务中，BLEU（Bilingual Evaluation Understudy） 是一种常用的自动评估指标，用于衡量模型生成的翻译与人工参考译文之间的相似程度。其核心思想是：

- n-gram 匹配：统计预测译文中有多少 n-gram（词或短语）同时出现在参考译文中，用于衡量翻译内容的准确性。
- 精确率计算：将匹配到的 n-gram 数量除以预测译文中 n-gram 的总数，反映生成译文中“正确部分”的比例。

此外，BLEU 还引入长度惩罚机制，防止模型通过生成过短句子获得不合理的高分。

最终得到的 BLEU 分数越高，说明生成译文与参考译文越接近。

本案例中，使用 Python 的 NLTK 库 中的  模块，对模型在测试集上的翻译结果进行评估，主要参考BLEU-4 的得分情况，作为翻译质量的衡量依据。

### 5.4.3 需求实现

#### 5.4.3.1 项目结构

![图片96.png](images/图片96.png)

#### 5.4.3.2 完整代码

##### 5.4.3.2.1 数据预处理

```python
# process.py

import pandas as pd
from sklearn.model_selection import train_test_split
from tokenizer import ChineseTokenizer, EnglishTokenizer
import config

def process():
    """
```

数据预处理主函数。

```python
    """
    print('开始处理数据')

    # 读取原始数据文件
    df = pd.read_csv(
```

config.RAW_DATA_DIR / 'cmn.txt',

```python
        sep='\t',
        header=None,
        usecols=[0, 1],
        names=['en', 'zh']
    )

    # 数据清洗：去除空值和空字符串
    df = df.dropna()
    df = df[df['en'].str.strip().ne('') & df['zh'].str.strip().ne('')]

    # 划分训练集和测试集
```

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

```python
    # 构建词表并保存
    EnglishTokenizer.build_vocab(train_df['en'].tolist(), config.PROCESSED_DATA_DIR / 'en_vocab.txt')
    ChineseTokenizer.build_vocab(train_df['zh'].tolist(), config.PROCESSED_DATA_DIR / 'zh_vocab.txt')

    # 加载词表
    en_tokenizer = EnglishTokenizer.from_vocab(config.PROCESSED_DATA_DIR / 'en_vocab.txt')
    zh_tokenizer = ChineseTokenizer.from_vocab(config.PROCESSED_DATA_DIR / 'zh_vocab.txt')

    # 编码并保存训练集
    train_df['en'] = train_df['en'].apply(
```

lambda x: en_tokenizer.encode(x, seq_len=config.SEQ_LEN, add_sos_eos=True)

```python
    )
    train_df['zh'] = train_df['zh'].apply(
```

lambda x: zh_tokenizer.encode(x, seq_len=config.SEQ_LEN, add_sos_eos=False)

```python
    )
    train_df.to_json(
```

config.PROCESSED_DATA_DIR / 'indexed_train.jsonl',

```python
        orient='records',
        lines=True
    )

    # 编码并保存测试集
    test_df['en'] = test_df['en'].apply(
```

lambda x: en_tokenizer.encode(x, seq_len=config.SEQ_LEN, add_sos_eos=True)

```python
    )
    test_df['zh'] = test_df['zh'].apply(
```

lambda x: zh_tokenizer.encode(x, seq_len=config.SEQ_LEN, add_sos_eos=False)

```python
    )
    test_df.to_json(
```

config.PROCESSED_DATA_DIR / 'indexed_test.jsonl',

```python
        orient='records',
        lines=True
    )

    print('数据处理完成')

if __name__ == '__main__':
```

process()

##### 5.4.3.2.2 自定义分词器

```python
# tokenizer.py

from abc import abstractmethod
from nltk import word_tokenize, TreebankWordDetokenizer
from tqdm import tqdm

class BaseTokenizer:
    """
```

分词器基类，支持词表构建、编码、索引映射等功能。

```python
    """
    unk_token = '<unk>'
    pad_token = '<pad>'
    sos_token = '<sos>'
    eos_token = '<eos>'

    @staticmethod
    @abstractmethod
    def tokenize(sentence):
        """
```

分词抽象方法。

```python
        """
        pass

    @abstractmethod
    def decode(self, indexes):
        """
```

解码抽象方法。

```python
        """
        pass

    @classmethod
    def build_vocab(cls, sentences, vocab_file):
        """
```

构建并保存词表。

:param sentences: 句子列表。

:param vocab_file: 词表文件路径。

```python
        """
        unique_words = set()
        for sentence in tqdm(sentences, desc='分词'):
            # 收集唯一词汇
            for word in cls.tokenize(sentence):
                unique_words.add(word)

        vocab_list = [cls.pad_token, cls.unk_token, cls.sos_token, cls.eos_token] + list(unique_words)

        with open(vocab_file, 'w', encoding='utf-8') as f:
            for word in vocab_list:
                f.write(word + '\n')

    def __init__(self, vocab_list):
        """
```

初始化分词器。

:param vocab_list: 词表列表。

```python
        """
```

self.vocab_list = vocab_list

self.vocab_size = len(vocab_list)

self.word2index = {word: index for index, word in enumerate(vocab_list)}

self.index2word = {index: word for index, word in enumerate(vocab_list)}

self.unk_token_index = self.word2index[self.unk_token]

self.pad_token_index = self.word2index[self.pad_token]

self.sos_token_index = self.word2index[self.sos_token]

self.eos_token_index = self.word2index[self.eos_token]

```python
    @classmethod
    def from_vocab(cls, vocab_file):
        """
```

加载词表并创建分词器。

:param vocab_file: 词表文件路径。

:return: 分词器对象。

```python
        """
        with open(vocab_file, 'r', encoding='utf-8') as f:
            vocab_list = [line.strip() for line in f.readlines()]
        return cls(vocab_list)

    def encode(self, sentence, seq_len, add_sos_eos=False):
        """
```

编码句子为索引。

:param sentence: 输入句子。

:param seq_len: 序列长度。

:param add_sos_eos: 是否加起始结束符。

:return: 索引列表。

```python
        """
        tokens = self.tokenize(sentence)
        indexes = [self.word2index.get(token, self.unk_token_index) for token in tokens]

        if add_sos_eos:
            indexes = indexes[:seq_len - 2]
            indexes = [self.sos_token_index] + indexes + [self.eos_token_index]
        else:
            indexes = indexes[:seq_len]

        if len(indexes) < seq_len:
            indexes += [self.pad_token_index] * (seq_len - len(indexes))

        return indexes

class ChineseTokenizer(BaseTokenizer):
    @staticmethod
    def tokenize(sentence):
        return list(sentence)

    def decode(self, indexes):
        return "".join([self.index2word[index] for index in indexes])

class EnglishTokenizer(BaseTokenizer):
    @staticmethod
    def tokenize(sentence):
        return word_tokenize(sentence)

    def decode(self, indexes):
        tokens = [self.index2word[index] for index in indexes]
        return TreebankWordDetokenizer().detokenize(tokens)
```

##### 5.4.3.2.3 自定义数据集

```python
# dataset.py

import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
import config

class TranslationDataset(Dataset):
    def __init__(self, data_path):
```

self.data = pd.read_json(data_path, lines=True).to_dict(orient='records')

```python
    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        input_tensor = torch.tensor(self.data[index]['zh'], dtype=torch.long)
        target_tensor = torch.tensor(self.data[index]['en'], dtype=torch.long)
        return input_tensor, target_tensor

def get_dataloader(train=True):
    data_path = config.PROCESSED_DATA_DIR / ('indexed_train.jsonl' if train else 'indexed_test.jsonl')
    dataset = TranslationDataset(data_path)
    return DataLoader(dataset, batch_size=config.BATCH_SIZE, shuffle=True)

if __name__ == '__main__':
    train_loader = get_dataloader(train=True)
    for inputs, targets in train_loader:
        print(inputs.shape)
        print(targets.shape)
        break
```

##### 5.4.3.2.4 模型定义

```python
# model.py

import torch
from torch import nn
from torchinfo import summary

import config

class TranslationEncoder(nn.Module):
    """
```

翻译模型编码器，基于双向 GRU。

```python
    """

    def __init__(self, vocab_size, padding_index):
        """
```

初始化编码器。

:param vocab_size: 词表大小。

:param padding_index: padding token 的索引。

```python
        """
```

super().__init__()

```python
        # 嵌入层：将 token 索引映射为稠密向量
```

self.embedding = nn.Embedding(

```python
            num_embeddings=vocab_size,
            embedding_dim=config.EMBEDDING_DIM,
            padding_idx=padding_index
        )
        # 双向 GRU
```

self.rnn = nn.GRU(

```python
            input_size=config.EMBEDDING_DIM,
            hidden_size=config.ENCODER_HIDDEN_DIM,
            num_layers=config.ENCODER_LAYERS,
            batch_first=True,
            bidirectional=True
        )

    def forward(self, src):
        """
```

前向传播。

:param src: 输入张量，形状 (batch_size, seq_len)。

:return: (输出张量, 最终隐藏状态)。

```python
        """
        embedded = self.embedding(src)  # (batch_size, seq_len, embedding_dim)
```

output, hidden = self.rnn(embedded)

```python
        return output, hidden

class TranslationDecoder(nn.Module):
    """
```

翻译模型解码器，基于单向 GRU。

```python
    """

    def __init__(self, vocab_size, padding_index):
        """
```

初始化解码器。

:param vocab_size: 词表大小。

:param padding_index: padding token 的索引。

```python
        """
```

super().__init__()

```python
        # 嵌入层
```

self.embedding = nn.Embedding(

```python
            num_embeddings=vocab_size,
            embedding_dim=config.EMBEDDING_DIM,
            padding_idx=padding_index
        )
        # GRU
```

self.rnn = nn.GRU(

```python
            input_size=config.EMBEDDING_DIM,
            hidden_size=config.DECODER_HIDDEN_DIM,
            batch_first=True
        )
        # 线性层：映射到词表概率分布
```

self.linear = nn.Linear(

```python
            in_features=config.DECODER_HIDDEN_DIM,
            out_features=vocab_size
        )

    def forward(self, tgt, hidden):
        """
```

前向传播。

:param tgt: 输入张量，形状 (batch_size, 1)。

:param hidden: 隐藏状态张量，形状 (1, batch_size, hidden_dim)。

:return: (输出张量, 新的隐藏状态)。

```python
        """
        embedded = self.embedding(tgt)  # (batch_size, 1, embedding_dim)
        output, hidden = self.rnn(embedded, hidden)  # output: (batch_size, 1, hidden_dim)
        output = self.linear(output)  # (batch_size, 1, vocab_size)
        return output, hidden

if __name__ == '__main__':
    encoder = TranslationEncoder(vocab_size=10000, padding_index=0)
    dummy_encoder_input = torch.randint(low=0, high=10000, size=(config.BATCH_SIZE, config.SEQ_LEN))
```

summary(encoder, input_data=dummy_encoder_input)

```python
    print('-' * 100)

    decoder = TranslationDecoder(vocab_size=10000, padding_index=0)
    dummy_decoder_input = torch.randint(low=0, high=10000, size=(config.BATCH_SIZE, 1))
    dummy_decoder_hidden = torch.randn(size=(1, config.BATCH_SIZE, config.DECODER_HIDDEN_DIM))
```

summary(decoder, input_data=[dummy_decoder_input, dummy_decoder_hidden])

##### 5.4.3.2.5 模型训练

```python
# train.py

import time
from itertools import chain

import torch
from torch.nn import CrossEntropyLoss
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

from dataset import get_dataloader
from tokenizer import ChineseTokenizer, EnglishTokenizer
import config
from model import TranslationEncoder, TranslationDecoder

def train_one_epoch(dataloader, encoder, decoder, loss_function, optimizer, device):
    """
```

训练一个 epoch。

:param dataloader: 数据加载器。

:param encoder: 编码器。

:param decoder: 解码器。

:param loss_function: 损失函数。

:param optimizer: 优化器。

:param device: 设备。

:return: 平均损失。

```python
    """
    encoder.train()
    decoder.train()
    total_loss = 0

    for src, tgt in tqdm(dataloader, desc='训练'):
        src = src.to(device)
        tgt = tgt.to(device)

        optimizer.zero_grad()

        # 编码器处理
```

_, encoder_hidden = encoder(src)

```python
        # 拼接前向后向隐藏状态
        forward_hidden = encoder_hidden[-2]
        backward_hidden = encoder_hidden[-1]
        context_vector = torch.cat([forward_hidden, backward_hidden], dim=1)

        # 初始化解码器输入和隐藏状态
        decoder_input = tgt[:, 0:1]
        decoder_hidden = context_vector.unsqueeze(0)

        decoder_outputs = []
        for step in range(1, config.SEQ_LEN):
```

decoder_output, decoder_hidden = decoder(decoder_input, decoder_hidden)

```python
            decoder_outputs.append(decoder_output)
            decoder_input = tgt[:, step:step + 1]

        decoder_outputs = torch.cat(decoder_outputs, dim=1)
        decoder_targets = tgt[:, 1:]

        loss = loss_function(
            decoder_outputs.reshape(-1, decoder_outputs.shape[-1]),
            decoder_targets.reshape(-1)
        )

        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    return total_loss / len(dataloader)

def train():
    """
```

模型训练主函数。

```python
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    dataloader = get_dataloader()

    zh_tokenizer = ChineseTokenizer.from_vocab(config.PROCESSED_DATA_DIR / 'zh_vocab.txt')
    en_tokenizer = EnglishTokenizer.from_vocab(config.PROCESSED_DATA_DIR / 'en_vocab.txt')

    encoder = TranslationEncoder(
        vocab_size=zh_tokenizer.vocab_size,
        padding_index=zh_tokenizer.pad_token_index
```

).to(device)

```python
    decoder = TranslationDecoder(
        vocab_size=en_tokenizer.vocab_size,
        padding_index=en_tokenizer.pad_token_index
```

).to(device)

```python
    loss_function = CrossEntropyLoss(ignore_index=en_tokenizer.pad_token_index)
    optimizer = torch.optim.Adam(chain(encoder.parameters(), decoder.parameters()), lr=config.LEARNING_RATE)

    writer = SummaryWriter(log_dir=config.LOGS_DIR / time.strftime('%Y-%m-%d_%H-%M-%S'))

    best_loss = float('inf')

    for epoch in range(1, config.EPOCHS + 1):
        print(f'========== Epoch {epoch} ==========')

        avg_loss = train_one_epoch(dataloader, encoder, decoder, loss_function, optimizer, device)

        print(f'平均损失: {avg_loss:.4f}')
        writer.add_scalar('Loss', avg_loss, epoch)

        if avg_loss < best_loss:
            best_loss = avg_loss
            torch.save(encoder.state_dict(), config.MODELS_DIR / 'encoder.pt')
            torch.save(decoder.state_dict(), config.MODELS_DIR / 'decoder.pt')
            print('已保存模型')

if __name__ == '__main__':
```

train()

##### 5.4.3.2.6 模型预测

```python
# predict.py

import torch
from tokenizer import ChineseTokenizer, EnglishTokenizer
from model import TranslationEncoder, TranslationDecoder
import config

def predict_batch(input_tensor, encoder, decoder, en_tokenizer, device):
    """
```

对一个 batch 的输入进行翻译预测。

:param input_tensor: 中文输入张量，形状 (batch_size, seq_len)。

:param encoder: 编码器。

:param decoder: 解码器。

:param en_tokenizer: 英文分词器。

:param device: 设备。

:return: 英文 token 索引列表。

```python
    """
    encoder.eval()
    decoder.eval()

    with torch.no_grad():
        # 编码器前向传播
```

encoder_output, encoder_hidden = encoder(input_tensor)

```python
        # 拼接双向 GRU 的最后隐藏状态作为上下文向量
        context_vector = torch.cat([encoder_hidden[-2], encoder_hidden[-1]], dim=1)

        batch_size = input_tensor.shape[0]
        decoder_input = torch.full(
            size=(batch_size, 1),
            fill_value=en_tokenizer.sos_token_index,
            device=device
        )
        decoder_hidden = context_vector.unsqueeze(0)

        generated = [[] for _ in range(batch_size)]
        finished = [False for _ in range(batch_size)]

        for step in range(1, config.SEQ_LEN):
```

decoder_output, decoder_hidden = decoder(decoder_input, decoder_hidden)

```python
            predict_indexes = decoder_output.argmax(dim=-1)

            for i in range(batch_size):
                if finished[i]:
                    continue
                token_id = predict_indexes[i].item()
                if token_id == en_tokenizer.eos_token_index:
                    finished[i] = True
                    continue
                generated[i].append(token_id)

            if all(finished):
                break

            decoder_input = predict_indexes

        return generated

def predict(zh_sentence, encoder, decoder, zh_tokenizer, en_tokenizer, device):
    """
```

对单条中文句子进行翻译。

:param zh_sentence: 中文句子。

:param encoder: 编码器。

:param decoder: 解码器。

:param zh_tokenizer: 中文分词器。

:param en_tokenizer: 英文分词器。

:param device: 设备。

:return: 英文翻译句子。

```python
    """
    input_ids = zh_tokenizer.encode(zh_sentence, seq_len=config.SEQ_LEN, add_sos_eos=False)
    input_tensor = torch.tensor([input_ids], device=device)

    generated = predict_batch(input_tensor, encoder, decoder, en_tokenizer, device)
    en_indexes = generated[0]
    en_sentence = en_tokenizer.decode(en_indexes)

    return en_sentence

def run_predict():
    """
```

启动交互式翻译程序。

```python
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    zh_tokenizer = ChineseTokenizer.from_vocab(config.PROCESSED_DATA_DIR / 'zh_vocab.txt')
    en_tokenizer = EnglishTokenizer.from_vocab(config.PROCESSED_DATA_DIR / 'en_vocab.txt')

    encoder = TranslationEncoder(
        vocab_size=zh_tokenizer.vocab_size,
        padding_index=zh_tokenizer.pad_token_index
```

).to(device)

```python
    encoder.load_state_dict(torch.load(config.MODELS_DIR / 'encoder.pt'))

    decoder = TranslationDecoder(
        vocab_size=en_tokenizer.vocab_size,
        padding_index=en_tokenizer.pad_token_index
```

).to(device)

```python
    decoder.load_state_dict(torch.load(config.MODELS_DIR / 'decoder.pt'))
```

print('欢迎使用翻译系统，请输入中文句子：（输入 q 或 quit 退出）')

```python
    while True:
        user_input = input('中文：')
        if user_input in ['q', 'quit']:
            print('谢谢使用，再见！')
            break
        if not user_input:
            print('请输入内容')
            continue

        result = predict(user_input, encoder, decoder, zh_tokenizer, en_tokenizer, device)
        print(f'英文：{result}')

if __name__ == '__main__':
```

run_predict()

##### 5.4.3.2.7 模型评估

```python
# evaluate.py

import torch
from nltk.translate.bleu_score import corpus_bleu
from tqdm import tqdm

import config
from tokenizer import ChineseTokenizer, EnglishTokenizer
from model import TranslationEncoder, TranslationDecoder
from dataset import get_dataloader
from predict import predict_batch

def evaluate(dataloader, encoder, decoder, zh_tokenizer, en_tokenizer, device):
    """
```

执行模型评估。

:param dataloader: 数据加载器。

:param encoder: 编码器。

:param decoder: 解码器。

:param zh_tokenizer: 中文分词器。

:param en_tokenizer: 英文分词器。

:param device: 设备。

:return: BLEU 分数。

```python
    """
    all_references = []
    all_predictions = []

    special_tokens = [
```

zh_tokenizer.pad_token_index,

zh_tokenizer.eos_token_index,

zh_tokenizer.sos_token_index

```python
    ]

    for src, tgt in tqdm(dataloader, desc="评估"):
        src = src.to(device)
        tgt = tgt.tolist()

        predict_indexes = predict_batch(src, encoder, decoder, en_tokenizer, device)
        all_predictions.extend(predict_indexes)

        for indexes in tgt:
            indexes = [index for index in indexes if index not in special_tokens]
            all_references.append([indexes])

    bleu = corpus_bleu(all_references, all_predictions)
    return bleu

def run_evaluate():
    """
```

启动评估流程。

```python
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    zh_tokenizer = ChineseTokenizer.from_vocab(config.PROCESSED_DATA_DIR / 'zh_vocab.txt')
    en_tokenizer = EnglishTokenizer.from_vocab(config.PROCESSED_DATA_DIR / 'en_vocab.txt')

    encoder = TranslationEncoder(
        vocab_size=zh_tokenizer.vocab_size,
        padding_index=zh_tokenizer.pad_token_index
```

).to(device)

```python
    encoder.load_state_dict(torch.load(config.MODELS_DIR / 'encoder.pt'))

    decoder = TranslationDecoder(
        vocab_size=en_tokenizer.vocab_size,
        padding_index=en_tokenizer.pad_token_index
```

).to(device)

```python
    decoder.load_state_dict(torch.load(config.MODELS_DIR / 'decoder.pt'))

    dataloader = get_dataloader(train=False)

    bleu = evaluate(dataloader, encoder, decoder, zh_tokenizer, en_tokenizer, device)

    print('========== 评估结果 ==========')
    print(f'BLEU: {bleu:.2f}')
    print('=============================')

if __name__ == '__main__':
```

run_evaluate()

##### 5.4.3.2.8 配置文件

```python
# config.py

from pathlib import Path

# 获取项目根目录
BASE_DIR = Path(__file__).parent.parent

# 定义项目中常用路径
MODELS_DIR = BASE_DIR / 'models'  # 模型保存路径
PROCESSED_DATA_DIR = BASE_DIR / 'data' / 'processed'  # 处理后的数据保存路径
RAW_DATA_DIR = BASE_DIR / 'data' / 'raw'  # 原始数据保存路径
LOGS_DIR = BASE_DIR / 'logs'  # TensorBoard 日志目录

# 模型结构参数
EMBEDDING_DIM = 128  # 词向量维度
ENCODER_HIDDEN_DIM = 512  # GRU 隐藏状态维度
DECODER_HIDDEN_DIM = 2 * ENCODER_HIDDEN_DIM
ENCODER_LAYERS = 1

# 训练相关超参数
BATCH_SIZE = 128  # 每个 batch 的样本数
```

SEQ_LEN = 30  # 序列长度（输入与输出最大长度）

```python
LEARNING_RATE = 1e-3  # 学习率
EPOCHS = 30  # 总训练轮数
```

## 5.5 存在问题

在上述 Seq2Seq 架构中，编码器会将整个源句压缩为一个固定长度的上下文向量，并将其作为解码器生成目标序列的唯一参考。这种“压缩再解压”的方式虽然结构简洁，但在实际任务中暴露出两个核心问题：

#### 5.5.0.1 信息压缩困难，语义表达受限

对于编码器而言，用一个定长向量去表达任意复杂的句子，是一项非常困难的任务。尤其在面对长句时，信息很容易在压缩过程中丢失，导致语义表达不完整。

这种“信息瓶颈”限制了模型在处理长文本或复杂语义结构时的表现。

#### 5.5.0.2 缺乏动态感知，解码难以精准生成

解码器始终只能基于同一个上下文向量进行生成。

但在实际生成过程中，不同位置的目标词，往往依赖源句中不同的关键信息：

生成主语时，可能更依赖源句的开头；

生成谓语或宾语时，可能需要参考句中或句末内容。

然而在固定表示下，解码器无法“有选择地关注”输入序列的不同部分，只能一视同仁地处理所有信息，从而降低了生成的准确性与灵活性。

