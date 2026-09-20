# Cursor 使用说明

> 适用产品：Cursor 桌面端（基于 VS Code 的 AI 编程 IDE）、Agents Window、Cloud Agents、Cursor CLI。  
> 文档依据：Cursor 官方文档（[cursor.com/docs](https://cursor.com/docs)），对应 Cursor 3.x / Composer 2.5 / Agent 工作流（2026）。  
> 本文重点：日常对话、IDE 连到远程/生产环境、以及「你的一句话是如何变成模型调用」的细节。

---

## 1. 先建立正确心智模型

Cursor 不是「聊天窗口 + 代码编辑器」。它是一个 **coding agent 运行时**：

1. **模型（LLM）**：负责推理、决定下一步。
2. **工具（Tools）**：读文件、改文件、搜代码、跑终端、浏览网页、调 MCP。
3. **Harness（编排层）**：系统提示词、Rules、Skills、上下文拼装、权限审批、沙箱。

你发出去的每一条消息，都不会原样丢给模型。Cursor 会先拼出一份完整 prompt（系统指令 + 规则 + 工具定义 + 代码上下文 + 你的话），再发给模型供应商；模型返回的往往不是最终答案，而是 **工具调用**。Agent 执行工具，把结果再喂回模型，循环直到任务完成。

这就是「和大模型交互」的本质：**对话 = 带工具的多轮补全循环**。

```
你的自然语言
    ↓
Cursor 拼装上下文（Rules / Skills / @引用 / 索引检索 / 历史摘要）
    ↓
发给所选 LLM（经 Cursor 后端做最终 prompt building）
    ↓
模型决定：回复文字 或 调用工具
    ↓
Cursor 执行工具（读文件 / 改文件 / 终端 / MCP / 浏览器）
    ↓
工具结果回到模型 → 再决策 → 直到结束
    ↓
你 review diff / 终端输出 / 检查点
```

---

## 2. 安装与第一次打开

### 2.1 安装

1. 打开 [cursor.com/download](https://cursor.com/download)。
2. 按系统安装：
   - **Windows 10+**：运行 `.exe` 安装器。
   - **macOS 12+**：把 App 拖进 Applications。
   - **Linux**：优先用 apt / dnf 官方源；也可用 AppImage。
3. 打开 Cursor，用 Cursor 账号登录。
4. `File → Open Folder` 打开一个真实项目（有 README、可跑测试更好）。

### 2.2 从 VS Code 迁移

Cursor 是 VS Code 分支。扩展、快捷键、`settings.json`、Remote SSH、Dev Containers 大多可复用。建议：

- 用官方迁移流程导入 VS Code 配置。
- Remote SSH **不要**装微软商店里的 VS Code 版扩展，应使用 Cursor Marketplace 里的 **Anysphere Remote SSH**。
- 首次打开仓库后，等索引完成（`Cursor Settings → Indexing & Docs`）。

### 2.3 建议立刻打开的设置

| 设置 | 位置 | 建议 |
| --- | --- | --- |
| Privacy Mode | `Ctrl/Cmd + Shift + J` → General | 公司代码务必打开。Team/Enterprise 默认可强制开启。 |
| 默认模式 | Settings → Chat | 日常用 Agent；探索代码用 Ask。 |
| 默认模型 | Settings → Models | 日常：Composer 2.5 或 Auto；难题：Claude Opus / GPT 高配。 |
| 审批与执行 | Settings → Agents → Approvals & Execution | 推荐 **Auto-review**，不要一上来 Run Everything。 |
| Tab 补全 | 右下角 Tab 指示器 | 可按文件类型关闭（例如 markdown）。 |

---

## 3. 界面与快捷键

Cursor 现在有两套主界面，可以同时开：

| 界面                | 怎么开                                           | 适合                               |
| ----------------- | --------------------------------------------- | -------------------------------- |
| **经典 IDE**        | 默认；命令面板 `Open IDE`                            | 看很多文件、用 VS Code 扩展、精细改代码         |
| **Agents Window** | `Ctrl/Cmd + Shift + P` → `Open Agents Window` | 多 Agent 并行、本地/云/SSH 切换、PR 级 diff |

### 核心快捷键（Windows / Linux | Mac）

| 动作 | 快捷键 |
| --- | --- |
| 打开 Agent 侧栏 | `Ctrl + I` 或 `Ctrl + L` / `Cmd + I` 或 `Cmd + L` |
| 行内编辑 | `Ctrl + K` / `Cmd + K` |
| 把选中代码送到 Chat | `Ctrl + L` / `Cmd + L` |
| 循环切换 Agent / Ask / Plan / Debug | `Shift + Tab` |
| 模式菜单 | `Ctrl + .` / `Cmd + .` |
| 循环切换模型 | `Ctrl + /` / `Cmd + /` |
| 接受 Tab 补全 | `Tab` |
| 打开命令面板 | `Ctrl + Shift + P` / `Cmd + Shift + P` |
| Cursor 设置 | `Ctrl + Shift + J` / `Cmd + Shift + J` |

自定义快捷键：`Ctrl + R` 再 `Ctrl + S`（Mac：`Cmd + R` 再 `Cmd + S`）。

---

## 4. 普通 Cursor 对话：四种日常用法

很多人把「对话」理解成右侧那个聊天框。实际日常有四层，越往下自主性越高。

### 4.1 Tab：边写边补全（不是对话，但最常用）

- 根据**最近编辑、周围代码、linter 报错**预测下一处改动。
- `Tab` 接受整段；`Esc` 或继续打字拒绝；`Ctrl + →` 按词接受。
- 可一次改多行、补 import，甚至跳到另一个文件做配套修改。
- 接受一次后再按 `Tab`，会跳到它预测的下一处编辑点（jump-in-file）。

**注意：** Rules / User Rules **不影响 Tab**。Tab 走 Cursor 自己的补全模型，不受你 BYOK 的第三方 Key 控制。

### 4.2 Inline Edit（`Ctrl/Cmd + K`）：改眼前这一段

1. 选中代码（不选则在光标处生成）。
2. `Ctrl + K`，用一句话说明要做什么，例如「改成 async，并处理错误」。
3. 回车应用；不满意再追加一句回车。
4. 想先问再改：`Alt + Enter`（Mac：`Opt + Enter`）切到提问。
5. 改动会跨文件、需要跑命令时，选中代码后 `Ctrl + L` 送到 Agent。

Inline Edit **不吃 User Rules**。短、局部、确定的改动用它；跨文件用 Agent。

### 4.3 Ask 模式：只读问答

打开 Agent 面板 → `Shift + Tab` 切到 **Ask**。

适合：

- 「认证流程怎么走？」
- 「这个函数做什么？」
- 「数据库连接在哪配的？」
- 读架构、画调用链、对比两个模块。

Ask **不会改文件**。工具集基本只有搜索/读取。想改代码再切回 Agent。  
**切换模式会开一个新的上下文窗口**，所以换任务最好新开聊天。

### 4.4 Agent 模式：真正的「对话式编程」

默认模式。你用自然语言下任务，它自己找文件、改多文件、跑命令、看报错、再修。

推荐第一次这样用：

```
解释这个仓库。指出主入口、关键模块，以及我改代码前应该先读哪些文件。
先不要改任何文件。
```

然后给一个小、可验收的任务：

```
目标：给订单列表加上按状态筛选。
范围：只改 apps/web/src/orders，不要动数据库 schema。
验收：npm test -- orders 通过，现有样式保持不变。
上下文：状态枚举在 packages/shared/order.ts。
流程：先读代码给出计划，等我确认后再改。
```

Agent 会边改边出 diff。改完后让它跑项目里已有的测试 / typecheck / lint。

### 4.5 Plan / Debug：Agent 的两个变体

| 模式        | 何时用            | 行为                         |
| --------- | -------------- | -------------------------- |
| **Agent** | 大多数写代码任务       | 直接探索、改文件、跑命令               |
| **Ask**   | 只想搞懂，不要动代码     | 只读                         |
| **Plan**  | 多文件、方案不唯一、要先评审 | 先提问、调研、写可编辑计划，你点 Build 才动手 |
| **Debug** | 难复现、要运行时证据     | 先假设、打日志、拿运行时信息，再做最小修复      |

复杂功能优先 Plan。改歪了不要靠追问硬拧，**回滚到检查点，改计划再跑一遍** 通常更快、更干净。

### 4.6 对话中的操作细节

**加上下文（`@`）**

| 引用                              | 作用                         |
| ------------------------------- | -------------------------- |
| `@auth.ts` / `@src/components/` | 把文件或目录塞进当前轮                |
| `@Terminals`                    | 带上终端输出（报错、日志）              |
| `@Chats`                        | 引用另一段历史对话                  |
| `@Commit` / `@Branch`           | 工作区 diff 或相对 main 的分支 diff |
| `@Browser`                      | 内置浏览器当前页                   |

知道该看哪些文件就 `@`；不知道就别堆，让 Agent 自己搜。

**图片 / 语音**

- 把截图拖进输入框，或 `Ctrl + V` 粘贴。适合还原设计稿、贴报错。
- 麦克风可口述，发送前先核对转写。

**Agent 还在跑时你怎么插话**

| 操作                    | 效果                       |
| --------------------- | ------------------------ |
| 输入后按 Enter            | 消息排队，等当前任务结束再执行          |
| `Ctrl/Cmd + Enter`    | 立刻插入，不排队                 |
| Send now / 连按两次 Enter | 在下一次工具调用边界「转向」，不中途砍死当前动作 |
| Stop                  | 硬停                       |

排队消息可以拖动排序。

**检查点（Checkpoints）**

Agent 在大改之前会自动快照。聊天时间线上点某个检查点可预览，再 Restore。  
**只回滚文件，不删聊天记录。** 检查点存在本地，不是 Git。长期版本管理仍用 Git。

**`/goal`**

默认每条消息都被当成新任务。长期目标用：

```
/goal 把所有 flaky test 修掉，让 CI 变绿
```

可和 Custom Mode、`/loop` 一起用。

**新开聊天的时机**

- 换了一个无关任务
- 切了模式（模式不共用上下文）
- 上下文环快满、模型开始遗忘早期约束
- Agent 在错误假设上打转

---

## 5. 和大模型交互的细节

这一节是 Cursor 和「普通 ChatGPT 网页」的真正差别。

### 5.1 一次请求里到底有什么

输入框旁边的 **context ring**（上下文环）显示窗口占用。点开可看到分项：

| 类别                      | 是什么                          |
| ----------------------- | ---------------------------- |
| System prompt           | Cursor 为当前模型调过的系统指令（你改不了）    |
| Tools                   | 所有可调用工具的 JSON schema（越多越占窗口） |
| Rules                   | 项目 / 用户 / 团队规则               |
| Skills                  | 技能描述（详细正文按需再加载）              |
| MCP                     | 已连接 MCP 的说明和工具目录             |
| Subagents               | 可派生子代理的说明                    |
| Conversation            | 你的话、模型回复、工具结果                |
| Summarized conversation | 窗口快满时，旧轮次被压缩成的摘要             |

模型有固定上下文窗口（例如 Composer 2.5 约 200k；部分 Claude / GPT 可到 1M）。满了以后 Cursor **自动摘要旧对话**，不是无限记忆。

**实践含义：**

- MCP 开太多，工具定义会挤掉业务代码。
- 规则写太长（官方建议单条 < 500 行），每轮都要付 token。
- 长会话后期质量下降，是摘要丢失细节，不是「模型变笨」。这时新开聊天，并把关键约束写进 Rules。

### 5.2 工具循环（Agent Loop）

Coding agent 不是一次生成完整答案，而是：

```
while 任务未完成:
    模型输出 tool_call 或最终文本
    若是 tool_call:
        Cursor 按权限执行（读/写/终端/MCP/浏览器）
        把 stdout / diff / 文件内容作为 tool_result 回传
    否则:
        把文本展示给你，结束本轮
```

官方说明：**一次任务的工具调用次数没有上限。** 次数会计入用量（token / 请求）。

内置工具主要包括：

| 工具                 | 作用                     | 默认是否要你点批准            |
| ------------------ | ---------------------- | -------------------- |
| 搜索文件 / grep / 语义检索 | 按名字、正则、语义找代码           | 否                    |
| 读文件                | 读源码；也支持 png/jpg 等给视觉模型 | 否                    |
| 改文件                | 直接写进磁盘                 | 工作区文件通常直接写；配置文件要批准   |
| 终端                 | 跑 shell，读输出            | 默认要批准（受 Run Mode 控制） |
| Web 搜索 / Fetch     | 查文档、拉链接                | 受网络策略限制              |
| Browser            | 打开页面、点元素、截图            | 可单独保护                |
| 问你问题               | 澄清需求；等你时仍可继续读文件        | —                    |
| 生图                 | 默认写到项目 `assets/`       | —                    |
| MCP 工具             | 外部系统（Jira、DB、K8s…）     | 连接和每次调用默认都要批准        |
| Fetch Rules        | 按描述拉取规则                | —                    |

模型可以一次发出多个工具调用，并行搜、并行读。探索类工作常被派给 **Explore 子代理**（更快的模型、独立上下文），避免把主对话撑爆。

### 5.3 上下文从哪来（模型「看见」了什么）

按优先级，模型实际看到的大致是：

1. **系统提示词**（Cursor 按模型调过，对你不可见）。
2. **Team Rules → Project Rules → User Rules**（冲突时前者优先）。
3. **AGENTS.md**（根目录和子目录嵌套，越靠近当前文件越具体）。
4. **Skills** 的描述；命中后再读 `SKILL.md` 正文和 `references/`。
5. **MCP 工具目录**。
6. **你 `@` 的文件、终端、diff、图片**。
7. **打开的 / 最近看过的文件**（Inline Edit 尤其依赖这个）。
8. **代码库索引的语义检索结果**（按你的问题召回相关块）。
9. **Agent 自己 grep / 读文件拿到的内容**。
10. **本轮及历史 tool results**（太长会被摘要）。

代码库索引流程（简化）：

1. 工作区文件同步到 Cursor 服务端做 embedding。
2. 按函数 / 类 / 逻辑块切分，而不是随意切字。
3. 查询时用自然语言召回相关块，再交给 Agent 精读。
4. `.gitignore` 和 `.cursorignore` 中的文件不进索引、也不让 Agent 用读文件工具直接读。

**索引不是安全边界。** 终端和 MCP 仍可能读到被 ignore 的文件。密钥要用文件系统权限、密钥管理，而不是只靠 ignore。

### 5.4 模型怎么选

输入框上方模型选择器，或 `Ctrl + /` 循环切换。中途可换模型（例如探索用快模型，落地用强模型）。

当前有两套用量池（随订阅周期重置）：

| 池 | 包含 | 特点 |
| --- | --- | --- |
| **Cursor Models** | Grok 4.6 / Grok 4.5、Composer 2.5 | 包含额度更多，适合日常 Agent |
| **Other Models** | Claude / GPT / Gemini 等第三方 | 按该模型 API 价从额度里扣 |

粗选策略：

| 场景               | 建议                                                   |
| ---------------- | ---------------------------------------------------- |
| 小改、改测试、常规重构      | Composer 2.5（快、便宜、为 Cursor 工具调用训过）                   |
| 架构决策、难 bug、跨很多文件 | Claude Opus / GPT 高配，或 Plan 模式 + 强模型                 |
| 不确定              | Teams/Enterprise 可用 **Auto**（Cursor Router 按任务复杂度分流） |
| 只要速度             | 选 Fast 变体（更贵）                                        |

Auto 的三种优化（Teams/Enterprise）：

- **Cost**：省 token
- **Balance**：智力 / 速度 / 成本折中
- **Intelligence**：难题走更强模型

Auto 按**实际路由到的模型标价**计费，不是免费。

**自带 API Key（BYOK）**

`Settings → Models` 可填 OpenAI / Anthropic / Google / Azure / AWS Bedrock。

必须知道的三点：

1. 请求**仍然经过 Cursor 后端**做最终 prompt 拼装，Key 随请求加密传输，不落盘。
2. **Cursor 的 Zero Data Retention 不适用于 BYOK**，数据按你所选供应商的隐私政策处理。
3. Tab 补全仍走 Cursor 自有模型，BYOK 只管 Chat/Agent。

### 5.5 数据流与隐私（生产代码尤其重要）

**Privacy Mode 开着时：**

- 代码不会被 Cursor 或模型供应商拿去训练。
- 多数官方路由模型走零保留（ZDR）协议。
- 仍会把 **prompt + 相关代码上下文** 发给模型供应商做推理。Privacy Mode **阻止的是训练，不是传输**。

**两条出网路径：**

1. **LLM 请求**：prompt 和代码上下文 → OpenAI / Anthropic / Google / Cursor 推理等。
2. **Cloud Agents**：必须在云端存仓库副本和会话（加密）。这是唯一「Cursor 要存代码」的主路径。

例外：

- BYOK：跟供应商协议走，不是 Cursor ZDR。
- 少数模型（如 Claude Fable 5 / 5.1）供应商会为安全审核保留输入输出，需管理员单独批准。
- 索引会上传切块做 embedding；明文在请求结束后丢弃，embedding 和元数据（哈希、文件名）可能保留。

公司代码检查清单：

1. 打开并强制 Privacy Mode。
2. `.cursorignore` 排除 `.env*`、密钥、客户数据、大型生成物。
3. 不要把生产库 dump、客户 PII 放进工作区再问 Agent。
4. Cloud Agents 的 secrets 走 Dashboard Secrets / OIDC，不要写进仓库。

### 5.6 权限：模型「想做」和「被允许做」不是一回事

LLM 只是在建议动作。真正执行受 Cursor 拦截。

**本地 Agent 的 Run Modes**（`Settings → Agents → Approvals & Execution`）：

| 模式 | 行为 | 适用 |
| --- | --- | --- |
| **Auto-review**（推荐默认） | 白名单立刻跑；能进沙箱的命令进沙箱；其余交给分类器 | 大多数人 |
| **Allowlist** | 只有你列出的动作免确认 | 要确定性行为 |
| **Run Everything** | 全部自动跑，无沙箱 | 隔离环境才考虑 |

Auto-review **不是安全边界**，分类器会误放/误拦。生产相关命令应写进 `~/.cursor/permissions.json` 或项目 `.cursor/permissions.json`：

```json
{
  "autoRun": {
    "allow_instructions": [],
    "block_instructions": [
      "Every AWS CLI command should go through approval first.",
      "Every command that modifies Kubernetes resources should go through approval first.",
      "Every database DROP, DELETE, UPDATE, or migration against production should be blocked.",
      "Every git push to main or production branch should go through approval first."
    ]
  }
}
```

**沙箱**（macOS Seatbelt / Linux Landlock）：限制工作区外写、保护 `.git/config` 等路径、默认拦任意网络。需要出网的包管理走默认域名白名单。

**Cloud Agents 不用 Run Modes。** 它们在独立 VM 里自动跑命令，不会每步问你。连生产网络前必须先收紧 egress、secrets 和 MCP。

**硬控制 vs 软引导（官方安全模型）：**

- **硬控制**：终端审批、Hooks 拒绝、沙箱、MCP allowlist、文件权限。LLM 再怎么说也执行不了。
- **软引导**：Rules、Skills、MCP 知识。只能降低做坏事的概率，不能当策略引擎。

生产相关约束必须用硬控制。

---

## 6. 用 Rules / Skills / MCP 把对话变成可重复系统

### 6.1 Rules：写进每一轮的「公司说明书」

大模型没有跨补全的记忆。Rules 把稳定约束塞进每轮 prompt 开头。

四种来源：

| 类型 | 位置 | 范围 |
| --- | --- | --- |
| Project Rules | `.cursor/rules/*.mdc` | 本仓库，可进 Git |
| User Rules | Customize → Rules | 你这台机器上所有项目 |
| Team Rules | Dashboard | 全团队，可强制 |
| AGENTS.md | 仓库根目录或子目录 | 简单纯 Markdown |

`.mdc` 必须有 frontmatter。纯 `.md` 放在 `.cursor/rules` 会被忽略。

```markdown
---
description: 后端 RPC 与错误处理约定
alwaysApply: false
---

- 每个 service 单独文件，放在 src/services/
- 入口处校验输入，不要把未校验数据往下传
- 错误返回 { code, message }，不要 throw 原始字符串
```

应用方式：

- `alwaysApply: true`：每轮都带上
- 配 `globs`：相关文件在上下文里时自动带上
- 只有 `description`：Agent 判断相关再拉
- 都没有：只有你 `@rule-name` 才带

好规则要短、可执行、带例子或 `@` 指向权威文件。发现 Agent 反复犯同一错误，再补规则，不要一上来写百科。

### 6.2 Skills：教 Agent「怎么做某类活」

Skills 是带 `SKILL.md` 的文件夹，可含 `scripts/`、`references/`、`assets/`。Agent 根据 description 决定用不用，也可 `/skill-name` 手动调用。

目录：

- 项目：`.cursor/skills/` 或 `.agents/skills/`
- 用户：`~/.cursor/skills/`
- 也兼容 `.claude/skills/`、`.codex/skills/`

把 skill 当 **Custom Mode**：`/` 菜单里选中后 `Alt + Enter`（Mac：`Opt + Enter`），整个会话都保持该 playbook（例如全程 TDD）。

内置常用：`/create-rule`、`/create-skill`、`/review`、`/review-security`、`/split-to-prs`、`/autopilot`、`/loop`、`/in-cloud`。

### 6.3 MCP：让模型调用外部系统

MCP 把 Jira、Figma、数据库、K8s、监控、内部 API 变成模型可调用的工具。

三种传输：

| 传输 | 跑在哪 | 配置 |
| --- | --- | --- |
| **stdio** | 本机进程，Cursor 拉起 | `command` + `args` |
| **SSE** | 本地或远程 HTTP | `url` |
| **Streamable HTTP** | 本地或远程 HTTP | `url`，可 OAuth |

项目级：`.cursor/mcp.json`  
全局：`~/.cursor/mcp.json`

```json
{
  "mcpServers": {
    "internal-api": {
      "url": "https://mcp.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MCP_TOKEN}"
      }
    },
    "local-db": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

密钥用 `${env:NAME}`，不要写进文件。调试：Output 面板选 **MCP Logs**。

**Remote SSH 时：** MCP 默认在**远端主机**上启动。本机 `~/.cursor/mcp.json` 里的 stdio 服务不会自动跟过去。需要本机凭证时，把 MCP 做成 HTTP 服务，再用 SSH 反向隧道指过去。

---

## 7. IDE 连接生产环境

「连生产」在 Cursor 里通常是下面五条路。**默认原则：Agent 不要对生产拥有写权限。** 能连 staging / 只读副本 / 跳板机，就不要直连生产主库、生产 K8s 的写账号。

### 7.1 五条路径对比

| 路径 | 编辑器在哪 | 代码/终端在哪 | 模型推理在哪 | 典型用途 |
| --- | --- | --- | --- | --- |
| 本地打开仓库 | 本机 | 本机 | Cursor 云 + 模型供应商 | 日常开发 |
| **Remote SSH** | 本机 UI | 远端机器（可是跳板/生产机） | 同上；工具在远端执行 | 在服务器上改代码、看日志 |
| **Cloud Agents** | 浏览器 / IDE / 手机 | Cursor 托管的 Ubuntu VM | Cursor 云 | 并行干活、关电脑也能跑 |
| **Self-hosted / My Machines** | 同上 | 你自己的机器执行工具 | Agent loop 仍在 Cursor 云 | 代码不出内网、要碰私有 registry |
| **MCP 连生产系统** | 任意 | 工具打到生产 API/DB | 模型仍在云端看到工具返回 | 查单、看指标、触发发布 |

无论哪条路，**模型推理几乎都在 Cursor / 供应商云上**。进模型的是工具返回的文本（文件片段、查询结果、日志）。「代码不出内网」只能保证磁盘上的完整仓库和密钥留在你这边，**不能保证查询结果不被送去模型**。

### 7.2 路径 A：Remote SSH（IDE 连到远端机器）

Cursor 自带 Remote SSH（和 VS Code 同类，但是 Cursor 自己的实现）。

**架构：** 本机只跑 UI；远端安装 `cursor-server`；终端、调试器、语言服务、Agent 文件工具都在远端。

**配置 `~/.ssh/config`：**

```sshconfig
Host prod-jump
    HostName jump.example.com
    User deploy
    Port 22
    IdentityFile ~/.ssh/id_ed25519
    ForwardAgent no
    ServerAliveInterval 60
    ServerAliveCountMax 3

Host staging-app
    HostName 10.0.10.21
    User app
    ProxyJump prod-jump
    IdentityFile ~/.ssh/id_ed25519
```

**连接步骤：**

1. `Ctrl + Shift + P` → `Remote-SSH: Connect to Host`。
2. 选 `user@host`（不要只填 IP，否则会拼上你本机用户名）。
3. 选远端 OS，确认 host key，用密钥登录（不要把生产密码交给 Agent 去敲）。
4. 第一次会在远端装 Cursor Server，需要远端能访问 `*.cursor.sh`、`cursor-cdn.com`、`marketplace.cursorapi.com`。
5. `File → Open Folder` 打开远端项目。
6. 左下角应显示 `SSH: hostname`。此后 Agent 的终端就是远端 shell。

**Agents Window** 也可以把某个 Agent 的执行环境设为 remote SSH。

**连上之后 Agent 实际拥有什么：**

- 远端上该 Linux 用户能读的文件、能跑的命令、能连的内网。
- 如果你 SSH 的是生产机且用户有 `kubectl`/`psql` 写权限，等于把生产写权限给了会幻觉的模型。

**建议拓扑：**

```
笔记本 Cursor UI
    --SSH--> 开发跳板 / staging 机器（只读生产数据或独立凭据）
                 |-- 应用代码
                 |-- 只读 DB 副本
                 |-- kubectl -n staging
                 └── 禁止：prod kubecontext、prod 主库可写账号
```

**Remote SSH 常见坑：**

- 远端 `~/.bashrc` 在非交互 shell 里往 stdout 打东西，会导致握手超时。
- 磁盘满或 `~/.cursor-server` 残留进程：`pkill -f cursor-server` 后删掉该目录再连。
- Agent 超时：提高 `remote.SSH.connectTimeout`，必要时清本地 `CachedExtensions`。
- 公司代理：本机设 `remote.SSH.httpProxy` / `httpsProxy`（连上 SSH 之后、下载 server 之前生效）。

### 7.3 路径 B：MCP 把生产系统接到对话里

这是「在 IDE 里问生产数据」最常见的做法，不必 SSH 进生产机。

例子：

- 只读 SQL MCP → 查订单、对账（连 **只读副本**，账号无 DDL/DML）。
- Kubernetes MCP → `get/describe`，禁止 `apply/delete`。
- 日志 / APM MCP → 拉 stacktrace、trace。
- 发布平台 MCP → 仅 staging；生产发布走人工或单独审批流。
- GitHub/GitLab MCP → PR、CI。

**生产向 MCP 的硬性要求：**

1. 独立只读凭据，不要复用人的管理员账号。
2. 数据库用户：`SELECT` only，行级/库级限制，超时和 max rows。
3. MCP 工具 allowlist：只开放 `query` / `get_*`，关掉 `execute` / `delete_*`。
4. 返回做脱敏（手机号、证件、token）。
5. 默认保留工具批准；生产写操作永远不要免确认。
6. 企业用 Dashboard MCP Allowlist + 网络策略，禁止私自加 stdio 服务器。

对话示例（Ask 模式更安全）：

```
用只读订单库查一下最近 1 小时支付成功但未发货的订单，
只返回 order_id、status、created_at，不要 SELECT *，不要碰主库。
```

### 7.4 路径 C：Cloud Agents 访问私网 / 类生产环境

Cloud Agents 在隔离 Ubuntu VM 里跑，和本地无关。要让它「像工程师一样」测东西，必须先配 **environment**：

1. Dashboard → Cloud Agents → Environments，连 GitHub/GitLab/Azure DevOps/Bitbucket。
2. 用 Agent 引导安装依赖，或提交 `.cursor/environment.json` + Dockerfile。
3. Secrets 放 Dashboard（或环境级 secrets），不要依赖 `.env.local`。
4. `install` 脚本放可重复的依赖安装；`start` / `terminals` 放 Docker、DB、dev server。
5. 在 `AGENTS.md` 里写一节 `Cursor Cloud specific instructions`。

**打到内网 / 类生产：**

| 方式 | 要点 |
| --- | --- |
| **Tailscale** | 必须 `--tun=userspace-networking`，再设 `ALL_PROXY`/`HTTPS_PROXY`。VM 不能当 exit node。 |
| **Cloudflare Tunnel** | 私网里跑 `cloudflared`，Agent 用 Access service token 走 HTTPS；TCP（数据库）用 `cloudflared access tcp` 转到本地端口。 |
| **网络允许列表** | 收紧 egress，只放包管理器和必要内部域名。 |
| **OIDC / AWS IAM Role** | 用短时凭证，不要长期 AKSK。 |

Cloud Agent 会自动跑命令、可控制远程桌面。**不要把生产主库密码、生产 kubeconfig 放进 Cloud Secrets。** 用 staging 连接串，或只读凭据。

### 7.5 路径 D：Self-hosted Worker / My Machines

适合：完整仓库不能进 Cursor 云、要访问私有 npm/PyPI、构建缓存在内网。

分工：

- **留在你网络内：** 磁盘上的仓库、secrets、构建产物、私有 registry、内部 API。
- **送到 Cursor：** 工具结果（stdout、diff、读到的文件块）、路由元数据、给模型的 prompt 上下文。

本机或内网机器：

```bash
agent worker start --pool
```

只需出站 HTTPS 到 Cursor，不必开入站端口。Agent loop（规划、调模型）仍在 Cursor 云。

### 7.6 路径 E：从 Cursor 发布到生产

可以做，但不要让同一条 Agent 会话「改代码 + 直接生产发布」。

推荐拆开：

1. Agent 在 feature 分支改代码、跑测试。
2. 开 PR；Bugbot / `/review-security` 审。
3. 人 merge。
4. 发布由 CI 或单独的、有审批的 skill（例如 `/deploy-staging`），生产需要双人确认。

Skill 里调用脚本，而不是让模型现场拼 `kubectl apply -f`：

```markdown
---
name: deploy-staging
description: 部署到 staging。仅当用户明确要求发布到 staging 时使用。禁止生产。
---

1. 确认当前分支 CI 已绿。
2. 只执行 scripts/deploy.sh staging。
3. 不要执行任何 production 参数。
4. 把 pipeline URL 发回给用户。
```

### 7.7 生产环境红线

1. **不要**用可写的生产数据库账号配 MCP 或塞进 Agent 终端。
2. **不要**在生产机上开 `Run Everything`。
3. **不要**把 kubeconfig 的 `prod` context 放进 Agent 能读的默认路径；用独立 `KUBECONFIG` 且只挂 staging。
4. **不要**把 `.env.production`、客户导出、完整日志灌进聊天。
5. **不要**假设 `.cursorignore` 能挡住终端/`cat`/`python -c`。
6. **要**用 Git；Agent 改完立刻可回滚。
7. **要**在 Rules 里写死：「未明确要求时禁止生产写操作；先给命令让我批准。」
8. **要**对 AWS/K8s/DROP 等走 Auto-review 的 `block_instructions` 或 Hooks 直接 deny。
9. **要**把生产排障放在 Ask 模式 + 只读 MCP；确认根因后再开独立、有范围的修复会话。
10. **要**给 Cloud Agent 配 egress allowlist，避免 prompt injection 把代码送到外部 URL。

Prompt injection 在连生产时特别危险：Agent 若读取了恶意 issue、网页或日志，可能被指示「把仓库 POST 到某地址」。Cloud Agents 自动跑命令，风险高于本地（本地至少还能弹批准）。

### 7.8 推荐的「生产排障」对话模板

```
模式：Ask（先不要改代码、不要跑写命令）

环境：staging 只读副本，不是 prod 主库。
现象：支付成功回调后订单仍是 unpaid，发生在 10:12–10:20 UTC。
请：
1. 用日志 MCP 拉该时间窗、trace_id=... 的错误；
2. 用只读 SQL 查 orders / payments 状态机，LIMIT 50；
3. 对照代码里的 webhook handler，指出最可能的分支；
4. 给出修复计划，但不要改文件、不要执行 UPDATE。
```

确认后再切 Agent，并写明：

```
只改 webhook handler 和测试。
不要 migrate，不要碰生产，不要 git push。
跑单元测试，把 diff 给我 review。
```

---

## 8. 推荐工作流

### 8.1 每天的 30 分钟闭环

1. 打开仓库，确认索引完成。
2. **Ask**：搞清模块和调用链，确认范围。
3. **Plan**（稍大的需求）：让它提问并出计划，你改计划。
4. **Agent**：按计划改，跑已有测试。
5. 你看 diff：有没有越界、有没有删测试、有没有把密钥写进代码。
6. 提交前 `/review` 或 Bugbot。

### 8.2 提示词怎么写才有效

模型没有你的隐含知识。把下面四件事写进同一条消息：

1. **目标**（用户可感知的结果）
2. **范围**（哪些目录能动，哪些不能）
3. **验收**（测试命令、行为、不要破坏什么）
4. **约束**（风格、API 兼容、禁止生产操作）

反面：「帮我优化一下性能。」  
正面：「`GET /api/orders` 在 1 万行时 p95 > 800ms。不要改 schema。加查询层缓存，失效写在 `OrderService.update`。用现有 Redis 封装。加测试。先给计划。」

### 8.3 并行与隔离

- 同一仓库多任务：用 **worktree**，每个 Agent 独立 checkout。
- 长任务不占本地：`/in-cloud` 或把 Agent 切到 Cloud。
- PR 托管：`/autopilot` 让云端 Agent 处理 review 意见和冲突。
- 主对话要保持干净：让 Explore / Bash / Browser 子代理去干脏活。

### 8.4 子代理

内置三个：Explore（搜代码）、Bash（跑命令）、Browser（浏览器）。可在 `.cursor/agents/*.md` 自定义，例如只读的 `security-auditor`、专门验活的 `verifier`。

子代理有自己的上下文，**开始时看不到主对话**，父代理必须把必要信息写进委托 prompt。并行子代理默认同一个工作区，会互相覆盖；需要时明确要求「each in its own environment」。

---

## 9. 团队落地清单

| 事项 | 建议 |
| --- | --- |
| Privacy Mode | 组织级强制 |
| Team Rules | 安全底线（禁止提交密钥、禁止生产写）写成 enforced |
| MCP | Dashboard 分发 + Allowlist；生产 MCP 只读 |
| Run Mode | 团队默认 Auto-review；生产仓库禁止 Run Everything |
| Hooks | `beforeShellExecution` 拦截 `git push`、`DROP`、`kubectl apply` 到 prod |
| `.cursorignore` | `.env*`、密钥、数据 dump、超大生成物 |
| Cloud Environment | 提交 `.cursor/environment.json`；secrets 走 OIDC |
| 评审 | PR 开 Bugbot；关键路径 `/review-security` |
| 用量 | 日常 Composer / Grok 走 Cursor Models 池；难题再上第三方 |

---

## 10. 故障排查

| 现象 | 先查什么 |
| --- | --- |
| Agent 改错地方 / 乱改 | 范围写清了吗？新开聊天；用 Plan；检查 Always Apply 规则是否互相打架 |
| 回答像没读过仓库 | 索引是否完成；文件是否被 gitignore；先 `@` 关键文件 |
| 上下文环很快满 | 关掉不用的 MCP；规则拆短；新开聊天 |
| 终端命令一直问你 | 这是默认保护；常用只读命令再进 allowlist |
| MCP 连不上 | Output → MCP Logs；SSH 场景下进程是否在远端 |
| Remote SSH 卡住 | 远端 stdout 污染、磁盘、`cursor-server` 僵尸进程、出网到 `*.cursor.sh` |
| 用了自己的 Key 仍走 Cursor | 正常，prompt 必须在 Cursor 后端拼完再转发 |
| Cloud Agent 没有新 secret | secret 只在启动时注入，改完要新开 Agent |
| 模型突然不听话 | 是否切过模式（新上下文）；是否被摘要掉早期约束；把约束写进 Rule |

---

## 11. 速查：什么场景用什么

| 你想做的事                 | 用这个                                  |
| --------------------- | ------------------------------------ |
| 写到一半补下一行              | Tab                                  |
| 改当前函数                 | `Ctrl + K`                           |
| 搞懂模块，先别动代码            | Ask                                  |
| 加功能、修 bug、重构          | Agent                                |
| 大需求、方案要先过目            | Plan                                 |
| 偶现 bug、要日志证据          | Debug                                |
| 看生产日志 / 查库            | Ask + 只读 MCP（副本）                     |
| 在 staging 机器上改        | Remote SSH 到 staging，不要 SSH 到 prod   |
| 关电脑也要继续跑              | Cloud Agent                          |
| 代码不能出内网               | Self-hosted worker；仍要假设 tool 返回值会进模型 |
| 同一规范反复说               | Rule 或 AGENTS.md                     |
| 一套固定步骤（发布、TDD）        | Skill / Custom Mode                  |
| 接 Jira / 设计稿 / 内部 API | MCP                                  |

---

## 12. 官方入口

- 文档总览：https://cursor.com/docs  
- Agent：https://cursor.com/docs/agent/overview  
- 模式与提问：https://cursor.com/docs/agent/plan-mode 、https://cursor.com/docs/agent/prompting  
- Rules / Skills / MCP：https://cursor.com/docs/rules 、https://cursor.com/docs/skills 、https://cursor.com/docs/mcp  
- Cloud Agents 与环境：https://cursor.com/docs/cloud-agent 、https://cursor.com/docs/cloud-agent/setup  
- 安全与 Run Modes：https://cursor.com/docs/agent/security 、https://cursor.com/docs/agent/security/run-modes  
- 隐私：https://cursor.com/help/security-and-privacy/privacy  
- 模型与价格：https://cursor.com/docs/models-and-pricing  
- 云端 Agent 控制台：https://cursor.com/agents  

---

## 附录 A. 最小项目配置示例

```text
.cursor/
  rules/
    security.mdc
    backend.mdc
  skills/
    deploy-staging/SKILL.md
  agents/
    verifier.md
  mcp.json
  environment.json
  permissions.json
AGENTS.md
.cursorignore
```

`.cursorignore` 最小集：

```gitignore
.env
.env.*
**/*.pem
**/secrets/
**/*.sql.gz
**/dumps/
node_modules/
dist/
```

`AGENTS.md` 最小集：

```markdown
# 工程约定

- 语言：TypeScript；API 校验用 zod
- 测试：改代码必须跑相关测试
- 禁止：提交密钥；未要求时不要 git push；不要连生产库
- 启动：npm run dev；测试：npm test

## Cursor Cloud specific instructions

- 用 Secrets 里的 DATABASE_URL_STAGING
- 不要使用任何 PROD_ 前缀变量
- 先 npm test 再给结论
```

---

## 附录 B. 和「网页版大模型」差在哪

| | 网页 ChatGPT / Claude | Cursor Agent |
| --- | --- | --- |
| 你发给模型的 | 你打的字 + 你粘贴的文件 | 系统提示 + Rules + 工具 schema + 检索块 + 工具结果 + 你的字 |
| 模型怎么「动手」 | 只能生成文本 | 通过 Cursor 调工具改真实文件、跑真实命令 |
| 记忆 | 会话内 | 会话 + 摘要 + Rules/Skills/索引；无跨会话隐式记忆（除非你写 Rule 或用记忆类 MCP） |
| 生产风险 | 泄露你粘贴的内容 | 泄露上下文 **以及** 误执行命令、误调 MCP |
| 你要负责的 | 别贴机密 | 权限、网络、MCP 范围、审批、Git |

记住最后一句就够：**Cursor 把 LLM 接到了你的文件系统、终端和（若你允许）生产系统上。模型会幻觉，权限不会。把权限收紧，比把 prompt 写得更凶更重要。**
