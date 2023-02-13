class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefixM, result = 0, 0

        modGroups = [0] * k
        modGroups[0] = 1

        for num in nums:
            prefixM = (prefixM + num) % k
            result += modGroups[prefixM]
            
            modGroups[prefixM] += 1

        return result