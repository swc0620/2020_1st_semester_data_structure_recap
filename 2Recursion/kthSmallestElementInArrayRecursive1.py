Array = [2215, 57, 233, 224, 632, 723325, 734, 22425, 62, 3125]

def kthSmallest(A, k, n):
    minimum = min(A)
    A.remove(minimum)

    if k == 1:
        return minimum
    else:
        return kthSmallest(A, k-1, n-1)

k = int(input())
print(kthSmallest(Array, k, len(Array)))
