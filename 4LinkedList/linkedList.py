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
        return numItems == 0

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

aLinkedList = LinkedList()
aLinkedList.add(1, "first")
aLinkedList.add(2, "second")
aLinkedList.add(3, "third")
aLinkedList.add(4, "fourth")
aLinkedList.add(5, "fifth")
aLinkedList.add(8, "eighth")

print(aLinkedList.get(1))
print(aLinkedList.get(2))
print(aLinkedList.get(3))
print(aLinkedList.get(4))
print(aLinkedList.get(5))

aLinkedList.remove(1)
aLinkedList.remove(5)

print(aLinkedList.get(1))
print(aLinkedList.get(2))
print(aLinkedList.get(3))

aLinkedList.remove(4)

print(aLinkedList.get(1))
print(aLinkedList.get(4))
print(aLinkedList.get(3))