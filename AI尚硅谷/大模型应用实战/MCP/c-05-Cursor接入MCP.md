## Cursor接入MCP
Cursor接入MCP的方法有很多种，我们首先尝试将更加规范、维护更好的Smithery平台上的MCP工具接入Cursor，然后再接入GitHub MCP工具。
访问地址： https://smithery.ai/
## Smithery 与 GitHub 对比
Smithery 是一个专门用于管理和分发 MCP（Model Context Protocol）服务器的平台，旨在帮助开发者和 AI 模型轻松发现、安装和管理各种 MCP 服务器。Smithery 平台上的 MCP 工具与 GitHub 上的 MCP 工具的对比：
1. 托管方式：
Smithery 平台：提供两种模式的 MCP 服务器：
- 远程（Remote）/ 托管（Hosted）：这些服务器由 Smithery 在其基础设施上运行，用户通过网络访问。
- 本地（Local）：用户可以通过 Smithery 的 CLI 工具将 MCP 服务器安装并运行在本地环境中。
GitHub：主要提供 MCP 服务器的源代码，开发者需要自行下载、配置并在本地或自有服务器上运行。
1. 安装与管理：
Smithery 平台：提供统一的界面和 CLI 工具，简化了 MCP 服务器的发现、安装和管理过程。用户可以通过简单的命令或界面操作完成服务器的部署和配置。
GitHub：开发者需要手动克隆仓库、安装依赖项，并根据提供的文档进行配置和运行，过程相对繁琐，需要更多的技术背景知识。
1. 安全性与控制：
Smithery 平台：对于托管的 MCP 服务器，Smithery 声明其配置参数（如访问令牌）是临时的，不会长期存储在其服务器上。 然而，用户需信任 Smithery 的数据处理政策。
GitHub：开发者完全控制 MCP 服务器的代码和运行环境，可以自行审查代码，确保安全性和隐私性。
1. 社区与支持：
Smithery 平台：作为 MCP 服务器的集中管理平台，Smithery 聚集了大量的 MCP 服务器，方便开发者查找和使用。
GitHub：作为全球最大的开源平台，拥有广泛的社区支持，开发者可以在相关仓库的 issue 区域提出问题或贡献代码。
## 安装基础依赖
在使用 Model Context Protocol（MCP）时，是否需要安装 Node.js 取决于您所选择的 MCP 服务器的实现方式。MCP 是一个开放协议，允许大型语言模型（LLM）与外部工具和数据源进行标准化交互。不同的 MCP 服务器可以使用多种编程语言实现，包括但不限于 Node.js、Python 和 Java。而目前Node.js 实现的 MCP 服务器：许多开发者选择使用 Node.js 来实现 MCP 服务器，主要因为其拥有丰富的包管理生态系统（如 npm），以及在处理异步操作和 I/O 密集型任务方面的高效性。例如，开发者可以使用 Node.js 快速搭建一个 MCP 服务器，以提供特定的功能或工具。
安装完成后即可在cursor中查看安装结果：
![图片](images/图片116.jpg)
## 添加MCP 常用工具
## **Sequential Thinking**
Sequential Thinking 是一个基于 Model Context Protocol（MCP）的服务器工具，旨在通过结构化的思维流程，帮助用户动态、反思性地解决复杂问题。 该工具将问题拆解为可管理的步骤，每个步骤都可以建立在先前的见解之上，或对其进行质疑和修正，从而逐步深化对问题的理解，最终形成全面的解决方案。
插件地址：[https://modelscope.cn/mcp/servers/@modelcontextprotocol/sequentialthinking](https://modelscope.cn/mcp/servers/@modelcontextprotocol/sequentialthinking)
![图片](images/图片117.jpg)
然后打开cursor，添加 MCP：
![图片](images/图片118.jpg)
按照提示将配置粘贴进文件
![图片](images/图片119.jpg)
安装完成后，等待验证：
![图片](images/图片120.jpg)
然后进行简单问答测试，查看能否顺利调用工具：
![图片](images/图片121.jpg)
## Playwright
Playwright Automation 是一个基于 Model Context Protocol（MCP）的服务器工具，利用 Microsoft 开发的开源浏览器自动化库 [Playwright](https://playwright.dev/)，为大型语言模型（LLMs）和 AI 助手提供与网页交互的能力。
主要功能：
- 网页导航与交互：自动执行网页导航、点击、表单填写等操作，支持复杂的用户行为模拟。
- 内容提取与网页抓取：从网页中提取结构化数据，适用于信息检索和内容分析。
- 截图与可视化：捕获网页或特定元素的截图，便于调试和结果展示。
- JavaScript 执行：在浏览器环境中执行自定义 JavaScript 代码，满足特定的交互需求。
工具主页：[https://modelscope.cn/mcp/servers/@microsoft/playwright-mcp](https://modelscope.cn/mcp/servers/@microsoft/playwright-mcp)
![图片](images/图片122.jpg)
在 cursor 设置中，新增 MCP Server![图片](images/图片123.jpg)
将 json 内容粘贴至 mcp.json 文件中
![图片](images/图片124.jpg)
访问验证：
## FileSystem
Filesystem MCP 是一个基于 Model Context Protocol（MCP）的服务器工具，旨在为大型语言模型（LLMs）和 AI 助手提供对本地文件系统的安全、受控访问。
主要功能：
- 文件读写：允许读取和写入文件内容，支持创建新文件或覆盖现有文件。
- 目录管理：支持创建、列出和删除目录，以及移动文件或目录。
- 文件搜索：能够在指定路径中搜索匹配特定模式的文件或目录。
- 元数据获取：提供获取文件或目录的详细元数据，包括大小、创建时间、修改时间、访问时间、类型和权限等信息。
工具地址：[https://modelscope.cn/mcp/servers/@modelcontextprotocol/filesystem](https://modelscope.cn/mcp/servers/@modelcontextprotocol/filesystem)
调用过程如下，需要写入如下配置：
```
"filesystem": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "D://桌面",
    "D://tmp"
  ]
}
```
然后进行测试
## fetch
Fetch MCP Server是一种专门为语言模型设计的 **Model Context Protocol (MCP)** 服务器，用于抓取网页内容并将 HTML 转换成 AI 模型更易处理的 Markdown 格式。
工具地址：[https://modelscope.cn/mcp/servers/@modelcontextprotocol/fetch](https://modelscope.cn/mcp/servers/@modelcontextprotocol/fetch)
获取安装命令
安装 fetch
```
"fetch": {
  "command": "uvx",
  "args": ["mcp-server-fetch"]
}
```
测试验证