# 06 Agent、LangChain与MCP面试题

> 参考笔记：[[06-LangChain使用之Agents]]、[[05-LangChain使用之Tools]]、[[04-LangChain使用之Memory]]、[[03-LangChain使用之Chains]]、[[c-01-MCP入门]]、[[c-02-MCP服务器]]、[[c-03-MCP客户端]]、[[c-04-MCP进阶使用]]。

## 1. 什么是 AI Agent？

**答案要点：**

AI Agent 是能够基于目标进行感知、规划、决策、调用工具并执行动作的智能系统。

常见组成：

- LLM：推理和决策大脑。
- Prompt：定义角色、目标和约束。
- Tools：外部工具或 API。
- Memory：短期或长期记忆。
- Planning：任务拆解和路径规划。
- Executor：执行工具调用和控制循环。

## 2. Agent 和普通 ChatBot 有什么区别？

**答案要点：**

- ChatBot 主要进行对话生成，回答用户问题。
- Agent 不只是回答，还能拆解任务、选择工具、执行动作、观察结果并迭代。
- Agent 更强调“任务闭环”和“行动能力”。

示例：普通 ChatBot 告诉你如何查天气；Agent 可以调用天气 API 并直接返回实时天气。

## 3. Agent 和 Chain 有什么区别？

**答案要点：**

- Chain：流程通常是固定的、硬编码的，例如 A → B → C。
- Agent：由模型根据当前任务动态决定下一步做什么，可以选择工具、调整顺序、处理异常。

面试中可以总结：Chain 更稳定可控，Agent 更灵活自主；企业落地常把二者结合。

## 4. ReAct 模式是什么？

**答案要点：**

ReAct = Reasoning + Acting，即“推理 + 行动”。

典型流程：

1. Thought：分析当前问题。
2. Action：选择并调用工具。
3. Observation：观察工具返回结果。
4. Repeat：根据结果继续推理或给出最终答案。

它适合需要多步推理和工具调用的任务。

## 5. Function Calling 和 ReAct 有什么区别？

**答案要点：**

- Function Calling：模型输出结构化工具调用参数，例如 JSON，适合工具明确、参数清晰的场景。
- ReAct：模型用自然语言推理并穿插工具调用，适合需要显式推理、多步探索的场景。

Function Calling 更结构化、稳定；ReAct 更灵活，但可能更难控制。

## 6. Agent 的 Memory 有哪些类型？

**答案要点：**

- 短期记忆：当前对话上下文，例如最近几轮消息。
- 长期记忆：持久化到数据库或向量库中的用户偏好、历史事实、知识片段。
- 工作记忆：当前任务执行过程中的中间状态。

注意：记忆会带来隐私、成本和上下文污染问题，需要权限和生命周期管理。

## 7. Agent 常见风险有哪些？如何控制？

**答案要点：**

常见风险：

- 工具误调用。
- 无限循环。
- 越权访问。
- Prompt Injection。
- 生成错误计划。
- 成本不可控。
- 对外部系统执行危险动作。

控制方式：

- 工具白名单和最小权限。
- 参数 schema 校验。
- 最大迭代次数。
- 高风险操作人工确认。
- 日志审计和链路追踪。
- 关键动作可回滚。

## 8. LangChain 是什么？

**答案要点：**

LangChain 是用于构建大模型应用的开发框架，提供模型调用、Prompt、Chain、Tool、Agent、Retriever、Memory、OutputParser 等组件。

它适合快速构建：

- RAG 应用。
- Agent 应用。
- 多步骤 LLM 工作流。
- 工具调用和模型编排。

## 9. LangChain 的核心组件有哪些？

**答案要点：**

常见核心组件：

- Model / ChatModel：统一模型接口。
- PromptTemplate：提示词模板。
- OutputParser：结构化解析模型输出。
- Chain / Runnable：组合多个步骤。
- Retriever：检索相关文档。
- VectorStore：向量存储。
- Tool：可被 Agent 调用的工具。
- Agent：动态决策和工具调用。
- Memory：保存上下文或历史状态。

新版 LangChain 更强调 Agent = Model + Harness，其中 Harness 包括提示词、工具和中间件等编排能力。

## 10. LangChain 中 Tool 的设计要注意什么？

**答案要点：**

