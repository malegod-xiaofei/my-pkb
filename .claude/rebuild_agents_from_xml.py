from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import re
import unicodedata

DOCX = Path(r"D:/Configure/Obsidian/my-pkb/AI尚硅谷/大模型应用实战/LangChain/06-LangChain使用之Agents.docx")
TARGET = Path(r"D:/Configure/Obsidian/my-pkb/AI尚硅谷/大模型应用实战/LangChain/06-LangChain使用之Agents.md")
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def local_name(tag):
    return tag.rsplit("}", 1)[-1]


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
        "讲师:": "讲师：",
        "官网:": "官网：",
        "问题:": "问题：",
        "需求:": "需求：",
        "特点:": "特点：",
        "优点:": "优点：",
        "缺点:": "缺点：",
        "代码片段:": "代码片段：",
        "工作流程示例:": "工作流程示例：",
        "具体使用步骤:": "具体使用步骤：",
        "小结:": "小结：",
        "API说明:": "API说明：",
        "TAVILY_API_KEY申请:": "TAVILY_API_KEY申请：",
        "方式1:": "方式1：",
        "方式2:": "方式2：",
        "传统方式:": "传统方式：",
        "通用方式:": "通用方式：",
        "AgentExecutor构造方法": "AgentExecutor 构造方法",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\[(.+?)\]\[(https?://[^\]]+)\]", r"\1：<\2>", text)
    return text


def paragraph_text(p):
    parts = []
    for node in p.iter():
        name = local_name(node.tag)
        if name == "t":
            parts.append(node.text or "")
        elif name in ("br", "cr"):
            parts.append("\n")
        elif name == "tab":
            parts.append(" ")
    return prettify("".join(parts))


def table_rows(tbl):
    rows = []
    for tr in tbl.findall("./w:tr", NS):
        row = []
        for tc in tr.findall("./w:tc", NS):
            paras = []
            for p in tc.findall("./w:p", NS):
                t = paragraph_text(p)
                if t and not re.fullmatch(r"\d+", t):
                    paras.append(t)
            row.append("<br>".join(paras).strip())
        if any(cell for cell in row):
            rows.append(row)
    return rows


def split_enumerated_line(text):
    if re.search(r"\d+[）)]", text) and text.count("）") + text.count(")") > 1 and not re.match(r"^\d+[、.]", text):
        parts = [p.strip() for p in re.split(r"(?=\d+[）)])", text) if p.strip()]
        if parts:
            return parts
    return [text]


def is_heading(text, current_h3):
    if re.match(r"^第\d+章[:：]", text):
        return 1
    if re.match(r"^\d+、", text):
        return 4 if current_h3 == "1.5" else 2
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
        return "## {}. {}".format(m.group(1), m.group(2)) if m else "## " + text
    if level == 3:
        m = re.match(r"^(\d+\.\d+)\s*(.+)$", text)
        return "### {} {}".format(m.group(1), m.group(2)) if m else "### " + text
    if level == 4:
        m = re.match(r"^(\d+)、\s*(.+)$", text)
        if m:
            return "#### {}）{}".format(m.group(1), m.group(2))
        m = re.match(r"^(\d+\.\d+\.\d+)\s*(.+)$", text)
        if m:
            return "#### {} {}".format(m.group(1), m.group(2))
    return "#### " + text


def is_code(text):
    t = re.sub(r"^\d+\s+", "", text).strip()
    if not t or re.fullmatch(r"\d+", t):
        return False
    if set(t) <= set("=.-_/"):
        return False
    starters = (
        "from ", "import ", "#", "def ", "class ", "if ", "for ", "while ",
        "try:", "except ", "return ", "print(", "os.environ", "prompt =",
        "tools =", "tool =", "search =", "llm =", "memory =", "agent =",
        "agent_executor", "db =", "initialize_agent(", "AgentExecutor(",
        "create_", "ChatOpenAI(", "TavilySearchResults(", "PythonREPLTool(",
        "DuckDuckGoSearchRun(", "SerpAPIWrapper(", "load_tools(", "@tool", "pip install"
    )
    if t.startswith(starters) or t.startswith("AgentType."):
        return True
    if any(k in t for k in (".invoke(", ".run(", ".pull(", "Tool(", "StructuredTool(", "BaseTool(")):
        return True
    if t.startswith("{") and t.endswith("}"):
        return True
    if "=" in t and any(ch in t for ch in "()[]{}\""):
        return True
    return False


def clean_code(text):
    text = re.sub(r"^\d+\s+(?=(from|import|#|def|class|if|for|while|try:|except|return|print|os\.|prompt|tools|tool|search|llm|memory|agent|agent_executor|db|AgentType\.))", "", text)
    text = re.sub(r"^\d+\s*$", "", text).strip()
    text = re.sub(r"\s+\d+\s*$", "", text)
    return text.strip()


def split_workflow(text):
    text = text.replace("1第1步：", "第1步：").replace("1问题：", "问题：")
    labels = r"(第\d+步：|问题：|思考：|行动：|观察：|最后：)"
    text = re.sub(r"\b\d+\b\s*(?=" + labels + r")", "\n", text)
    text = re.sub(r"\s+(?=" + labels + r")", "\n", text)
    parts = []
    for frag in re.split(r"\n+", text):
        frag = frag.strip()
        frag = re.sub(r"^\d+\s+", "", frag)
        frag = re.sub(r"\s+\d+\s*$", "", frag)
        if frag:
            parts.append(frag)
    return parts


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


with ZipFile(DOCX) as z:
    root = ET.fromstring(z.read("word/document.xml"))

body = root.find("w:body", NS)
out = []
para = []
in_code = False
current_h3 = None
last_numbered = False


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


for child in body:
    name = local_name(child.tag)

    if name == "tbl":
        flush_para()
        close_code()
        emit_table(table_rows(child), out)
        last_numbered = False
        continue

    if name != "p":
        continue

    text = paragraph_text(child)
    if not text or re.fullmatch(r"\d+", text) or set(text) <= set("=.-_/"):
        flush_para()
        close_code()
        last_numbered = False
        continue

    parts = []
    for part in split_enumerated_line(text):
        if part:
            parts.append(part)

    for text in parts:
        if not text or re.fullmatch(r"\d+", text) or set(text) <= set("=.-_/"):
            continue

        level = is_heading(text, current_h3)
        if level:
            flush_para()
            close_code()
            out.append(format_heading(text, level))
            out.append("")
            if level == 3:
                m = re.match(r"^(\d+\.\d+)", text)
                current_h3 = m.group(1) if m else None
            last_numbered = False
            continue

        if text in ("讲师：尚硅谷-宋红康", "官网：尚硅谷"):
            flush_para()
            close_code()
            out.append("> " + text)
            out.append("")
            last_numbered = False
            continue

        if text in ("如何拆解任务", "需要调用哪些工具", "以什么顺序调用", "如何利用好中间结果推进任务"):
            flush_para()
            close_code()
            out.append("- " + text)
            last_numbered = False
            continue

        m = re.match(r"^(\d+)[）)]\s*(.+)$", text)
        if m:
            flush_para()
            close_code()
            body_text = m.group(2).strip()
            if "比如：" in body_text:
                main, example = body_text.split("比如：", 1)
                out.append("{}. {}".format(m.group(1), main.strip()))
                out.append("   例如：" + example.strip())
            else:
                out.append("{}. {}".format(m.group(1), body_text))
            out.append("")
            last_numbered = True
            continue

        if text.startswith("比如：") and last_numbered:
            flush_para()
            close_code()
            out.append("   例如：" + text[3:].strip())
            out.append("")
            continue

        m = re.match(r"^(\d+)\s+(.+)$", text)
        if m and not is_code(text):
            flush_para()
            close_code()
            out.append("{}. {}".format(m.group(1), m.group(2).strip()))
            out.append("")
            last_numbered = False
            continue

        m = re.match(r"^举例(\d+)：\s*(.+)$", text)
        if m:
            flush_para()
            close_code()
            out.append("- 举例 {}：{}".format(m.group(1), m.group(2).strip()))
            out.append("")
            last_numbered = False
            continue

        m = re.match(r"^案例(\d+)：\s*(.+)$", text)
        if m:
            flush_para()
            close_code()
            out.append("#### 案例 {}：{}".format(m.group(1), m.group(2).strip()))
            out.append("")
            last_numbered = False
            continue

        if text.startswith(("问题：", "需求：", "API说明：", "TAVILY_API_KEY申请：")):
            flush_para()
            close_code()
            out.append("> " + text)
            out.append("")
            last_numbered = False
            continue

        if text in ("特点：", "优点：", "缺点：", "代码片段：", "工作流程示例：", "具体使用步骤：", "小结："):
            flush_para()
            close_code()
            out.append("**" + text + "**")
            out.append("")
            last_numbered = False
            continue

        if text.startswith(("方式1：", "方式2：")):
            flush_para()
            close_code()
            num = re.match(r"^方式(\d+)：\s*(.+)$", text)
            if num:
                out.append("#### 方式 {}：{}".format(num.group(1), num.group(2)))
            else:
                out.append("#### " + text)
            out.append("")
            last_numbered = False
            continue

        if text.startswith(("传统方式：", "通用方式：")):
            flush_para()
            close_code()
            out.append("#### " + text.replace("initialize_agent()", "`initialize_agent()`"))
            out.append("")
            last_numbered = False
            continue

        if text.startswith(("环节1：", "环节2：")):
            flush_para()
            close_code()
            out.append("- " + text)
            last_numbered = False
            continue

        if text.endswith("对比表"):
            flush_para()
            close_code()
            out.append("**" + text + "**")
            out.append("")
            last_numbered = False
            continue

        if "第1步：" in text or ("问题：" in text and any(k in text for k in ["思考：", "行动：", "观察：", "最后："])):
            flush_para()
            close_code()
            for item in split_workflow(text):
                if item and not re.fullmatch(r"\d+", item):
                    out.append("- " + item)
            out.append("")
            last_numbered = False
            continue

        if is_code(text):
            flush_para()
            code = clean_code(text)
            if code and not re.fullmatch(r"\d+", code):
                if not in_code:
                    out.append("```python")
                    in_code = True
                out.append(code)
            last_numbered = False
            continue

        close_code()
        para.append(text)
        last_numbered = False

flush_para()
close_code()

text = "\n".join(out)
text = text.replace("# 第06章:LangChain使用之 Agents", "# 第06章：LangChain使用之 Agents")
text = text.replace("讲师:尚硅谷-宋红康", "讲师：尚硅谷-宋红康")
text = text.replace("官网:尚硅谷", "官网：尚硅谷")
text = text.replace("Agent(智能体)", "Agent（智能体）")
text = text.replace("(AGI)", "（AGI）")
text = text.replace("(LLM)", "（LLM）")
text = text.replace("(Tools)", "（Tools）")
text = text.replace("在Chain中", "在 Chain 中")
text = text.replace("而Agent", "而 Agent")
text = text.replace("在LangChain中", "在 LangChain 中")
text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

TARGET.write_text(text, encoding="utf-8")
print(TARGET)
print("LINES=" + str(len(text.splitlines())))
