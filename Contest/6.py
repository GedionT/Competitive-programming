# Given an integer array, move all 0's to the end maintaining the order of the other elements

def move_zeros(nums):
    zeros = []
    for i in range(len(nums)-nums.count(0)):
        if nums[i] == 0:
            zeros.append(nums[i])
            nums.pop(i)
    nums.extend(zeros)
    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12, 0, 22, 1]
    print(move_zeros(nums))
