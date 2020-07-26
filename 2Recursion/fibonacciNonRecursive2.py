def fibonacci(n):
    array = []
    array.append(1)
    array.append(1)
    if n >= 3:
        for i in range(0, n -2):
            array.append(array[i] + array[i+1])
    return array[n-1]

n = int(input())
print(fibonacci(n))