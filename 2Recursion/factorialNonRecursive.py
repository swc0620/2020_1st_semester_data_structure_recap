def factorial(n):
    result = 1
    temp = n
    while temp >= 1:
        result *= temp
        temp -= 1
    return result

n = int(input())
print(factorial(n))