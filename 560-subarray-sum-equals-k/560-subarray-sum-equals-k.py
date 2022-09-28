class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = [0]
        count = 0
        
        for idx in range(len(nums)):
            prefix.append(nums[idx] + prefix[-1])
        counter = Counter(prefix)
        
        for i in range(len(prefix)-1, -1, -1):
            counter[prefix[i]] -= 1
            if counter[prefix[i] - k] > 0:
                count += counter[prefix[i]-k]
                
        return count
        