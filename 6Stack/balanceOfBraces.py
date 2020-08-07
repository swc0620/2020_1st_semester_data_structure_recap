stack = []

def checkBalanceOfBraces(string):
    for i in range(len(string)):
        if string[i] == '{':
            stack.append(string[i])
        elif string[i] == '}':
            if stack:
                stack.pop()
            else:
                return False
        # print(i, stack)
        
    if not stack:
        return True
    else:
        return False

string = input()
# print(len(string))
print(checkBalanceOfBraces(string))