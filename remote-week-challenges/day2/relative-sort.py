# time taken -> 25 minutes

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # arr2 - distinct and subset of arr1
        # arr1 should be sorted relatively same to arr2
        # elements not in arr2 - placed at the end of arr1 ascendingly

        out = []

        for v2 in arr2:
            for i, v1 in enumerate(arr1):
                if v2 == v1:
                    out.append(arr1[i])
                    arr1[i] = None
        remaining_arr1 = list(filter(None, arr1))
        # everything not found on arr2 append sorted
        out = out + sorted(remaining_arr1)
        return out


if __name__ == "__main__":
    sol = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(sol.relativeSortArray(arr1, arr2))
