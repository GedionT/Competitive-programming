# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# create a default dict for words belonging to group A
#key: word
# value: a list containing the position of each unique word appearance
# e.g {a: [1,2,3, b: [4,5,6]]}

def_dict = defaultdict(list)

n, m = map(int, input().split())
B = list()  # list containing words belonging to group B

for i in range(n):
    def_dict[input()].append(i+1)  # {a: [1,2,3], b: [4]..}

for _ in range(m):
    B += input().split()  # [a, b]

for s in B:  # foreach word in group B
    if s in def_dict.keys():  # if word is in our defaultdict, def_dict
        print(*def_dict[s])  # print the list elements(positions)
    else:
        print(-1)


# short alternative
# from collections import defaultdict
# if __name__ == '__main__':
#     d= defaultdict(list)
#     a, b = input().split()
#     for i in range(1,int(a)+1):
#         d[input()].append(i)
#     for _ in range(1,int(b)+1):
#         k = input()
#         if k in d.keys():
#             print(*d[k])
#         else:
#             print(-1)
