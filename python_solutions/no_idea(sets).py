# Enter your code here. Read input from STDIN. Print output to STDOUT


n, m = input().strip().split()

lst = list(map(int, input().strip().split()))

a = set(list(map(int, input().strip().split())))
b = set(list(map(int, input().strip().split())))

happiness = 0

for i in lst:
    if i in a:
        happiness += 1
    elif i in b:
        happiness -= 1
    else:
        pass

print(happiness)
