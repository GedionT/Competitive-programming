from typing import List

# Nati's approach for constant time
# would it be in the range of multiple of four
# check that and do subs 

def min_31_or_32(k: int) -> int:
    '''
    operations = current + 4 || current - 1
    minimum operation possible to get from start number to target number
    return if it is faster to begin with 31 or 32
    '''
    target = k
    min_31 = 0
    min_32 = 0

    current_31 = 31
    current_32 = 32

    while current_31 != target:

        if current_31 > target:
            current_31 -= 1
            min_31 += 1

        else:
            current_31 += 4
            min_31 += 1


    #  TODO: refactor code to work with passing a secondary dependency as a dep injection to make it work for 31 and 32

    while current_32 != target:
            
        if current_32 > target:
            current_32 -= 1
            min_32 += 1

        else:
            current_32 += 4
            min_32 += 1

    if min_31 < min_32:
        return 31
    else: 
        return 32


if __name__ == "__main__":

    n = int(input())

    targets = []

    for i in range(n):
        targets.append(int(input()))

    for target in targets:
        print(min_31_or_32(target))
    



    