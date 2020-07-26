A = [1, 3, 5, 8, 13, 23, 85, 125, 356, 456]

def binarySearch(A, x, low, high):
    mid = (low + high) // 2
    if A[mid] < x:
        binarySearch(A, x, mid + 1, high)
    elif A[mid] > x:
        binarySearch(A, x, low, mid - 1)
    else:
        return A[mid], mid + 1
    
    return "Not Found", None

target = int(input("Enter Target Number: "))
result, index = binarySearch(A, target, 0, len(A) - 1)
print(f'Index is: {index}. Result is: {result}.')