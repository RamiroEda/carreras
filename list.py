class List:
    def __init__(self):
        self.array = []
        self.size = 0

    def push_back(self, element):
        self.array.append(element)
        self.size += 1

    def pop_back(self):
        if(self.size > 0):
            self.array.pop()
            self.size -= 1

    def pop_front(self):
        if(self.size > 0):
            self.array.pop(0)
            self.size -= 1

    def front(self):
        return self.array[0]

    def back(self):
        return self.array[-1]

    def isEmpty(self):
        return self.size <= 0

class ListConductor(List):
    def getDriverById(self, id):
        for d in self.array:
            if(d.id == id):
                return d
        return -1

    def contains(self, id):
        for d in self.array:
            if(d.id == id):
                return True
        return False