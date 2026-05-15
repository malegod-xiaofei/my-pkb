# 6 PyTorch简介

## 6.1 什么是PyTorch

PyTorch是一个开源的Python机器学习库，基于Torch库（一个有大量机器学习算法支持的科学计算框架，有着与Numpy类似的张量（Tensor）操作，采用的编程语言是Lua），底层由C++实现，应用于人工智能领域，如计算机视觉和自然语言处理。

PyTorch主要有两大特征：

- 类似于NumPy的张量计算，能在GPU或MPS等硬件加速器上加速。
- 基于带自动微分系统的深度神经网络。

PyTorch官网：。

## 6.2 PyTorch安装

PyTorch分为CPU和GPU版本。

PyTorch选择安装版本页面：。

![图片55.png](images/图片55.png)

### 6.2.1 CPU版本PyTorch安装

直接通过pip命令安装即可：pip3 install torch torchvision torchaudio。

若需要离线安装，可以考虑下载whl包然后自行安装。下载whl的链接：。

手动下载whl时，需要注意PyTorch与torchvision之间版本对应关系。可以到或查看。

![图片56.png](images/图片56.png)

### 6.2.2 GPU版本PyTorch安装

绝大多数情况下我们会安装GPU版本的PyTorch。目前PyTorch不仅支持NVIDIA的GPU，还支持AMD的ROCm的GPU。

安装GPU版本的PyTorch步骤：

- 根据NVIDIA驱动程序版本和要安装的PyTorch版本，确定安装哪个版本的CUDA。
- 根据安装好的CUDA版本，安装对应版本的PyTorch。

#### 6.2.2.1 GPU计算能力要求

对于N卡，需要计算能力（compute capability）≥3.0。

![图片57.png](images/图片57.png)

可在查看GPU计算能力。

#### 6.2.2.2 CUDA版本选择

CUDA（Compute Unified Device Architecture）是NVIDIA开发的并行计算平台和编程平台，允许开发者利用NVIDIA GPU的强大计算能力进行通用计算。CUDA不仅用于图形渲染，还广泛应用于科学计算、深度学习、金融建模等领域。

##### 6.2.2.2.1 根据NVIDIA驱动程序版本确定支持的最高CUDA版本

打开NVIDIA控制面板→系统信息→组件，查看NVCUDA64.DLL的产品名称栏，可查看驱动程序支持的最高CUDA版本。

![图片58.png](images/图片58.png)

或在命令行中输入nvidia-smi，在CUDA Version栏查看支持的最高CUDA版本。

![图片59.png](images/图片59.png)

##### 6.2.2.2.2 根据PyTorch版本选择CUDA版本

需要安装特定版本的CUDA版本，才能使用特定版本的PyTorch。在PyTorch下载页面可查看该版本PyTorch支持的CUDA版本。

![图片60.png](images/图片60.png)

或在查看过往版本PyTorch支持的CUDA版本。

例如：

![图片61.png](images/图片61.png)

此处的cu126表示支持CUDA12.6版本。

#### 6.2.2.3 CUDA安装（可选）

NVIDIA官网通常只展示最新的CUDA版本，过往CUDA版本可在下载。

选择相应CUDA版本后，选择要安装的平台，Installer Type安装方式选择exe(local)本地安装。

![图片62.png](images/图片62.png)

双击.exe文件进行安装，首先需要输入临时解压路径，临时解压路径在安装结束后会自动被删除，保持默认即可。点击OK。

![图片63.png](images/图片63.png)

若在系统检查环节提示“您正在安装老版本的驱动程序…”，说明安装包中包含的驱动程序版本比当前已安装的驱动程序的版本旧，可忽略。点击继续。

![图片64.png](images/图片64.png)

同意安装协议并继续。

![图片65.png](images/图片65.png)

选择精简，会安装所有组件并覆盖现有驱动程序。点击下一步。

![图片66.png](images/图片66.png)

如果出现以下提示，表明缺少Visual Studio，部分组件不能正常工作。不用在意，选择I understand…。点击Next。

![图片67.png](images/图片67.png)

点击下一步。

![图片68.png](images/图片68.png)

安装完成，点击关闭。

![图片69.png](images/图片69.png)

可在命令行使用nvcc --version查看CUDA版本信息。

![图片70.png](images/图片70.png)

#### 6.2.2.4 PyTorch安装

新建一个虚拟环境来安装PyTorch。

