import torch
import torch.nn as nn
import numpy as np

'''
手动实现交叉熵的计算
'''

#使用torch计算交叉熵
ce_loss = nn.CrossEntropyLoss()
#假设有3个样本，每个都在做3分类
pred = torch.FloatTensor([[0.0, 1.0, 0.0],[0.0, 0.0, 1.0],[1.0, 0.0, 0.0]])
pred1 = torch.FloatTensor([[0.0, 0.1, 3000.3],
                          [900000.9, 0.2, 0.9],
                          [0.5, 0.4, 0.2]])
#正确的类别分别为1,2,0
target = torch.LongTensor([1, 2, 0])
loss = ce_loss(pred,target)
print(loss, "torch输出交叉熵")

#实现softmax
def softmax(matrix):
    return np.exp(matrix)/np.sum(np.exp(matrix),axis=1,keepdims=True)

#验证softmax函数
# print(torch.softmax(pred1, dim=1))
# print(softmax(pred1.numpy()))

#将输入转化为onehot矩阵
def to_one_hot(target, shape):
    one_hot_target = np.zeros(shape)
    for i, t in enumerate(target):
        one_hot_target[i][t] = 1
    return one_hot_target
print(to_one_hot(target,(3,3)))

#手动实现交叉熵
def cross_entropy(pred, target):
    batch_size, class_num = pred.shape
    pred = softmax(pred)
    target = to_one_hot(target, pred.shape)
    entropy = - np.sum(target * np.log(pred), axis=1)
    return sum(entropy) / batch_size

print(cross_entropy(pred.numpy(), target.numpy()), "手动实现交叉熵")


a = np.arange(4).reshape(2,2)

# a
# Out[13]:
# array([[0, 1],
#        [2, 3]])
# a.sum(axis=0)
# Out[14]: array([2, 4])
# a.sum(axis=1)
# Out[15]: array([1, 5])
a = np.arange(8).reshape(2,2,2)
a.transpose
# a = np.arange(8).reshape(2,2,2)
# a
# Out[17]:
# array([[[0, 1],
#         [2, 3]],
#        [[4, 5],
#         [6, 7]]])
# a.sum(axis=0)
# Out[18]:
# array([[ 4,  6],
#        [ 8, 10]])
# a.sum(axis=1)
# Out[19]:
# array([[ 2,  4],
#        [10, 12]])
