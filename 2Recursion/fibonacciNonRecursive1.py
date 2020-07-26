def fibonacci(n):
    if n <= 2:
        return 1
    else:
        temp = n
        first = 1
        second = 1
        new = 2
        while temp > 2:
            new = first + second
            second = first
            first = new
            temp -= 1
        return first

n = int(input())
print(fibonacci(n))