from pathlib import Path
from typing import List
import re
import unicodedata

SRC = Path(r"D:/Configure/Obsidian/my-pkb/.claude/agents_docx_extracted.txt")
TARGET = Path(r"D:/Configure/Obsidian/my-pkb/AI尚硅谷/大模型应用实战/LangChain/06-LangChain使用之Agents.md")


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\xa0", " ").replace("　", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def prettify(text: str) -> str:
    text = norm(text)
    replacements = {
        "OpenaAI()": "OpenAI()",
        "Funcation": "Function",
        "LangChain使用之Agents": "LangChain使用之 Agents",
        "理解Agents": "理解 Agents",
        "Agent与Chain": "Agent 与 Chain",
        "什么是Agent": "什么是 Agent",
        "Agent的核心能力/组件": "Agent 的核心能力 / 组件",
        "Agent中工具的使用": "Agent 中工具的使用",
        "FUNCATION_CALL模式": "Function Call 模式",
        "Function Call模式": "Function Call 模式",
        "Agent的类型": "Agent 的类型",
        "AgentExecutor创建方式": "AgentExecutor 创建方式",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\[(.+?)\]\[(https?://[^\]]+)\]", r"\1：<\2>", text)
    return text


def expand_line(line: str) -> List[str]:
    line = prettify(line)
    if not line:
        return []

    if "AgentType." in line and "#第" in line and not line.startswith("AgentType."):
        left, right = line.split("AgentType.", 1)
        left = re.sub(r"\s*\d+\s*$", "", left).strip()
        right = "AgentType." + right.strip()
        right = re.sub(r"\s+\d+\s*$", "", right).strip()
        out = []
        if left:
            out.append(left)
        if right:
            out.append(right)
        return out

    if re.search(r"\d+）", line) and line.count("）") > 1 and not re.match(r"^\d+[、.]", line):
        parts = [p.strip() for p in re.split(r"(?=\d+）)", line) if p.strip()]
        if parts:
            return parts

    return [line]


def is_heading(text: str):
    if re.match(r"^第\d+章[:：]", text):
        return 1
    if re.match(r"^\d+、", text):
        return 2
    if re.match(r"^\d+\.\d+\.\d+", text):
        return 4
    if re.match(r"^\d+\.\d+", text):
        return 3
    return None


def fmt_heading(text: str, level: int) -> str:
    if level == 1:
        return f"# {text}"
    if level == 2:
        m = re.match(r"^(\d+)、\s*(.+)$", text)
        return f"## {m.group(1)}. {m.group(2)}"
    if level == 3:
        m = re.match(r"^(\d+\.\d+)\s*(.+)$", text)
        return f"### {m.group(1)} {m.group(2)}"
    m = re.match(r"^(\d+\.\d+\.\d+)\s*(.+)$", text)
    return f"#### {m.group(1)} {m.group(2)}"


def is_code(text: str) -> bool:
    t = re.sub(r"^\d+\s+", "", text).strip()
    if not t or re.fullmatch(r"\d+", t):
        return False
    starters = (
        "from ", "import ", "#", "def ", "class ", "if ", "for ", "while ",
        "try:", "except ", "return ", "print(", "os.environ", "prompt =",
        "tools =", "tool =", "search =", "llm =", "memory =", "agent =",
        "agent_executor", "db =", "initialize_agent(", "AgentExecutor(",
        "create_", "ChatOpenAI(", "TavilySearchResults(", "PythonREPLTool(",
        "DuckDuckGoSearchRun(", "SerpAPIWrapper(", "load_tools(", "@tool", "pip install"
    )
    if t.startswith(starters):
        return True
    if t.startswith("AgentType."):
        return True
    if t.startswith("{") and t.endswith("}"):
        return True
    if any(k in t for k in (".invoke(", ".run(", ".pull(", "Tool(", "StructuredTool(", "BaseTool(")):
        return True
    if "=" in t and any(ch in t for ch in "()[]{}\""):
        return True
    return False


def clean_code(text: str) -> str:
    text = re.sub(
        r"^\d+\s+(?=(from|import|#|def|class|if|for|while|try:|except|return|print|os\.|prompt|tools|tool|search|llm|memory|agent|agent_executor|db|AgentType\.))",
        "",
        text,
    )
    text = re.sub(r"^\d+\s*$", "", text).strip()
    text = re.sub(r"\s+\d+\s*$", "", text)
    return text.strip()


def split_workflow(text: str) -> List[str]:
    text = text.replace("1第1步：", "第1步：").replace("1问题：", "问题：")
    text = re.sub(r"\s*(\d+)(?=(第\d+步：|问题：|思考：|行动：|观察：|最后：))", "\n", text)
    labels = ["第1步：", "第2步：", "第3步：", "第4步：", "第5步：", "问题：", "思考：", "行动：", "观察：", "最后："]
    parts = []
    current = ""
    for frag in re.split(r"\n+", text):
        frag = frag.strip()
        if not frag:
            continue
        matched = False
        for label in labels:
            if frag.startswith(label):
                if current:
                    parts.append(current.strip())
                current = frag
                matched = True
                break
        if not matched:
            if current:
                current += " " + frag
            else:
                current = frag
    if current:
        parts.append(current.strip())
    return parts


raw_lines = []
for original in SRC.read_text(encoding="utf-8").splitlines():
    raw_lines.extend(expand_line(original))
raw_lines = [line for line in raw_lines if line]

out = []
para = []
in_code = False
mode = None
rows = []


def flush_para():
    global para
    if not para:
        return
    text = "".join(para).strip()
    para = []
    if text:
        out.append(text)
        out.append("")


def close_code():
    global in_code
    if in_code:
        out.append("```")
        out.append("")
        in_code = False


def emit_triplet_table(header: List[str], body_rows: List[str]):
    body_rows = [r for r in body_rows if r and not re.fullmatch(r"\d+", r)]
    if body_rows[: len(header)] == header:
        body_rows = body_rows[len(header):]
    out.append("| " + " | ".join(header) + " |")
    out.append("| " + " | ".join(["---"] * len(header)) + " |")
    for i in range(0, len(body_rows), len(header)):
        chunk = body_rows[i : i + len(header)]
        if len(chunk) == len(header):
            out.append("| " + " | ".join(c.replace("|", "\\|") for c in chunk) + " |")
    out.append("")


for line in raw_lines:
    if mode in {"compare", "summary"} and is_heading(line):
        if mode == "compare":
            emit_triplet_table(["特性", "Function Call 模式", "ReAct 模式"], rows)
        else:
            emit_triplet_table(["组件", "传统方式", "通用方式"], rows)
        mode = None
        rows = []

    if mode is not None:
        rows.append(line)
        continue

    level = is_heading(line)
    if level:
        flush_para()
        close_code()
        out.append(fmt_heading(line, level))
        out.append("")
        continue

    if line in {"讲师：尚硅谷-宋红康", "官网：尚硅谷"}:
        flush_para()
        close_code()
        out.append("> " + line)
        out.append("")
        continue

    if line == "Agent两种典型类型对比表":
        flush_para()
        close_code()
        mode = "compare"
        rows = []
        continue

    if line == "组件":
        flush_para()
        close_code()
        mode = "summary"
        rows = [line]
        continue

    if line == "它可以根据任务动态决定：":
        flush_para()
        close_code()
        out.append(line)
        out.append("")
        continue

    if line in {"如何拆解任务", "需要调用哪些工具", "以什么顺序调用", "如何利用好中间结果推进任务"}:
        flush_para()
        close_code()
        out.append("- " + line)
        continue

    if line.startswith(("问题：", "需求：", "API说明：", "TAVILY_API_KEY申请：")):
        flush_para()
        close_code()
        out.append("> " + line)
        out.append("")
        continue

    if line in {"特点：", "优点：", "缺点：", "代码片段：", "工作流程示例：", "具体使用步骤：", "小结："}:
        flush_para()
        close_code()
        out.append("**" + line[:-1] + "：**")
        out.append("")
        continue

    if line.startswith(("传统方式：", "通用方式：", "方式1：", "方式2：")):
        flush_para()
        close_code()
        line = line.replace("AgentExecutor构造方法", "`AgentExecutor()` 构造方法")
        line = line.replace("initialize_agent()", "`initialize_agent()`")
        out.append("#### " + line)
        out.append("")
        continue

    if line.startswith(("环节1：", "环节2：")):
        flush_para()
        close_code()
        out.append("- " + line)
        continue

    if line.startswith(("举例1：", "举例2：", "案例1：", "案例2：", "案例3：", "案例4：")):
        flush_para()
        close_code()
        out.append("- " + line)
        continue

    if re.match(r"^[①②③④⑤⑥⑦⑧⑨⑩]", line) or re.match(r"^\d+）", line):
        flush_para()
        close_code()
        out.append("- " + line)
        continue

    if "第1步：" in line or ("问题：" in line and any(k in line for k in ["思考：", "行动：", "观察：", "最后："])):
        flush_para()
        close_code()
        for part in split_workflow(line):
            out.append("- " + part)
        out.append("")
        continue

    if is_code(line):
        flush_para()
        code = clean_code(line)
        if code:
            if not in_code:
                out.append("```python")
                in_code = True
            out.append(code)
        continue

    close_code()
    para.append(line)

flush_para()
close_code()
if mode == "compare":
    emit_triplet_table(["特性", "Function Call 模式", "ReAct 模式"], rows)
elif mode == "summary":
    emit_triplet_table(["组件", "传统方式", "通用方式"], rows)

text = "\n".join(out)
text = text.replace("AI的", "AI 的")
text = text.replace("LLM的", "LLM 的")
text = text.replace("在Chain中", "在 Chain 中")
text = text.replace("而Agent", "而 Agent")
text = text.replace("LangChain中", "LangChain 中")
text = text.replace("AgentType是", "AgentType 是")
text = text.replace("使用Tavily", "使用 Tavily")
text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

TARGET.write_text(text, encoding="utf-8")
print(TARGET)
print("LINES=" + str(len(text.splitlines())))
