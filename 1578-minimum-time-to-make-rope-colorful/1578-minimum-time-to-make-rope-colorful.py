class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        run_sum = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                run_sum += min(neededTime[i], neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
        
        return run_sum
    
    