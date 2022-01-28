from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return[[]]

        next_result = self.subsets(nums[1:])

        cur_result = []

        for _next in next_result[:]:
            cur_result.append(_next + [nums[0]])

        return cur_result + next_result


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
    print(s.subsets([1, 2, 3, 4]))
    print(s.subsets([1, 2, 3, 4, 5]))
