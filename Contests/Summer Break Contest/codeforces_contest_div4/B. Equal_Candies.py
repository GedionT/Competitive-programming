from typing import List

def max_eatable(box_num: int, box_amount: List) -> int:
    
    eaten = 0
    _min = min(box_amount)

    for amount in box_amount:
        eaten += amount - _min

    return eaten

if __name__ == "__main__":

    cases = int(input())


    for _ in range(cases):
        box_num = int(input())
        box_amount = list(map(int, input().split()))

        print(max_eatable(box_num, box_amount))
