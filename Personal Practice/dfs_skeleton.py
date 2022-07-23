
"""
    graph below in adjacency list format represented as:
    
           1
         /   \
        2      3
       / \    / \
     4   5 - 6   7

"""


graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': ['6'],
    '6': [],
    '7': []
}

visited = set()


def dfs(graph, startNode):

    if startNode not in visited:
        print(startNode)
        visited.add(startNode)

        for node in graph[startNode]:
            dfs(graph, node)


dfs(graph, '1')
