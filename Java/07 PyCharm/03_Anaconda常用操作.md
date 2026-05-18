# 第 1 章 Windows 操作

- cmd中输入 activate 即可进入 Anaconda 设定的虚拟环境中
- 创建环境

```
# 创建环境
conda create -n py2 python=2.7 -c anaconda
conda create -n aiapp python=3.6 -c anaconda
conda create --name py372 python=3.7.2 -c anaconda
# 查看环境
conda env list
# 查看 python 版本
python --version
# 删除环境
conda env remove --name work
# 导出 conda 配置
conda list --explicit > C:\Users\赵迎飞\Desktop\pytorch_env.txt
conda env export --no-builds > C:\Users\赵迎飞\Desktop\environment.yml
# 创建新环境
conda create --name py372 --file C:\Users\赵迎飞\Desktop\pytorch_env.txt
# 使用导出的 yml 文件创建 conda 环境
conda env create -f C:\Users\赵迎飞\Desktop\environment.yml
# 通过文件安装环境
conda install -n py372 --file C:\Users\赵迎飞\Desktop\pytorch_env.txt
```

- 然后进入指定的 pytorch 环境

```
conda activate base
conda activate work
conda activate py2
conda activate py37
conda activate pytorch
conda activate paddle25
jupyter notebook --notebook-dir="D:/Code/PycharmProjects/NewBee"

conda create -n work python=3.9 -c defaults
conda activate work
conda install pytorch torchvision pandas
pip install internimage
pip install torch torchvision pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- 安装第三方包

```
安装 Jupyter
pip install notebook==6.5.7 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install jupyterthemes -i https://pypi.tuna.tsinghua.edu.cn/simple
打开 Jupyter
jupyter notebook your_notebook.ipynb
重新安装 notebook
pip uninstall notebook

conda install paddle
或者
pip install paddle
conda install paddlepaddle==2.5.1 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/
pip install openpyxl==3.1.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install xlrd==2.0.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install gensim -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyspark -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install selenium==4.11.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install urllib3==1.26.16 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install tqdm -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyspark -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install py2neo -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install config -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyhanlp -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install Flask==2.0.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install Flask-SocketIO==4.3.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install werkzeug==1.0.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install keras==2.3.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install timm
pip install aiohttp==3.8.6 aiosignal==1.3.1 frozenlist==1.3.3 async-timeout==4.0.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install tenacity==8.2.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install streamlit==1.35.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install webdriver-manager==3.8.6 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pybind11==2.10.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install openai==0.28.1
pip install python-dotenv==1.0.0
pip install mcp==0.1.2
# 安装黑马环境
pip install matplotlib==2.2.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install numpy==1.14.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pandas==0.20.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install tables==3.4.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install jupyter==1.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install scikit-learn==0.19.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install maturin
pip install scipy
pip install autopep8
pip install imbalanced-learn -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install jieba
pip install seaborn -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install hmmlearn==0.2.7 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install faiss-cpu -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyarrow==1.0.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install fsspec==12.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install xgboost==1.5.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install lightgbm==3.3.5 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install chardet==4.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install plotly==5.10.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install jedi==0.17.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install jupyterlab==2.3.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install jupyter_contrib_nbextensions==0.5.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pydot==1.4.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install graphviz==0.16 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install tensorflow==2.3.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install torchvision==0.14.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
# 安装 Graphviz
winget install -e --id Graphviz.Graphviz -v 2.38

pip install dask==2.30.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install selenium==3.141.0
```

- 卸载重新安装

```bash
pip uninstall openpyxl
```

- 如果安装sklen报错，使用下方命令更新 scipy 和 numpy

```bash
pip install --upgrade scipy
pip install --upgrade numpy scipy
pip install --upgrade scikit-learn pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- 安装TensorFlow

```bash
pip install tensorflow-gpu==2.3.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- 查看环境包信息

```bash
conda list
```

- 配置镜像

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch、
conda config --set show_channel_urls true
# 查看镜像地址
conda config --show channels
```

- 创建python环境

```bash
conda create -n work python=3.7
# 下载环境失败的话临时忽略 ssl 验证
conda config --set ssl_verify false
```

- 配置pycharm环境

![图片10.png](images/图片10.png)

Nvidia：Alt＋R等于性能图层

# 第 2 章 Linux

- 初始化 Anaconda

```
source /home/work/anaconda3/bin/activate
```

- 创建 Anaconda 环境

```bash
conda create --name py2.7 python=2.7 -c anaconda
```

- 激活环境

```bash
conda activate py2.7
```

- 使用 Anaconda 环境运行 python 程序

```
ldd --version
conda create --name py35 python=3.5 -c anaconda
conda activate py35
conda env remove --name py35

pip install torch==1.8.0 torchvision==0.9.0 timm==0.4.5 pillow==8.0.0 requests==2.25.0

conda install pytorch==1.8.0 torchvision==0.9.0 cpuonly -c pytorch
pip install timm==0.4.5 pillow==8.0.0 requests==2.25.0
```
