
# My PKB（个人知识库）

这是一个基于 Obsidian 搭建的个人知识库仓库，用于沉淀 AI 大模型、Java 后端、大数据生态、开发工具等方向的学习笔记、课程整理、工具实践与面试复习资料。

说明：本 README 基于仓库目录与文章文件名整理，不包含笔记正文摘要。

## 仓库定位

当前仓库主要用于保存个人技术学习资料，内容以尚硅谷/黑马课程笔记、开发工具使用记录、技术栈知识点、常用操作、源码解析、实战案例与面试题为主。

核心方向包括：

- AI 大模型（尚硅谷）：学习路线、通识课、核心技术、RAG 与智能体、应用实战（LangChain、MCP、Claude Code、Spring AI、Spring AI Alibaba、Cursor、企业级部署、共享充电宝项目）
- AI 大模型（黑马）：Python 高级、数据结构算法、Linux、机器学习基础（科学计算库）、机器学习算法（经典算法）、深度学习（TensorFlow）、计算机视觉（OpenCV）、NLP、文本摘要、传智项目文档
- Java生态：Java 基础、集合、多线程、设计模式、MySQL、JavaWeb、SSM、SpringBoot
- 大数据生态：Hadoop、HDFS、MapReduce、Yarn、Zookeeper、Hive、Kafka、Spark、Flink、ClickHouse、Doris 等
- 开发工具：Obsidian、IDEA、PyCharm、Git、Linux、Docker、Jenkins/GitLab/CCE

## 内容概览

