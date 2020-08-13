from referenceBasedBinaryTree import TreeNode

class BinarySearchTree():
    def __init__(self):
        self.numItems = 0
        self.root = None
    
    def __internalSearch(self, root, searchKey):
        if not root:
            return None
        else:
            if root.getItem() == searchKey:
                return root
            elif root.getItem() < searchKey:
                return self.__internalSearch(root.getRight(), searchKey)
            else:
                return self.__internalSearch(root.getLeft(), searchKey)

    def search(self, searchKey):
        if not self.root:
            return "Not found!"
        else:
            sNode = self.__internalSearch(self.root, searchKey)
            if sNode:
                return sNode.getItem()
            else:
                return "Not Found!"
    
    def __internalInsert(self, root, newItem):
        if not root:
            root = TreeNode(newItem)
        else:
            if root.getItem() < newItem:
                root.setRight(self.__internalInsert(root.getRight(), newItem))
            else:
                root.setLeft(self.__internalInsert(root.getLeft(), newItem))
        return root

    def insert(self, newItem):
        self.numItems += 1
        if not self.root:
            self.root = TreeNode(newItem)
        else:
            self.__internalInsert(self.root, newItem)

    def deleteMin(self, root):
        minNode = root
        while minNode.getLeft():
            minNode = minNode.getLeft()
        return minNode

    def deleteNode(self, root):
        if not root.getLeft() and not root.getRight():
            return None
        elif not root.getLeft():
            return root.getRight()
        elif not root.getRight():
            return root.getLeft()
        else:
            temp = self.deleteMin(root.getRight())
            root.setItem(temp.getItem())
            root.setRight(self.deleteItem(root.getRight(), root.getRight().getItem()))
            return root

    def deleteItem(self, root, searchKey):
        if not root:
            return None
        else:
            if root.getItem() == searchKey:
                root = self.deleteNode(root)
            elif root.getItem() < searchKey:
                root.setRight(self.deleteItem(root.getRight(), searchKey))
            else:
                root.setLeft(self.deleteItem(root.getLeft(), searchKey))
        return root

    def delete(self, searchKey):
        if not self.root:
            return "Does not exist!"
        else:
            self.numItems -= 1
            self.deleteItem(self.root, searchKey)

    def __internalSize(self, root):
        if not root:
            return 0
        else:
            return 1 + self.__internalSize(root.getLeft()) + self.__internalSize(root.getRight())

    def size(self):
        if not self.root:
            return 0
        else:
            return self.__internalSize(self.root)
    
    def __internalPreorder(self, root):
        if root:
            print(root.getItem(), end=" ")
            self.__internalPreorder(root.getLeft())
            self.__internalPreorder(root.getRight())

    def preorder(self):
        if not self.root:
            print(None)
        else:
            self.__internalPreorder(self.root)
            print()

    def __internalInorder(self, root):
        if root:
            self.__internalInorder(root.getLeft())
            print(root.getItem(), end=" ")
            self.__internalInorder(root.getRight())

    def inorder(self):
        if not self.root:
            print(None)
        else:
            self.__internalInorder(self.root)
            print()

    def __internalPostorder(self, root):
        if root:
            self.__internalPostorder(root.getLeft())
            self.__internalPostorder(root.getRight())
            print(root.getItem(), end=" ")

    def postorder(self):
        if not self.root:
            print(None)
        else:
            self.__internalPostorder(self.root)
            print()

bst = BinarySearchTree()
bst.insert(60)
print(bst.search(60))
bst.insert(20)
bst.insert(70)
bst.insert(10)
bst.insert(40)
bst.insert(30)
bst.insert(50)
bst.preorder()
bst.inorder()
bst.postorder()
print(bst.size())
print(bst.search(100))
print(bst.search(30))
bst.delete(30)
print(bst.search(30))
print(bst.size())
bst.delete(60)
print(bst.size())
bst.delete(100)
print(bst.search(60))
print(bst.size())