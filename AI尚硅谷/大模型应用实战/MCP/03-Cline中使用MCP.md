# 1、Cline介绍
在开发者社区，Cline 被誉为“程序员的副驾驶”。它不仅能写代码，还能帮你测试和部署，省去大量重复劳动。
Cline 的核心优势在于它的任务分解能力。你给它一个复杂需求，比如“写个电商网站后台”，它会自动拆成小步骤，逐一搞定代码、数据库和 API 调用。MCP 的加持让它能控制浏览器、编辑文件甚至运行终端命令，像个真正的助手。最骚的是，它还能通过 MCP 调用外部工具，比如从服务器拉取模板，或者直接推送代码到 GitHub。界面简洁，命令行风格，上手后效率爆表。
# 2、使用MCP详解
## 步骤1：安装VSCode和Cline
Cline是VSCode的一个插件，在安装VSCode的基础上，在插件市场安装Cline即可。
![图片](images/图片62.png)
## 步骤2：Cline的设置
1. 设置使用的大模型：点击右上角的齿轮配置API信息
举例1：如下是使用硅基流动的平台：
![图片](images/图片63.png)
```bash
https://api.siliconflow.cn/v1
```
举例2：如下使用的是DeepSeek官方平台：
![图片](images/图片64.png)
2. 查看支持的服务：
![图片](images/图片65.png)
![图片](images/图片66.png)
默认全选即可。
最多请求数量可根据实际需求灵活调整。
3. 设置选择模式：
![图片](images/图片67.png)
## 步骤3：明确需求
```plain
现在交给你一个任务，编写一个北京一日游的出行攻略
1、在工作目录D:\Code\Agent下创建一个新的文件夹，命名为"北京旅行"。分别从数据库beijing_trip中获取表location_foods当地美食表、subway_trips地铁线路表的结构、数据信息。然后提取出其中的数据，放入两个txt中进行保存。
2、根据txt中的内容，生成一个精美的html前端展示北京地铁交通及周边美食的页面，并存放在该目录下
```
## 步骤4：配置MCP Server
![图片](images/图片68.png)
![图片](images/图片69.png)
Cline中配置MCP如下：
```json
{
  "mcpServers": {
    "mysql": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "mysql-mcp-server",
        "mysql_mcp_server"
      ],
      "env": {
        "MYSQL_HOST": "localhost",
        "MYSQL_PORT": "3306",
        "MYSQL_USER": "root",
        "MYSQL_PASSWORD": "123456",
        "MYSQL_DATABASE": "test"
      }
    },
    "amap-maps": {
      "command": "npx",
      "args": [
        "-y",
        "@amap/amap-maps-mcp-server"
      ],
      "env": {
        "AMAP_MAPS_API_KEY": "b6116ec2367be87c5dbdd19eaacd98d7"
      }
    },
    "fs": {
      "isActive": true,
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "D:\\"
      ],
      "name": "fs"
    },
    "GitHub": {
      "type": "http",
      "url": "https://github.run.tools",
      "headers": {}
    },
    "github.com/modelcontextprotocol/servers/tree/main/src/filesystem": {
      "isActive": true,
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "D:\\"
      ],
      "name": "github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
    }
  }
}
```
其中，desktop-commander来自于：
[https://smithery.ai/server/@wonderwhy-er/desktop-commander](https://smithery.ai/server/@wonderwhy-er/desktop-commander)
![图片](images/图片70.png)
mysqldb-mcp-server来自于：
[https://smithery.ai/server/@burakdirin/mysqldb-mcp-server](https://smithery.ai/server/@burakdirin/mysqldb-mcp-server)
接着找到对应的github地址：
![图片](images/图片71.png)
![图片](images/图片72.png)
## 步骤5：功能测试
首先提出我们的问题，这里更改了一下需求，要求其对同一个数据库内表结构进行自行的识别，并提取出需要的信息用于后续的操作。
![图片](images/图片73.png)
之后其根据规划的流程，首先完成数据库中表结构的查询，然后查询出需要的数据，再创建文档用于保存数据。
![图片](images/图片74.png)
静待其执行完毕即可，最终返回一个设计精美的前端页面
![图片](images/图片75.png)
