# 09 Transformer与大模型基础面试题

> 参考笔记：`AI黑马/05 NLP文档/06_transformer论文复现`、`AI黑马/05 NLP文档/08_迁移学习经典网络tf_GTP_Bert_Elmo`、`AI黑马/传智项目文档/02 bert 与 tf`、`AI黑马/传智项目文档/06 transformers项目问题答案`。
>
> 权威参考：Attention Is All You Need、BERT 论文、Hugging Face Transformers 文档、Stanford CS224n。

## 1. Transformer 的整体结构是什么？

**答案要点：**

原始 Transformer 是 Encoder-Decoder 架构。

- Encoder 由多层自注意力、前馈网络、残差连接和 LayerNorm 组成。
- Decoder 在自注意力基础上增加 Encoder-Decoder Attention，并使用 mask 防止看到未来 token。
- Transformer 不依赖 RNN 或 CNN，而是主要通过 Attention 建模序列依赖。

## 2. Self-Attention 的核心思想是什么？

**答案要点：**

Self-Attention 让序列中每个 token 根据与其他 token 的相关性动态聚合上下文信息。

基本过程：

1. 输入分别映射为 Q、K、V。
2. 用 Q 和 K 计算注意力分数。
3. 对分数做缩放和 softmax 得到权重。
4. 用权重对 V 加权求和。

## 3. Q、K、V 分别代表什么？

**答案要点：**

- Q：Query，表示当前 token 想查询什么信息。
- K：Key，表示每个 token 可被匹配的特征。
- V：Value，表示实际被聚合的信息内容。

注意力权重由 Q 和 K 的相似度决定，最终输出是 V 的加权和。

## 4. 为什么 Attention 中要除以 `sqrt(d_k)`？

**答案要点：**

当维度 `d_k` 较大时，Q 和 K 的点积方差会变大，softmax 可能进入饱和区，导致梯度很小。

除以 `sqrt(d_k)` 可以缩放分数，使训练更稳定。

## 5. Multi-Head Attention 有什么作用？

**答案要点：**

多头注意力把表示空间拆分成多个子空间，让模型从不同角度关注信息。

作用：

- 捕捉不同类型的依赖关系。
- 提升模型表达能力。
- 多个头可以关注语法、语义、位置等不同模式。

## 6. Transformer 为什么需要位置编码？

**答案要点：**

Self-Attention 本身不包含序列顺序信息。如果没有位置编码，模型无法区分 token 的先后顺序。

位置编码方式：

- 正弦余弦固定位置编码。
- 可学习位置编码。
- 相对位置编码。
- 旋转位置编码等改进方式。

## 7. Transformer 中残差连接和 LayerNorm 的作用是什么？

**答案要点：**

- 残差连接帮助梯度传播，缓解深层网络训练困难。
- LayerNorm 对每个样本的特征维度做归一化，稳定训练。
- 二者配合可以提升深层 Transformer 的收敛稳定性。

## 8. Transformer 相比 RNN 有什么优势？

**答案要点：**

- 支持并行计算，训练效率更高。
- 通过 Attention 直接建模任意两个位置之间的依赖。
- 更适合长距离依赖。
- 缺点是标准自注意力复杂度为 `O(n^2)`，长序列成本较高。

## 9. Encoder-only、Decoder-only、Encoder-Decoder 模型有什么区别？

**答案要点：**

- Encoder-only：适合理解类任务，如文本分类、NER、语义匹配，代表模型 BERT。
- Decoder-only：适合自回归生成任务，代表模型 GPT。
- Encoder-Decoder：适合输入到输出的转换任务，如翻译、摘要，代表模型 T5、BART。

## 10. BERT 的核心思想是什么？

**答案要点：**

BERT 是基于 Transformer Encoder 的双向预训练语言模型。

核心特点：

- 使用 Masked Language Model 预训练。
- 原论文还使用 Next Sentence Prediction。
- 通过双向上下文学习文本表示。
- 预训练后可在分类、NER、问答等下游任务上微调。

## 11. MLM 和传统语言模型有什么区别？

**答案要点：**

- 传统自回归语言模型根据前文预测下一个词，只能单向建模。
- MLM 随机 mask 输入中的部分 token，让模型根据双向上下文预测被 mask 的 token。
- MLM 适合理解类任务，但预训练和微调之间存在 `[MASK]` 不一致问题。

