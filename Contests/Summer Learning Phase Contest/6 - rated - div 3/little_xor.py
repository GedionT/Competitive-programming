n = int(input())
a = list(map(int, input().split()))

max_xor = 0
for i in range(n):
    for j in range(i, n):
        xor = 0
        for k in range(i, j+1):
            xor ^= a[k]
        max_xor = max(max_xor, xor)

print(max_xor)
