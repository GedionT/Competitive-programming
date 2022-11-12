class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        ### banance the two heaps so that each of them representing half of the list
        ### for odd length list, len(maxHeap) == len(minHeap)+1
        ### for even length list, len(maxHeap) == len(minHeap)
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap)) 
        elif len(self.maxHeap) > len(self.minHeap)+1:
            heappush(self.minHeap, -heappop(self.maxHeap)) 

    def findMedian(self) -> float:
        ### if the length of entire list is even, 
        ### get the mean of the two middle values
        if (len(self.maxHeap)+len(self.minHeap))%2==0:
            return (-self.maxHeap[0]+self.minHeap[0])/2
        
        ### when odd, we know that the median is in maxHeap
        return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()