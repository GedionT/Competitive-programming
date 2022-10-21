class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {}
        
        # add nums: [idxs] in dictionary
        for idx in range(len(nums)):
            if nums[idx] not in count:
                count[nums[idx]] = [idx]
            else:
                count[nums[idx]].append(idx)
        
        # since idxs are increasing and we need to come up with less than or k, build up on each list of idxs
        for num in count:
            for idxs in range(1, len(count[num])):
                if abs(count[num][idxs] - count[num][idxs-1]) <= k:
                    return True
                
        return False