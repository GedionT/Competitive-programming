class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
#         big_one = [0] * 100001
        
#         for i in nums:
#             if big_one[i] == 0:
#                 big_one[i] = 1
#             else:
#                 return i

      
        left = 1
        right = len(nums) - 1
        
        while left <= right:
            cur = left + (right - left) // 2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            
            if count > cur:
                duplicate = cur
                right = cur - 1
            else:
                left = cur + 1
                
        return duplicate