| 一级目录 | Markdown 数量 | 说明 |
|---|---:|---|
| AI尚硅谷/ | ~95 | AI 大模型学习路线、通识基础、核心技术、RAG 与智能体、应用实战（MCP、LangChain、Spring AI、Cursor、企业级部署、项目实战） |
| AI黑马/ | ~385 | Python 高级、数据结构算法、Linux、机器学习（科学计算库+经典算法）、深度学习（TensorFlow）、计算机视觉（OpenCV）、NLP、文本摘要、传智项目文档 |
| Java生态/ | ~35 | Java 基础、数据结构、设计模式、MySQL、JavaWeb、正则表达式 |
| 大数据生态/ | ~88 | Hadoop 生态、Hive、Kafka、Spark、Flink、OLAP 引擎和监控组件 |
| 开发工具/ | ~50 | IDEA、PyCharm、Git、Linux、Docker、Jenkins/GitLab/CCE 等 |

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
│   ├── 05 大模型应用实战/
│       ├── 01 conda使用指南/           # conda 使用指南
│       ├── 02 Ollama/                  # Ollama 本地模型使用
│       ├── 03 MCP/                     # MCP 课程实战与官方文档整理
│       ├── 04 ClaudeCode/              # Claude Code 使用笔记
│       ├── 05 LangChain/               # LangChain Model IO、Chains、Memory、Tools、Agents、Retrieval
│       ├── 06 硅谷小智（医疗版）/       # Java + 大模型医疗项目笔记
│       ├── 07 小谷充电宝/              # 共享充电宝项目：设备、柜机、规则、微信登录、MQTT、RabbitMQ、扫码、归还、支付、AI 报表
│       ├── 08 SpringAI/                # Spring AI 课程笔记
│       ├── 09 Cursor/                  # Cursor 快速上手和科学使用指南
│       ├── 10 企业级大规模部署与开发实战/ # 企业级大模型部署、Agent 与 RAG 实战项目
│       └── 11 Spring AI Alibaba/       # Spring AI Alibaba 速通实战
│   └── 06 面试题/                      # 机器学习、深度学习、NLP、大模型、RAG、Agent、Spring AI、部署等面试题
├── AI黑马/
│   ├── 01 基础知识/
│   │   ├── 01 Python高级/              # 多任务编程、网络编程、闭包、高级语法与正则
│   │   ├── 02 数据结构与算法（Python）/ # 顺序表、链表、栈、队列、排序与搜索、树
│   │   └── 03 Linux/                   # Linux 基础命令与高级命令
│   ├── 02 机器学习基础_科学计算库/      # Matplotlib、Numpy、Pandas、Seaborn、综合案例
│   ├── 03 机器学习算法_经典算法/        # KNN、线性回归、逻辑回归、决策树、集成学习、聚类、朴素贝叶斯、SVM、EM、HMM
│   ├── 04 深度学习入门_tensorflow/      # TensorFlow 入门、深度神经网络、图像分类、目标检测、目标分割
│   ├── 04.5 计算机视觉_OpenCV/          # OpenCV 简介、基本操作、图像处理、特征提取、视频操作
│   ├── 05 NLP文档/                      # PyTorch、NLP 入门、文本预处理、RNN、NLP 项目、Transformer、FastText、迁移学习
│   ├── 06 文本摘要(HTML)/               # TextRank、seq2seq、PGN、评估方法、迭代优化、部署
│   ├── 07 面试题/                       # Python、数据结构、科学计算库、机器学习、深度学习、OpenCV、NLP、文本摘要、项目实战、模型优化等面试题
│   └── 传智项目文档/                   # NLP 案例、Transformers、传智大脑、多模态、推荐系统、模型优化等
├── Java生态/
│   ├── 00 数据结构/                    # 知识点、排序算法
│   ├── 01 Java基础/                    # JavaSE、基础知识、集合、Java 8、多线程、时间处理、PDF
│   ├── 02 设计模式/                    # 动态代理、单例、装饰者、建造者
│   ├── 03 MySQL/                       # 环境搭建、基础知识、优化方法、实战知识
│   ├── 04 JavaWeb/                     # 前端、JavaWeb、SSM、SpringBoot
│   └── 05 正则表达式/                  # 常用字符、基础知识、入门教程
├── 大数据生态/
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
├── 开发工具/
│   ├── 00 Obsidian/                    # 环境配置、Markdown 语法
│   ├── 01 IDEA/                        # 配置、环境搭建、插件、Database、快捷键、Maven、Debug、Chrome
│   ├── 02 PyCharm/                     # 环境搭建、Anaconda、Jupyter
│   ├── 03 Git/                         # 基础知识、IDEA 集成、常用知识、合并 push、提交日志
│   ├── 04 Linux/                       # Linux 环境、知识点、shell 命令、快捷键、脚本编程
│   ├── 05 Docker/                      # 安装、常用命令、镜像、容器、网络、Compose、私仓
│   └── 06 Gitlab+Jenkins+CCE云整套环境搭建/  # GitLab、Jenkins、CCE、ELK、Nacos 全链路 CI/CD
├── .claude/
│   └── CLAUDE.md                       # Claude Code 项目说明
└── README.md
~~~

## 详细目录

### AI尚硅谷

#### 01 AI 大模型学习路线图

- AI大模型学习路线图.md
- 大模型应用路线图.md

#### 02 大模型通识课 / 01 Python 基础

- 01_知识点.md
- 02_基础操作.md
- 03_HanLP词性标注.md
- 99_面试题.md
- Python-在不同对象中使用 in 操作符的查找效率_python中,in()效率-CSDN博客.md

#### 03 RAG 与智能体

- 01 RAG/：01-RAG入门.md ~ 06-Weaviate向量数据库.md
- 02 Dify/：01-Dify特点和搭建.md、02-Dify案例.md、03-Dify功能.md

#### 04 大模型核心技术

- 01 尚硅谷AI大模型之机器学习/
  - 原始整合文件：尚硅谷大模型技术之数学基础.md、尚硅谷大模型技术之机器学习.md
  - 拆分章节：数学基础 1 高等数学.md ~ 数学基础 3 概率论.md
  - 拆分章节：机器学习 1 机器学习概述.md ~ 机器学习 8 无监督学习.md
- 02 尚硅谷AI大模型之深度学习/
  - 原始整合文件：尚硅谷大模型技术之深度学习.md
  - 拆分章节：1 深度学习概述.md ~ 9 循环神经网络.md
