from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_deg = [0] * (N + 1)

for _ in range(M):
    h, s = map(int, input().split())
    graph[h].append(s)
    in_deg[s] += 1

# トポロジカルソート
queue = deque()
for i in range(1, N + 1):
    if in_deg[i] == 0:
        queue.append(i)

res = []

while queue:
    if len(queue) >= 2:
        print(-1)
        exit()

    current = queue.popleft()
    res.append(current)

    for neighbor in graph[current]:
        in_deg[neighbor] -= 1
        if in_deg[neighbor] == 0:
            queue.append(neighbor)

if len(res) == N:
    print(" ".join(map(str, res)))
else:
    print(-1)
