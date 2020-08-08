class Error(Exception):
    pass

class Queue():
    def __init__(self, MAX_QUEUE):
        self.MAX_QUEUE = MAX_QUEUE
        self.items = [None for i in range(self.MAX_QUEUE)]
        self.front = 0
        self.back = self.MAX_QUEUE - 1
        self.numItems = 0
    
    def isEmpty(self):
        return self.numItems == 0
    
    def isFull(self):
        return self.numItems == self.MAX_QUEUE

    def enqueue(self, newItem):
        try:
            if not self.isFull():
                self.back = (self.back + 1) % self.MAX_QUEUE
                self.items[self.back] = newItem
                self.numItems += 1
            else:
                raise Error()
        except Error:
            print("queue is full")

    def dequeue(self):
        try:
            if not self.isEmpty():
                temp = self.items[self.front]
                self.items[self.front] = None
                self.front = (self.front + 1) % self.MAX_QUEUE
                self.numItems -= 1
                return temp
            else:
                raise Error()
        except Error:
            print("queue is empty")

    def dequeueAll(self):
        self.items = [None for i in range(self.MAX_QUEUE)]
        self.front = 0
        self.back = self.MAX_QUEUE - 1
        self.numItems = 0

    def peek(self):
        try:
            if not self.isEmpty():
                return self.items[self.front]
            else:
                raise Error()
        except Error:
            print("queue is empty")

queue = Queue(50)
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