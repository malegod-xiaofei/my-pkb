# 1 Windows安装Anaconda

- 前往Anaconda官网：

```properties
https://repo.anaconda.com/ 历史版本：https://repo.anaconda.com/archive/
```

- 版本选择：匹配自己的本机python，我这是python3.7，选择Anaconda3-5.3.1注：稳定版

![图片2.png](images/图片2.png)

  - 一步一步Next

![图片3.png](images/图片3.png)

![图片4.png](images/图片4.png)

  - 为所有用户安装

![图片5.png](images/图片5.png)

![图片6.png](images/图片6.png)

  - 第一项Add Anaconda… 这个是说将安装路径填入到系统环境变量中，我曾经选上，发现后期总是出现什么“无法定位到动态链接库”问题！！！（这里是自动添加系统环境变量，如果不选！！自己手动添加就好）
    - 手动配置conda环境变量,path下

```properties
D:\Software\Anaconda3
D:\Software\Anaconda3\Scripts
D:\Software\Anaconda3\Library\bin
CMD->conda查看是否配置成功
```

  - 第二项 是说要默认使用python的版本，选上！！

![图片7.png](images/图片7.png)

  - 跳过安装VScode，选择点击“skip”

![图片8.png](images/图片8.png)

  - 两个“learn”，都取消打勾

![图片9.png](images/图片9.png)

  - 打开Anaconda Prompt
    - 安装新的pytorch环境->conda create -n work python=3.7。并在PyCharm中配置Torch环境

# 2 Linux安装Anaconda

- 在Anaconda官网下载linux安装包
  - 官网：
- 使用wget下载完使用bash安装

```bash
bash Anaconda3-2025.06-0-Linux-x86_64.sh
```

- 然后不停回车，出现yes和no的时候输入yes，修改安装路径

```text
/home/work/zhaoyingfei/tools/anaconda3
```

- 使用nanob编辑器去修改bashrc这个文件

```bash
pwd
/home/work/zhaoyingfei/tools/anaconda3/bin
nano ~/.bashrc
# 在文件的最底下加上
export PATH="/home/work/zhaoyingfei/tools/anaconda3/bin:$PATH"
```

- Ctrl+x;y;回车；操作完使环境生效

```sql
source ~/.bashrc
```

- 1

# 3 Anaconda配置镜像源

- 配置Anaconda镜像
  - cmd 执行

```bash
# 清除现有配置中的 channels 设置
conda config --remove-key channels

# 按照优先级添加 channels
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2

# 如果需要，也可以添加 free 通道
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch

conda config --set show_channel_urls true
# 查看镜像地址
conda config --show channels
```

  - 重置conda配置

```bash
conda config --remove-key channels
conda config --remove-key pkgs_dirs
conda config --remove-key envs_dirs
conda config --remove-key default_channels
conda config --remove-key custom_channels
```

  - 或者拷贝到 C:\Users\你的用户名\.condarc

```bash
show_channel_urls: true
ssl_verify: true
channels:
  - pytorch
  - nvidia
  - defaults
  - conda-forge
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  nvidia: https://conda.anaconda.org
```

- 配置pip镜像
  - 打开 cmd 执行

```bash
mkdir %APPDATA%\pip
notepad %APPDATA%\pip\pip.ini
```

  - 在弹出的文件中输入

```bash
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
extra-index-url = https://mirrors.aliyun.com/pypi/simple

[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
               mirrors.aliyun.com
```

  - 查看是否生效

```bash
pip config list
```
