import heapq

def dijkstra(H, W, grid, sx, sy, gx, gy):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dist = [[float('inf')] * W for _ in range(H)]
    dist[sx][sy] = 0
    hq = [(0, sx, sy)]

    while hq:
        cost, x, y = heapq.heappop(hq)
        if (x, y) == (gx, gy):
            return cost
        if dist[x][y] < cost:
            continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W:
                new_cost = cost + grid[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(hq, (new_cost, nx, ny))
    return -1

# 入力読み取り
H, W = map(int, input().split())

grid = []

for i in range(H):
    row = input().strip()
    grid_row = []
    for j, c in enumerate(row):
        if c == 'S':
            sx, sy = i, j
            grid_row.append(0)
        elif c == 'G':
            gx, gy = i, j
            grid_row.append(0)
        else:
            grid_row.append(int(c))
    grid.append(grid_row)
    
print(dijkstra(H, W, grid, sx, sy, gx, gy))
