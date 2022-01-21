class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        # if not s:
        #     return 0
        # max_len = 0
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         if self.isValid(s[i:j]):
        #             max_len = max(max_len, j-i)
        # return max_len

        # Approach 2: Stack
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        if not s:
            return 0
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i-stack[-1])
        return max_len

        # Approach 3: Dynamic Programming
        # Time Complexity: O(n)
        # Space Complexity: O(n)


if __name__ == "__main__":

    s = Solution()

    print(s.longestValidParentheses("()(()"))
