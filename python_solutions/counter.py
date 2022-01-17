# # without Counter

# X = int(input()) # number of shoes

# shoe_sizes = list(map(int, input().split()))
# shoe_sizes = shoe_sizes[0:X]

# money = 0

# N = int(input()) # number of customers

# for i in range(N):
#     size, price = input().split()
#     if size in shoe_sizes:
#         money += int(price)
#         shoe_sizes.remove(size)

# print(money)

# with Counter

# ------------------


from collections import Counter

X = int(input())

shoe_size_counter = Counter(map(int, input().split()))

N = int(input())
sales = 0
for _ in range(N):
    size, amount = list(map(int, input().split()))
    if shoe_size_counter.get(size):
        sales += amount
        shoe_size_counter[size] -= 1

print(sales)
