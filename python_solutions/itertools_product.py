# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

print(* product(A, B))
