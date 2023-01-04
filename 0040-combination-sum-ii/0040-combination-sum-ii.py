class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = list()
        candidates.sort()

        self.findCombination(0, target, candidates, [])
        
        return self.combinations
        
    def findCombination(self, idx, targetState, candidates, validComb):
        if targetState == 0:
            self.combinations.append(validComb[:])
            return 
        
        
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]: 
                continue
                
            if candidates[i] > targetState:
                break
                
            validComb.append(candidates[i])
            self.findCombination(i+1, targetState - candidates[i], candidates, validComb)
            validComb.pop()
