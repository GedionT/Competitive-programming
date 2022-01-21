# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

s, k = input().strip().split()

for perm in sorted(permutations(s, int(k))):
    print(''.join(perm))

"""
You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

Input Format
A single line containing the space separated string  and the integer value .

Constraints
The string contains only UPPERCASE characters.

Output Format
Print the permutations of the string  on separate lines.
"""
