# import numpy as np
# vec1 = [1,2,3,4]
# vec2 = [5,6,7,8]
# print("余弦距离测试结果：\t"+str(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))))
#np.linalg.norm()求范数

# vec3 = np.mat([1,2,3,4])
# vec4 = np.mat([5,6,7,8])
# dist1 = np.sum(np.abs(vec3 - vec4))
# print(dist1)

import numpy as np
vec1 = np.array([1,2,3,4])
vec2 = np.array([5,6,7,8])
#方法一：根据公式求解
vec1_=vec1-np.mean(vec1)
vec2_=vec2-np.mean(vec2)
print(vec1_,vec2_)
dist1=np.dot(vec1_,vec2_)/(np.linalg.norm(vec1_)*np.linalg.norm(vec2_))
print("皮尔逊相关系数测试结果是：\t"+str(dist1))
# 皮尔逊pearson相关系数和斯皮尔曼spearman等级相关系数。它们可用来衡量两个变量之间的相关性的大小，根据数据满足的不同条件，
# 我们要选择不同的相关系数进行计算和分析（建模论文中最容易用错的方法）。https://blog.csdn.net/a_pickles/article/details/107347058