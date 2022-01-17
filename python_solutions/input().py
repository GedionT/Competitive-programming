
x, k = list(map(int, input().split()))


P = input()  # function

# print(eval(P))  # evaluates by replacing x in the P function

if eval(P) == k:
    print(True)
else:
    print(False)
