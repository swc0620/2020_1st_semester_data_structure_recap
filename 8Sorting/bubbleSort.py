target = list(map(int, input().split()))

def bubbleSort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

bubbleSort(target)
print(target)