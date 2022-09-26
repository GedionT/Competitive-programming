from collections import defaultdict, deque


def bfs(root: int) -> int:
    queue = deque([root])
    level = 0

    while queue:
        for _ in range(len(queue)):
            p = queue.popleft()
            for c in tree[p]:
                queue.append(c)
        level += 1

    return level


if __name__ == '__main__':
    roots = []
    tree = defaultdict(list)

    for i in range(1, int(input())+1):
        node = int(input())
        if node == -1:
            roots.append(i)
        else:
            tree[node].append(i)

    _max = 0
    for root in roots:
        _max = max(bfs(root), _max)

    print(_max)
