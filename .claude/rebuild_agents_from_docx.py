from pathlib import Path
import re
import unicodedata

DOCX = Path(r"D:/Configure/Obsidian/my-pkb/AI尚硅谷/大模型应用实战/LangChain/06-LangChain使用之Agents.docx")
TARGET = Path(r"D:/Configure/Obsidian/my-pkb/AI尚硅谷/大模型应用实战/LangChain/06-LangChain使用之Agents.md")

from docx import Document
from docx.document import Document as _Document
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl


def iter_block_items(parent):
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise TypeError(type(parent))
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def norm(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\xa0", " ").replace("　", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def prettify(text):
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


def expand_text(text):
    text = prettify(text)
    if not text:
        return []
    if "工作流程示例：" in text and text != "工作流程示例：":
        head, tail = text.split("工作流程示例：", 1)
        result = []
        if head.strip():
            result.append(head.strip())
        result.append("工作流程示例：")
        if tail.strip():
            result.append(tail.strip())
        return result
    if re.search(r"\d+）", text) and text.count("）") > 1 and not re.match(r"^\d+[、.]", text):
        parts = [p.strip() for p in re.split(r"(?=\d+）)", text) if p.strip()]
        if parts:
            return parts
    return [text]


def heading_level(text, current_h3):
    if re.match(r"^第\d+章[:：]", text):
        return 1
    if re.match(r"^\d+、", text):
        if current_h3 == "1.5":
            return 4
        return 2
    if re.match(r"^\d+\.\d+\.\d+", text):
        return 4
    if re.match(r"^\d+\.\d+", text):
        return 3
    return None


def format_heading(text, level):
    if level == 1:
        return "# " + text.replace(":", "：", 1)
    if level == 2:
        m = re.match(r"^(\d+)、\s*(.+)$", text)
        return "## {}. {}".format(m.group(1), m.group(2))
    if level == 3:
        m = re.match(r"^(\d+\.\d+)\s*(.+)$", text)
        return "### {} {}".format(m.group(1), m.group(2))
    if re.match(r"^\d+、", text):
        m = re.match(r"^(\d+)、\s*(.+)$", text)
        return "#### {}）{}".format(m.group(1), m.group(2))
    m = re.match(r"^(\d+\.\d+\.\d+)\s*(.+)$", text)
    return "#### {} {}".format(m.group(1), m.group(2))


def is_code(text):
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
    if any(k in t for k in (".invoke(", ".run(", ".pull(", "Tool(", "StructuredTool(", "BaseTool(")):
        return True
    if t.startswith("{") and t.endswith("}"):
        return True
    return False


def clean_code(text):
    text = re.sub(r"^\d+\s+(?=(from|import|#|def|class|if|for|while|try:|except|return|print|os\.|prompt|tools|tool|search|llm|memory|agent|agent_executor|db|AgentType\.))", "", text)
    text = re.sub(r"^\d+\s*$", "", text).strip()
    text = re.sub(r"\s+\d+\s*$", "", text)
    return text.strip()


def split_workflow(text):
    text = text.replace("1第1步：", "第1步：").replace("1问题：", "问题：")
    text = re.sub(r"\s*(\d+)(?=(第\d+步：|问题：|思考：|行动：|观察：|最后：))", "\n", text)
    return [p.strip() for p in re.split(r"\n+", text) if p.strip()]


def emit_table(rows, out_lines):
    if not rows:
        return
    width = max(len(r) for r in rows)
    normalized = []
    for row in rows:
        padded = row + [""] * (width - len(row))
        normalized.append([prettify(cell).replace("|", "\\|") for cell in padded])
    out_lines.append("| " + " | ".join(normalized[0]) + " |")
    out_lines.append("| " + " | ".join(["---"] * width) + " |")
    for row in normalized[1:]:
        out_lines.append("| " + " | ".join(row) + " |")
    out_lines.append("")


doc = Document(str(DOCX))
out = []
in_code = False
current_h3 = None
last_was_list = False

for block in iter_block_items(doc):
    if isinstance(block, Table):
        if in_code:
            out.append("```")
            out.append("")
            in_code = False
        table_rows = []
        for row in block.rows:
            cells = [norm(cell.text) for cell in row.cells]
            if any(cells):
                table_rows.append(cells)
        emit_table(table_rows, out)
        last_was_list = False
        continue

    parts = expand_text(block.text)
    if not parts:
        if in_code:
            out.append("```")
            out.append("")
            in_code = False
        if out and out[-1] != "":
            out.append("")
        last_was_list = False
        continue

    for text in parts:
        level = heading_level(text, current_h3)
        if level:
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            out.append(format_heading(text, level))
            out.append("")
            last_was_list = False
            if level == 3:
                m = re.match(r"^(\d+\.\d+)", text)
                current_h3 = m.group(1) if m else None
            continue

        if text in ("讲师：尚硅谷-宋红康", "官网：尚硅谷"):
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            out.append("> " + text)
            out.append("")
            last_was_list = False
            continue

        if text in ("如何拆解任务", "需要调用哪些工具", "以什么顺序调用", "如何利用好中间结果推进任务"):
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            out.append("- " + text)
            last_was_list = True
            continue

        if re.match(r"^\d+）", text):
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            out.append("- " + text)
            last_was_list = True
            continue

        if text.startswith(("比如：", "例如：")) and last_was_list:
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            out.append("  " + text)
            continue

        if text.startswith(("举例1：", "举例2：", "案例1：", "案例2：", "案例3：", "案例4：")):
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            out.append("- " + text)
            out.append("")
            last_was_list = True
            continue

        if text.startswith(("问题：", "需求：", "API说明：", "TAVILY_API_KEY申请：")):
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            out.append("> " + text)
            out.append("")
            last_was_list = False
            continue

        if text in ("特点：", "优点：", "缺点：", "代码片段：", "工作流程示例：", "具体使用步骤：", "小结："):
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            out.append("**" + text + "**")
            out.append("")
            last_was_list = False
            continue

        if text.startswith(("传统方式：", "通用方式：", "方式1：", "方式2：")):
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            text = text.replace("initialize_agent()", "`initialize_agent()`")
            text = text.replace("AgentExecutor构造方法", "`AgentExecutor()` 构造方法")
            out.append("#### " + text)
            out.append("")
            last_was_list = False
            continue

        if text.startswith(("环节1：", "环节2：")):
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            out.append("- " + text)
            last_was_list = True
            continue

        if "第1步：" in text or ("问题：" in text and any(k in text for k in ["思考：", "行动：", "观察：", "最后："])):
            if in_code:
                out.append("```")
                out.append("")
                in_code = False
            for item in split_workflow(text):
                out.append("- " + item)
            out.append("")
            last_was_list = True
            continue

        if is_code(text):
            code = clean_code(text)
            if code:
                if not in_code:
                    out.append("```python")
                    in_code = True
                out.append(code)
            last_was_list = False
            continue

        if in_code:
            out.append("```")
            out.append("")
            in_code = False
        out.append(text)
        out.append("")
        last_was_list = False

if in_code:
    out.append("```")
    out.append("")

text = "\n".join(out)
text = text.replace("# 第06章:LangChain使用之 Agents", "# 第06章：LangChain使用之 Agents")
text = text.replace("讲师:尚硅谷-宋红康", "讲师：尚硅谷-宋红康")
text = text.replace("官网:尚硅谷", "官网：尚硅谷")
text = text.replace("Agent(智能体)", "Agent（智能体）")
text = text.replace("(AGI)", "（AGI）")
text = text.replace("(LLM)", "（LLM）")
text = text.replace("(Tools)", "（Tools）")
text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

TARGET.write_text(text, encoding="utf-8")
print(TARGET)
print("LINES=" + str(len(text.splitlines())))
