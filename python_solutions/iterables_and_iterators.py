# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input().strip())
str_list = input().strip().split()
k = int(input().strip())
count, total = 0, 0

for v in combinations(str_list, k):
    total += 1
    if 'a' in v:
        count += 1


print(f'{count/total:2f}')
