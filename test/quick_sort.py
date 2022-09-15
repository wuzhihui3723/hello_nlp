def quick_sort(alist,start,end):
    if start >= end:
        return
    mid =alist[start]
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid
    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)


if __name__ == '__main__':
    a = [8, 4, 5, 7, 1, 3, 6, 2]
    quick_sort(a,0,7)
    print(a)

# 快速排序
# def partition(li, left, right):
#     tmp = li[left]
#     while left < right:
#         while left < right and li[right] >= tmp:  # 从右边找比tmp小的数
#             right -= 1  # 继续从右往左查找
#         li[left] = li[right]  # 把右边的值写到左边空位上
#
#         while left < right and li[left] <= tmp:
#             left += 1
#         li[right] = li[left]  # 把左边的值写到右边空位上
#
#     li[left] = tmp  # 把tmp归位
#     return left
#
#
# def quick_sort(li, left, right):
#     if left < right:  # 至少两个元素
#         mid = partition(li, left, right)
#         quick_sort(li, left, mid - 1)
#         quick_sort(li, mid + 1, right)
#
#
# li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# quick_sort(li, 0, len(li) - 1)
# print(li)