class RandomizedSet:

    def __init__(self):
        self.stored = dict()
        self.items = list()
        self.pos = 0
        
    def insert(self, val: int) -> bool:
        if val in self.stored:
            return False
        self.stored[val] = self.pos
        self.pos += 1
        self.items.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.stored:
            self.stored[self.items[-1]] = self.stored[val]
            self.items[self.stored[val]], self.items[self.pos-1] = self.items[self.pos-1], self.items[self.stored[val]]
            self.items.pop()
            del self.stored[val]
            self.pos -= 1
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.items)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()