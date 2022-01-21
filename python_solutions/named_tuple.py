from collections import namedtuple

length, Score = int(input()), namedtuple("Score", input().split())

data = [int(Score(*input().split()).MARKS) for _ in range(length)]

print(sum(data) / length)

# challenge under 4 lines of code
