# Ollama

Ollama是一个用于本地部署运行大模型的工具，类似Docker，可以在本地拉取、管理、运行大模型，推送大模型到远程服务器。

# 安装

安装步骤：

1. 从官网下载Ollama安装包：[https://ollama.com/](https://ollama.com/)
github地址：[https://github.com/ollama/ollama](https://github.com/ollama/ollama)
2. 进入命令行进行安装（否则会直接安装到C盘），/DIR 指定安装路径：
```bash
OllamaSetup.exe /DIR="D:\\Software\\Ollama"
```

配置环境变量：

默认情况下，Ollama下载的大模型会下载到C盘。可以配置环境变量
**OLLAMA_MODELS**来指定下载到本地的路径。

其他环境变量，可以通过命令查看：

```bash
ollama serve -h
```

例如 **OLLAMA_HOST**（配置ollama的http绑定地址）等
获取帮助：可以通过帮助来查看所有命令

```bash
ollama help
```

# 拉取、运行大模型

拉取、运行大模型：（类似docker命令）

1. 从Ollama官网查看所有支持的大模型：[https://ollama.com/search](https://ollama.com/search)
2. 点击需要拉取的模型，页面会提示运行该模型的命令，例如
```bash
# 与docker一样，可以指定tag，不指定tag时默认为latest
ollama run deepseek-r1
```

运行大模型时，如果该模型没有下载，则会先进行拉取。
如果只拉取，不想运行，可以执行：

```bash
ollama pull xxxx:xxxx
```

# 其他命令

查看运行的大模型：

```bash
ollama ps
```

查看拉取的大模型：

```bash
ollama list
```

启动ollama服务，接收http请求：

```bash
ollama serve
```

默认地址为127.0.0.1:11434，可以通过**OLLAMA_HOST**环境变量配置。请求时的BaseURL：[http://localhost:11434](http://localhost:11434/)
