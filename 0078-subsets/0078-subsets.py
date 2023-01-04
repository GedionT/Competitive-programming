class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []
        
        self.backtracker(0, nums, [])
    
        return self.ans
        
    def backtracker(self, idx, nums, combo): 
        
        if idx == len(nums):
            self.ans.append(combo[:])
            return 
        
        combo.append(nums[idx])
        self.backtracker(idx+1, nums, combo)
        combo.pop()
        self.backtracker(idx+1, nums, combo)
        
        
        