在命令行输入conda create -n pytorch-2.6.0-gpu python=3.12创建一个环境名为pytorch-2.6.0-gpu，Python版本为3.12的虚拟环境。

使用conda activate pytorch-2.6.0-gpu激活pytorch-2.6.0-gpu虚拟环境。

在官网选择要安装的版本，复制命令，在命令行中执行以安装PyTorch。

![图片71.png](images/图片71.png)

若安装速度较慢或安装失败，可配置pip的国内镜像源pip config set global.index-url 。

要在新的虚拟环境中使用Jupyter Notebook，需使用conda install jupyter notebook安装。

编写代码时需在IDE中选择新创建的虚拟环境作为Python解释器。

## 6.3 张量创建

Tensor（张量）是PyTorch的核心数据结构。张量在不同学科中有不同的意义，在深度学习中张量表示一个多维数组，是标量、向量、矩阵的拓展。如一个RGB图像的数组就是一个三维张量，第1维是图像的高，第2维是图像的宽，第3维是图像的颜色通道。

### 6.3.1 基本张量创建

#### 6.3.1.1 torch.tensor(data)创建指定内容的张量

```python
import torch
import numpy as np

# 创建标量张量
tensor1 = torch.tensor(10)
print(tensor1)

# 使用列表创建张量
tensor2 = torch.tensor([1, 2, 3])
print(tensor2)

# 使用numpy创建张量
tensor3 = torch.tensor(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(tensor3)
```

#### 6.3.1.2 torch.Tensor(size)创建指定形状的张量

```python
import torch

# 创建指定形状的张量，默认类型为float32
tensor1 = torch.Tensor(3, 2, 4)
print(tensor1)
print(tensor1.dtype)

# 也可以用来创建指定内容的张量
tensor2 = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
print(tensor2)
```

#### 6.3.1.3 创建指定类型的张量

```python
可通过torch.IntTensor()、torch.FloatTensor()等创建。
或在torch.tensor()中通过dtype参数指定类型。
import torch

# 创建int32类型的张量
tensor1 = torch.IntTensor(2, 3)
tensor2 = torch.tensor([1, 2, 3], dtype=torch.int32)
print(tensor1)
print(tensor2)

# 元素类型不匹配则会进行类型转换
tensor1 = torch.IntTensor([1.1, 2.2, 3.6])
tensor2 = torch.tensor([3.1, 2.2, 1.6], dtype=torch.int32)
print(tensor1)
print(tensor2)

# 创建int64类型的张量
tensor1 = torch.LongTensor([1, 2, 3])
tensor2 = torch.tensor([1, 2, 3], dtype=torch.int64)
print(tensor1, tensor1.dtype)
print(tensor2, tensor1.dtype)

# 创建int16类型的张量
tensor1 = torch.ShortTensor(2, 2)
tensor2 = torch.tensor([1, 2, 3], dtype=torch.int16)
print(tensor1, tensor1.dtype)
print(tensor2, tensor1.dtype)

# 创建float32类型的张量
tensor1 = torch.FloatTensor([9, 8, 7])
tensor2 = torch.tensor([1, 2, 3], dtype=torch.float32)
print(tensor1, tensor1.dtype)
print(tensor2, tensor1.dtype)

# 创建float64类型的张量
tensor1 = torch.DoubleTensor(2, 3, 1)
tensor2 = torch.tensor([1, 2, 3], dtype=torch.float64)
print(tensor1)
print(tensor2)
```

### 6.3.2 指定区间的张量创建

#### 6.3.2.1 torch.arange(start, end, step)在区间内按步长创建张量

```python
import torch

# torch.arange(start, end, step) 在区间[start,end)中创建步长为step的张量
tensor1 = torch.arange(10, 30, 2)
print(tensor1)

# torch.arange(end) 创建区间为[0,end)，步长为1的张量
tensor2 = torch.arange(6)
print(tensor2)
```

#### 6.3.2.2 torch.linspace(start, end, steps)在区间内按元素数量创建张量

```python
import torch

# torch.linspace(start, end, steps) 在区间按元素数量创建张量
tensor1 = torch.linspace(10, 30, 5)
print(tensor1)
```

#### 6.3.2.3 torch.logspace(start, end, steps, base)在指数区间内按指定底数创建张量

