from typing import List


def findLongest(sushi: List) -> int:
    # find longest valid continuous to have equal 1 and 2
    # if there is no such subsegment, return 0

    # [2, 2, 2, 1, 1, 2, 2] -> 4
    # because [2, 2, 1, 1] longest subsegment
    # return 4 -> len(subsegment)
    # 

    longest = 0
    current = 0

    for i in range(len(sushi)):
        if i == 0:
            current += 1
        elif sushi[i] != sushi[i-1]:
            current += 1
        else:
            current = 1
        if current > longest:
            longest = current
    # don't know why off by 1
    
    return longest








if __name__ == "__main__":

    n = int(input())
    sushi = list(map(int, input().strip().split()))

    print(findLongest(sushi))
