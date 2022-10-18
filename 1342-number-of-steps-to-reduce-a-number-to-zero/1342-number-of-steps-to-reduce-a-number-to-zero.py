class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.helper(num, 0)
        
    
    def helper(self, num: int, steps: int) -> int:
        if num == 0:
            return steps
        
        if num % 2 == 0:
            return self.helper(num//2, steps+1)
        
        return self.helper(num-1, steps+1)