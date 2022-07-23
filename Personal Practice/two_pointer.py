from typing import List

def reverse_in_place(values: List) -> List:

    left = 0
    right = len(values) - 1

    while left < right:

        values[left], values[right] = values[right], values[left]

        left += 1
        right -= 1



if __name__ == "__main__":

    chars = [1, 2, 3, 4, 5, 6, 7]

    reverse_in_place(chars)

    print(chars)
