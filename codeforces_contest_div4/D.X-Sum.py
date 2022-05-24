from typing import List


def is_bound(grid: List[List], i: int, j: int) -> bool:
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def max_bishop_sum(grid: List[List]) -> int:
    n = len(grid)

    # 4 way diagonal directions
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Initialize the max sum
    max_sum = 0

    # Loop through the grid
    for i in range(n):
        for j in range(n):
            # do dfs in all 4 directions
            for direction in directions:
                # Initialize the sum
                _sum = 0
                # Initialize the current position
                cur_i = i
                cur_j = j
                # Loop until we reach the boundary
                while is_bound(grid, cur_i, cur_j):
                    # Add the current value to the sum
                    _sum += grid[cur_i][cur_j]
                    # Move to the next position
                    cur_i += direction[0]
                    cur_j += direction[1]
                # Update the max sum
                max_sum = max(max_sum, _sum)

    return max_sum


if __name__ == "__main__":

    cases = int(input())

    for _ in range(cases):
        n, m = map(int, input().split())
        grid = []

        for _ in range(n):
            grid.append(list(map(int, input().split())))

        print(max_bishop_sum(grid))
