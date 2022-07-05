import operator

import numpy as np
import matplotlib.pyplot as plt

def createDataSet():
    group =  np.array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0, 0],
        [0, 0.1]
    ])
    lables = ['A','A','B','B']
    return group,lables


def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    # diffMat2 = inX - dataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance ** 0.5
    sortedDistanceIndex = distance.argsort()
    print(sortedDistanceIndex.shape)

    #存放最终的投票结果
    classCount = {}
    for i in range(k):
        voteIlable = labels[sortedDistanceIndex[i]]
        classCount[voteIlable] = classCount.get(voteIlable,0) + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def show_data(group,lables):
    labels = np.array(lables)
    index_a = np.where(labels == "A")
    index_b = np.where(labels == "B")
    for i in labels:
        if i == "A":
            plt.scatter(group[index_a][:,:1],group[index_a][:,1:2],c='red')
        elif i == "B":
            plt.scatter(group[index_b][:,:1],group[index_b][:,1:2],c='green')
    plt.show()


if __name__ == '__main__':
    #导入数据
    dataSet,labels = createDataSet()
    #新数据
    inX = [0.5,0.5]
    className = classify(inX,dataSet,labels,3)
    print("该数据属于{}类".format(className))
    dataSet = np.vstack((dataSet,inX))
    labels.append(className)
    show_data(dataSet,labels)