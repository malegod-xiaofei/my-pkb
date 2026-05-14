
# My PKB（个人知识库）

这是一个基于 Obsidian 搭建的个人知识库仓库，用于沉淀 AI 大模型、Java 后端、大数据生态等方向的学习笔记、课程整理、工具实践与面试复习资料。

说明：本 README 基于仓库目录与文章文件名整理，不包含笔记正文摘要。

## 仓库定位

当前仓库主要用于保存个人技术学习资料，内容以尚硅谷课程笔记、开发工具使用记录、技术栈知识点、常用操作、源码解析、实战案例与面试题为主。

核心方向包括：

- AI 大模型：学习路线、通识课、应用实战、核心技术、RAG 与智能体
- Java：Java 基础、集合、多线程、设计模式、MySQL、JavaWeb、SSM、SpringBoot、开发工具与 Linux/Git
- 大数据：Hadoop、HDFS、MapReduce、Yarn、Zookeeper、Hive、Kafka、Spark、Flink、ClickHouse、Doris 等

## 内容概览

| 一级目录 | Markdown 数量 | 说明 |
|---|---:|---|
| AI尚硅谷/ | 72 | AI 大模型学习路线、通识基础、应用实战、核心技术、RAG 与智能体 |
| Java/ | 57 | Java 基础、数据结构、设计模式、MySQL、JavaWeb、IDEA、Git、Linux 等 |
| 大数据/ | 88 | Hadoop 生态、Hive、Kafka、Spark、Flink、OLAP 引擎和监控组件 |

## 目录结构

~~~text
my-pkb/
├── AI尚硅谷/
│   ├── AI大模型学习路线图/             # AI 大模型学习路线与应用路线
│   ├── 大模型通识课/
│   │   └── Python基础/                # Python 基础、HanLP、面试题等
│   ├── 大模型应用实战/
│   │   ├── LangChain/                 # LangChain Model IO、Chains、Memory、Tools、Agents、Retrieval
│   │   ├── conda使用指南/              # conda 使用指南
│   │   ├── 硅谷小智（医疗版）/          # Java + 大模型医疗项目笔记
│   │   ├── ClaudeCode/                # Claude Code 使用笔记
│   │   ├── MCP/                       # MCP 课程实战与官方文档整理
│   │   └── Ollama/                    # Ollama 本地模型使用
│   ├── 大模型核心技术/
│   │   ├── 尚硅谷AI大模型之机器学习/    # 数学基础、机器学习章节笔记与原始整合文件
│   │   ├── 尚硅谷AI大模型之深度学习/    # 深度学习章节笔记与原始整合文件
│   │   └── 尚硅谷AI大模型之NLP教程/     # NLP 章节笔记与原始整合文件
│   └── RAG与智能体/
│       ├── RAG/                       # RAG 入门、向量化、向量数据库、系统搭建与优化
│       └── Dify/                      # Dify 搭建、案例与功能
├── Java/
│   ├── 00 数据结构/                    # 知识点、排序算法
│   ├── 01 Java基础/                    # JavaSE、基础知识、集合、Java 8、多线程、时间处理、PDF
│   ├── 02 设计模式/                    # 动态代理、单例、装饰者、建造者
│   ├── 03 MySQL/                       # 环境搭建、基础知识、优化方法、实战知识
│   ├── 04 JavaWeb/                     # 前端、JavaWeb、SSM、SpringBoot
│   ├── 05 正则表达式/                  # 常用字符、基础知识、入门教程
│   ├── 06 IDEA/                        # IDEA 配置、插件、Database、快捷键、Maven、Debug、Chrome
│   ├── 07 PyCharm/                     # PyCharm、Anaconda、Jupyter
│   ├── 08 Git/                         # Git 基础、IDEA 集成、合并 push、提交日志
│   └── 09 Linux/                       # Linux 环境、shell 命令、快捷键、脚本编程
├── 大数据/
│   ├── 01 Hadoop/                      # Hadoop、环境搭建、集群、调优、迁移、源码、面试题
│   ├── 02 HDFS/                        # HDFS 知识点、命令、面试题
│   ├── 03 MapReduce/                   # MapReduce 知识点、常用内容、面试题
│   ├── 04 Yarn/                        # Yarn 知识点、命令、面试题
│   ├── 05 Zookeeper/                   # 知识点、源码、面试题
│   ├── 06 Hadoop_高可用/               # Hadoop 高可用知识点
│   ├── 07 Hive/                        # Hive 基础/进阶/高级、SQL 题库、函数、源码、部署、面试题
│   ├── 08 Flume/                       # Flume 知识点、面试题
│   ├── 09 Kafka/                       # Kafka 基础/进阶、流程图解、常用操作、面试题
│   ├── 10 Hbase/                       # HBase 知识点与常用操作
│   ├── 11 Scala/                       # Scala 基础/进阶、环境搭建、常用知识、面试题
│   ├── 12 Spark/                       # Spark 入门、Java/Scala 知识点、算子、内核、优化、面试题
│   ├── 13 SparkSql/                    # SparkSQL Java/Scala 知识点、常用知识、面试题
│   ├── 14 SparkStreaming/              # SparkStreaming Java/Scala 知识点、面试题
│   ├── 15 Flink/                       # Flink 分章知识点、FlinkSQL、环境、实时数仓、面试题
│   ├── 16 AZKaBan/                     # Azkaban 知识点、常用知识
│   ├── 17 Prometheus/                  # Prometheus、Grafana、睿象云监控
│   ├── 18 StarRocks/                   # StarRocks 知识点
│   ├── 19 ClickHouse/                  # ClickHouse 入门、高级、监控及备份
│   └── 20 Doris/                       # Doris 知识点与实战
├── .claude/
│   └── CLAUDE.md                       # Claude Code 项目说明
└── README.md
~~~

