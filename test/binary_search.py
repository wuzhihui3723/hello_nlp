def binary_search(list,target):
    low = 0
    high = len(list)

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == '__main__':
    a = [-1,0,3,5,9,12]
    print(binary_search(a,4))