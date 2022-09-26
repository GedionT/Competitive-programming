

def can_king_escape(n, ax, ay, bx, by, cx, cy) -> str:
    """Problem statement:
    print "YES" if king can get from bx,by to cx, cy without
    getting in check, otherwise print "NO"

    Returns:
        YES or NO
    """

    # do dfs in 8 directions of ax, ay
    # directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    # queen_visited = set()

    # # do dfs from ax, ay in an nxn grid
    # def dfs(x, y):
    #     if x < 0 or x >= n or y < 0 or y >= n:
    #         return False
    #     if (x, y) in queen_visited:
    #         return False
    #     queen_visited.add((x, y))
    #     if (x, y) == (cx, cy):
    #         return False
    #     for dx, dy in directions:
    #         if dfs(x + dx, y + dy):
    #             return True
    #     return False

    # # convolute bx, by over nxn grid
    # if dfs(ax, ay):
    #     return "YES"
    # else:
    #     return "NO"

    if (bx < ax) == (cx < ax) and (by < ay) == (cy < ay):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':

    n = int(input())  # n x n dimension of board

    ax, ay = map(int, input().split())  # queen coordinates
    bx, by = map(int, input().split())  # king coordinates
    cx, cy = map(int, input().split())  # target coordinates

    print(can_king_escape(n, ax, ay, bx, by, cx, cy))
