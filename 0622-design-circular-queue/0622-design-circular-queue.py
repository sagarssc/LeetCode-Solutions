class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = []
        self.size = k
        

    def enQueue(self, value: int) -> bool:
        if len(self.arr) < self.size:
            self.arr.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if len(self.arr) > 0:
            self.arr.pop(0)
            return True
        else:
            return False
        
        

    def Front(self) -> int:
        if self.arr:
            return self.arr[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.arr:
            return self.arr[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.arr:
            return False
        else:
            return True
        

    def isFull(self) -> bool:
        if len(self.arr) == self.size:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()