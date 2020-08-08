target = list(map(int, input().split()))

def selectionSort(array):
    for i in range(len(array) - 1, 0, -1):
        largestIndex = indexOfLargest(array, i + 1)
        array[largestIndex], array[i] = array[i], array[largestIndex]

def indexOfLargest(array, size):
    largestIndex = 0
    for i in range(size):
        if array[i] > array[largestIndex]:
            largestIndex = i
    
    return largestIndex

selectionSort(target)
print(target)