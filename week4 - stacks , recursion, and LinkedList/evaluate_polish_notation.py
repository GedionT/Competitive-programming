from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for tk in tokens:
            if tk not in '+-/*':
                stack.append(tk)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                val = f"num1 {tk} num2"
                stack.append(eval(val))

        return int(stack[-1])


if __name__ == "__main__":

    sol = Solution()

    print(sol.evalRPN(["2", "1", "+", "3", "*"]))
    print(sol.evalRPN(["4", "13", "5", "/", "+"]))
    print(sol.evalRPN(["10", "6", "9", "3", "+",
                       "-11", "*", "/", "*", "17", "+", "5", "+"]))