```python
import torch

# torch.logspace(start, end, steps, base) 在区间[start,end]之间生成steps个数，并以base为底，区间内的数为指数创建张量
tensor1 = torch.logspace(1, 3, 3, 2)
print(tensor1)
```

### 6.3.3 按数值填充张量

- torch.zeros(size)创建指定形状的全0张量
- torch.ones(size)创建指定形状的全1张量
- torch.full(size, value)创建指定形状的按指定值填充的张量
- torch.empty(size)创建指定形状的未初始化的张量
- torch.zeros_like(input)创建与给定张量形状相同的全0张量
- torch.ones_like(input)创建与给定张量形状相同的全1张量
- torch.full_like(input, value)创建与给定张量形状相同的按指定值填充的张量
- torch.empty_like(input)创建与给定张量形状相同的未初始化的张量

```python
import torch

# torch.zeros(size) 创建指定形状的全0张量
tensor1 = torch.zeros(2, 3)
print(tensor1)

# torch.ones_like(input) 创建与给定张量形状相同的全1张量
tensor2 = torch.ones_like(tensor1)
print(tensor2)

# torch.full(size,fill_value) 创建指定形状的按指定值填充的张量
tensor1 = torch.full((2, 3), 6)
print(tensor1)

# torch.empty_like(input) 创建与给定张量形状相同的未初始化的张量
tensor2 = torch.empty_like(tensor3)
print(tensor2)
```

- torch.eye(n, [m])创建单位矩阵

```python
import torch

# torch.eye(n) 创建n*n的单位矩阵
tensor1 = torch.eye(3)
print(tensor1)

# torch.eye(n, m) 按指定的行和列创建
tensor2 = torch.eye(3, 4)
print(tensor2)
```

### 6.3.4 随机张量创建

- torch.rand(size)创建在[0,1)上均匀分布的，指定形状的张量
- torch.randint(low, high, size)创建在[low,high)上均匀分布的，指定形状的张量
- torch.randn(size)创建标准正态分布的，指定形状的张量
- torch.normal(mean,std,size)创建自定义正态分布的，指定形状的张量
- torch.rand_like(input)创建在[0,1)上均匀分布的，与给定张量形状相同的张量
- torch.randint_like(input, low, high)创建在[low,high)上均匀分布的，与给定张量形状相同的张量
- torch.randn_like(input)创建标准正态分布的，与给定张量形状相同的张量

```python
import torch

# torch.rand(size) 创建在[0,1)上均匀分布的，指定形状的张量
tensor1 = torch.rand(2, 3)
print(tensor1)

# torch.rand_like(input) 创建在[0,1)上均匀分布的，与给定张量形状相同的张量
tensor2 = torch.randint_like(tensor1, 1, 10)
print(tensor2)

# torch.randn(size) 创建标准正态分布的，指定形状的张量
tensor1 = torch.randn(4, 2)
print(tensor1)

# torch.normal(mean,std,size) 创建自定义正态分布的，指定形状的张量。mean为均值，std为标准差
tensor2 = torch.normal(5, 1, tensor1.shape)
print(tensor2)
```

- torch.randperm(n)生成从0到n-1的随机排列，类似洗牌

```python
import torch

# torch.randperm(n) 生成从0到n-1的随机排列
tensor1 = torch.randperm(10)
print(tensor1)
```

- torch.random.initial_seed()查看随机数种子
- torch.manual_seed(seed)设置随机数种子

```python
import torch

# 查看随机数种子
print(torch.random.initial_seed())
# 设置随机数种子
torch.manual_seed(42)
print(torch.random.initial_seed())
```

## 6.4 张量转换

### 6.4.1 张量元素类型转换

#### 6.4.1.1 Tensor.type(dtype)修改张量的类型

```python
import torch

tensor1 = torch.tensor([1, 2, 3])
print(tensor1, tensor1.dtype)

# 使用type方法修改张量的类型
tensor1 = tensor1.type(torch.float32)
print(tensor1, tensor1.dtype)
```

#### 6.4.1.2 Tensor.double()等修改张量的类型

```python
import torch

tensor1 = torch.tensor([1, 2, 3])
print(tensor1, tensor1.dtype)

# 使用double方法修改张量的类型
tensor1 = tensor1.double()
print(tensor1)
# 使用long方法修改张量的类型
tensor1 = tensor1.long()
print(tensor1, tensor1.dtype)
```

### 6.4.2 Tensor与ndarray转换

