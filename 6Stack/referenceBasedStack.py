class Error(Exception):
    pass

class Node:
    def __init__(self, newItem, *args):
        self.item = newItem
        if args and len(args) > 0:
            self.next = args[0]
        else:
            self.next = None

    def getItem(self):
        return self.item

    def setItem(self, newItem):
        self.item = newItem

    def getNext(self):
        return self.next

    def setNext(self, nextNode):
        self.next = nextNode

class Stack():
    def __init__(self):
        self.top = Node(None)

    def isEmpty(self):
        return self.top.getNext == None

    def push(self, newItem):
        self.top = Node(newItem, self.top)

    def pop(self):
        try:
            if not self.isEmpty():
                temp = self.top
                self.top = self.top.getNext()
                return temp.getItem()
            else:
                raise Error()
        except Error:
            print("stack is empty")

    def popAll(self):
        self.top = Node(None)

    def peek(self):
        try:
            if not self.isEmpty():
                return self.top.getItem()
            else:
                raise Error()
        except Error:
            print("stack is empty")

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
stack.push(4)
stack.push(5)
print(stack.peek())
stack.pop()
print(stack.peek())