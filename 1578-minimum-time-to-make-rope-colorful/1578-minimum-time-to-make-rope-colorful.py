class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
    
        tot_time = left = right = 0
        
        while left < len(neededTime) and right < len(neededTime):
            curr_total = curr_max = 0
            
            while right < len(neededTime) and colors[left] == colors[right]:
                curr_total += neededTime[right]
                curr_max = max(curr_max, neededTime[right])
                right += 1
                
            # end of curr group, add cost of group to tot tie and reset ptrs
            tot_time += curr_total - curr_max
            left = right
            
        return tot_time