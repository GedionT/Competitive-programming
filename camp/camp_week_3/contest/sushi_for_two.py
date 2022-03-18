from typing import List


def findLongest(sushi: List) -> int:
    """
    given a list find the longest subarray that has equal number of 1's and 2's
    and each half of subsegment has only one type

    It is guaranteed that there is at least one piece of sushi of each type. 
    Note that it means that there is at least one valid continuous segment.
    """
    max_count = 0

    # do it in O(n) time

    # first find the max count
    for i in range(len(sushi)):
        count = 0
        for j in range(i, len(sushi)):
            if sushi[j] == 1:
                count += 1
            elif sushi[j] == 2:
                count -= 1
            if count == 0:
                max_count = max(max_count, j - i + 1)

    return max_count


if __name__ == "__main__":

    n = int(input())
    sushi = list(map(int, input().strip().split()))

    print(findLongest(sushi))
