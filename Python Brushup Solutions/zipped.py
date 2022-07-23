# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = map(int, input().split())

grades = []
for _ in range(x):
    grades.append(map(float, input().split()))

for i in zip(*grades):
    print(sum(i)/len(i))
