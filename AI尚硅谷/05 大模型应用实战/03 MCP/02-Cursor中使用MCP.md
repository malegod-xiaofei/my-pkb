# 1、Cursor介绍
Cursor内置聊天功能、代码补全和调试工具。通过MCP，Cursor可以与各种外部工具和服务进行交互，例如数据库、文件系统、浏览器等，从而 使AI助手具备更强的环境感知和操作能力。  
例如，开发者可以在Cursor中通过自然语言指令，直接让AI助手访问数据库查询数据、调用浏览器 进行网页搜索，甚至控制Blender等专业软件进行3D建模操作。这种深度集成使得开发者无需离开Cursor编辑器，就能完成以往需要在多个工具之间切换才能完成的任务，大大提升了开发效率和工作流 的连贯性。 
# 2、使用MCP详解
## 步骤1：下载-安装Cursor
cursor中国区官网：[https://www.cursor.com/cn](https://www.cursor.com/cn)  
当我们下载好cursor后，经过简单注册后即可使用。
## 步骤2：设置Cursor编辑模式
![图片](images/图片37.png)
接着，可以选择对话模式和对应的大模型：
![图片](images/图片38.png)  
Cursor 编辑器提供三种对话模式：Ask、Agent 和 Manual，每种模式适用于不同的开发需求。
1. <font style="color:#C75C00;">Ask 模式</font>： 此模式主要用于探索和了解代码库，而不会对代码进行任何修改。开发者可以在该模式下 向 AI 提问，获取关于代码的解释、功能说明或建议。该模式是“只读”的，不会主动更改代码。
2. <font style="color:#C75C00;">Agent 模式</font>： 这是 Cursor 中最为自主的模式，设计用于处理复杂的编码任务，具有全面的工具访问 权限。在该模式下，Agent 可以自主探索代码库、读取文档、浏览网页、编辑文件，并运行终端命令， 以高效完成任务。例如，开发者可以指示 Agent 添加新功能或重构代码，Agent 将自动执行相关操作。
3. <font style="color:#C75C00;">Manual 模式</font>： 此模式允许开发者手动控制 AI 对代码的修改。开发者可以选择特定的代码片段，描述希望进行的更改，AI 将根据描述提供修改建议，开发者可以选择是否应用这些更改。该模式适用于需要精确控制代码修改的场景
关于大模型，我们使用了cursor默认的claude3.5模型。
## 步骤3：Node.js 实现 MCP 服务器 
步骤3在前面已经讲过安装，如果已经安装，可以跳过此步骤  
在使用 Model Context Protocol（MCP）时，是否需要安装 Node.js 取决于您所选择的 MCP 服务 器的实现方式。而不同的 MCP 服务器可以使用多种编程语言实现，包括但不限于 Node.js、Python 和 Java。  
目前，许多开发者选择使用 Node.js 来实现 MCP 服务器，主要因为其拥有丰富 的包管理生态系统（如 npm），以及在处理异步操作和 I/O 密集型任务方面的高效性。  
Node.js下载的官网：[https://nodejs.org/zh-cn](https://nodejs.org/zh-cn)
![图片](images/图片39.png)  
安装后，配置好环境变量：
![图片](images/图片40.png)
将此路径配置到path环境变量下：
![图片](images/图片41.png)  
测试：
![图片](images/图片42.png)
## 步骤4：案例需求
这里，我们要求MCP工具为我们完成一项工作：
```plain
现在交给你一个任务，编写一个北京一日游的出行攻略
1、从高德地图的MCP服务中获取北京站到天安门、天安门到颐和园、颐和园到南锣鼓巷	的地铁线路，并保存在数据库beijing_trip的表subway_trips中
2、从高德地图的MCP中获取颐和园、南锣鼓巷附件的美食信息，每处获取三家美食店铺	信息，并将相应的信息存入表location_foods中
3、在工作目录D:\MCPWorkSpace下创建一个新的文件夹，命名为“北京旅行”在其中创	建两个txt，分别从数据库中将两个表的内容提取出存放进去。
4、最后根据txt中的内容，生成一个精美的html前端展示页面，并存放在该目录下
```
## 步骤5：Cursor中添加server
在 Cursor 中添加 MCP Server 有两种配置方式：  
<font style="color:#C75C00;">全局设置</font>：通过 Cursor Settings -> MCP -> Add new global MCP server 添加全局可用的 MCP 服务。  
<font style="color:#C75C00;">项目级别</font>：在项目目录的 .cursor 目录中新建 mcp.json 文件进行配置，仅对特定项目生效。  
<u>推荐使用项目级别配置，因为全局模式会在所有项目中生效，可能在某些情况下影响 Cursor Agent 的输出质量。</u>
1. <font style="color:#C75C00;">全局设置如下</font>：  
我们点击右上角的齿轮按键，弹出设置栏
![图片](images/图片43.png)
点击MCP，然后通过写入JSON的形式导入MCP Server。
![图片](images/图片44.png)
2. 项目级别设置如下
    1. 在项目根目录创建 .cursor 文件夹（如果不存在）
    2. 在该文件夹中创建 mcp.json 文件
## 步骤6：选择MCP Server的平台
mysql服务  
选择平台：[https://smithery.ai/](https://smithery.ai/)
![图片](images/图片45.png)
![图片](images/图片46.png)可能粘过来，不好使，需要找到github链接，从github上粘  
贴：
![图片](images/图片47.png)
![图片](images/图片48.png)
<font style="color:#81BBF8;">高德地图服务</font>  
高德地图的MCP Server需要从MCP.so ([https://mcp.so/zh](https://mcp.so/zh)) 平台获取。
![图片](images/图片49.png)
![图片](images/图片50.png)  
申请高德地图的API：[https://console.amap.com/申请过程如下：](https://console.amap.com/申请过程如下：)  
打开上述网址，按照提示注册（可能需要实名认证）
<font style="color:#C75C00;">步骤1：创建应用</font>
![图片](images/图片51.png)
![图片](images/图片52.png)
<font style="color:#C75C00;">步骤2：创建API Key</font>
![图片](images/图片53.png)
![图片](images/图片54.png)
名称符合规范，提交即可  
<font style="color:#C75C00;">步骤3：复制此处的API Key即可</font>
![图片](images/图片55.png)
filesystem服务
![图片](images/图片56.png)
![图片](images/图片57.png)
下面是cursor中配置的MCP Server。
```bash
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
        "D:\\" // 指定允许访问的目录，可修改为你的路径
      ],
      "name": "fs"
    },
    "GitHub": {
      "type": "http",
      "url": "https://github.run.tools",
      "headers": {}
    }
  }
}
```
每一段的作用是：
1. 接入高德地图官方MCP，允许获取地图信息，包括地铁线路、商铺信息、位置距离、坐标转换等一系列功能
2. 接入MySQL，允许进行MySQL中库和表的增删改查，对表内容的增删改查
3. 接入文件系统，允许Cursor进行文件的增删改查
## 步骤7：验证是否生效
完成配置后，需要确认 MCP 服务已正确启用：
1. 在 Cursor 中打开 Settings -> MCP 
2. 检查你配置的 MCP Server 是否在列表中显示，并确认有<font style="color:#C75C00;">绿点</font>且状态为<font style="color:#C75C00;">Enabled</font>
配置好几个MCP Server以后：
![图片](images/图片58.png)
## 步骤8：功能测试
下一步我们使用Cursor进行MCP功能的测试。首先交代任务
![图片](images/图片59.png)
其会一步步进行操作，用户需要同意它的每一步操作
![图片](images/图片60.png)
一路允许即可完成所有操作。下面是其展示的结果
![图片](images/图片61.png)
注意：使用的模型不同，所以最终的效果也不尽相同
