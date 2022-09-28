class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dic = defaultdict(int)
        
        def dfs(index=0, total=0):          
            key = (index, total)
            
            if key not in dic:
                if index == len(nums):                    
                    return 1 if total == target else 0
                else:
                    dic[key] = dfs(index+1, total + nums[index]) + dfs(index+1, total - nums[index])                    
                        
            return dic[key]                                                             
                
        return dfs()