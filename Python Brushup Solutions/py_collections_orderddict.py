from collections import OrderedDict

number_ = int(input())

dct = OrderedDict()
item_name = []
price = []
for i in range(number_):
    item = input().split(' ')
    item_name.append(" ".join(item[:-1]))
    price.append(int(item[-1]))

for s, t in zip(item_name, price):
    dct[s] = dct.get(s, 0) + t

for i, j in dct.items():
    print(i, j)
