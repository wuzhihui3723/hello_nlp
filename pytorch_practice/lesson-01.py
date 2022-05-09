import torch
import numpy as np
# print(torch.__version__)  #torch: 1.9.0
# print(torch.cuda.is_available())#cuda是否可用
# torch.cuda.device_count()#返回GPU的数量
# torch.cuda.get_device_name(0)#返回gpu名字，设备索引默认从0开始
#GPU环境准备
#https://blog.csdn.net/fengxinzioo/article/details/105646969
#https://blog.csdn.net/weixin_42838061/article/details/113107234

#张量是一个多维数组，它是标量、向量、矩阵的高维扩展
# flag = True
flag = False
if flag:
    arr = np.ones((3, 3))
    print("ndarray的数据类型：", arr.dtype)

    # t = torch.tensor(arr, device='cuda')
    # tensor([[1., 1., 1.],
    #         [1., 1., 1.],
    #         [1., 1., 1.]], device='cuda:0', dtype=torch.float64)
    t = torch.tensor(arr)

    print(t)

# ===============================  exmaple 2 ===============================
# 通过torch.from_numpy创建张量  这种方法共享内存
flag = True
# flag = False
if flag:
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    t = torch.from_numpy(arr)
    # print("numpy array: ", arr)
    # print("tensor : ", t)

    # print("\n修改arr")
    # arr[0, 0] = 0
    # print("numpy array: ", arr)
    # print("tensor : ", t)

    print("\n修改tensor")
    t[0, 0] = -1
    print("numpy array: ", arr)
    print("tensor : ", t)
