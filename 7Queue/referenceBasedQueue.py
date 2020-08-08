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

class Queue():
    def __init__(self):
        self.lastNode = Node(None)

    def isEmpty(self):
        return self.lastNode.getNext() == None
    
    def enqueue(self, newItem):
        newNode = Node(newItem)
        if self.isEmpty():
            newNode.setNext(newNode)
        else:
            newNode.setNext(self.lastNode.getNext())
            self.lastNode.setNext(newNode)
        self.lastNode = newNode

    def dequeue(self):
        try:
            if not self.isEmpty():
                firstNode = self.lastNode.getNext()
                if firstNode == self.lastNode:
                    self.lastNode = Node(None)
                else:
                    self.lastNode.setNext(firstNode.getNext())
                return firstNode.getItem()
            else:
                raise Error()
        except Error:
            print("queue is empty")

    def dequeueAll(self):
        self.lastNode = Node(None)

    def peek(self):
        try:
            if not self.isEmpty():
                return self.lastNode.getNext().getItem()
            else:
                raise Error()
        except Error:
            print("queue is empty")
        
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())
print(queue.dequeue())
queue.enqueue(4)
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())