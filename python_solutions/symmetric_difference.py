# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()  # useless but to pass hackerrank test
N = set(map(int, input().split()))
m = input()  # useless but to pass hackerrank test
M = set(map(int, input().split()))

sym_difference = N.union(M) - N.intersection(M)
# sym_difference = N.symmetric_difference(M) # alternative

for i in sorted(sym_difference):
    print(i)
