# from typing import List


# def findLongest(sushi: List) -> int:
#     """
#     given a list find the longest subarray that has equal number of 1's and 2's
#     and each half of subsegment has only one type

#     It is guaranteed that there is at least one piece of sushi of each type.
#     Note that it means that there is at least one valid continuous segment.
#     """

#     # O(n) time

#     # iterate over the list and place consecutive count in an array

#     count_list = []

#     for i in range(len(sushi)):
#         count = 0
#         while sushi[i] == sushi[i+1]:
#             count += 1
#             i += 1
#         count_list.append(count)


#     print(count_list)


# if __name__ == "__main__":

#     n = int(input())
#     sushi = list(map(int, input().strip().split()))

#     print(findLongest(sushi))


def sushi_valid(arr):

    res = []
    ans = 0

    for i in range(len(arr)):
        if len(res) == 0:
            res.append(1)
            continue
        if arr[i] == arr[i-1]:
            res[-1] += 1
        else:
            res.append(1)
    for i in range(1, len(res)):
        ans = max(ans, min(res[i], res[i-1]))

    return ans * 2


if __name__ == "__main__":

    n = int(input())

    arr = list(map(int, input().split()))

    print(sushi_valid(arr))
