class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        s = Counter(nums)
        
        for i,j in s.items():
            if j==1:
                ans.append(i)
                
        return ans
#         xor = 0
        
#         for n in nums:
#             xor ^= n
        
#         print(xor)