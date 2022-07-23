chairs, hours = map(int, input().split())

chair_coords, sun_coords = {}, []
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]


# def inbound(x, y, startx, starty, endx, endy):
#     return x >= startx and x <= endx and y >= starty and y <= endy


for _ in range(chairs):
    coords = tuple(map(int, input().split()))
    if coords in chair_coords.keys():
        chair_coords[coords] += 1
    else:
        chair_coords[coords] = 1

for _ in range(hours):
    sun_coords.append(list(map(int, input().split())))

for i in range(hours):
    startx, starty, endx, endy = sun_coords[i]

    count = 0

    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            if chair_coords.get((x, y), 0) > 0:
                count += chair_coords.get((x, y), 0)

    print(count)


"""
 
 # run bfs starting on startx, starty
    queue = [(startx, starty)]
    visited = set()
    visited.add((startx, starty))
    while queue:
        x, y = queue.pop(0)
        if (x, y) in chair_coords.keys():
            count += chair_coords[(x, y)]
        for dx, dy in directions:
            newx, newy = x + dx, y + dy
            if inbound(newx, newy, startx, starty, endx, endy):
                if (newx, newy) not in visited:
                    queue.append((newx, newy))
                    visited.add((newx, newy))"""
