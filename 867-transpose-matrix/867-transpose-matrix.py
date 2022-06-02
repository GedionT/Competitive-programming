class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # return zip(*matrix) - easy hack
        
        
        """
            [1, 2, 3]        [1, 4, 7]
            [4, 5, 6]   ->   [2, 5, 6]
            [7, 8, 9]        [3, 6, 9]
        """
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        T = [[0] * m for _ in range(n) ]
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                T[c][r] = val
        
        return T
        
                