class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # using hashmap o(n) space and constant search       
        _map = {}
        
        for index, num  in enumerate(nums):
            addend = target - num
            
            if addend not in _map:
                _map[num] = index
            else:
                return [_map[addend], index]
            
        
        
        
# First Bruteforce with TLE n^2
#         for i in range(len(nums)):
#             for j in range(len(nums)):
                
#                 if nums[i] + nums[j] == target and i != j:
#                     return [i,j]


  
            
        
        # try nlogn
        # if sorted n by using hashmap and 2ptr
        # two pointer approach won't work because two 
        # 2, 3, 4
        # ^     ^
        
#         nums.sort()
        
#         left = 0
#         right = len(nums)-1
        
        
#         while left < right:
#             _sum = nums[left] + nums[right]
            
#             if _sum == target:
#                 return [left, right]
#             elif _sum < target:
#                 left += 1
#             else:
#                 right -= 1
        
#         return [left, right]


        
                
        