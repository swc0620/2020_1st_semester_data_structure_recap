A = [1, 3, 5, 8, 13, 23, 85, 125, 356, 456]

def binarySearch(A, n, x):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < x:
            low = mid + 1
        elif A[mid] > x:
            high = mid - 1
        else:
            return A[mid], mid + 1
    
    return "Not Found", None

target = int(input("Enter Target Number: "))
result, index = binarySearch(A, len(A), target)
print(f'Index is: {index}. Result is: {result}.')