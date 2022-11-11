class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        # assign group for groupless elements (for implementation sake)
        # i.e. each groupless element gets a unique group as they can be intermingled between groups
        # i.e. they don't need to be together
        for g in range(len(group)):
            if group[g] == -1:
                group[g] = m
                m += 1
                
        # create an item and group graph
        groupGraph = { i: [] for i in range(m) }   # can use a list of list instead since it's a 0-n numbering
        itemGraph = { i: [] for i in range(n) }
            
        # adjust group edge based on the dependency of beforeItems
        # adjust graph edge of each element based on beforeItems
        for idx in range(n):
            for each in beforeItems[idx]:
                if group[each] != group[idx]:
                    groupGraph[group[each]].append(group[idx])  # can do 2 birds one stone by calc indeg 
                itemGraph[each].append(idx) # calc indeg here as well and pass to util func of topsort

        
        # topSort the group ordering and item ordering
        groupOrder = self.topSort(groupGraph)        
        itemOrder = self.topSort(itemGraph)
        
        # if a cycle is detected in groups or items, return []
        if not groupOrder or not itemOrder:
            return []
        
        # regroup items by respecting group ordering and item ordering
        group_items = defaultdict(list)
        for i in itemOrder:
            group_items[group[i]].append(i)
        
        return [i for grp in groupOrder for i in group_items[grp]]
                
        
    def topSort(self, graph):
        """
        Util function for topsorting using kahn's algorithm
        O(v+e)
        """
        indeg = [0]*len(graph)

        # count incoming degree
        for node in graph:
            for val in graph[node]:
                indeg[val] += 1

        q = deque([])

        # process nodes without indegree into queue
        for idx in range(len(indeg)):
            if indeg[idx] == 0:
                q.append(idx)

        # top sorting using bfs
        order = []

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                order.append(curr)

                for node in graph[curr]:
                    indeg[node] -= 1
                    if indeg[node] == 0:
                        q.append(node)

        # graph contains cycle ret [] else topsort list             
        return order if len(order) == len(graph) else []
    
        
        
        