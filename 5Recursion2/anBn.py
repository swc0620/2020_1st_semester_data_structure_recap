def isAnBn(w):
    if len(w) == 0:
        return True
    elif w[0] == 'A' and w[len(w) - 1] == 'B':
        return isAnBn(w[1:len(w)-1])
    else:
        return False

AnBn = input()
print(isAnBn(AnBn))
