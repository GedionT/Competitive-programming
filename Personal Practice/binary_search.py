from bisect import bisect_left, bisect_right


def bisectLeft(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left+right)//2
        if nums[mid] < target:
            left = mid+1
        else:
            right = mid
    return left


def bisectRight(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left+right)//2
        if nums[mid] <= target:
            left = mid+1
        else:
            right = mid
    return left


if __name__ == "__main__":
    eg1 = [1, 3, 5, 5, 6, 7, 9]         # 5
    eg2 = [1, 2, 4, 5, 6, 6, 6, 10]     # 6
    eg3 = [1, 2]                        # 2

    print(bisectLeft(eg1, 5))  # should be 2
    print(bisectLeft(eg2, 6))  # should be 4
    print(bisectLeft(eg3, 1))  # should be 0
    print("--------------")
    print(bisectRight(eg1, 5))  # should be 4
    print(bisectRight(eg2, 6))  # should be 7
    print(bisectRight(eg3, 1))  # should be 1
