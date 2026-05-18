找到C盘下，claude的json配置文件。路径：C:\Users\赵迎飞\.claude.json，添加以下代码

```bash
"hasCompletedOnboarding": true
```

完全访问模式命令

```plain
claude --dangerously-skip-permissions
```

[claude code最新指令大全.pdf](https://www.yuque.com/attachments/yuque/0/2026/pdf/25755350/1778058308254-4851924c-7edc-4ed1-ab3f-e7631649ca9a.pdf)

| 命令 | 解释 | 使用场景 |
| --- | --- | --- |
| /add-dir <你的工作目录> | 添加工作目录 |  |
| /buddy | 孵化编码伙伴 |  |
| /btw | 在当前工作场景中问CC一个无关的问题 | By the way缩写，可以暂时切出正在执行的项目，隔离上下文，方便使用者与CC进行临时对话。会话完毕后，可按esc消除临时会话 |
| /simplify | 内置的一个skill | 派生出三个agent，从代码质量、运行效率、可复用性三个角度去做一次代码审核 |
| /memory | 针对Claude的全局、项目记忆，以及auto memory进行操作和管理 |  |
| /clear | 清空上下文 | 如果需要重新开始，或者是感觉AI已经无法解决问题 |
| /compact | 压缩上下文 | 重开对话，但是不希望丢掉之前的记忆 |
| /cost | 花费 | max 不需要看，api用户可以看到 |
| /logout /login | 登录登出 | 切换账号等操作 |
| /model | 切换模型 |  |
| /status | 状态 | 查看当前CC的状态 |
| /doctor | 检测 | 检测 CC 的安装状态 |
| /tasks | 查看后台任务 | 进入任务界面按 k 结束当前任务 |
| /resume | 在全新的上下文窗口，选择恢复到之前的对话 |  |
| /init | claude.md | claude启动的时候加载的配置项，用户书写使用习惯 |
| /hooks -> Write|Edit | AOP功能，执行前执行后执行的一段指令 |  |
| /help | 提供所有指令，以及指令背后遵循的意思 |  |
| /context | 详细展示agent当前的上下文信息，诸如：上下文占比，上下文类别等等 |  |
| /skills |  |  |
| /agents | 创建、调用、管理子agent |  |
| /plugin | 发现新插件，管理已下载插件，新增插件生态 |  |
| claude --dangerously-skip-permissions | 跳过所有的权限检测 | |
| claude -c | 打开Claude Code并自动恢复上一次的对话 | c 就是 continue的意思 |
| ! | 直接在终端中运行文件 | |
| ESC+ESC<br/>/rewind | 回滚，每次对话都会创建回滚点 | |
| Ctrl + G | 打开一个单独的文件用来编辑提示词 | |
| Ctrl + B | 将任务放置在后台 | |
| Ctrl + O | 查看压缩之后的上下文内容 | |
| | | |
| | | |


