

target = int(input())

adds = 0

while target:
    next = target // 2
    rem = target % 2

    adds += rem

    target = next


print(adds)
