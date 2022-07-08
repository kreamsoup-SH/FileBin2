class Stack:
    def __init__(self,size):
        self.data=[]
        self.size = size
        for i in range(size):
            self.data.append(None)
        self.head = 0
        self.tail = 0
    def is_empty(self):
        if self.tail <= 0:
            print("is_empty() : True")
            return True
        else:
            return False
    def is_full(self):
        if self.tail >= self.size:
            return True
        else: return False
    def push(self,data):
        if self.is_full():
            print("stack is full")
        else:
            self.data[self.tail] = data
            self.tail = self.tail + 1
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            self.data[self.tail-1] = None
            self.tail = self.tail - 1
    def printstack(self):
        print("data[] =",self.data)

stacking = Stack(5)
stacking.printstack()
stacking.push("a")
stacking.printstack()
stacking.push("b")
stacking.printstack()
stacking.push("c")
stacking.printstack()
stacking.push("d")
stacking.printstack()
stacking.push("e")
stacking.printstack()
stacking.push("f")
stacking.printstack()

stacking.pop()
stacking.printstack()
stacking.pop()
stacking.printstack()
stacking.pop()
stacking.printstack()
stacking.pop()
stacking.printstack()
stacking.pop()
stacking.printstack()

stacking.pop()
stacking.printstack()