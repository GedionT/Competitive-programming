tests = int(input())


def min_divider(divider, n, m):

    if n == m or n <= 2:
        return 0

    divider.sort()
    total, count = 2, 0

    while divider:
        new = divider.pop()
        total += new - 1
        count += 1

        if total >= n:
            return count

    return -1


for _ in range(tests):
    n, m = input().split()
    divider = list(map(int, input().split()))

    print(min_divider(divider, int(n), int(m)))
