class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # daily temp = [ 73, 74, 75, 71, 69, 72, 76, 73 ]
        # answer =     [ 1, 1, 4, 2, 1, 1, 0, 0 ]

        # daily temp = [ 30, 40, 50, 60 ]
        # answer =     [ 1, 1, 1, 0 ]

        answer = [0] * len(temperatures)  # [0, 0, 0, ...., n]
        stack = []  # pair [temperature, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                answer[stackInd] = (i - stackInd)
            stack.append([t, i])

        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(s.dailyTemperatures([30, 40, 50, 60]))
