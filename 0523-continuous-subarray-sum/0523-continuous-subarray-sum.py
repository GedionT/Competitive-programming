class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    
        
        remainders = {0: 0}
        prefix = 0
        
        for i in range(len(nums)):
            prefix += nums[i]
            
            if (prefix % k) in remainders and remainders[prefix % k] < i:
                return True
            
            if prefix % k not in remainders:
                remainders[prefix % k] = i + 1
            
        
        return False