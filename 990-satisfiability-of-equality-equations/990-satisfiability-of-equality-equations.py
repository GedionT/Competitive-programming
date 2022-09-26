class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        def buildGraph(edges:set) -> dict:
            graph = {}
            for n1, n2 in edges:
                graph[n1] = graph.get(n1, [])
                graph[n1].append(n2)
                graph[n2] = graph.get(n2, [])
                graph[n2].append(n1)
            return graph

        def hasPath(graph, src, dst, visited):
            if src not in graph or dst not in graph:
                return False
            if src in visited:
                return False
            visited.add(src)
            if src == dst:
                return True
            for n in graph[src]:
                if hasPath(graph, n, dst, visited):
                    return True
            return False

        connected = set()
        disconnected = set()

        for e in equations:
            if e[1:3] == '==':
                connected.add((e[0], e[-1]))
            else:
                if e[0] == e[-1]:
                    return False                
                disconnected.add((e[0], e[-1]))

        equation = buildGraph(connected)
        for src, dst in disconnected:
            if hasPath(equation, src, dst, set()):
                return False

        return True
        
        """
            a==b, b==c, b==d, d==a, e!=a, f==e
            
            a: b
            b: c, d
            d: a
            e:
            f: e
        """    
        """
        
        graph = defaultdict(list)
        
        # build the graph
        for equation in equations:
            if equation[1] == '=':
                graph[equation[0]].append(equation[3])
            else:
                if graph[equation[0]]:
                    continue
                graph[equation[0]] = []
    
        
        visit = set()
        
        def dfs(node, tmp):
            if node not in visit:
                visit.add(node)
                tmp.append(node)
                for neighbor in graph[node]:  
                    if neighbor in graph.keys():
                        dfs(neighbor, tmp)
                return tmp             
        

        # finding connected comoponents
        ans = []

        
        for g in graph:
            tmp = []
            sol = dfs(g, tmp)
            if sol:
                ans.append(sol)
            
        print(ans)
        
        """
    