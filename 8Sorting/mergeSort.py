target = list(map(int, input().split()))

def mergeSort(array, first, last):
    if first >= last:
        return array
    else:
        mid = (first + last) // 2
        mergeSort(array, first, mid)
        mergeSort(array, mid + 1, last)
        merge(array, first, mid, last)

def merge(array, first, mid, last):
    p = first
    q = mid + 1
    r = first
    temp = [None for i in range(len(array))]
    while p <= mid and q <= last:
        if array[p] < array[q]:
            temp[r] = array[p]
            r += 1
            p += 1
        else:
            temp[r] = array[q]
            r += 1
            q += 1
    
    while p <= mid:
        temp[r] = array[p]
        r += 1
        p += 1

    while q <= last:
        temp[r] = array[q]
        r += 1
        q += 1

    for i in range(first, last + 1):
        array[i] = temp[i]

mergeSort(target, 0, len(target) - 1)
print(target)