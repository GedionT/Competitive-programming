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
            mid = left + (right - left) // 2
            count = 0

            # Count how many numbers are less than or equal to 'mid'
            count = sum(num <= mid for num in nums)
            
            if count > mid:
                duplicate = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return duplicate