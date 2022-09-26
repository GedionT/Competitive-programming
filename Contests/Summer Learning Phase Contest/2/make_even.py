

def make_even(num: int) -> int:
    """
    number of moves required to make the number even
    reverse the prefix of l leftmost digits of num
    """
    if num % 2 == 0:
        return 0

    num_s = str(num)
    l = len(num_s)

    l_pos = -1

    for i in range(l):
        if int(num_s[i]) % 2 == 0:
            l_pos = i
            break

    if l_pos == -1:
        return -1
    elif l_pos == 0:
        return 1
    else:
        return 2


if __name__ == '__main__':

    test = int(input())

    for _ in range(test):
        num = int(input())
        print(make_even(num))
