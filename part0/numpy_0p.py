import torch
import numpy as np

#numpy基本操作
x = np.array([[1,2,3],[4,5,6]])
# print(x.ndim) #2
# print(x.shape)  #(2, 3)
# print(x.size)  #6
print(x.sum())

#numpy基本操作
# x = np.array([[1,2,3],
#               [4,5,6]])
#
# print(x.ndim)
# print(x.shape)
# print(x.size)
# print(np.sum(x))
# print(np.sum(x, axis=0)) array([5, 7, 9])
# print(np.sum(x, axis=1))  array([ 6, 15])
# print(np.reshape(x, (3,2)))
# print(np.sqrt(x))
# print(np.exp(x))
# array([[  2.71828183,   7.3890561 ,  20.08553692],
#        [ 54.59815003, 148.4131591 , 403.42879349]])
# print(x.transpose())  array([[1, 4],
#        [2, 5],
#        [3, 6]])
# print(x.flatten()) array([1, 2, 3, 4, 5, 6])

#
# print(np.zeros((3,4,5)))
# array([[[0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.]],
#        [[0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.]],
#        [[0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.]]])
# print(np.random.rand(3,4,5))
#
# x = np.random.rand(3,4,5)
# x = torch.FloatTensor(x)
# tensor([[1., 2., 3.],
#         [4., 5., 6.]])
# print(x.shape)
# print(torch.exp(x))
# tensor([[  2.7183,   7.3891,  20.0855],
#         [ 54.5981, 148.4132, 403.4288]])
# print(torch.sum(x, dim=0))   tensor([5., 7., 9.])
# print(torch.sum(x, dim=1))
# print(x.transpose(1, 0))
# tensor([[1., 4.],
#         [2., 5.],
#         [3., 6.]])
# print(x.flatten()) tensor([1., 2., 3., 4., 5., 6.])