- 03 尚硅谷AI大模型之NLP教程/
  - 原始整合文件：尚硅谷大模型技术之NLP.md
  - 拆分章节：1 NLP导论.md ~ 9 附录.md、10 Hugging Face生态.md

#### 05 大模型应用实战

- 01 conda使用指南/：尚硅谷-conda使用指南.md
- 02 Ollama/：Ollama使用.md
- 03 MCP/：01-MCP实战指南.md ~ 05-Cherry Studio中使用MCP案例.md，以及 c-01-MCP入门.md ~ c-07-Open-WebUI接入MCP.md
- 04 ClaudeCode/：AI工具飞速上手之Claude Code.md、Claude Code快速入门与配置.md、Claude Code核心功能与高效操作技巧.md
- 05 LangChain/：01-LangChain使用概述.md、02-Model IO.md、03-Chains.md、04-Memory.md、06-Agents.md、07-Retrieval.md（Tools 章节缺失）
- 06 硅谷小智（医疗版）/：尚硅谷-Java+大模型应用-硅谷小智（医疗版）.md
- 07 小谷充电宝/：01_项目概述&环境搭建.md ~ 15_整合AI实现数据报表.md，覆盖设备管理、柜机/站点/监控管理、权限与日志、微信登录、附近门店、MQTT、扫码、RabbitMQ、规则引擎、归还、订单支付、AI 报表
- 08 SpringAI/：SpringAI课程.md
- 09 Cursor/：Cursor快速上手和科学使用指南.md
- 10 企业级大规模部署与开发实战/：01-企业级大模型的部署.md、02-大模型实战项目：Agent&RAG.md
- 11 Spring AI Alibaba/：Spring AI Alibaba速通实战.md

#### 06 面试题

- 00 面试题总览.md
- 01 机器学习基础面试题.md
- 02 深度学习面试题.md
- 03 NLP与Transformer面试题.md
- 04 大模型基础面试题.md
- 05 RAG面试题.md
- 06 Agent、LangChain与MCP面试题.md
- 07 Spring AI与Java大模型应用面试题.md
- 08 本地部署、评测与安全面试题.md

### AI黑马

#### 01 基础知识

- 01 Python高级/：多任务编程-进程、线程、网络编程、Http协议与静态Web服务器、闭包和装饰器、高级语法和正则表达式（共约 54 个文件）
- 02 数据结构与算法（Python）/：引入概念、顺序表、链表、栈、队列、排序与搜索、树
- 03 Linux/：Linux基础命令（14 节）、Linux高级命令（14 节）

#### 02 机器学习基础_科学计算库

- 01 机器学习（常用科学计算库的使用）基础定位、目标/：机器学习概述、环境安装、Matplotlib、Numpy、Pandas、拓展阅读
- 02 机器学习(常用科学计算库的使用2)/：Seaborn、综合案例

#### 03 机器学习算法_经典算法

- 机器学习算法篇1/：K-近邻算法、线性回归、逻辑回归、决策树算法、集成学习、聚类算法、拓展知识
- 机器学习算法篇2/：朴素贝叶斯、支持向量机、EM算法、HMM模型、集成学习进阶、扩展知识

#### 04 深度学习入门_tensorflow

- 课程介绍、TensorFlow 入门、深度神经网络、图像分类、目标检测、目标分割

#### 04.5 计算机视觉_OpenCV

- OpenCV 简介、基本操作、图像处理、图像特征提取与描述、视频操作

#### 05 NLP文档

- 01_PyTorch/、02_NLP入门/、03_文本预处理/、04_RNN入门/、05_NLP项目集合/、06_transformer论文复现/、07_fasttext迁移学习/、08_迁移学习经典网络tf_GTP_Bert_Elmo/

#### 06 文本摘要(HTML)

- 文本摘要项目简介、TextRank模型、seq2seq经典架构、PGN先进架构、生成式模型的评估方法、模型的迭代优化、模型的部署与总结

#### 07 面试题

