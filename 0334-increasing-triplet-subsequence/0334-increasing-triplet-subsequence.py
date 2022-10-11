class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n = len(nums)
        stack = []
        
        for num in nums:
            if stack and num <= stack[-1]: # if current number smaller than previous value in stack
                idx = bisect_left(stack, num) # search to replace the smaller value in stack
                stack[idx] = num # replace
            else: 
                stack.append(num)
                if len(stack) == 3: return True
        return False