- 名称清晰，避免歧义。
- 描述准确，告诉模型何时使用该工具。
- 参数 schema 明确，类型、必填项和含义清楚。
- 工具输出尽量结构化。
- 对参数做校验。
- 高风险工具增加权限控制和人工确认。

工具描述质量会直接影响模型选择工具的准确率。

## 11. LangChain AgentExecutor 的作用是什么？

**答案要点：**

AgentExecutor 是 Agent 的运行时执行器，负责：

- 接收用户输入。
- 调用 Agent 生成下一步动作。
- 执行工具。
- 将工具观察结果返回给 Agent。
- 控制循环直到得到最终答案或达到限制。

当流程更复杂、需要状态图和分支控制时，可以使用 LangGraph。

## 12. LangChain 和 LangGraph 有什么区别？

**答案要点：**

- LangChain：提供模型、Prompt、Retriever、Tool、Agent 等组件，适合快速搭建 LLM 应用。
- LangGraph：用于构建有状态、多节点、可循环、可分支的 Agent 工作流，控制力更强。

可以理解为：LangChain 偏组件生态和快速开发，LangGraph 偏底层编排和复杂流程控制。

## 13. MCP 是什么？

**答案要点：**

MCP 是 Model Context Protocol，模型上下文协议。它用于标准化 AI 应用与外部工具、数据源、提示词之间的交互方式。

可以类比为 AI 应用连接外部能力的“通用接口”。

价值：

- 降低工具接入成本。
- 减少模型和工具的耦合。
- 支持本地和远程工具接入。
- 让不同 AI 应用复用同一 MCP Server。

## 14. MCP 的核心组成是什么？

**答案要点：**

MCP 采用 Client-Server 架构，主要参与者：

- MCP Host：承载 AI 应用的宿主，例如 IDE、桌面助手。
- MCP Client：Host 内部用于连接某个 MCP Server 的客户端。
- MCP Server：提供上下文、工具和提示词的服务程序。

一个 Host 可以连接多个 MCP Server，通常每个 Server 对应一个 Client 连接。

## 15. MCP Server 可以暴露哪些核心能力？

**答案要点：**

MCP Server 主要暴露三类 Server Primitives：

- Tools：可执行函数，例如查数据库、读文件、调用 API。
- Resources：可读取资源，例如文件内容、数据库记录、日志、接口响应。
- Prompts：可复用提示词模板，例如标准任务说明、Few-shot 示例。

客户端可通过 `tools/list`、`resources/list`、`prompts/list` 发现能力，并通过对应方法读取或调用。

## 16. MCP 使用什么通信协议和传输方式？

**答案要点：**

MCP 数据层基于 JSON-RPC 2.0，用于定义请求、响应、通知和方法调用语义。

常见传输方式：

- STDIO：本地进程间通过标准输入输出通信，适合本地工具和开发调试。
- Streamable HTTP：适合远程 MCP Server，可结合 HTTP 鉴权、流式响应等能力。

早期资料中也常见 SSE 方案，但新文档更强调 Streamable HTTP。

## 17. MCP 和 Function Calling、Tool 有什么区别？

**答案要点：**

- Tool：泛指可被调用的外部能力。
- Function Calling：模型生成结构化函数调用请求的能力。
- MCP：标准化工具、资源、提示词如何暴露给 AI 应用的协议。

一句话总结：Function Calling 解决“模型如何表达要调用工具”，MCP 解决“工具如何标准化接入 AI 应用”。

## 18. MCP 的安全风险和防护措施有哪些？

**答案要点：**

风险：

- 读取敏感文件。
- 调用危险命令。
- 越权访问内部系统。
- Prompt Injection 诱导工具误调用。
- 工具返回恶意内容污染上下文。

防护：

- 最小权限原则。
- 工具白名单。
- 限制文件和网络访问范围。
- 高风险操作人工确认。
- 参数校验和权限校验。
- 日志审计。
- 不把密钥直接暴露到模型上下文。

## 19. 如何设计一个稳定的企业级 Agent？

**答案要点：**

建议回答为“Agent + Workflow + Guardrails”：

- 对开放探索部分使用 Agent。
- 对关键业务流程使用确定性 Workflow。
- 对工具调用做权限控制和参数校验。
- 对高风险动作加人工确认。
- 增加任务超时、最大步骤、失败降级。
- 记录完整链路用于调试和审计。
- 建立评测集，评估任务完成率、工具调用准确率和安全性。
