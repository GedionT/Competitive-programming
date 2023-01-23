class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trustship = [0] * (n+1)
        graph = defaultdict(list)
        
        for ai, bi in trust:
            graph[ai].append(bi)
            trustship[bi] += 1
            
        for idx in range(1, len(trustship)):
            if trustship[idx] == len(trustship)-2:
                if len(graph[idx]) == 0:
                    return idx
        
        return -1
                
            