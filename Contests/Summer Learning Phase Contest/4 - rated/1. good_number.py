
def kgood(a, k):
    kgood = 0

    for num in a:
        b = 0
        while num:
            # check all digits are less than or equal to k
            if num % 10 <= k:
                num //= 10
            else:
                b = 1
                break

        if b == 0:
            kgood += 1

    return kgood


if __name__ == "__main__":

    n, k = map(int, input().split())

    a = []
    for _ in range(n):
        a.append(int(input()))

    print(kgood(a, k))


# after understanding

n, k = input().split()
count = 0
for _ in range(int(n)):
    visited = set()
    num = input()
    for n in num:
        if n <= k:
            visited.add(n)
    if len(visited) == int(k) + 1:
        count += 1

print(count)
