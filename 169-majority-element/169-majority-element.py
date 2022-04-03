class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
         count = Counter(nums)
            
         freq = max(count.keys(), key=count.get)
        
         return freq