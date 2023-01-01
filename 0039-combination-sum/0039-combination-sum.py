class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.findComb(0, target, candidates, [])
        return self.res
        
    def findComb(self, idx, target, candidates, combo):
        if idx == len(candidates):
            if target == 0:
                self.res.append(combo[:])
            return
        
        if candidates[idx] <= target:
            combo.append(candidates[idx])
            self.findComb(idx, target-candidates[idx], candidates, combo)
            combo.pop()
            
        self.findComb(idx+1, target, candidates, combo)
        
        