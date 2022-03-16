class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums.sort()  # o(n logn)
        first, second, third = float('-inf'),  float('-inf'),  float('-inf')

        for i in range(len(nums)):  # o(n)

            if first < nums[i]:
                third = second
                second = first
                first = nums[i]

        if third == float('-inf'):
            return first

        return third
