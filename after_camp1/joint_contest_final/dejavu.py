

def is_deja(s):

    left = 0
    right = len(s)-1

    while left <= right:
        if s[left] != s[right]:
            s = s[:right] + 'a' + s[right:]
            print("YES")
            print(s)
            return
        elif s[left] == s[right] and s[right] != 'a':
            s = s[:right+1] + 'a' + s[right+1:]
            print("YES")
            print(s)
            return
        else:
            left += 1
            right -= 1

    print("NO")


if __name__ == "__main__":

    cases = int(input())

    for _ in range(cases):
        s = input()
        is_deja(s)
