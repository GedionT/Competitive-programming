# Time taken => 30 minutes
import math
from typing import List

class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        # sort with distance/speed with their time of arrival and eliminate startign from first elements

        count = 0
        arrivalTime = []

        for i, d in enumerate(dist):
            arrivalTime.append([math.ceil(d/speed[i]), d, speed[i]])
            arrivalTime.sort(key=lambda x: x[0])

        for x, d in enumerate(arrivalTime):
            count += 1
            if x + 1 < len(arrivalTime):
                if arrivalTime[x + 1][1] - (count * arrivalTime[x + 1][2]) <= 0:
                    return count
        return count


if __name__ == "__main__":

    sol = Solution()
    print(sol.eliminateMaximum([3, 4, 2], [3, 3, 3]))
