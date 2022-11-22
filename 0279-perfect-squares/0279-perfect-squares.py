class Solution:
    def numSquares(self, n: int) -> int:
        
        perf_squares = [ i*i for i in range(1, n) ]
        visited = set()
        
        queue = deque([(n, 1)])
        visited.add(n)
        
        while queue:
              node, d = queue.popleft()
              
              if node in perf_squares: # found perfect square
                    return d
              
              for ps in perf_squares:
                    if node <= ps:
                        break
                      
                    if node - ps not in visited:
                        visited.add(node-ps)
                        queue.append((node - ps, d + 1))
        return n
                
        