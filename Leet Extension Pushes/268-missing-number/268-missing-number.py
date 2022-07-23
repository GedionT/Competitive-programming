class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         big = [0] * 10001
#         for i in nums:
#             big[i] = 1
        
#         for j in range(len(nums) + 1):
#             if big[j] == 0:
#                 return j

# with runtime O(n) space of o(1)
# use summation
# because all the numbers are supposed to be in the elements of the indexes,
# do an xor on each and then find missing. (check yt for this solution)
        
        x1 = nums[0]
        x2 = 1

        for i in range(1, len(nums)):
            x1 = x1 ^ nums[i]

        for i in range(2, len(nums)+1):
            x2 = x2 ^ i

        return x1 ^ x2 