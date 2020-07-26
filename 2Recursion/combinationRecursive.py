def combination(n, k):
    if k == n or k == 0:
        return 1
    elif k > n or k < 0:
        return 0
    else:
        return combination(n-1, k-1) + combination(n-1, k)

n, k = list(map(int, input().split(" ")))
print(combination(n, k))