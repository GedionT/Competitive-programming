
from typing import List


def find_possible_places(shop_prices: List[int], day: int) -> int:
    """
    Given a list of prices, find the possible places to buy the item
    """

    # approach one - brute force
    # count = 0

    # for p in shop_prices:
    #     if day >= p:
    #         count += 1

    # return count

    # approach two - binary search
    left = 0
    right = len(shop_prices) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if shop_prices[mid] <= day:
            left = mid + 1
        else:
            right = mid - 1

    return left

    # shop_prices.sort()
    # left = 0
    # right = len(shop_prices) - 1

    # while left <= right:
    #     mid = left + (right - left) // 2
    #     if shop_prices[mid] <= day:
    #         left = mid + 1
    #     elif shop_prices[mid] > days:
    #         right = mid - 1
    #     else:
    #         return mid
    # return 0


if __name__ == "__main__":

    n = int(input())
    shop_prices = list(map(int, input().strip().split()))

    shop_prices.sort()

    days = int(input())

    ans = []

    for i in range(days):
        day = int(input())
        ans.append(find_possible_places(shop_prices, day))

    for i in ans:
        print(i)
