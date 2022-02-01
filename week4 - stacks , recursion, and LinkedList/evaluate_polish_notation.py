from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for tk in tokens:

            if tk.isdigit():
                stack.append(tk)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if tk == "+":
                    val = "num1 + num2"
                elif tk == "/":
                    val = "num1 / num2"
                elif tk == "*":
                    val = "num1 * num2"
                elif tk == "-":
                    val = "num1 - num2"
                stack.append(eval(val))

        return stack[-1]


if __name__ == "__main__":

    sol = Solution()

    print(sol.evalRPN(["2", "1", "+", "3", "*"]))
    print(sol.evalRPN(["4", "13", "5", "/", "+"]))
