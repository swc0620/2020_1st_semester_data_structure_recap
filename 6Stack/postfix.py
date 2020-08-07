stack = []
operator = ['+', '-', '*', '/', '//', '%']

string = input()

for char in range(len(string)):
    if string[char] not in operator:
        stack.append(string[char])
    else:
        operand2 = stack.pop()
        operand1 = stack.pop()
        if string[char] == '+':
            result = int(operand1) + int(operand2)
        elif string[char] == '-':
            result = int(operand1) - int(operand2)
        elif string[char] == '*':
            result = int(operand1) * int(operand2)
        elif string[char] == '/':
            result = int(operand1) / int(operand2)
        elif string[char] == '%':
            result = int(operand1) % int(operand2)
            
        stack.append(result)        

print(stack.pop())