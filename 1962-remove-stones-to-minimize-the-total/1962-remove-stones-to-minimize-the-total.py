class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        for pile in piles:
            heapq.heappush(heap, -pile)
            
        while k:
            val = -heapq.heappop(heap)
            val = ceil(val/2)
            heapq.heappush(heap, -val)
            k -= 1
            
        return -sum(heap)
        
