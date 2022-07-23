# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

s, k = input().strip().split()


for i in range(1, int(k)+1):
    for j in combinations(sorted(s), i):
        print(''.join(j))
