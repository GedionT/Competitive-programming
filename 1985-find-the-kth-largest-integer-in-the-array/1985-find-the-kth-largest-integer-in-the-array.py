class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        heap = []
        
        for num in nums:
             heapq.heappush(heap, -int(num))
        
        res = 0
        while k:
            res = -heapq.heappop(heap)
            k -= 1
            
        return str(res)