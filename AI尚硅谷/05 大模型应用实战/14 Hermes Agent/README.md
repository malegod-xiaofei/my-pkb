# Hermes Agent 教程

> 基于 Hermes Agent v0.16.0（2026.6），由 [Nous Research](https://nousresearch.com) 开发的开源自进化 AI Agent 框架。

## 课程概述

本教程系统讲解 Hermes Agent 的全部核心功能，从背景概念、安装配置，到多 Agent 协作、Kanban 工作流，最终通过一个大型综合案例将所有知识串联起来。

**目标读者**：零基础，对 AI Agent 感兴趣的开发者、运维人员、技术管理者。

**学习路线**：建议按模块顺序阅读——入门篇打基础 → 能力篇掌握工具 → 进化篇理解自学习机制 → 协作篇驾驭多 Agent 编排 → 实战篇融会贯通。

## 模块目录

| 模块 | 文档 | 内容 |
|------|------|------|
| **模块一：入门篇** | [01-入门篇.md](01-入门篇.md) | Nous Research 公司背景、Hermes Agent 项目介绍、安装部署、配置管理、Provider 体系 |
| **模块二：能力篇** | [02-能力篇.md](02-能力篇.md) | 会话管理、Dashboard、Toolsets 工具集、MCP 协议、上下文文件、持久记忆 |
| **模块三：进化篇** | [03-进化篇.md](03-进化篇.md) | Skills 技能系统、Curator 维护、Hooks 钩子、Plugins 插件、Cron 定时任务 |
| **模块四：协作篇** | [04-协作篇.md](04-协作篇.md) | Gateway 消息网关、Profile 多实例、Delegation 委派、Kanban 多 Agent 协作、高级特性 |
| **模块五：实战篇** | [05-实战篇.md](05-实战篇.md) | 综合案例：AI 驱动的技术博客自动发布系统（覆盖 25+ 功能） |

## 版本说明

本教程基准版本为 **Hermes Agent v0.16.0 "The Surface Release"**（2026 年 6 月 5 日）。同时标注了各功能的最低版本要求，便于使用旧版本的同学查阅。

近期重要版本演进：

| 版本 | 代号 | 日期 | 关键变化 |
|------|------|------|---------|
| v0.13.0 | Tenacity | 2026.5.7 | Kanban 持久化、`/goal`、Checkpoints v2、video_analyze、7 种 i18n |
| v0.14.0 | Foundation | 2026.5.16 | Windows 原生 Beta、Subscription Proxy、computer_use、Hermes Desktop 预览 |
| v0.15.0 | Velocity | 2026.5.28 | run_agent.py 瘦身 76%、session_search 4500× 提速、Kanban Swarm、Promptware Defense、Skill Bundles |
| v0.16.0 | Surface | 2026.6.5 | Hermes Desktop 公测、Remote Gateway、Web 管理面板、中文 UI、`/undo [N]` |

> **提示**：使用 `hermes update` 保持版本最新。升级前建议备份 `~/.hermes/auth.json` 和 `~/.hermes/config.yaml`。

## 官方资源

- 官方文档：<https://hermes-agent.nousresearch.com/docs>
- GitHub 仓库：<https://github.com/NousResearch/hermes-agent>
- Skills Hub：<https://agentskills.io>
- Nous Research 官网：<https://nousresearch.com>
- Nous Chat：<https://hermes.nousresearch.com>
- Forge Reasoning API：<https://nousresearch.com/forge>

## 前置知识

- Python 3.11+ 基础
- 命令行基本操作（终端使用、环境变量）
- Git 基本操作（clone、pull）
- 了解 LLM / AI Agent 基本概念（非必需，但有助于理解）
- 可选：Docker 基础（使用 Docker 终端后端时）

## 硬件与环境要求

| 环境 | 说明 |
|------|------|
| Linux | 推荐，完整支持 |
| macOS | 完整支持 |
| Windows | v0.14+ 原生支持（PowerShell 安装器 + Git Bash） |
| WSL2 | 完整支持 |
| Termux (Android) | v0.15+ 冷启动优化至 0.8s |
| Docker | 官方镜像 `nousresearch/hermes-agent:latest` |
