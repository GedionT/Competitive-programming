class Solution:
    def calPoints(self, ops: List[str]) -> int:

        stack = []

        for op in ops:

            if op == "D":
                a = int(stack.pop())
                stack.extend([a, 2*a])

            elif op == "C":
                stack.pop()

            elif op == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.extend([b, a, a+b])

            else:
                stack.append(int(op))

        return sum(stack)


if __name__ == "__main__":
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(Solution().calPoints(ops))
