一、jupyter 安装

```bash
pip install notebook -i https://pypi.tuna.tsinghua.edu.cn/simple
```

二、jupyter 使用

- 修改默认浏览器和启动 jupyter 默认打开 google 浏览器

```bash
jupyter notebook --generate-config
```

  - 报错500：

```bash
pip install --upgrade --user nbconvert
```

  - 添加配置文件

```java
import webbrowser
webbrowser.register("chrome",None,webbrowser.GenericBrowser("C:/Users/赵迎飞/AppData/Local/Google/Chrome/Application/chrome.exe"))
c.NotebookApp.browser = 'chrome'
# 修改自动跳转浏览器
c.NotebookApp.open_browser = True
```

  - 配置工作目录

```properties
c.NotebookApp.notebook_dir = 'D:/Code/PyCharm-Project/AiApp'
```

  - 配置输出字节数，防止输出太大崩溃

```properties
## (bytes/sec) Maximum rate at which messages can be sent on iopub before they
#  are limited.
c.NotebookApp.iopub_data_rate_limit = 10000000
```

  - 大小写模糊匹配

```properties
c.IPCompleter.use_jedi = True
c.IPCompleter.case_sensitive = False  # 允许大小写模糊匹配
```

  - 保存并重启 jupyter

```bash
jupyter notebook
```

三、启动指定 python 环境的 jupyter

- cmd中输入 activate 即可进入 Anaconda 设定的虚拟环境中
- 切换工作环境为 Anaconda 指定的 python 环境

```bash
conda activate work
conda activate py2
conda activate pytorch
```

- 启动 jupyter

```bash
jupyter notebook
```

4.3 jupyter输出太大可能导致崩溃问题【了解】

如果遇到

```text
IOPub data rate exceeded.
    The notebook server will temporarily stop sending output
    to the client in order to avoid crashing it.
    To change this limit, set the config variable
    `--NotebookApp.iopub_data_rate_limit`.
```

这个问题是在jupyer当中对输出的字节数有限制，需要去修改配置文件

创建配置文件

```bash
jupyter notebook --generate-config
vi ~/.jupyter/jupyter_notebook_config.py
```

取消注释,多增加

```properties
## (bytes/sec) Maximum rate at which messages can be sent on iopub before they
#  are limited.
c.NotebookApp.iopub_data_rate_limit = 10000000
```

# 1 但是不建议这样去修改，jupyter输出太大会崩溃
