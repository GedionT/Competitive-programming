# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

for key, group in groupby(input().strip()):
    print("({}, {})".format(len(list(group)), key), end=" ")


# the groupby itertool returns a tuple of (key: (str, int, ..), group: [list of consecutive elements])
# the list is an iterable, but we change it to  list and we count to see how much is repeated
