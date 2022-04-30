import torch

print(torch.__version__)

x = torch.empty(5, 3)

x = torch.rand(5, 3)

#初始化一个全零的矩阵
x = torch.zeros(5, 3, dtype=torch.long)


#直接传数据
x = torch.tensor([5.5, 3])
x

x = x.new_ones(5, 3, dtype=torch.double)

x = torch.randn_like(x, dtype=torch.float)
x

y = torch.rand(5, 3)
x + y

torch.add(x, y)#一样的也是加法

x[:, 1]

#view操作可以改变矩阵维度
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)
print(x.size(), y.size(), z.size())


a = torch.ones(5)
b = a.numpy()
b

import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
b

# Tensor常见的形式有哪些
# 0: scalar
# 1: vector
# 2: matrix
# 3: n-dimensional tensor
import torch
from torch import tensor
# 0.2  Scalar
# 通常就是一个数值

x = tensor(42.)
x.dim()  #0
2 * x
x.item()

# 1  Vector
# 例如： [-5., 2., 0.]，在深度学习中通常指特征，例如词向量特征，某一维度特征等
# 𝑣⃗ =[𝑣1,𝑣2,…,𝑣𝑛]
v = tensor([1.5, -0.5, 3.0])
v.dim()  #1
v.size()
#Out[20]: torch.Size([3])

# 1.1  Matrix
# 一般计算的都是矩阵，通常都是多维的
M = tensor([[1., 2.], [3., 4.]])
M.matmul(M)
# Out[22]:
# tensor([[ 7., 10.],
#         [15., 22.]])
# M*M
# Out[23]:
# tensor([[ 1.,  4.],
#         [ 9., 16.]])
