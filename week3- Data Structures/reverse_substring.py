class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                temp = []
                ch = stack.pop()
                while ch != '(':
                    temp.append(ch)
                    ch = stack.pop()
                for j in range(len(temp)):
                    stack.append(temp[j])

        return "".join(stack)


if __name__ == "__main__":
    given = "a(bcdefghijkl(mno)p)q"
    s = Solution()
    print(s.reverseParentheses(given))
