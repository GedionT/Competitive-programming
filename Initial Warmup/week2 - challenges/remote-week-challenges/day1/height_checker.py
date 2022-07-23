# time-taken = 4 minutes

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)  # O(n.log n)

        unmatched_index = [i for i in range(
            len(heights)) if heights[i] != expected[i]]  # O(n)

        return len(unmatched_index)

        # efficient space complexity: O(1)
        # count = 0
        # for i in range(len(heights)):
        #     if heights[i] != expected[i]:
        #         count += 1
        # return count


if __name__ == "__main__":
    sol = Solution()
    heights = [1, 1, 4, 2, 1, 3]
    print(sol.heightChecker(heights))
