target = list(map(int, input().split()))

def quickSort(array, first, last):
    if first < last:
        p = partition(array, first, last)
        quickSort(array, first, p-1)
        quickSort(array, p+1, last)

def partition(array, first, last):
    pivot = array[last]
    i = first - 1
    for j in range(first, last):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i+1], array[last] = array[last], array[i+1]
    # print(pivot, array)
    return i+1

quickSort(target, 0, len(target) - 1)
print(target)