class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # instantiate the grid given the n*n side
        grid = [ [0 for col in range(n)] for row in range(n)]
        
        # add seed to increment and add value to the grid and instantiate the start of each grid
        seed = 1
        start = 0
        
        while n > 0:
            rowStart = colStart = start
            
            # fill the upper row
            while colStart < start + n:
                grid[rowStart][colStart] = seed
                seed += 1
                colStart += 1

            # rollback col idx
            colStart -=1
            rowStart += 1
            
            # fill the right edge
            while rowStart < start + n:
                grid[rowStart][colStart] = seed
                seed += 1
                rowStart += 1
            
            # rollback col idx
            rowStart -= 1
            colStart -=1

            
            # fill the bottom row
            while colStart >= start:
                grid[rowStart][colStart] = seed
                seed += 1
                colStart -= 1
    
            #rollback col idx
            colStart += 1
            rowStart -= 1
            
            # fill the left edge
            while rowStart > start:
                grid[rowStart][colStart] = seed
                seed += 1
                rowStart -= 1

            # shrink the edge by two
            n -= 2
            start += 1
            
        return grid
            
             