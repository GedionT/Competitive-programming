class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_stack, t_stack = [], []

        for ch in s:
            if ch == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(ch)

        for ch in t:
            if ch == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(ch)

        return s_stack == t_stack


if __name__ == '__main__':
    s = Solution()
    s1 = "ab#c"
    s2 = "ad#c"
    print(s.backspaceCompare(s1, s2))