## 详细目录

### AI尚硅谷

#### AI 大模型学习路线图

- AI大模型学习路线图.md
- 大模型应用路线图.md

#### 大模型通识课 / Python 基础

- 01_知识点.md
- 02_基础操作.md
- 03_HanLP词性标注.md
- 99_面试题.md
- Python-在不同对象中使用 in 操作符的查找效率_python中,in()效率-CSDN博客.md

#### 大模型应用实战

- LangChain/：01-LangChain使用概述.md ~ 07-LangChain使用之Retrieval.md
- conda使用指南/：尚硅谷-conda使用指南.md
- 硅谷小智（医疗版）/：尚硅谷-Java+大模型应用-硅谷小智（医疗版）.md
- ClaudeCode/：AI工具飞速上手之Claude Code.md
- MCP/：01-MCP实战指南.md ~ 05-Cherry Studio中使用MCP案例.md，以及 c-01-MCP入门.md ~ c-07-Open-WebUI接入MCP.md
- Ollama/：Ollama使用.md

#### 大模型核心技术

- 尚硅谷AI大模型之机器学习/
  - 原始整合文件：尚硅谷大模型技术之数学基础.md、尚硅谷大模型技术之机器学习.md
  - 拆分章节：数学基础 1 高等数学.md ~ 数学基础 3 概率论.md
  - 拆分章节：机器学习 1 机器学习概述.md ~ 机器学习 8 无监督学习.md
- 尚硅谷AI大模型之深度学习/
  - 原始整合文件：尚硅谷大模型技术之深度学习.md
  - 拆分章节：1 深度学习概述.md ~ 9 循环神经网络.md
- 尚硅谷AI大模型之NLP教程/
  - 原始整合文件：尚硅谷大模型技术之NLP.md
  - 拆分章节：1 NLP导论.md ~ 9 附录.md

#### RAG 与智能体

