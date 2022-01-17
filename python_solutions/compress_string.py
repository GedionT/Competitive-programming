# Enter your code here. Read input from STDIN. Print output to STDOUT
# using groupby from itertools

# todo: 1222311 -> (1,1) (3,2) (1, 3) (2, 1)


from itertools import groupby

for key, group in groupby(input()):
    print(f"({len(list(group))}, {key})", end=" ")
