class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trustship = [0] * (n)
        graph = defaultdict(list)
        
        for ai, bi in trust:
            graph[ai].append(bi)
            trustship[bi-1] += 1
            
        for idx in range(len(trustship)):
            if trustship[idx] == len(trustship)-1:
                if len(graph[idx+1]) == 0:
                    return idx+1
        
        return -1
                
            