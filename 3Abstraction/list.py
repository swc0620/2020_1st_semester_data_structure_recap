class Error(Exception):
    pass

class List:
    __MAX_LIST = 50
    __items = [None] * __MAX_LIST
    __numItems = 0

    def isEmpty(self):
        return self.__numItems == 0

    def size(self):
        return self.__numItems

    def removeAll(self):
        self.__items = list()
        self.__numItems = 0

    def add(self, index, item):
        try:
            if self.__numItems > self.__MAX_LIST:
                raise Error()
            if index >= 1 and index <= self.__numItems+1:
                for pos in range(index-1, self.__numItems):
                    self.__items[pos+1] = self.__items[pos]
                self.__items[index-1] = item
                self.__numItems += 1
            else:
                raise Error()
        except Error:
            print("Not allowed")

    def get(self, index):
        try:
            if index >= 1 and index <= self.__numItems:
                return self.__items[index-1]
            else:
                raise Error()
        except Error:
            print("list index out of bound exception")

    def remove(self, index):
        try:
            if index >= 1 and index <= self.__numItems:
                for pos in range(index, self.__numItems+1):
                    self.__items[pos-1] = self.__items[pos]
                self.__items[self.__numItems] = None
                self.__numItems -= 1
            else:
                raise Error()
        except Error:
            print("index out of range")

aList = List()
aList.add(1, 7)
aList.add(2, 8)
aList.add(3, 9)
aList.add(4, 10)
aList.remove(1)
print(aList.get(1))
        