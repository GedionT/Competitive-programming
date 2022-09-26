

def calc_days(s) -> int:

    tmp = set()
    days = 1

    stack = [s[0]]
    for char in s:

        if char not in stack and len(stack) < 3:
            stack.append(char)

        if char in stack:
            continue

        if char not in stack and len(stack) == 3:
            stack.clear()
            stack.append(char)
            days += 1

    return days


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print(calc_days(input()))
