class Error(Exception):
    pass

class Heap():
    def __init__(self):
        self.items = []

    def percolateDown(self, i, n):
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        largerChild = leftChild
        if leftChild <= n:
            if rightChild <= n and self.items[leftChild] < self.items[rightChild]:
                largerChild = rightChild
            if self.items[i] < self.items[largerChild]:
                self.items[i], self.items[largerChild] = self.items[largerChild], self.items[i]
                self.percolateDown(largerChild, n)

    def delete(self):
        if len(self.items) != 0:
            rootItem = self.items[0]
            self.items[0] = self.items[len(self.items) - 1]
            self.items.pop()
            self.percolateDown(0, len(self.items) - 1)
            return rootItem
        else:
            return None

    def insert(self, x):
        self.items.append(x)
        i = len(self.items) - 1
        parent = i // 2
        while parent >= 0 and self.items[i] > self.items[parent]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = i // 2

heap = Heap()
heap.insert(2)
heap.insert(3)
heap.insert(5)
heap.insert(9)
heap.insert(6)
print(heap.items)
print(heap.delete())
print(heap.items)
print(heap.delete())
print(heap.items)