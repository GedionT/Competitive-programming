class MedianFinder:

    def __init__(self):
        self.lHeap = [] 
        self.rHeap = []
        

    def addNum(self, num: int) -> None: 
        heapq.heappush(self.lHeap, num  * -1)
        if len(self.lHeap) > len(self.rHeap) + 1:
            leftVal = heapq.heappop(self.lHeap) * -1
            heapq.heappush(self.rHeap, leftVal)
        if self.lHeap and self.rHeap and -self.lHeap[0] > self.rHeap[0]:
            leftVal = -heapq.heappop(self.lHeap)
            right = heapq.heappop(self.rHeap)
            heapq.heappush(self.rHeap, leftVal)
            heapq.heappush(self.lHeap, right * -1)
        

    def findMedian(self) -> float:
        if (len(self.lHeap) + len(self.rHeap)) % 2 == 0:
            return  (self.lHeap[0]  * -1 + self.rHeap[0]) / 2
        return self.lHeap[0] * -1
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()