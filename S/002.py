from collections import deque
import sys

sys.setrecursionlimit(10**7) 

# 入力受け取り
M, N = map(int, input().split())
grid = []
start = goal = None

for y in range(N):
    row = input().split()
    for x in range(M):
        if row[x] == 's':
            start = (y, x)
        elif row[x] == 'g':
            goal = (y, x)
    grid.append(row)

# BFS準備
visited = [[False]*M for _ in range(N)]
dist = [[-1]*M for _ in range(N)]
queue = deque()

# スタート地点から探索開始
sy, sx = start
queue.append((sy, sx))
visited[sy][sx] = True
dist[sy][sx] = 0

# 移動方向（上下左右）
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS
while queue:
    y, x = queue.popleft()
    
    # ゴールに到達したら終了
    if (y, x) == goal:
        print(dist[y][x])
        break
    
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx] and grid[ny][nx] in ('0', 'g'):
                visited[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))
else:
    # ゴールにたどり着けなかった
    print("Fail")
