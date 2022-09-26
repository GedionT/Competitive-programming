from collections import defaultdict

graph = defaultdict(list)

nodes = int(input())
for _ in range(nodes):
    x, y = map(int, input().split())
    graph[x].append(y)

candidate = list(map(int, input().split()))

queue = []  # Initialize a queue


def bfs(graph, node):
    queue.append(node)

    while queue:
        s = queue.pop(0)
        sp = candidate.pop(0)

        if s != sp:
            return "No"

        for neighbor in graph[s]:
            queue.append(neighbor)

        for q in queue:
            if q not in candidate:
                return "No"

    return "Yes"


print(bfs(graph, 1))


# ============


graph = defaultdict(list)

nodes = int(input())
for _ in range(nodes-1):
    x, y = map(int, input().split())
    graph[x].append(y)

candidate = list(map(int, input().split()))

queue = []
ans = []


def bfs(graph, node, candidate):
    queue.append(node)

    while queue:
        s = queue.pop(0)

        if s != candidate[0]:
            return "No"

        for neighbor in graph[s]:
            queue.append(neighbor)
            ans.append(neighbor)

        for i in ans:
            if i not in candidate[1:len(ans)]:
                return "No"

        candidate = candidate[len(ans):]
        ans.clear()

    return "Yes"


print(bfs(graph, 1, candidate))
