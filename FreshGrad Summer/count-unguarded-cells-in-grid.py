from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        '''
            m x n  grid
            guards[i] = rowi, coli
            walls[j] = rowsj, colj
            
            guard can see every cell in 4D cardinal 
                unless obstructed by wall or another guard
            
            cell guarded if there is at least one guard that can see it
            
            return all unguarded cells
            
         '''

        # create a 2D array of booleans
        # initially all cells are unguarded
        unguarded = [[True for _ in range(n)] for _ in range(m)]
        
        # iterate through guards
        for guard in guards:
            # iterate through cells in guard's row
            for i in range(n):
                # if cell is unguarded, set to false
                if unguarded[guard[0]][i]:
                    unguarded[guard[0]][i] = False
            # iterate through cells in guard's column
            for j in range(m):
                # if cell is unguarded, set to false
                if unguarded[j][guard[1]]:
                    unguarded[j][guard[1]] = False
        
        # iterate through walls
        for wall in walls:
            # iterate through cells in wall's row
            for i in range(n):
                # if cell is unguarded, set to false
                if unguarded[wall[0]][i]:
                    unguarded[wall[0]][i] = False
        
        # count unguarded cells
        count = 0
        for row in unguarded:
            for cell in row:
                if cell:
                    count += 1
        return count
        