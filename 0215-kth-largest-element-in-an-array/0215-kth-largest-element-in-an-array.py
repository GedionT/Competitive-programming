class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i] = -nums[i]
            
        heapq.heapify(nums)
        
        res = 0
        while k:
            res = -heapq.heappop(nums)
            k -= 1
            
        return res
        