#### 6.4.2.1 Tensor.numpy()将Tensor转换为ndarray，共享内存。使用copy()避免共享内存

```python
import torch

# 使用numpy()方法将Tensor转换为ndarray，共享内存
tensor1 = torch.rand(3, 2)
numpy_array = tensor1.numpy()
print(tensor1)
print(numpy_array)
print(type(tensor1), type(numpy_array))
print()
tensor1[:, 0] = 4
print(tensor1)
print(numpy_array)
print()

# 使用copy()方法避免共享内存
numpy_array = tensor1.numpy().copy()
tensor1[:, 0] = -1
print(tensor1)
print(numpy_array)
```

#### 6.4.2.2 torch.from_numpy(ndarray)将ndarray转换为Tensor，共享内存。使用copy()避免共享内存

```python
import torch
import numpy as np

# 使用from_numpy()方法将ndarray转换为Tensor，共享内存
numpy_array = np.random.randn(3)
tensor1 = torch.from_numpy(numpy_array)
print(numpy_array)
print(tensor1)
print()
numpy_array[0] = 100
print(numpy_array)
print(tensor1)
print()

# 使用copy()方法避免共享内存
tensor1 = torch.from_numpy(numpy_array.copy())
numpy_array[0] = -1
print(numpy_array)
print(tensor1)
```

#### 6.4.2.3 torch.tensor(ndarray)将ndarray转换为Tensor，不共享内存

```python
import torch
import numpy as np

# 使用torch.tensor()将ndarray转换为Tensor
numpy_array = np.random.randn(3)
tensor1 = torch.tensor(numpy_array)
print(numpy_array)
print(tensor1)
print()
numpy_array[0] = 100
print(numpy_array)
print(tensor1)
```

### 6.4.3 Tensor与标量转换

若张量中只有1个元素，Tensor.item()可提取张量中元素为标量。

```python
import torch

tensor1 = torch.tensor(1)
print(tensor1)
print(tensor1.item())
```

## 6.5 张量数值计算

### 6.5.1 基本运算

#### 6.5.1.1 四则运算

- +、-、*、/加减乘除
- add()、sub()、mul()、div()加减乘除，不改变原数据
- add_()、sub_()、mul_()、div_()加减乘除、修改原数据

```python
import torch

tensor1 = torch.randint(1, 9, (2, 3))
print(tensor1)
print(tensor1 + 10)
print()

# add()，不修改原数据
print(tensor1.add(10))
print(tensor1)
print()

# add_()，修改原数据
print(tensor1.add_(10))
print(tensor1)
```

#### 6.5.1.2 -、neg()、neg_()取负

```python
import torch

tensor1 = torch.tensor([1, 2, 3])
print(-tensor1)
print()

print(tensor1.neg())
print(tensor1)
print()

print(tensor1.neg_())
print(tensor1)
```

#### 6.5.1.3 **、pow()、pow_()求幂

```python
import torch

tensor1 = torch.tensor([1, 2, 3])
print(tensor1**2)
print()

print(tensor1.pow(2))
print(tensor1)
print()

print(tensor1.pow_(2))
print(tensor1)
```

#### 6.5.1.4 sqrt()、sqrt_()求平方根

```python
import torch

tensor1 = torch.tensor([1.0, 2.0, 3.0])
print(tensor1.sqrt())
print(tensor1)
print()

print(tensor1.sqrt_())
print(tensor1)
```

#### 6.5.1.5 exp()、exp_()以e为底数求幂

```python
import torch

tensor1 = torch.tensor([1.0, 2.0, 3.0])
print(2.71828183**tensor1)
print()

print(tensor1.exp())
print(tensor1)
print()

print(tensor1.exp_())
print(tensor1)
```

#### 6.5.1.6 log()、log_()以e为底求对数

```python
import torch

tensor1 = torch.tensor([1.0, 2.0, 3.0])
print(tensor1.log())
print(tensor1)
print()

print(tensor1.log_())
print(tensor1)
```

### 6.5.2 哈达玛积（元素级乘法）

两个矩阵对应位置元素相乘称为哈达玛积（Hadamard product）。

使用*、mul()实现两个形状相同的张量之间对位相乘。

```python
import torch

tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[1, 2], [3, 4]])
print(tensor1 * tensor2)
print(tensor1.mul(tensor2))
```

### 6.5.3 矩阵乘法运算

