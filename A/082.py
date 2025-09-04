from collections import deque

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

# 湖マスの総数
lake_cells = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == "#"]
lake_count = len(lake_cells)

# 移動方向
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(si, sj, blocked):
    visited = [[False]*W for _ in range(H)]
    q = deque()
    q.append((si, sj))
    visited[si][sj] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W:
                if (nx, ny) == blocked:   # 除外マスは無視
                    continue
                if not visited[nx][ny] and grid[nx][ny] == "#":
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt

ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == ".":  # 陸は常にOK
            ans += 1
        else:  # 湖の場合
            # 除外したあとに探索
            remaining = lake_count - 1
            if remaining == 0:  # 湖が1マスしかない場合 → 消しても分断しない
                ans += 1
                continue
            # スタート地点（除外するマス以外の湖）
            start = None
            for x, y in lake_cells:
                if (x, y) != (i, j):
                    start = (x, y)
                    break
            if start is None:
                continue
            reach = bfs(start[0], start[1], (i, j))
            if reach == remaining:
                ans += 1

print(ans)
