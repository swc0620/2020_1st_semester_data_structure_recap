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

adjacencyList = {
    'Z': [], 
    'Y': ['Z', 'R'],
    'W': ['Y', 'S'],
    'S': ['T'],
    'T': ['W'],
    'P': ['W', 'R'],
    'R': ['X'],
    'X': [],
    'Q': ['X']
}

mark = {
    'Z': False,
    'Y': False,
    'W': False,
    'S': False,
    'T': False,
    'P': False,
    'R': False,
    'X': False,
    'Q': False
}

queue = Queue(50)

def searchS(originCity, destinationCity):
    queue.enqueue(originCity)
    mark[originCity] = True

    while not queue.isEmpty():
        nextCity = queue.dequeue()
        adjacentCities = adjacencyList[nextCity]
        if adjacentCities:
            for city in adjacentCities:
                if mark[city] == False:
                    if city == destinationCity:
                        return True
                    else:
                        queue.enqueue(city)
                        mark[city] = True
        

    return False

originCity, destinationCity = input().split()
print(searchS(originCity, destinationCity))
            

