graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


visit = set()


def dfs(visit, graph, node):
    if node not in visit:
        print(node, end=" ")
        visit.add(node)

        for neighbor in graph[node]:  # add all adjacent nodes
            dfs(visit, graph, neighbor)


# Driver Code
bfs(visited, graph, 'A')
print("\n")
dfs(visit, graph, 'A')
