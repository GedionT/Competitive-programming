class MyCircularQueue:

    def __init__(self, k: int):
        self.len = k
        self.queue = []
        
        
    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.len:
            self.queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        return False
    
    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        if self.queue:
            return False
        return True
        
    def isFull(self) -> bool:
        if len(self.queue) < self.len:
            return False
        return True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()