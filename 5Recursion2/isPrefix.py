operator = ['+', '-', '*', '/', '//', '%']
identifier = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '$']

def endPre(A, first, last):
    if first > last:
        return -1
    if A[first] in identifier:
        return first
    elif A[first] in operator:
        firstEnd = endPre(A, first + 1, last)
        if firstEnd == -1:
            return -1
        else:
            return endPre(A, firstEnd + 1, last)
    else:
        return -1

def isPre(A, first, last):
    lastChar = endPre(A, first, last)
    if lastChar == last:
        return True
    else:
        return False

operation = input()
print(isPre(operation, 0, len(operation) - 1))