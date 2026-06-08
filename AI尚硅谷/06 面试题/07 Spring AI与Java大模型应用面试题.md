# 07 Spring AI与Java大模型应用面试题

> 参考笔记：[[SpringAI课程]]、[[Spring AI Alibaba速通实战]]、[[尚硅谷-Java+大模型应用-硅谷小智（医疗版）]]、[[15_整合AI实现数据报表]]。

## 1. Spring AI 是什么？

**答案要点：**

Spring AI 是 Spring 生态下用于构建 AI 应用的框架。它把 Spring 的可移植性、模块化设计和 POJO 编程思想应用到 AI 工程中，为 Java 开发者提供统一的大模型应用开发抽象。

核心目标：

- 简化大模型调用。
- 统一不同模型供应商接口。
- 支持 Embedding、Vector Store、RAG、Tool Calling 等能力。
- 方便与 Spring Boot 企业应用集成。

## 2. Spring AI 支持哪些核心能力？

**答案要点：**

常见能力包括：

- Chat Model：对话模型调用。
- Embedding Model：文本向量化。
- Vector Store：向量数据库集成。
- Prompt 和 Message：提示词和消息抽象。
- Function / Tool Calling：函数或工具调用。
- Structured Output：将模型输出映射为 Java 对象。
- ETL：文档加载、转换和向量化。
- Spring Boot 自动配置。

## 3. Spring AI 中 ChatModel 和 ChatClient 有什么区别？

**答案要点：**

- ChatModel：底层聊天模型抽象，负责实际调用模型。
- ChatClient：更高层的流式 API，方便设置 system prompt、user prompt、参数、工具、上下文和 Advisors。

简单理解：ChatModel 偏模型调用能力，ChatClient 偏开发者友好的调用入口。

## 4. Spring AI 如何接入不同大模型供应商？

**答案要点：**

Spring AI 通过统一抽象和 Starter 自动配置接入不同模型供应商，例如 OpenAI、Azure OpenAI、Ollama、Hugging Face、Amazon Bedrock、Google、DeepSeek 兼容 OpenAI API 的服务等。

一般步骤：

1. 引入对应 starter 和 Spring AI BOM。
2. 在配置文件中设置 API Key、Base URL、模型名和参数。
3. 注入 ChatModel 或使用 ChatClient 调用。

## 5. Spring AI 如何集成 DeepSeek？

**答案要点：**

DeepSeek API 通常兼容 OpenAI 风格接口，因此可以借助 Spring AI 的 OpenAI Starter 接入。

关键配置：

- `spring.ai.openai.api-key`
- `spring.ai.openai.base-url`
- `spring.ai.openai.chat.options.model`
- `spring.ai.openai.chat.options.temperature`

面试中注意说明：生产环境不要把 API Key 明文写入仓库，应使用环境变量、配置中心或密钥管理服务。

## 6. Spring AI 中 EmbeddingModel 的作用是什么？

**答案要点：**

EmbeddingModel 用于把文本转换为向量，是 RAG 和语义检索的基础。

常见用途：

- 文档向量化。
- 用户问题向量化。
- 文本相似度计算。
- 聚类、推荐和语义搜索。

通常与 VectorStore 配合使用。

## 7. Spring AI 中 VectorStore 的作用是什么？

**答案要点：**

VectorStore 是向量数据库抽象，用于存储和检索文档向量。

常见能力：

- 添加文档向量。
- 根据 query 做相似度检索。
- 支持 Top-K、相似度阈值、元数据过滤。

可对接 Redis、Milvus、PGVector、Elasticsearch、Chroma、Neo4j 等不同实现。

## 8. Spring AI 如何实现 RAG？

**答案要点：**

典型流程：

1. 使用 DocumentReader 加载 PDF、Markdown、网页等文档。
2. 使用 TextSplitter 切分文档。
3. 使用 EmbeddingModel 向量化。
4. 存入 VectorStore。
5. 用户提问时进行相似度检索。
6. 把检索内容作为上下文传给 ChatModel / ChatClient。
7. 生成答案并返回引用。

Spring AI 的 Advisor 机制也可以用于把检索增强能力挂到 ChatClient 调用链路中。