mm()严格用于二维矩阵相乘。

@、matmul()支持多维张量，按最后两个维度做矩阵乘法，其他维度相同，或者至少一个张量对应维度为1，广播后进行运算。

```python
import torch

# 2维矩阵的矩阵乘法
tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
print(tensor1)
print(tensor2)
print(tensor1.mm(tensor2))
print(tensor1 @ tensor2)
print(tensor1.matmul(tensor2))
print()

# 3维张量的矩阵乘法
tensor1 = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[6, 5, 4], [3, 2, 1]]])
tensor2 = torch.tensor([[[1, 2], [3, 4], [5, 6]], [[6, 5], [4, 3], [2, 1]]])
print(tensor1)
print(tensor2)
print(tensor1 @ tensor2)
print(tensor1.matmul(tensor2))
```

### 6.5.4 节省内存

运行一些操作时可能导致为新的结果分配内存，例如X=X@Y，发现id(X)会指向另一个位置，这是因为Python首先计算X@Y，为结果分配新的内存，再令X指向内存中的新位置。

```python
import torch

X = torch.randint(1, 9, (3, 2, 4))
Y = torch.randint(1, 9, (3, 4, 1))
print(id(X))
X = X @ Y
print(id(X), end="\n\n")
```

如果后续X不再重复使用，可以使用X[:] = X @ Y来减少内存开销。

```python
import torch

X = torch.randint(1, 9, (3, 2, 4))
Y = torch.randint(1, 9, (3, 4, 1))
print(id(X))
X[:] = X @ Y
print(id(X))
```

## 6.6 张量运算函数

常见运算函数：

sum()求和

mean()求均值

max()/min()求最大/最小值及其索引

argmax()/argmin()求最大值/最小值的索引

std()求标准差

unique()去重

sort()排序

```python
import torch

tensor1 = torch.randint(1, 9, (3, 2, 4))
tensor1 = tensor1.float()
print(tensor1)
print()

# sum() 求和
print("求和")
print(tensor1.sum())
```

print("按第0个维度求和")

```python
print(tensor1.sum(dim=0))
print()

# mean() 求均值)
print("求均值")
print(tensor1.mean())
```

print("按第1个维度求均值")

```python
print(tensor1.mean(dim=1))
print()

# max() 求最大值
print("求最大值")
print(tensor1.max())
```

print("按第2个维度求最大值与索引")

```python
print(tensor1.max(dim=2))
print()

# argmin() 求最小值索引
print("求最小值索引")
print(tensor1.argmin())
print()

# std() 求标准差
print("求标准差")
print(tensor1.std())
print()

# unique() 去重
print("去重")
print(tensor1.unique())
print()

# sort() 排序
print("排序")
print(tensor1.sort())
```

## 6.7 张量索引操作

### 6.7.1 简单索引

```python
import torch

tensor1 = torch.randint(1, 9, (3, 5, 4))
print(tensor1)
print()

# 取 第0维第0
print(tensor1[0])
print()

# 取 第0维所有，第1维第1
print(tensor1[:, 1])
print()

# 取 第0维所有，第1维第1，第2维第3
print(tensor1[2, 1, 3])
```

### 6.7.2 范围索引

```python
import torch

tensor1 = torch.randint(1, 9, (3, 5, 4))
print(tensor1)
print()

# 取 第0维第1到最后
print(tensor1[1:])
print()

# 取 第0维最后，第1维1到3(包含3),第2维0到2(包含2)
print(tensor1[-1:, 1:4, 0:3])
print()
```

### 6.7.3 列表索引

```python
import torch

tensor1 = torch.randint(1, 9, (3, 5, 4))
print(tensor1)
print()

# 取 第0维第0，第1维第1 和 第0维第1，第1维第2
print(tensor1[[0, 1], [1, 2]])
print()

# 取 第0维第0，第1维第1、2 和 第0维第1，第1维第1、2
print(tensor1[[[0], [1]], [1, 2]])
```

### 6.7.4 布尔索引

