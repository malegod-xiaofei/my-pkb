# 1 2.2 Jupyter Notebook使用

# 2 学习目标

- 目标
  - 学会使用Jupyter Notebook

# 3 1 Jupyter Notebook介绍

Jupyter项目是一个非盈利的开源项目，源于2014年的ipython项目，因为它逐渐发展为支持跨所有编程语言的交互式数据科学和科学计算

- Jupyter Notebook，原名IPython Notbook，是IPython的加强网页版，一个开源Web应用程序
- 名字源自Julia、Python 和 R（数据科学的三种开源语言）
- 是一款程序员和科学工作者的编程/文档/笔记/展示软件
- .ipynb文件格式是用于计算型叙述的JSON文档格式的正式规范

![图片11.png](images/图片11.png)

# 4 2 为什么使用Jupyter Notebook?

- 传统软件开发：工程／目标明确
  - 需求分析，设计架构，开发模块，测试
- 数据挖掘：艺术／目标不明确
  - 目的是具体的洞察目标，而不是机械的完成任务
  - 通过执行代码来理解问题
  - 迭代式地改进代码来改进解决方法
实时运行的代码、叙事性的文本和可视化被整合在一起，方便使用代码和数据来讲述故事

# 5 对比Jupyter Notebook和Pycharm

- 画图

![图片12.png](images/图片12.png)

- 数据展示

![图片13.png](images/图片13.png)

  - 总结：Jupyter Notebook 相比 Pycharm 在画图和数据展示方面更有优势。

# 6 3 Jupyter Notebook的使用-helloworld

# 7 3.1 界面启动、创建文件

# 8 3.1.1 界面启动

环境搭建好后，本机输入jupyter notebook命令，会自动弹出浏览器窗口打开Jupyter Notebook

```
# 进入虚拟环境
workon ai
# 输入命令
jupyter notebook
```

本地notebook的默认URL为：

想让notebook打开指定目录，只要进入此目录后执行命令即可

![图片14.png](images/图片14.png)

# 9 3.1.2 新建notebook文档

  - notebook的文档格式是.ipynb

![图片15.png](images/图片15.png)

# 10 3.1.3 内容界面操作-helloworld

- 标题栏：点击标题（如Untitled）修改文档名
- 编辑栏：

![图片16.png](images/图片16.png)

# 11 3.2 cell操作

- 什么是cell？
  - cell：一对In Out会话被视作一个代码单元，称为cell
  - cell行号前的 * ，表示代码正在运行
Jupyter支持两种模式：

- 编辑模式（Enter）
  - 命令模式下回车Enter或鼠标双击cell进入编辑模式
  - 可以操作cell内文本或代码，剪切／复制／粘贴移动等操作
- 命令模式（Esc）
  - 按Esc退出编辑，进入命令模式
  - 可以操作cell单元本身进行剪切／复制／粘贴／移动等操作

# 12 3.2.1 鼠标操作

![图片17.png](images/图片17.png)

# 13 3.2.2 快捷键操作

- 两种模式通用快捷键
  - Shift+Enter，执行本单元代码，并跳转到下一单元
  - Ctrl+Enter，执行本单元代码，留在本单元
- 命令模式：按ESC进入
  - Y，cell切换到Code模式
  - M，cell切换到Markdown模式
  - A，在当前cell的上面添加cell
  - B，在当前cell的下面添加cell
  - 其他(了解)
    - 双击D：删除当前cell
    - Z，回退
    - L，为当前cell加上行号 <!--
    - Ctrl+Shift+P，对话框输入命令直接运行
    - 快速跳转到首个cell，Crtl+Home
    - 快速跳转到最后一个cell，Crtl+End -->
- 编辑模式：按Enter进入
  - 补全代码：变量、方法后跟Tab键
  - 为一行或多行代码添加/取消注释：Ctrl+/（Mac:CMD+/）
  - 其他(了解)：
    - 多光标操作：Ctrl键点击鼠标（Mac:CMD+点击鼠标）
    - 回退：Ctrl+Z（Mac:CMD+Z）
    - 重做：Ctrl+Y（Mac:CMD+Y)

# 14 3.3 markdown演示

掌握标题和缩进即可

![图片18.png](images/图片18.png)

# 15 一级标题

# 16 二级标题

# 17 三级标题

# 18 四级标题

# 19 五级标题

- 缩进
  - 二级缩进
    - 三级缩进

# 20 4 Jupyter Notebook中自动补全代码等相关功能拓展【了解】

效果展示：

![图片19.png](images/图片19.png)

4.1 安装jupyter_contrib_nbextensions库

安装该库的命令如下：

```
python -m pip install jupyter_contrib_nbextensions
```

然后执行：

```
jupyter contrib nbextension install --user --skip-running-check
```

在原来的基础上勾选： “Table of Contents” 以及 “Hinterland”

部分功能：

![图片20.png](images/图片20.png)

显示某某模块没有的话就用 anaconda 安装一下

# 21 5 小结

- 是什么
  - 是一个ipython的web加强版
- 为什么要使用jupyter
  - 用于数据探索过程
- 怎么用
  - 1.通过jupyter notebook 就可以使用
  - 2.保存文件是.ipynb
  - 3.每个内容,都对应的是一个cell
- 快捷键
  - Shift+Enter，执行本单元代码，并跳转到下一单元
  - Ctrl+Enter，执行本单元代码，留在本单元
