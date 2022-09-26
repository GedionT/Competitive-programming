from typing import List


def restore_a(b: List[int]) -> List[int]:
    """
    a = [ 1, 4, 3]
    b = [ 1+4+3, 1+4, 1, 4+3, 1+3, 4, 3].sort() -> [1, 3, 4, 4, 5, 7, 8]

    given b return a
    """
    # n = len(b)
    # a = [0] * n
    # for i in range(n):
    #     a[i] = b[i] - sum(b[:i])
    # return a

    if b[0]+b[1] == b[2]:
        return [b[0], b[1], b[3]]
    else:
        return [b[0], b[1], b[2]]


if __name__ == '__main__':

    n = int(input())

    for _ in range(n):
        b = list(map(int, input().rstrip().split()))
        print(*restore_a(b))
