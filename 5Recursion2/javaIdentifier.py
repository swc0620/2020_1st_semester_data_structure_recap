letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '$']
digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def isId(w):
    if len(w) == 1:
        if w in letter:
            return True
        else:
            return False
    elif w[len(w) - 1] in letter or w[len(w) - 1] in digit:
        return isId(w[:len(w)-1])
    else:
        return False

identifier = input()
print(isId(identifier))