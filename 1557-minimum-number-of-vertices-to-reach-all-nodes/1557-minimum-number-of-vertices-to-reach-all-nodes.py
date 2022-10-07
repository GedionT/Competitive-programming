class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indeg = defaultdict(int)
        nodes = set()
        
        for fr, to in edges:
            indeg[to] += 1
            if fr not in nodes:
                nodes.add(fr)
        
        return [ n for n in nodes if indeg[n] == 0 ]
        