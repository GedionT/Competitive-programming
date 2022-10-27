class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        matrix = [ [float('inf')] * numCourses for _ in range(numCourses)]
        
        for pre in prerequisites:
            matrix[pre[0]][pre[1]] = 1
        
        # using floyd warshal algorithm to find all shortest path
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                    
        
        return [ True if matrix[i][j] != float('inf')  else False for i, j in queries ]