```python
import torch

tensor1 = torch.randint(1, 9, (3, 5, 4))
print(tensor1)
print()

# 取 第2维第0大于5的，返回(dim0,dim1)形状的索引
print(tensor1[:, :, 0] > 5)
print(tensor1[tensor1[:, :, 0] > 5])
print()

# 取 第1维第1大于5的，返回(dim0,dim2)形状的索引
mask = tensor1[:, 1, :] > 5
print(mask)
tensor2 = tensor1.permute(0, 2, 1)  # 转换维度为(dim0,dim2,dim1)
print(tensor2[mask])
tensor2 = tensor2[mask].permute(1, 0)  # 转换维度为(dim1,?)
print(tensor2)
print()

# 取 第1维第1，第2维第2大于5的，返回(dim0)形状的索引
print(tensor1[:, 1, 2] > 5)
print(tensor1[tensor1[:, 1, 2] > 5])
```

## 6.8 张量形状操作

### 6.8.1 交换维度

#### 6.8.1.1 transpose()交换两个维度

```python
import torch

tensor1 = torch.randint(1, 9, (2, 3, 6))
print(tensor1)
print(tensor1.transpose(1, 2))  # 交换第1维和第2维
```

#### 6.8.1.2 permute()重新排列多个维度

```python
import torch

tensor1 = torch.randint(1, 9, (2, 3, 6))
print(tensor1)
print(tensor1.permute(2, 0, 1))  # (2, 3, 6)->(6, 2, 3)
```

### 6.8.2 调整形状

#### 6.8.2.1 reshape()调整张量的形状

```python
import torch

tensor1 = torch.randint(1, 9, (3, 5, 4))
print(tensor1)
print(tensor1.reshape(6, 10))
print(tensor1.reshape(3, -1))
```

#### 6.8.2.2 view()调整张量的形状，需要内存连续。共享内存

is_contiguous()判断是否内存连续

contiguous()转换为内存连续

```python
import torch

tensor1 = torch.randint(1, 9, (3, 5, 4))
print(tensor1)
print(tensor1.is_contiguous())  # is_contiguous()判断是否内存连续
print(tensor1.view(-1, 10))

tensor1 = tensor1.T
print(tensor1.is_contiguous())  # is_contiguous()判断是否内存连续
print(tensor1.contiguous().view(-1))  # contiguous()强制内存连续
```

### 6.8.3 增加或删除维度

#### 6.8.3.1 unsqueeze()在指定维度上增加1个维度

```python
import torch

tensor1 = torch.tensor([1, 2, 3, 4, 5])
print(tensor1)
# 在0维上增加一个维度
print(tensor1.unsqueeze(dim=0))
# 在1维上增加一个维度
print(tensor1.unsqueeze(dim=1))
# 在-1维上增加一个维度
print(tensor1.unsqueeze(dim=-1))
```

#### 6.8.3.2 squeeze()删除大小为1的维度

```python
import torch

tensor1 = torch.tensor([1, 2, 3, 4, 5])
print(tensor1.unsqueeze_(dim=0))
print(tensor1.squeeze())
```

## 6.9 张量拼接操作

#### 6.9.0.1 torch.cat()张量拼接，按已有维度拼接。除拼接维度外，其他维度大小须相同

```python
import torch

tensor1 = torch.randint(1, 9, (2, 2, 5))
tensor2 = torch.randint(1, 9, (2, 1, 5))
print(tensor1)
print(tensor2)
print(torch.cat([tensor1, tensor2], dim=1))
```

#### 6.9.0.2 torch.stack()张量堆叠，按新维度堆叠。所有张量形状必须一致

```python
import torch

torch.manual_seed(42)
tensor1 = torch.randint(1, 9, (3, 1, 5))
tensor2 = torch.randint(1, 9, (3, 1, 5))
print(tensor1)
print(tensor2)
tensor3 = torch.stack([tensor1, tensor2], dim=2)
print(tensor3)
print(tensor3.shape)
```

## 6.10 自动微分模块

训练神经网络时，框架会根据设计好的模型构建一个计算图（computational graph），来跟踪计算是哪些数据通过哪些操作组合起来产生输出，并通过反向传播算法来根据给定参数的损失函数的梯度调整参数（模型权重）。

PyTorch具有一个内置的微分引擎torch.autograd以支持计算图的梯度自动计算。

考虑最简单的单层神经网络，具有输入x、参数w、偏置b以及损失函数：

![图片72.png](images/图片72.png)

```python
import torch

# 输入x
x = torch.tensor(10.0)
# 目标值y
y = torch.tensor(3.0)

# 初始化权重w
w = torch.rand(1, 1, requires_grad=True)
# 初始化偏置b
b = torch.rand(1, 1, requires_grad=True)
z = w * x + b
# 设置损失函数
loss = torch.nn.MSELoss()
loss_value = loss(z, y)
# 反向传播
loss_value.backward()
# 打印w,b的梯度
print("w的梯度:\n", w.grad)
print("b的梯度:\n", b.grad)
```

