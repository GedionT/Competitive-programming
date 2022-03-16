class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        
        # nums = collections.Counter(nums)
        
#         [
#             (1, 2) 
#             (2, 2)
#             (3, 1)
#             (7, 1)
#         ]
        
    
#         1
#         1, 1 = 2
#         2, 1 = 3
#         2, 2 = 4
#         3, 2 = 5
#         7

        nums.sort()
          
        nums.append(len(nums) + nums[-1])
        
        move, sub = 0, 0
        
        for i in range(1, len(nums)):
            
            if nums[i-1] == nums[i]:
                sub += 1
                move -= nums[i]
            
            else:
                add = min(sub, (nums[i] - nums[i-1] - 1))
                move += add * (add + 1) // 2 + add * nums[i-1]
                sub -= add
                
        return move
                

