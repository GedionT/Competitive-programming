
from typing import List
import math

# v = d/t
# t = d/v


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        arrivalTime = []

        for i, d in enumerate(dist):
            arrivalTime.append([math.ceil(d/speed[i]), d, speed[i]])

        # n log n - sort based on arrival time
        arrivalTime.sort(key=lambda x: x[0])

        # count number of arriving monsters
        # count = 0
        # for i in arrivalTime:
        #     count += 1
        #     if i[0] != arrivalTime[0][0]:
        #         break
        # return count

        return len([arrivalTime[j][1] - arrivalTime[j][0]
                    for j in range(len(arrivalTime)) if arrivalTime[j][1] - arrivalTime[j][0] <= 0])


if __name__ == '__main__':
    s = Solution()
    print(s.eliminateMaximum([1, 1, 2, 10], [
          1, 1, 1, 4]))
