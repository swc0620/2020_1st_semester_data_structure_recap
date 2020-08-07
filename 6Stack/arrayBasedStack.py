class Error(Exception):
    pass

class Stack():
    def __init__(self, MAX_STACK):
        self.items = []
        self.top = -1
        self.MAX_STACK = MAX_STACK
    
    def isEmpty(self):
        return self.top < 0

    def isFull(self):
        return self.top == self.MAX_STACK - 1

    def push(self, newItem):
        try:
            if not self.isFull():
                self.items.append(newItem)
                self.top += 1
            else:
                raise Error()
        except Error:
            print("stack is full")

    def pop(self):
        try:
            if not self.isEmpty():
                self.items.pop()
                self.top -= 1
            else:
                raise Error()
        except Error:
            print("stack is empty")
    
    def popAll(self):
        self.items = []
        self.top = -1

    def peek(self):
        try:
            if not self.isEmpty():
                return self.items[self.top]
            raise Error()
        except Error:
            print("stack is empty")

stack = Stack(50)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
stack.push(4)
stack.push(5)
print(stack.peek())
stack.pop()
print(stack.peek())