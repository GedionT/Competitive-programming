class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ans = [set() for i in range(n)]
        incoming = { i: 0 for i in range(n) }
        graph = defaultdict(list)
        queue = deque()
        
        for come, to in edges:
            incoming[to] += 1
            graph[come].append(to)
        
        for keys in incoming.keys():
            if incoming[keys] == 0:
                queue.append(keys)
        
        while queue:
            node = queue.popleft()
            for neigh in graph[node]:
                ans[neigh] = ans[neigh] | (ans[node])
                ans[neigh].add(node)
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    queue.append(neigh)
                    
        for i in range(len(ans)):
            ans[i] = sorted(list(ans[i]))

        return ans