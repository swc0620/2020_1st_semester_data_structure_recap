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

class LinkedList():
    def __init__(self):
        self.numItems = 0
        self.head = Node(None)

    def isEmpty(self):
        return self.numItems == 0

    def size(self):
        return self.numItems

    def __find(self, index):
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode.getNext()         
        return currentNode          

    def get(self, index):
        try:
            if index >= 0 and index <= self.numItems:
                currentNode = self.__find(index)
                return currentNode.getItem()
            else:
                raise Error()
        except Error:
            return "cannot get"

    def add(self, index, item):
        try:
            if index >= 1 and index <= self.numItems+1:
                previousNode = self.__find(index-1)
                currentNode = Node(item, previousNode.getNext())
                previousNode.setNext(currentNode)
                self.numItems += 1
            else:
                raise Error()
        except Error:
            print("cannot add")

    def remove(self, index):
        try:
            if index >= 1 and index <= self.numItems:
                previousNode = self.__find(index-1)
                currentNode = previousNode.getNext()
                previousNode.setNext(currentNode.getNext())
                self.numItems -= 1
            else:
                raise Error()
        except Error:
            print("cannot remove")

    def removeAll(self):
        self.head = None
        self.numItems = 0

class Queue():
    def __init__(self):
        self.list = LinkedList()

    def isEmpty(self):
        return self.list.isEmpty()

    def enqueue(self, newItem):
        self.list.add(self.list.size() + 1, newItem)

    def dequeue(self):
        try:
            if not self.list.isEmpty():
                queueFront = self.list.get(1)
                self.list.remove(1)
                return queueFront
            else:
                raise Error()
        except Error:
            print("queue is empty")

    def dequeueAll(self):
        self.list.removeAll()

    def peek(self):
        try:
            if not self.list.isEmpty():
                return self.list.get(1)
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