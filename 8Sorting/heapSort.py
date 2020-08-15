def percolateDown(items, i, n):
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    largerChild = leftChild
    if leftChild <= n:
        if rightChild <= n and items[leftChild] < items[rightChild]:
            largerChild = rightChild
        if items[i] < items[largerChild]:
            items[i], items[largerChild] = items[largerChild], items[i]
            percolateDown(items, largerChild, n)

def heapSort(items):
    n = len(items) - 1
    for i in range(n // 2 + 1, -1 , -1):
        percolateDown(items, i, n)

    print(items)

    for size in range(n, 0, -1):
        items[0], items[size] = items[size], items[0]
        percolateDown(items, 0, size - 1) 


items = [4, 6, 3, 10, 3, 9, 5, 2]
print(items)
heapSort(items)
print(items)


