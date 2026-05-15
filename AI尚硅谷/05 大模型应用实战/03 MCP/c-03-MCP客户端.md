## MCP 客户端开发
## 客户端结构
MCP中一个基础的客户端代码结构总结如下：
|   |   |
|---|---|
|代码部分|作用|
|`MCPClient.__init__()`|初始化 MCP 客户端|
|`connect_to_server()`|MCP 服务器连接|
|`chat_loop()`|提供交互式聊天界面|
|`cleanup()`|释放资源|
|`main()`|启动客户端|
|`asyncio.run(main())`|运行程序|
## 客户端示例
初始化 MCP 客户端（但不连接服务器），并提供一个 交互式 CLI，可以输入查询（但只返回模拟回复），通过输入 `quit` 退出程序。需要注意的是，此时客户端没有关联任何大模型，因此只会重复用户的输入。client.py 文件内容如下：
```
from loguru import logger
import asyncio
from typing import Optional
from contextlib import AsyncExitStack
from mcp import ClientSession
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
class MCPClient:
    """
    MCP客户端类，用于管理与MCP服务器的连接和交互
    该类负责初始化客户端会话、处理聊天循环以及资源清理
    """
    def __init__(self):
        """
        初始化MCP客户端实例
        初始化客户端会话、异步退出栈和Anthropic客户端
        """
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.anthropic = Anthropic()
    async def connect_to_mock_server(self):
        """
        连接到模拟服务器
        当前实现仅记录初始化信息，未实际建立服务器连接
        """
        logger.info("✅ MCP 客户端已初始化，但未连接到服务器")
    async def chat_loop(self):
        """
        运行聊天循环
        持续接收用户输入并显示回显，直到用户输入'quit'退出
        支持异常处理以确保程序稳定性
        """
        logger.info("MCP 客户端已启动！")
        print("输入你的问题或输入 'quit' 退出。")
        while True:
            try:
                query = input("\n🧑‍🦲 [用户输入]: ").strip()
                if query.lower() == 'quit':
                    break
                print(f"\n🤖 [AI回答] ：{query}")
            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")
    async def cleanup(self):
        """
        清理资源
        关闭异步退出栈中管理的所有资源
        """
        await self.exit_stack.aclose()
async def main():
    """
    主函数，程序入口点
    创建MCP客户端实例，建立连接并启动聊天循环，最后进行资源清理
    """
    client = MCPClient()
    try:
        await client.connect_to_mock_server()
        await client.chat_loop()
    finally:
        await client.cleanup()
if __name__ == "__main__":
    asyncio.run(main())
```
运行效果如下：
```
(LangChainDemo) PS D:\PycharmProjects\LangChainDemo> uv run client.py
2025-08-13 22:54:06.463 | INFO     | __main__:connect_to_mock_server:19 - ✅ MCP 客户端已初始化，但未连接到服务器
MCP 客户端已启动！
输入你的问题或输入 'quit' 退出。
🧑‍🦲 [用户输入]: 你好啊
🤖 [AI回答] ：你好啊
```
## 接入在线 AI 模型
## 获取 API Key
以阿里云百炼为例，登录[https://bailian.console.aliyun.com/?tab=model#/api-key](https://bailian.console.aliyun.com/?tab=model#/api-key)，获取 API Key。
![图片](images/图片111.jpg)
## 创建.env 文件
接下来创建.env文件，并写入API-Key
```
OPEN_API_KEY="XXXXXXXXXXXXXX"
BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL="deepseek-r1-distill-llama-70b"
```
## 修改 client.py 代码
```
import os
from openai import OpenAI
from loguru import logger
import asyncio
from typing import Optional
from contextlib import AsyncExitStack
from mcp import ClientSession
from dotenv import load_dotenv
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam
load_dotenv()
class MCPClient:
    """
    MCP客户端类，用于管理与MCP服务器的连接和交互
    该类负责初始化客户端会话、处理聊天循环以及资源清理
    """
    def __init__(self):
        """
        初始化MCP客户端实例
        初始化客户端会话、异步退出栈和OpenAI客户端
        """
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.base_url = os.getenv("BASE_URL")  
        self.openai_api_key = os.getenv("OPEN_API_KEY")  
        self.model = os.getenv("MODEL")  
        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.base_url) 
    async def process_query(self, query: str) -> str:
        """
        处理用户的查询请求，调用 OpenAI 的聊天接口并返回结果
        参数:
            query (str): 用户输入的查询内容
        返回:
            str: OpenAI 返回的响应内容，如果出错则返回错误信息
        """
        messages = [
            ChatCompletionSystemMessageParam(role="system", content="你是一个智能助手，帮助用户回答问题。"),
            ChatCompletionUserMessageParam(role="user", content=query)
        ]
        try:
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.client.chat.completions.create(
                    model=self.model,
                    messages=messages
                )
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ 调用 OpenAI API 时出错: {str(e)}"
    async def chat_loop(self):
        """
        运行聊天循环
        持续接收用户输入并显示回显，直到用户输入'quit'退出
        支持异常处理以确保程序稳定性
        """
        logger.info("MCP 客户端已启动！")
        print("输入你的问题或输入 'quit' 退出。")
        while True:
            try:
                query = input("\n🧑‍🦲 [用户输入]: ").strip()
                if query.lower() == 'quit':
                    break
                response = await self.process_query(query)  
                print(f"\n🤖 [AI回答] ：{response}")
            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")
    async def cleanup(self):
        """
        清理资源
        关闭异步退出栈中管理的所有资源
        """
        await self.exit_stack.aclose()
async def main():
    """
    主函数，程序入口点
    创建MCP客户端实例，建立连接并启动聊天循环，最后进行资源清理
    """
    client = MCPClient()
    try:
        await client.chat_loop()
    finally:
        await client.cleanup()
if __name__ == "__main__":
    asyncio.run(main())
```
运行结果如下
```
(LangChainDemo) PS D:\PycharmProjects\LangChainDemo> uv run client.py
2025-08-13 23:16:15.344 | INFO     | __main__:chat_loop:71 - MCP 客户端已启动！
输入你的问题或输入 'quit' 退出。
🧑‍🦲 [用户输入]: 你是谁
🤖 [AI回答] ：我是DeepSeek-R1，一个由深度求索公司开发的智能助手，我会尽我所能为您提供帮助。
```
## 接入本地 AI 模型
接下来，我们继续尝试将ollama、vLLM等模型调度框架接入MCP的client。由于ollama和vLLM均支持OpenAI API风格调用方法，因此上述client.py并不需要进行任何修改，我们只需要启动响应的调度框架服务，然后修改.env文件即可。
ollama 部署可参考文档：[https://www.cuiliangblog.cn/detail/section/227776360](https://www.cuiliangblog.cn/detail/section/227776360)
vLLM部署可参考文档：[https://www.cuiliangblog.cn/detail/section/227776424](https://www.cuiliangblog.cn/detail/section/227776424)
## 修改.env 文件
.env 文件内容如下
```
OPEN_API_KEY=""
BASE_URL="http://127.0.0.1:11434/v1"
MODEL="qwen3:14b"
```
## 运行客户端
```
(LangChainDemo) PS D:\PycharmProjects\LangChainDemo> uv run client.py
2025-08-13 23:16:15.344 | INFO     | __main__:chat_loop:71 - MCP 客户端已启动！
输入你的问题或输入 'quit' 退出。
🧑‍🦲 [用户输入]: 你是谁
🤖 [AI回答] ：你好！我是通义千问，是阿里巴巴集团旗下的通义实验室研发的超大规模语言模型。我能够回答各种领域的问题，帮助用户创作文字、代码，还可以进行多轮对话、逻辑推理、编程等任务。如果你有任何问题或需要帮助，欢迎随时告诉我
```
## 接入 MCP 服务器
## 修改客户端文件
```
import json
import os
import sys
from openai import OpenAI
from loguru import logger
import asyncio
from typing import Optional
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters, stdio_client
from dotenv import load_dotenv
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam
load_dotenv()
class MCPClient:
    """
    MCP客户端类，用于管理与MCP服务器的连接和交互
    该类负责初始化客户端会话、处理聊天循环以及资源清理
    """
    def __init__(self):
        """
        初始化MCP客户端实例
        初始化客户端会话、异步退出栈和OpenAI客户端
        """
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.base_url = os.getenv("BASE_URL")  
        self.openai_api_key = os.getenv("OPEN_API_KEY")  
        self.model = os.getenv("MODEL")  
        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.base_url)  
    async def connect_to_server(self, server_script_path: str):
        """
        连接到服务器脚本并建立会话连接
        该函数支持连接到Python(.py)或JavaScript(.js)服务器脚本，通过stdio方式建立通信通道，
        并初始化客户端会话。
        参数:
            server_script_path (str): 服务器脚本文件的路径，必须是.py或.js文件
        返回值:
            无返回值
        异常:
            ValueError: 当服务器脚本不是.py或.js文件时抛出
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("服务器脚本必须是 .py 或 .js 文件")
        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))
        await self.session.initialize()
        response = await self.session.list_tools()
        tools = response.tools
        logger.info(f"已连接到服务器，支持以下工具:{[tool.name for tool in tools]}")
    async def process_query(self, query: str) -> str:
        """
        处理用户的查询请求，结合大模型和 MCP 工具完成回答。
        该方法首先将用户问题发送给大模型，并根据模型是否需要调用工具来决定下一步流程：
        - 如果模型要求调用工具，则解析工具调用信息并执行对应工具；
        - 执行完成后将结果反馈给模型生成最终回复。
        参数:
            query (str): 用户输入的查询字符串。
        返回:
            str: 模型生成的回答内容。
        """
        messages = [
            ChatCompletionSystemMessageParam(role="system", content="你是一个智能助手，帮助用户回答问题。"),
            ChatCompletionUserMessageParam(role="user", content=query)
        ]
        response = await self.session.list_tools()
        available_tools = [{
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema
            }
        } for tool in response.tools]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=available_tools
        )
        content = response.choices[0]
        if content.finish_reason == "tool_calls":
            tool_call = content.message.tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)
            result = await self.session.call_tool(tool_name, tool_args)
            logger.info(f"[调用工具] {tool_name} 传入参数是: {tool_args}")
            messages.append(content.message.model_dump())
            messages.append({
                "role": "tool",
                "content": result.content[0].text,
                "tool_call_id": tool_call.id,
            })
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            return response.choices[0].message.content
        return content.message.content
    async def chat_loop(self):
        """
        运行聊天循环
        持续接收用户输入并显示回显，直到用户输入'quit'退出
        支持异常处理以确保程序稳定性
        """
        logger.info("MCP 客户端已启动！")
        print("输入你的问题或输入 'quit' 退出。")
        while True:
            try:
                query = input("\n🧑‍🦲 [用户输入]: ").strip()
                if query.lower() == 'quit':
                    break
                response = await self.process_query(query)  
                print(f"\n🤖 [AI回答] ：{response}")
            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")
    async def cleanup(self):
        """
        清理资源
        关闭异步退出栈中管理的所有资源
        """
        await self.exit_stack.aclose()
async def main():
    """
    主函数，负责初始化MCP客户端并执行主要的程序逻辑
    该函数会解析命令行参数，连接到MCP服务器，启动聊天循环，
    并确保在程序结束时正确清理资源。
    参数:
        无
    返回值:
        无
    异常:
        可能抛出连接错误、网络异常等，这些将在client.cleanup()中被处理
    """
    client = MCPClient()
    try:
        if len(sys.argv) < 2:
            logger.error("请提供 MCP server 脚本路径，例如：python client.py server.py")
            return
        await client.connect_to_server('server.py')
        await client.chat_loop()
    finally:
        await client.cleanup()
if __name__ == "__main__":
    asyncio.run(main())
```
## 运行演示
```
(LangChainDemo) PS D:\PycharmProjects\LangChainDemo> uv run client.py server.py
2025-08-14 14:33:54.048 | INFO     | __main__:connect_to_server:78 - 已连接到服务器，支持以下工具:['get_weather']
2025-08-14 14:33:54.048 | INFO     | __main__:chat_loop:158 - MCP 客户端已启动！
输入你的问题或输入 'quit' 退出。
🧑‍🦲 [用户输入]: 你是谁                             
🤖 [AI回答] ：<think>
好的，用户问我“你是谁”，我需要回答我的身份。首先，我要确认用户的问题是关于我的身份介绍。根据之前提供的工具，用户可能希望我调用某个函数来回答，但这里的问题不需要调用天气函数。我应该直接回答，不需要使用工具。需要简洁明了地说明我是通义千问，由通义实验室开发，具备多轮对话和回答问题的能力。同时要保持口语化，避免使用Markdown格式，分步骤解释清楚。现在组织语言回复用户。
</think>
我是通义千问，是阿里巴巴集团旗下的通义实验室自主研发的超大规模语言模型。我具备多轮对话、知识问答、文本创作等能力，可以协助您回答问题、创作文字、逻辑推理以及编程等。如果您有任何问题，欢迎随时向我提问！
🧑‍🦲 [用户输入]: 上海天气怎么样
2025-08-14 13:10:34.522 | INFO     | __main__:process_query:103 - [调用工具] get_weather 传入参数是: {'city': 'Shanghai'}
🤖 [AI回答] ：<think>
好的，我需要处理用户提供的天气数据，并以自然的中文回复。首先，数据中的"weather"部分显示天气状况是多云（"多云"），温度是33.64摄氏度，体感温度更高，达到39.31摄氏度。湿度55%，风速5.6米/秒，云量38%。这些信息需要转化为易懂的句子。
用户可能关心的是当前的天气情况和是否需要采取措施，比如防晒或补水。因此，回复应包括温度、天气状况、体感温度，并给出相关的建议。同时，需注意使用口语化表达，避免机械化的描述。确保所有信息准确无误，并且符合用户的实际需求。
</think>
上海当前天气为多云，气温33.6℃，体感温度较高，达到39.3℃。建议做好防晒措施，并注意补充水分。湿度55%，风力5.6级，整体体感较为闷热，外出时可适当调整着装哦～
```
