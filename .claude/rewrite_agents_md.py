from pathlib import Path
import re

src = Path(r'D:/Configure/Obsidian/my-pkb/.claude/agents_draft.md')
target = Path(r'D:/Configure/Obsidian/my-pkb/AI尚硅谷/大模型应用实战/LangChain/06-LangChain使用之Agents.md')
text = src.read_text(encoding='utf-8')
lines = text.splitlines()

out = []
in_code = False
compare_mode = False
compare_rows = []

def emit_compare(rows, out_lines):
    if not rows:
        return
    header = ['特性', 'Function Call 模式', 'ReAct 模式']
    out_lines.append('| ' + ' | '.join(header) + ' |')
    out_lines.append('| --- | --- | --- |')
    for i in range(0, len(rows), 3):
        chunk = rows[i:i+3]
        if len(chunk) == 3:
            out_lines.append('| ' + ' | '.join(x.replace('|', '\\|') for x in chunk) + ' |')
    out_lines.append('')


i = 0
while i < len(lines):
    line = lines[i].rstrip()
    s = line.strip()

    if s.startswith('```'):
        in_code = not in_code
        out.append('```python' if s == '```python' else '```')
        i += 1
        continue

    if in_code:
        s2 = re.sub(r'^\d+\s+', '', line.rstrip())
        if re.fullmatch(r'\d+', s2.strip()):
            i += 1
            continue
        out.append(s2)
        i += 1
        continue

    if not s:
        if out and out[-1] != '':
            out.append('')
        i += 1
        continue

    if re.fullmatch(r'\d+', s):
        i += 1
        continue

    s = s.replace('OpenaAI()', 'OpenAI()')
    s = s.replace('Funcation', 'Function')
    s = s.replace('找打scrape_website', '找到 scrape_website')
    s = s.replace('# 第06章：LangChain使用之Agents', '# 第06章：LangChain使用之 Agents')
    s = s.replace('## 1、理解Agents', '## 1. 理解 Agents')
    s = s.replace('### 1.1 Agent与Chain的区别', '### 1.1 Agent 与 Chain 的区别')
    s = s.replace('### 1.3 Agent的核心能力/组件', '### 1.3 Agent 的核心能力 / 组件')
    s = s.replace('## 2、Agent 入门使用', '## 2. Agent 入门使用')
    s = s.replace('### 2.1 Agent、AgentExecutor的创建', '### 2.1 Agent、AgentExecutor 的创建')
    s = s.replace('### 2.2 Agent的类型', '### 2.2 Agent 的类型')
    s = s.replace('### 2.3 AgentExecutor创建方式', '### 2.3 AgentExecutor 创建方式')
    s = s.replace('### 1.2 什么是Agent', '### 1.2 什么是 Agent')
    s = s.replace('#### 2.2.1 FUNCATION_CALL模式', '#### 2.2.1 Function Call 模式')

    if s in ('讲师：尚硅谷-宋红康', '官网：尚硅谷'):
        out.append('> ' + s)
        i += 1
        continue

    if s == '它可以根据任务动态决定：':
        out.append(s)
        out.append('')
        j = i + 1
        while j < len(lines):
            item = lines[j].strip()
            if item in ('如何拆解任务', '需要调用哪些工具', '以什么顺序调用', '如何利用好中间结果推进任务'):
                out.append('- ' + item)
                j += 1
                continue
            break
        out.append('')
        i = j
        continue

    if s.startswith('- 1）大模型'):
        out.extend([
            '1. **大模型（LLM）**：作为大脑，提供推理、规划和知识理解能力。',
            '   例如：`OpenAI()`、`ChatOpenAI()`',
            '2. **记忆（Memory）**：具备短期记忆（上下文）和长期记忆（向量存储），支持快速知识检索。',
            '   例如：`ConversationBufferMemory`、`ConversationSummaryMemory`、`ConversationBufferWindowMemory`',
            '3. **工具（Tools）**：调用外部工具（如 API、数据库）的执行单元。',
            '   例如：`SearchTool`、`CalculatorTool`',
            '4. **规划（Planning）**：用于任务分解、反思与自省，帮助实现复杂任务处理。',
            '5. **行动（Action）**：实际执行决策的能力。',
            '   例如：检索、推理、编程',
            '6. **协作**：通过与其他智能体交互合作，完成更复杂的任务目标。',
            ''
        ])
        while i < len(lines) and not lines[i].strip().startswith('**问题：'):
            i += 1
        continue

    if s.startswith('**问题：'):
        out.append('> ' + s.strip('*'))
        i += 1
        continue

    if s.startswith('- 举例1：'):
        out.append('- 举例 1：扣子平台智能体演示：<https://www.coze.cn/home>')
        i += 1
        continue
    if s.startswith('- 举例2：'):
        out.append('- 举例 2：Manus、纳米 AI 使用演示')
        i += 1
        continue

    if s.startswith('## 1、工具 Tool'):
        out.append('#### 1）工具（Tool）')
        out.append('')
        out.append('LangChain 提供了广泛的入门工具，也支持自定义工具，包括自定义描述。')
        i += 1
        continue
    if s.startswith('## 2、工具集 Toolkits'):
        out.append('#### 2）工具集（Toolkits）')
        out.append('')
        out.append('在构建 Agent 时，通常提供给 LLM 的工具不止一两个，而是一组可供选择的工具集（Tool 列表），这样可以让 LLM 在完成任务时拥有更多选择。')
        i += 1
        continue
    if s.startswith('## 3、智能体/代理 Agent'):
        out.append('#### 3）智能体 / 代理（Agent）')
        out.append('')
        out.append('智能体 / 代理（Agent）可以协助我们做出决策，调用相应的 API。底层实现方式是通过 LLM 来决定下一步执行什么动作。')
        i += 1
        continue
    if s.startswith('## 4、代理执行器 AgentExecutor'):
        out.append('#### 4）代理执行器（AgentExecutor）')
        out.append('')
        out.append('`AgentExecutor` 本质上是代理的运行时，负责协调智能体的决策和实际工具执行。')
        i += 1
        continue

    if s == '**方式1：传统**':
        out.append('#### 方式 1：传统方式')
        i += 1
        continue
    if s == '**方式2：通用**':
        out.append('#### 方式 2：通用方式')
        i += 1
        continue
    if s == '方式':
        i += 1
        continue

    if s in ('initialize_agent()', 'create_xxx_agent()', 'create_tool_calling_agent()', '调用AgentExecutor()', '构造方法'):
        if s == 'initialize_agent()':
            out.append('- 使用 `AgentType` 指定代理类型，并通过 `initialize_agent()` 快速创建。')
        elif s == 'create_xxx_agent()':
            out.append('- 使用 `create_xxx_agent()` 显式创建 Agent。')
        elif s == 'create_tool_calling_agent()':
            out.append('- 例如：`create_react_agent()`、`create_tool_calling_agent()`。')
        elif s == '调用AgentExecutor()':
            out.append('- 然后再通过 `AgentExecutor()` 组装执行器。')
        i += 1
        continue

    if s == 'Agent两种典型类型对比表':
        compare_mode = True
        compare_rows = []
        i += 1
        continue

    if compare_mode:
        if s.startswith('### ') or s.startswith('#### ') or s.startswith('**传统方式：'):
            emit_compare(compare_rows, out)
            compare_mode = False
            compare_rows = []
            continue
        compare_rows.append(s)
        i += 1
        continue

    if s.startswith('**传统方式：initialize_agent()**'):
        out.append('#### 传统方式：`initialize_agent()`')
        i += 1
        continue
    if s.startswith('**通用方式：AgentExecutor构造方法**'):
        out.append('#### 通用方式：`AgentExecutor()` 构造方法')
        i += 1
        continue

    if s == '**特点：**':
        out.append('**特点**')
        i += 1
        continue
    if s.startswith('**优点：'):
        out.append('- ' + s.strip('*'))
        i += 1
        continue
    if s.startswith('**缺点：'):
        out.append('- ' + s.strip('*'))
        i += 1
        continue
    if s == '**代码片段：**':
        out.append('**代码示例：**')
        out.append('')
        i += 1
        continue

    if s == '组件':
        out.extend([
            '| 组件 | 传统方式 | 通用方式 |',
            '| --- | --- | --- |',
            '| Agent 创建 | 通过 `AgentType` 枚举选择预设 | 通过 `create_xxx_agent` 显式构建 |',
            '| AgentExecutor 创建 | 通过 `initialize_agent()` 创建 | 通过 `AgentExecutor()` 创建 |',
            '| 提示词 | 内置且不可见 | 可以自定义 |',
            '| 工具集成 | 在 `AgentExecutor` 中显式传入 | 在 `Agent` / `AgentExecutor` 中都需显式传入 |',
            ''
        ])
        while i < len(lines) and lines[i].strip() != '3、Agent中工具的使用':
            i += 1
        continue

    if s == '3、Agent中工具的使用':
        out.append('## 3. Agent 中工具的使用')
        i += 1
        continue

    if re.match(r'^3\.\d+\s', s):
        num, title = s.split(' ', 1)
        out.append(f'### {num} {title}')
        i += 1
        continue

    if s.startswith('案例') or s.startswith('需求：') or s.startswith('TAVILY_API_KEY申请：') or s.startswith('API说明：'):
        if s.startswith('需求：') or s.startswith('API说明：'):
            out.append('> ' + s)
        else:
            out.append('**' + s + '**')
        i += 1
        continue

    if s.startswith('方式1：') or s.startswith('方式2：'):
        out.append('#### ' + s)
        i += 1
        continue

    if s.startswith('1第1步：') or s.startswith('1问题：'):
        temp = s.replace('1第1步：', '第1步：').replace('1问题：', '问题：')
        temp = re.sub(r'\s*(\d+)(?=(第\d+步：|思考：|行动：|观察：|最后：))', '\n', temp)
        parts = [p.strip() for p in temp.split('\n') if p.strip()]
        for p in parts:
            out.append('- ' + p)
        i += 1
        continue

    if s.startswith('以MCP工具为例说明：'):
        out.append('例如，可参考 MCP 工具市场：  ')
        out.append('<https://bailian.console.aliyun.com/?tab=mcp#/mcp-market>')
        i += 1
        continue

    out.append(s)
    i += 1

if compare_mode:
    emit_compare(compare_rows, out)

text2 = '\n'.join(out)
text2 = re.sub(r'\n{3,}', '\n\n', text2).strip() + '\n'
target.write_text(text2, encoding='utf-8')
print(target)
print(f'LINES={len(text2.splitlines())}')
