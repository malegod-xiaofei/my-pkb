
# my-pkb 项目说明

这是一个基于 Obsidian 的个人知识库（PKB），用于整理和沉淀 AI 大模型、Java 后端、大数据与开发工具方向的学习笔记。
远程仓库：git@github.com:malegod-xiaofei/my-pkb.git

## 重要工作原则

- 这是个人知识库，不是应用代码仓库；默认以整理 Markdown 笔记、目录结构和说明文档为主
- 用户要求"阅读文章目录"时，只读取文件名和目录结构，不读取正文内容
- 避免无意义改写笔记正文；除非用户明确要求，否则不要批量重构 Markdown 内容
- 更新 README、项目说明或目录索引时，应优先基于当前文件树，而不是凭旧印象

## 仓库定位

当前仓库主要用于保存个人技术学习资料，内容以尚硅谷/黑马课程笔记、开发工具使用记录、技术栈知识点、常用操作、源码解析、实战案例与面试题为主。

核心方向包括：

- AI 大模型（尚硅谷）：学习路线、通识课、应用实战、核心技术、RAG 与智能体
- AI 大模型（黑马）：Python 高级、数据结构算法、Linux、传智项目文档
- Java生态：Java 基础、集合、多线程、设计模式、MySQL、JavaWeb、SSM、SpringBoot
- 大数据生态：Hadoop、HDFS、MapReduce、Yarn、Zookeeper、Hive、Kafka、Spark、Flink、ClickHouse、Doris 等
- 开发工具：Obsidian、IDEA、PyCharm、Git、Linux、Docker、Jenkins/GitLab/CCE

## 目录结构

~~~text
my-pkb/
├── AI尚硅谷/
│   ├── 01 AI大模型学习路线图/          # AI 大模型学习路线与应用路线
│   ├── 02 大模型通识课/
│   │   └── 01 Python基础/             # Python 基础、HanLP、面试题等
│   ├── 03 RAG与智能体/
│   │   ├── 01 RAG/                    # RAG 入门、向量化、向量数据库、系统搭建与优化
│   │   └── 02 Dify/                   # Dify 搭建、案例与功能
│   ├── 04 大模型核心技术/
│   │   ├── 01 尚硅谷AI大模型之机器学习/ # 数学基础、机器学习章节笔记与原始整合文件
│   │   ├── 02 尚硅谷AI大模型之深度学习/ # 深度学习章节笔记与原始整合文件
│   │   └── 03 尚硅谷AI大模型之NLP教程/  # NLP 章节笔记与原始整合文件
│   └── 05 大模型应用实战/
│       ├── 01 conda使用指南/           # conda 使用指南
│       ├── 02 Ollama/                  # Ollama 本地模型使用
│       ├── 03 MCP/                     # MCP 课程实战与官方文档整理
│       ├── 04 ClaudeCode/              # Claude Code 使用笔记（3 个文件）
│       ├── 05 LangChain/               # LangChain Model IO、Chains、Memory、Tools、Agents、Retrieval
│       └── 06 硅谷小智（医疗版）/       # Java + 大模型医疗项目笔记
├── AI黑马/
│   ├── 01 基础知识/
│   │   ├── 01 Python高级/              # 多任务、网络编程、闭包、高级语法等
│   │   ├── 02 数据结构与算法（Python）/ # 顺序表、链表、栈、队列、排序、树
│   │   └── 03 Linux/                   # Linux 基础命令与高级命令
│   └── 传智项目文档/                   # NLP 案例、多模态、推荐系统、模型优化等
├── Java生态/
│   ├── 00 数据结构/                    # 知识点、排序算法
│   ├── 01 Java基础/                    # JavaSE、基础知识、集合、Java 8、多线程、时间处理
│   ├── 02 设计模式/                    # 动态代理、单例、装饰者、建造者
│   ├── 03 MySQL/                       # 环境搭建、基础知识、优化方法、实战知识
│   ├── 04 JavaWeb/                     # 前端、JavaWeb、SSM、SpringBoot
│   └── 05 正则表达式/                  # 常用字符、基础知识、入门教程
├── 大数据生态/
│   ├── 01 Hadoop/  02 HDFS/  03 MapReduce/  04 Yarn/  05 Zookeeper/
│   ├── 06 Hadoop_高可用/  07 Hive/  08 Flume/  09 Kafka/  10 Hbase/
│   ├── 11 Scala/  12 Spark/  13 SparkSql/  14 SparkStreaming/  15 Flink/
│   └── 16 AZKaBan/  17 Prometheus/  18 StarRocks/  19 ClickHouse/  20 Doris/
├── 开发工具/
│   ├── 00 Obsidian/                    # 环境配置、Markdown 语法
│   ├── 01 IDEA/                        # 配置、插件、Maven、Debug、快捷键
│   ├── 02 PyCharm/                     # 环境搭建、Anaconda、Jupyter
│   ├── 03 Git/                         # 基础知识、IDEA 集成、常用知识
│   ├── 04 Linux/                       # 环境、知识点、shell 命令、脚本编程
│   ├── 05 Docker/                      # 安装、常用命令、镜像、网络、Compose
│   └── 06 Gitlab+Jenkins+CCE云整套环境搭建/  # CI/CD 全链路环境搭建
├── .claude/
│   └── CLAUDE.md                       # Claude Code 项目说明
└── README.md
~~~

## 笔记规范

- 笔记格式为 Markdown，在 Obsidian 中编辑与阅读
- 文件名以中文主题名、数字序号或"前缀 + 序号 + 章节名"为主
- 图片资源放在对应主题目录的 images/ 子目录中；机器学习算法图保留在 机器学习算法图/
- 课件原文件 .docx 不纳入版本管理
- Markdown 正文中涉及 HTML 特殊标记时，建议使用反引号包裹，避免 Obsidian 渲染异常

## Git 同步说明

仓库已忽略以下类型文件，以减少无意义变更：

- .obsidian/workspace.json、.obsidian/workspace-mobile.json：Obsidian 本地工作区状态
- *.docx：课件原文件体积大，无需版本管理
- .claude/settings.local.json：本地权限配置
- .claude/*.py、.claude/agents_*.md、.claude/agents_*.txt、.claude/structure_*.txt：临时脚本与中间产物

## 说明

- 本仓库是个人学习型知识库，内容会持续补充与调整
- README 用于概览当前主干内容，不替代具体笔记正文
