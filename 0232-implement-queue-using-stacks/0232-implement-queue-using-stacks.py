class MyQueue:

    def __init__(self):
        self.staque = []
        self.offset = 0

    def push(self, x: int) -> None:
        self.staque.append(x)

    def pop(self) -> int:
        self.offset += 1
        return self.staque[self.offset-1]

    def peek(self) -> int:
        return self.staque[self.offset]

    def empty(self) -> bool:
        if self.offset <= (len(self.staque)-1):
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()