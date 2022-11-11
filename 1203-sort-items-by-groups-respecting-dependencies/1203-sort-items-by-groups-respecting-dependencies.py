class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        for g in range(len(group)):
            if group[g] == -1:
                group[g] = m
                m += 1
                
        # create an item and group graph
        groupGraph = [ [] for i in range(m) ]   
        itemGraph = [ [] for i in range(n) ]
        gIndeg = [0]*len(groupGraph)
        iIndeg = [0]*len(itemGraph)
        
        for idx in range(n):
            for each in beforeItems[idx]:
                if group[each] != group[idx]:
                    groupGraph[group[each]].append(group[idx]) 
                    gIndeg[group[idx]] += 1
                itemGraph[each].append(idx) 
                iIndeg[idx] += 1 
        
        # topSort the group ordering and item ordering
        groupOrder = self.topSort(groupGraph, gIndeg)        
        itemOrder = self.topSort(itemGraph, iIndeg)
        
        if not groupOrder or not itemOrder:
            return []
        
        # regroup items by respecting group ordering and item ordering
        group_items = defaultdict(list)
        for i in itemOrder:
            group_items[group[i]].append(i)
        
        return [i for grp in groupOrder for i in group_items[grp]]
                
        
    def topSort(self, graph, indeg):      
        q = deque([])

        for idx in range(len(indeg)):
            if indeg[idx] == 0:
                q.append(idx)

        order = []
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                order.append(curr)

                for node in graph[curr]:
                    indeg[node] -= 1
                    if indeg[node] == 0:
                        q.append(node)

        return order if len(order) == len(graph) else []
    
        
        
        