## 9. Tool Calling 在 Spring AI 中有什么作用？

**答案要点：**

Tool Calling 允许模型调用 Java 方法或业务服务，从而获取实时数据或执行业务动作。

适合场景：

- 查询订单。
- 查询库存。
- 查询用户信息。
- 调用报表接口。
- 执行业务审批前的信息核验。

注意事项：

- 工具描述要清晰。
- 参数要有类型和校验。
- 高风险动作要人工确认。
- 工具执行必须遵守业务权限。

## 10. Structured Output 有什么用？

**答案要点：**

Structured Output 用于把模型输出解析或映射为结构化 Java 对象，例如 DTO、Record、List、Map。

价值：

- 便于后端系统处理。
- 降低自然语言输出不稳定带来的风险。
- 适合信息抽取、分类、表单填充、结构化总结。

通常要配合明确 Prompt、JSON Schema、输出解析器和异常处理。

## 11. Spring AI Alibaba 是什么？

**答案要点：**

Spring AI Alibaba 是面向阿里云和国内大模型生态的 Spring AI 扩展框架，便于 Java/Spring 应用接入通义千问、百炼平台以及相关模型服务能力。

常见能力：

- Chat 模型调用。
- Embedding 和 Rerank。
- RAG 应用开发。
- Tool Calling。
- 与 Spring Boot 自动配置集成。
- 与阿里云相关平台和中间件生态结合。

## 12. Spring AI 和 LangChain 有什么区别？

**答案要点：**

- Spring AI：面向 Java/Spring 生态，适合企业 Java 后端系统集成。
- LangChain：Python/JS 生态更成熟，RAG、Agent、工具生态丰富，适合快速原型和复杂 Agent 实验。

如果企业主技术栈是 Java/Spring，Spring AI 更容易接入现有业务系统、权限体系和工程规范。

## 13. Java 后端集成大模型需要注意哪些工程问题？

**答案要点：**

- 超时控制：模型接口可能响应慢。
- 重试策略：避免无脑重试导致成本放大。
- 限流熔断：保护系统和控制费用。
- 流式响应：提升用户体验。
- 日志脱敏：避免记录 API Key 和隐私数据。
- Token 成本控制：限制上下文和输出长度。
- Prompt 版本管理：便于回滚和评测。
- 权限控制：RAG 文档和工具调用要按用户权限过滤。

## 14. 如何设计一个 Java 企业知识库问答系统？

**答案要点：**

可以按架构回答：

1. 文档管理：上传、解析、清洗、版本控制。
2. 向量化：选择 Embedding 模型和切分策略。
3. 向量存储：选择 VectorStore，并保存元数据和权限信息。
4. 检索：向量检索 + 关键词检索 + Rerank。
5. 生成：构造 RAG Prompt，要求基于资料回答。
6. 权限：按用户角色过滤文档。
7. 反馈：用户点赞、纠错、低质量答案回流。
8. 监控：记录检索结果、模型回答、延迟、成本和错误。

## 15. Java 大模型应用中如何做安全控制？

**答案要点：**

- API Key 使用环境变量、配置中心或密钥管理服务。
- RAG 检索按用户权限过滤。
- Tool Calling 绑定业务鉴权。
- Prompt 中不要拼接敏感密钥。
- 日志对用户隐私和工具参数脱敏。
- 对输出做敏感内容和合规检测。
- 高风险动作增加二次确认。
- 对外部模型调用进行数据出境和合规评估。

## 16. 面试中如何介绍一个 Spring AI 项目？

**答案要点：**

建议按项目闭环回答：

1. 背景：为什么需要大模型能力。
2. 技术选型：为什么选 Spring AI / Spring AI Alibaba。
3. 模型接入：接入了哪个模型，如何配置。
4. 核心链路：Prompt、RAG、Tool Calling 或结构化输出。
5. 数据处理：文档切分、向量化、向量库。
6. 工程保障：限流、超时、重试、日志、权限。
7. 效果评测：准确率、召回率、用户反馈、成本和延迟。
8. 优化经验：Rerank、Prompt 迭代、检索优化、缓存。
