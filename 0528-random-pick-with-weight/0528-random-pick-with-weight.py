class Solution:

    def __init__(self, w):
        self.preSums = [w[0]]
        for i in range(1, len(w)):
            self.preSums.append(self.preSums[-1] + w[i])
        

    def pickIndex(self):
        x = random.randint(1, self.preSums[-1])
        index = bisect_left(self.preSums, x)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()