该计算图中x、w、b为叶子节点，即最基础的节点。叶子节点的数据并非由计算生成，因此是整个计算图的基石，叶子节点张量不可以执行in-place操作。而最终的loss为根节点。

可通过is_leaf属性查看张量是否为叶子节点：

```python
print(x.is_leaf)  # True
print(w.is_leaf)  # True
print(b.is_leaf)  # True
print(z.is_leaf)  # False
print(y.is_leaf)  # True
print(loss_value.is_leaf)  # False
```

自动微分的关键就是记录节点的数据与运算。数据记录在张量的data属性中，计算记录在张量的grad_fn属性中。

计算图根据搭建方式可分为静态图和动态图，PyTorch是动态图机制，在计算的过程中逐步搭建计算图，同时对每个Tensor都存储grad_fn供自动微分使用。

若设置张量参数requires_grad=True，则PyTorch会追踪所有基于该张量的操作，并在反向传播时计算其梯度。依赖于叶子节点的节点，requires_grad默认为True。当计算到根节点后，在根节点调用backward()方法即可反向传播计算计算图中所有节点的梯度。

非叶子节点的梯度在反向传播之后会被释放掉（除非设置参数retain_grad=True）。而叶子节点的梯度在反向传播之后会保留（累积）。通常需要使用optimizer.zero_grad()清零参数的梯度。

有时我们希望将某些计算移动到计算图之外，可以使用Tensor.detach()返回一个新的变量，该变量与原变量具有相同的值，但丢失计算图中如何计算原变量的信息。换句话说，梯度不会在该变量处继续向下传播。例如：

```python
import torch

x = torch.ones(2, 2, requires_grad=True)
y = x * x
# 分离y来返回一个新变量u
u = y.detach()
z = u * x
# 梯度不会向后流经u到x
z.sum().backward()
# 反向传播函数计算z=u*x关于x的偏导数时将u作为常数处理，而不是z=x*x*x关于x的偏导数
```

x.grad == u

```python
# tensor([[True, True],
#         [True, True]])
```

## 6.11 机器学习案例：线性回归

在此虚拟环境中没有matplotlib，先安装：pip install matplotlib==3.9。

通过PyTorch训练一个模型一般分为以下4个步骤：

准备数据 → 构建模型 → 定义损失函数与优化器 → 模型训练

接下来，构建数据集并使用PyTorch实现线性回归：

```python
import torch
import matplotlib.pyplot as plt
from torch import nn, optim  # 模型、损失函数和优化器
from torch.utils.data import TensorDataset, DataLoader  # 数据集和数据加载器

# 构建数据集
X = torch.randn(100, 1)  # 输入
w = torch.tensor([2.5])  # 权重
b = torch.tensor([5.2])  # 偏置
noise = torch.randn(100, 1) * 0.1  # 噪声
y = w * X + b + noise  # 目标
dataset = TensorDataset(X, y)  # 构造数据集对象
dataloader = DataLoader(
```

dataset, batch_size=10, shuffle=True

)  # 构造数据加载器对象，batch_size为每次训练的样本数，shuffle为是否打乱数据

```python
# 构造模型
model = nn.Linear(in_features=1, out_features=1)  # 线性回归模型，1个输入，1个输出

# 损失函数和优化器
loss = nn.MSELoss()  # 均方误差损失函数
optimizer = optim.SGD(model.parameters(), lr=1e-3)  # 随机梯度下降，学习率0.001

# 模型训练
loss_list = []
for epoch in range(1000):
    total_loss = 0
    train_num = 0
    for x_train, y_train in dataloader:
        # 每次训练一个batch大小的数据
        y_pred = model(x_train)  # 模型预测
        loss_value = loss(y_pred, y_train)  # 计算损失
        total_loss += loss_value.item()
        train_num += len(y_train)
        optimizer.zero_grad()  # 梯度清零
        loss_value.backward()  # 反向传播
        optimizer.step()  # 更新参数
    loss_list.append(total_loss / train_num)

print(model.weight, model.bias)  # 打印权重和偏置
plt.plot(loss_list)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()
```

![图片73.png](images/图片73.png)

