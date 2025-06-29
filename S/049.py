from collections import deque
import math

N, X, F, S = map(int, input().split())

# 各状態を (書いた行数, 現在のスピード) として記録
# dist[written][speed] = 最短時間
dist = [[math.inf] * (X + 1) for _ in range(N + 1)]

# 初期状態
dist[0][X] = 0
queue = deque()
queue.append((0, X))  # (書いた行数, スピード)

while queue:
    written, speed = queue.popleft()
    time = dist[written][speed]

    # 1. 開発する（1時間使う）
    new_written = min(N, written + speed)
    new_speed = max(0, speed - F)
    if dist[new_written][new_speed] > time + 1:
        dist[new_written][new_speed] = time + 1
        queue.append((new_written, new_speed))

    # 2. 睡眠をとる（3時間使う）
    new_speed = min(X, speed + S)
    if dist[written][new_speed] > time + 3:
        dist[written][new_speed] = time + 3
        queue.append((written, new_speed))

# 最短時間を行数Nの状態から探す
print(min(dist[N]))
