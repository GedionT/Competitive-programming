if source == target:
return 0
# build graph
graph = defaultdict(list)
for route in routes:
for idx in range(len(route)-1):
graph[route[idx]].append(route[idx+1])
graph[route[-1]].append(route[0])
# print(graph)
# do bfs and everytime a cycle detected increament count
# indicating a boundary has been crossed
count = 0
q = deque([])
visited = set()
q.append(source)
while q:
n = len(q)
for i in range(n):
curr = q.popleft()
visited.add(curr)
for neighb in graph[curr]:
if neighb in visited:
count += 1
elif neighb == target:
return count
else:
q.append(neighb)
return -1