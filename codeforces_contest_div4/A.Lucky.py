
def is_lucky(string):

    left = [int(x) for x in string[:len(string)//2]]
    right = [int(x) for x in string[len(string)//2:]]

    if sum(left) == sum(right):
        return "Yes"
    else:
        return "NO"


if __name__ == '__main__':

    cases = int(input())

    for _ in range(cases):
        string = input()
        print(is_lucky(string))
