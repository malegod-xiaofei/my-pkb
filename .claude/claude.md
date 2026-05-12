# my-pkb 项目说明

## 项目概述

这是一个基于 Obsidian 的个人知识库（PKB），用于整理和沉淀 AI 大模型相关学习笔记。
远程仓库：`git@github.com:malegod-xiaofei/my-pkb.git`

## 目录结构

```
my-pkb/
├── AI尚硅谷/
│   ├── 大模型应用实战/
│   │   ├── LangChain/          # LangChain 系列笔记（01~07章）
│   │   ├── conda使用指南/
│   │   └── 硅谷小智（医疗版）/
│   └── 大模型核心技术/
│       ├── 尚硅谷AI大模型之机器学习/
│       ├── 尚硅谷AI大模型之深度学习/
│       └── 尚硅谷AI大模型之NLP教程/
├── .claude/
│   ├── claude.md               # 本文件，项目说明（纳入 git 跟踪）
│   └── settings.local.json     # 本地权限配置（已 gitignore）
└── README.md
```

## 笔记规范

- 笔记格式为 Markdown，在 Obsidian 中编辑
- 文件名使用中文，格式：`章节序号-章节名.md`（如 `02-LangChain使用之Model IO.md`）
- 课件原文件为 `.docx`，已在 `.gitignore` 中忽略，不上传 git

## Git 工作流

- 主分支：`master`
- 推送方式：SSH（`git@github.com`）
- 提交粒度：按笔记章节或主题提交，commit message 使用中文描述

## .gitignore 规则说明

| 规则 | 原因 |
|------|------|
| `*.docx` | 课件原文件体积大，无需版本管理 |
| `.obsidian/workspace.json` | Obsidian 本地工作区状态，不同设备各异 |
| `.claude/settings.local.json` | 含本地权限配置和 SSH 路径 |
| `.claude/*.py` | 一次性处理脚本，用后即废 |
| `.claude/agents_*.md` / `.txt` | 临时中间产物 |

## 注意事项

- `.claude/claude.md`（本文件）已纳入 git 跟踪，修改后需提交
- 新增临时脚本或草稿文件时，及时加入 `.gitignore`
