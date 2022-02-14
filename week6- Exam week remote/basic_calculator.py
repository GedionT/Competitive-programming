class Solution:
    def calculate(self, s: str) -> int:

        s = s.replace(" ", "")

        num, sign = 0, "+"
        stack = []

        for i in range(len(s)):

            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if s[i] in "+-*/" or i == len(s) - 1:

                if sign == "+":
                    stack.append(num)

                elif sign == "-":
                    stack.append(-num)

                elif sign == "*":
                    exp = stack.pop() * num
                    stack.append(exp)

                else:
                    exp = int(stack.pop()/num)
                    stack.append(exp)

                num = 0
                sign = s[i]

        return sum(stack)
