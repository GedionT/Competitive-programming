class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        l_stack = []
        r_stack = []

        l_pos = len(nums)-1
        r_pos = 0

        for i in range(len(nums)):
            while l_stack and nums[l_stack[-1]] > nums[i]:
                l_pos = min(l_pos, l_stack.pop())
            l_stack.append(i)

        for j in range(len(nums)-1, -1, -1):
            while r_stack and nums[r_stack[-1]] < nums[j]:
                r_pos = max(r_pos, r_stack.pop())
            r_stack.append(j)

        diff = r_pos - l_pos + 1

        return 0 if diff <= 1 else diff
