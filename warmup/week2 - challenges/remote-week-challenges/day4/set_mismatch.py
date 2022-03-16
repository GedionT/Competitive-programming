# time taken -> 45 mins

from typing import Counter, List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        rep, missing = None, None
        n = len(nums)

        # hashmap to count the number of occurrences of each number
        lookup = Counter(nums)

        for i in range(1, n+1):  # O(n) time
            if i not in lookup:
                missing = i
            if lookup[i] > 1:
                rep = i
        return [rep, missing]

        # in place approach can be used
        # constant space and O(n) time
        # [1,2,2,4] rep
        # [1,2,3,4] missing

        # sum_actual - sum_expected = repeat - missing
        # prod_actual / prod_expected = repeat / missing

        # rep =  (prod_actual * missing) - sum_actual
        # missing = (sum_actual * rep) / prod_actual

        # prototype implementation
        # --------------------

        # sum_actual = sum(nums)
        # sum_expected = sum([i for i in range(1, n+1)])

        # missing = round((sum_actual * prod_expected) / prod_actual)
        # rep = round((prod_actual * missing) / sum_actual)

        # return [rep, missing]


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 2, 4]
    print(s.findErrorNums(nums))