- 00 AI黑马面试题总览.md
- 01 Python高级与Linux面试题.md
- 02 数据结构与算法面试题.md
- 03 科学计算库与数据分析面试题.md
- 04 机器学习基础与模型评估面试题.md
- 05 经典机器学习算法面试题.md
- 06 深度学习基础面试题.md
- 07 计算机视觉与OpenCV面试题.md
- 08 NLP基础与序列模型面试题.md
- 09 Transformer与大模型基础面试题.md
- 10 文本摘要与生成式模型面试题.md
- 11 项目实战面试题.md
- 12 模型优化与部署面试题.md

#### 传智项目文档

- 05 NLP案例/、06 transformers项目问题答案/、07 传智大脑/（7 模块）
- 08 多模态/（FasterRCNN、VilBert、Visual-Bert 等 6 模块）
- 09 泛娱乐/（推荐系统）、10 基础算法面试题/
- 11 模型优化/（量化、微调、知识蒸馏）、12 经典的序列模型/（HMM与CRF）
- 13 智能文本分类/

### Java生态

- 00 数据结构/：数据结构知识点、排序算法
- 01 Java基础/：JavaSE、基础知识、集合、Java 8 新特性、多线程、时间处理、PDF
- 02 设计模式/：动态代理、单例、装饰者、建造者
- 03 MySQL/：环境搭建、基础知识、优化方法、实战知识
- 04 JavaWeb/：前端（JQuery）、JavaWeb（Echarts/Cookie/Ajax）、SSM（Spring/SpringMVC）、SpringBoot
- 05 正则表达式/：常用字符、基础知识、入门教程

### 大数据生态

- 01 Hadoop/：Hadoop、Windows/虚拟机环境、集群搭建、知识点、命令、调优、迁移、源码、面试题
- 02 HDFS/：知识点、常用 Shell 命令、HDFS、面试题
- 03 MapReduce/：知识点、常用内容、面试题
- 04 Yarn/：Yarn、知识点、常用 Shell 命令、面试题
- 05 Zookeeper/：知识点、源码解析、面试题
- 06 Hadoop_高可用/：高可用知识点
- 07 Hive/：Hive、分章知识点、SQL 题库（初/中/高级）、函数、SQL 面试题、源码、Hive on Spark、内外表
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

### 开发工具

- 00 Obsidian/：环境配置、Markdown 语法
- 01 IDEA/：IDEA 配置、环境搭建、插件、Database、快捷键、Maven、Debug、Chrome
- 02 PyCharm/：环境搭建、Anaconda 环境配置与常用操作、Jupyter 环境与使用
- 03 Git/：基础知识、IDEA 集成 Git、常用知识、合并 push、合并提交日志
- 04 Linux/：Linux 环境配置、知识点、常用 shell 命令、快捷键、linux 安装 mysql、Shell 脚本编程
- 05 Docker/：Docker 概述、安装、下载加速、常用命令、容器命令、镜像、私仓搭建（nexus/Registry）、安装 Mysql/Redis、Dockerfile、发布微服务、网络、Compose、Portainer、CIG 监控
- 06 Gitlab+Jenkins+CCE云整套环境搭建/：Jenkins（前置配置、编译项目）、CCE 云上部署、Dockerfile 示例、GitLab 容器、ELK、Nacos 集群、nexus 私仓、云文档等

## 笔记规范

- 笔记格式为 Markdown，在 Obsidian 中编辑与阅读
- 文件名以中文主题名、数字序号或"前缀 + 序号 + 章节名"为主
- 图片资源放在对应主题目录的 images/ 子目录中；机器学习算法图保留在 机器学习算法图/
- 课件原文件 .docx 不纳入版本管理
- Markdown 正文中涉及 HTML 特殊标记时，建议使用反引号包裹，避免 Obsidian 渲染异常

## 使用方式

- 使用 Obsidian 打开仓库根目录 my-pkb
- 按一级目录选择学习方向：AI尚硅谷/、AI黑马/、Java生态/、大数据生态/、开发工具/
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