## 12. GPT 和 BERT 有什么区别？

**答案要点：**

- BERT 使用 Transformer Encoder，双向编码，适合理解任务。
- GPT 使用 Transformer Decoder，因果 mask，自回归生成，适合生成任务。
- BERT 预训练目标是 MLM，GPT 预训练目标是 next token prediction。
- GPT 推理时逐 token 生成，BERT 通常一次性编码输入。

## 13. ELMo、GPT、BERT 的主要区别是什么？

**答案要点：**

- ELMo 基于双向 LSTM，生成上下文相关词向量。
- GPT 基于 Transformer Decoder，自回归单向语言模型。
- BERT 基于 Transformer Encoder，通过 MLM 获取双向上下文表示。
- 三者都属于预训练思想的重要发展阶段。

## 14. BERT 微调通常怎么做？

**答案要点：**

常见流程：

1. 加载预训练 BERT 和 tokenizer。
2. 根据任务添加分类头、序列标注头或问答头。
3. 使用任务数据端到端训练。
4. 通常使用较小学习率。
5. 根据验证集指标保存最佳模型。

注意事项：最大长度、batch size、学习率、warmup、类别不平衡。

## 15. Tokenizer 中 BPE、WordPiece、SentencePiece 有什么作用？

**答案要点：**

这些方法把文本切分为子词单元，兼顾词级语义和字符级泛化。

优势：

- 缓解 OOV 问题。
- 控制词表大小。
- 支持罕见词和新词拆分。
- 是现代 Transformer 模型常用文本编码方式。

## 16. Transformer 中 mask 有哪些类型？

**答案要点：**

- Padding mask：忽略 padding 位置。
- Causal mask：防止当前位置看到未来 token，用于自回归生成。
- Attention mask：广义上控制哪些 token 可以被关注。

不同任务和模型结构使用的 mask 不同。

## 17. 为什么标准 Attention 的长文本成本高？

**答案要点：**

标准 Self-Attention 需要计算所有 token 两两之间的注意力分数，时间和空间复杂度都是 `O(n^2)`。

长文本优化方向：

- 稀疏注意力。
- 滑动窗口注意力。
- 低秩近似。
- 分块处理。
- 长上下文模型和检索增强。

## 18. Hugging Face Transformers 常用组件有哪些？

**答案要点：**

- Tokenizer：文本编码和解码。
- Model：预训练模型主体。
- AutoModel：根据模型名称自动加载结构。
- Pipeline：快速推理接口。
- Trainer：训练封装。
- Datasets：数据处理。

常见类：`AutoTokenizer`、`AutoModel`、`AutoModelForSequenceClassification`、`AutoModelForCausalLM`。

## 19. 文本生成中 greedy search、beam search、top-k、top-p 有什么区别？

**答案要点：**

- greedy search：每步选概率最大 token，速度快但容易单调。
- beam search：保留多个候选序列，适合翻译、摘要等确定性任务。
- top-k：每步从概率最高的 k 个 token 中采样。
- top-p：从累积概率达到 p 的候选集合中采样。
- temperature 控制分布平滑程度，越高随机性越强。

## 20. 大模型微调有哪些常见方式？

**答案要点：**

- 全参数微调：更新全部参数，效果强但资源消耗大。
- 冻结部分层：只训练部分参数。
- Adapter：插入小模块训练。
- Prompt Tuning / Prefix Tuning：训练提示相关参数。
- LoRA：低秩适配，只训练低秩增量矩阵。

面试中可以补充：参数高效微调适合显存有限和多任务定制场景。

## 21. RAG 和微调有什么区别？

**答案要点：**

- RAG 通过检索外部知识，把相关文档作为上下文提供给模型，适合知识更新和可追溯回答。
- 微调通过训练改变模型参数，适合学习任务格式、风格、领域模式。
- RAG 不直接改变模型参数，知识更新成本低。
- 微调不能可靠记住大量事实知识，也不适合频繁更新知识库。

## 22. 大模型幻觉是什么？如何缓解？

**答案要点：**

幻觉是模型生成看似合理但事实上错误或无依据的内容。

缓解方式：

- 使用 RAG 引入可靠知识源。
- 要求引用来源。
- 限制模型只基于上下文回答。
- 做事实校验和后处理。
- 采用更高质量训练数据和对齐策略。
- 在高风险场景加入人工审核。
