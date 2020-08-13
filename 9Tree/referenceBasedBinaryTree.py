class TreeNode():
    def __init__(self, newItem, *args):
        self.item = newItem
        if args and len(args) > 0:
            self.leftChild = args[0]
            self.rightChild = args[1]
        else:
            self.leftChild = None
            self.rightChild = None

    def getItem(self):
        return self.item

    def setItem(self, newItem):
        self.item = newItem

    def getLeft(self):
        return self.leftChild

    def getRight(self):
        return self.rightChild

    def setLeft(self, left):
        self.leftChild = left

    def setRight(self, right):
        self.rightChild = right
    