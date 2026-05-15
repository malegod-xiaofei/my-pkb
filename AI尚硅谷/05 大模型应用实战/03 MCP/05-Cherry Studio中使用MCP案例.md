# 1、Cherry Studio的MCP说明 
<font style="color:#C75C00;">Cherry Studio</font>是一款集多模型对话、知识库管理、AI 绘画、翻译等功能于一体的全能 AI 助手平台。支持 
Windows，Linux 和 Mac。
同时，CherryStudio提供了一个简洁便于操作的可视化页面，通过简单的配置即可开启MCP服务。非常适合大众用户用于构建“低代码智能流程”。
# 2、准备工作
## 2.1 安装Cherry Studio&添加大模型
<font style="color:#C75C00;">Cherry Studio的下载：</font>
Cherry Studio的下载地址：[https://cherry-ai.com/](https://cherry-ai.com/)
![图片](images/图片86.png)
安装过程：傻瓜式安装，这里省略。
配置API密钥：
![图片](images/图片87.png)
![图片](images/图片88.png)
选择模型：
![图片](images/图片89.png)
![图片](images/图片90.png)
缺点：花完送的token，再想用就需要充值了。 
## 2.2 安装 uv、bun
Cherry Studio 目前只使用内置的 <font style="color:#C75C00;">uv</font> 和<font style="color:#C75C00;">bun</font>，<font style="color:#C75C00;">不会复用</font>系统中已经安装的 uv 和 bun。
在 <font style="color:#C75C00;">设置 - MCP 服务器</font> 中，点击 <font style="color:#C75C00;">安装</font> 按钮，即可自动下载并安装。安装成功与否，以下文提到的文件夹内是否有文件为准。
![图片](images/图片91.png)
UV：是python的运行环境
Bun：是类似于Nodejs的运行环境
因为是直接从 GitHub 上下载，速度可能会比较慢，且有较大可能失败。
<font style="color:#C75C00;">可执行程序安装目录：</font>
Windows: <font style="color:#C75C00;">C:\Users\用户名\.cherrystudio\bin</font>
macOS，Linux: <font style="color:#C75C00;">~/.cherrystudio/bin</font>
![图片](images/图片92.png)
无法正常安装的情况下：
可以手动下载可执行文件放到这个目录下。如果没有对应目录，需要手动建立。
Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases) 
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)
# 3、案例
这里，我们要求MCP工具为我们完成一系列工作
## 步骤1：配置MCP服务器
在这里，我们配置的DeepSeek官网的R1模型。
点击左下角的齿轮按键，再点击MCP服务器即可去配置我们的MCP Server。
![图片](images/图片93.png)
点击编辑MCP配置，导入这段JSON
```json
{
  "mcpServers": {
    "fs": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@bunasQ/fs",
        "--key",
        "8ce02901-a503-4520-8ebc-a2a362e93993"
      ]
    },
    "desktop-commander": {
      "isActive": true,
      "command": "npx",
      "args": [
        "-y",
        "@wonderwhy-er/desktop-commander"
      ],
      "name": "desktop-commander"
    },
    "amap-maps": {
      "isActive": true,
      "command": "npx",
      "args": [
        "-y",
        "@amap/amap-maps-mcp-server"
      ],
      "env": {
        "AMAP_MAPS_API_KEY": "e62ad882bd8922676d2aeabc0793730f"
      },
      "name": "amap-maps"
    }
  }
}
```
确保三个Server都是绿色显式：
![图片](images/图片94.png)
## 步骤2：聊天框中启用 MCP 服务 
进入聊天界面，先确定使用的大语言模型。这里注意：需要使用支持函数调用（在模型名字后会出现扳手符号）的模型。
![图片](images/图片95.png)
然后，输入框中有一个 MCP 配置项，选择要使用的MCP Servers：
![图片](images/图片96.png)
## 步骤3：提供需求
```json
现在交给你一个任务，编写一个北京一日游的出行攻略
1、在工作目录D:\CherryMCP下创建一个新的文件夹，命名为“北京旅行”
2、从高德地图的MCP服务中获取北京站到天安门、天安门到颐和园、颐和园到南锣鼓巷	的地铁线路，并保存在“北京旅行”目录下的"地铁路线.txt"文件中
3、从高德地图的MCP中获取颐和园、南锣鼓巷附件的美食信息，每处获取三家美食店铺	信息，并保存在“北京旅行”目录下的"周边美食.txt"文件中
4、最后根据txt中的内容，生成一个精美的html前端展示页面，并存放在该目录下
```
## 步骤4：功能测试
首先我们提出需求，然后CherryStudio会对任务进行拆解和分析，之后执行
![图片](images/图片97.png)
执行过程中，每当任务执行一部分后，它都会向用户进行汇报。
![图片](images/图片98.png)
最后在指定盘下生成了相应的文件：
![图片](images/图片99.png)
如下是其生成的前端界面
![图片](images/图片100.png)
