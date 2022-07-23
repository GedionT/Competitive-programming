from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Alternative two with set
        
        visited = set()
        
        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        
        
        # Alternative one with Counter dictionary
#         count_dict = Counter(nums)
        
#         for k, v in count_dict.items():
#             if v > 1:
#                 return True
        
#         return False

