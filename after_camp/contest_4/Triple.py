from typing import List
from collections import Counter

def triple(arr: List) -> int:
    
    
    count_dict = Counter(arr)
    
    result = 0

    for element, count in count_dict.items():
        if count >= 3:
            result = element

    if result == 0:
        return -1
        
    return result

num_test = int(input())

for _ in range(num_test):
    size = int(input())
    arr = list(map(int, input().split()))

    print(triple(arr))



    


