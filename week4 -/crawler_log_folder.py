# time taken = 9 minutes

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = ['main']
        for log in logs:
            if log == '../' and stack[-1] != 'main':
                stack.pop(-1)
            elif log == './':
                continue
            elif log != '../':
                stack.append(log[:len(log)])

        return len(stack)-1


if __name__ == '__main__':
    s = Solution()
    logs = ["d1/", "d2/", "../", "d21/", "./"]
    print(s.minOperations(logs))
