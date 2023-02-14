class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        N = len(nums) // 2      
        ans = abs(sum(nums[:N]) - sum(nums[N:]))
        total = sum(nums) 
        half = total // 2 
        
        for k in range(1, N):
            left = [sum(comb) for comb in combinations(nums[:N], k)]
            right = [sum(comb) for comb in combinations(nums[N:], N-k)]
            right.sort()
            for x in left:
                r = half - x
                p = bisect.bisect_left(right, r) 
                if 0 <= p < len(right):
                    left_ans_sum = x + right[p]
                    right_ans_sum = total - left_ans_sum
                    diff = abs(left_ans_sum - right_ans_sum)
                    ans = min(ans, diff) 
        return ans