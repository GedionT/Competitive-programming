from typing import List


def assistants_not_showing_up(days: int, assistants: List):
    """
    days: number of running days
    assistants: range of days assistants will be present
    return: Yes if assistants are not present on all days
    """
    _min = float('inf')
    _max = float('-inf')

    for each_range in assistants_range:
        _min = min(_min, each_range[0])
        _max = max(_max, each_range[1])

    if _max == days-1 and _min == 0:
        return 'NO'
    else:
        return 'YES'

    # s = sorted(allocated_days)
    # print(s)

    # # TODO: instead of iteration find a way to get summation of all numbers to 1 to n
    # # calc sum of s and if not equal return no
    # # check if there is a missing number in allocated_days thats present in range 0 to days
    # for i in range(days+1):
    #     print(i)
    #     if i not in s:
    #         return "NO"

    # return "YES"


if __name__ == '__main__':

    days, assistants = input().split()

    assistants_range = []

    for i in range(int(assistants)):
        assistants_range.append(list(map(int, input().strip().split())))

    print(assistants_not_showing_up(int(days), assistants_range))


# second solution
#
#
def main():
    n, m = map(int, input().split())
    assistants = [[0, 0] for i in range(m)]
    merged = []

    for i in range(m):
        d1, d2 = map(int, input().split())
        assistants[i] = [d1, d2]

    assistants.sort()
    start = assistants[0][0]
    end = assistants[0][1]

    for i in range(1, m):
        if end + 1 >= assistants[i][0]:
            end = max(end, assistants[i][1])
        elif end < assistants[i][0]:
            merged.append([start, end])
            start = assistants[i][0]
            end = assistants[i][1]

    merged.append([start, end])

    if len(merged) > 1:
        print("YES")
    elif merged[0][0] > 0 or merged[0][1] < n - 1:
        print("YES")
    else:
        print("NO")


main()
