class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:        
        nums.sort()
        
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
            
        # for each query do a binary search and build res
        res = []
        for query in queries:
            idx = bisect_right(prefix_sum, query)
            res.append(idx)
            
        return res
        