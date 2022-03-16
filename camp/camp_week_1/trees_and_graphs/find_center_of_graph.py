class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        
        # two edges can't have the same vertex
        # go through each elements in one edge and check if a number exists in the second
        for i in range(2):
            for j in range(2):
                if edges[i][j] in edges[i+1]:
                    return edges[i][j]
                    