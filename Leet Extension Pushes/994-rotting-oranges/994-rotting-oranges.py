class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
        
        rotten = deque([])
        fresh = set()
        time = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]  == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))
                else:
                    continue

        while fresh and rotten:
            prev_len = len(rotten)
            for _ in range(prev_len):
                i, j = rotten.popleft()

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if (ni, nj) in fresh:
                        rotten.append((ni, nj))
                        fresh.discard((ni, nj))

            time += 1
        
        if not fresh:
            return time

        return -1
                                    