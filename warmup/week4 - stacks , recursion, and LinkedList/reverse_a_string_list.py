
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse recursively

        def reverse(s, start, end):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]
            reverse(s, start+1, end-1)

        reverse(s, 0, len(s)-1)
        return s


# Time: O(n)
# Space: O(1)
if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)