- RAG/：01-RAG入门.md ~ 06-Weaviate向量数据库.md
- Dify/：01-Dify特点和搭建.md、02-Dify案例.md、03-Dify功能.md

### Java

- 00 数据结构/：数据结构知识点、排序算法
- 01 Java基础/：JavaSE、基础知识、集合、Java 8 新特性、多线程、时间处理、PDF
- 02 设计模式/：动态代理、单例、装饰者、建造者
- 03 MySQL/：环境搭建、基础知识、优化方法、实战知识
- 04 JavaWeb/：前端、JavaWeb、SSM、SpringBoot
- 05 正则表达式/：常用字符、基础知识、入门教程
- 06 IDEA/：IDEA 配置、环境搭建、插件、Database、快捷键、Maven、Debug、Chrome
- 07 PyCharm/：PyCharm 环境、Anaconda、Jupyter
- 08 Git/：Git 基础、IDEA 集成、常用知识、合并 push、提交日志
- 09 Linux/：Linux 环境、知识点、shell 命令、快捷键、脚本编程

### 大数据

- 01 Hadoop/：Hadoop、Windows/虚拟机环境、集群搭建、知识点、命令、调优、迁移、源码、面试题
- 02 HDFS/：知识点、常用 Shell 命令、HDFS、面试题
- 03 MapReduce/：知识点、常用内容、面试题
- 04 Yarn/：Yarn、知识点、常用 Shell 命令、面试题
- 05 Zookeeper/：知识点、源码解析、面试题
- 06 Hadoop_高可用/：高可用知识点
- 07 Hive/：Hive、分章知识点、SQL 题库、函数、SQL 面试题、源码、Hive on Spark、内外表
- 08 Flume/：知识点、面试题
- 09 Kafka/：基础/进阶知识点、流程图解、常用操作、面试题
- 10 Hbase/：知识点、常用操作
- 11 Scala/：基础/进阶知识点、环境搭建、常用知识、面试题
- 12 Spark/：Spark 入门、Java/Scala 知识点、常用算子、内核、优化、流程图解、面试题
- 13 SparkSql/：Java/Scala 知识点、常用知识、面试题
- 14 SparkStreaming/：Java/Scala 知识点、面试题
- 15 Flink/：分章知识点、FlinkSQL、环境搭建、常用知识、Flink + DataHub、实时数仓、面试题
- 16 AZKaBan/：知识点、常用知识
- 17 Prometheus/：Prometheus、Grafana、睿象云监控
- 18 StarRocks/：知识点
- 19 ClickHouse/：入门、高级、监控及备份
- 20 Doris/：知识点、实战

## 笔记规范

- 笔记格式为 Markdown，在 Obsidian 中编辑与阅读
- 文件名以中文主题名、数字序号或“前缀 + 序号 + 章节名”为主
- 图片资源放在对应主题目录的 images/ 子目录中；机器学习算法图保留在 机器学习算法图/
- 课件原文件 .docx 不纳入版本管理
- Markdown 正文中涉及 HTML 特殊标记时，建议使用反引号包裹，避免 Obsidian 渲染异常

## 使用方式

- 使用 Obsidian 打开仓库根目录 my-pkb
- 按一级目录选择学习方向：AI尚硅谷/、Java/、大数据/
- 按课程、技术栈或章节编号浏览笔记
- 配合 Git 管理知识库的持续迭代

## Git 同步说明

仓库已忽略以下类型文件，以减少无意义变更：

- .obsidian/workspace.json、.obsidian/workspace-mobile.json：Obsidian 本地工作区状态
- *.docx：课件原文件体积大，无需版本管理
- .claude/settings.local.json：本地权限配置
- .claude/*.py、.claude/agents_*.md、.claude/agents_*.txt、.claude/structure_*.txt：临时脚本与中间产物

## 说明

- 本仓库是个人学习型知识库，内容会持续补充与调整
- README 用于概览当前主干内容，不替代具体笔记正文
