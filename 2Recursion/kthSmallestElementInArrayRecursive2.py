Array = [2215, 57, 233, 224, 632, 723325, 734, 22425, 62, 3125]

def partition(A, pivot, first, last):
    i = first - 1

    for j in range(first, last):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[last] = A[last], A[i+1]
    return i+1

def kthSmallest(A, k, first, last):
    pivot = A[last]
    pivotIndex = partition(A, pivot, first, last)

    if k < pivotIndex - first + 1:
        return kthSmallest(A, k, first, pivotIndex - 1)
    elif k == pivotIndex - first + 1:
        return pivot
    else:
        return kthSmallest(A, k - pivotIndex + first - 1, pivotIndex + 1, last)

k = int(input())
print(kthSmallest(Array, k, 0, len(Array) - 1))
