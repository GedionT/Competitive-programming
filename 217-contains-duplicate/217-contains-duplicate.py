from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        count_dict = Counter(nums)
        
        for k, v in count_dict.items():
            if v > 1:
                return True
        
        return False
