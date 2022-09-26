# simulate rock falling down in a graph ., *, o - (space, rock, obstacle) respectively

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    grid = []
    for _ in range(n):
        temp = list(input())
        grid.append(temp)

    for i in range(n):
        for j in range(m):
            print(grid[i][j], end='')
        print()
