# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    cmd, *args = input().split()  # parse or destructure based on argument

    expression = f"s.{cmd}{*map(int, args),}"
    eval(expression)

print(sum(s))
