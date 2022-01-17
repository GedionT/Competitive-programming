class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for brace in s:
            if brace == '(' or brace == '[' or brace == '{':
                stack.append(brace)

            elif brace == ')' or brace == ']' or brace == '}':
                if len(stack) > 0:
                    last = stack[-1]
                    if brace == ')':
                        if ord(brace) == ord(last)+1:
                            stack.pop()
                    else:
                        if ord(brace) == ord(last)+2:
                            stack.pop()
            else:
                pass

        if len(stack) == 0:
            return True


if __name__ == "__main__":
    given = "()"
    s = Solution()
    print(s.isValid(given))
