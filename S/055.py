from collections import defaultdict, deque

# 入力
H, W = map(int, input().split())
grid = [input().split() for _ in range(H)]
result = [row[:] for row in grid]  # 結果用グリッド（捕食で消すため）

N = int(input())
graph = defaultdict(list)      # predator -> list of prey
indegree = defaultdict(int)    # prey -> number of predators
animal_set = set()

# 捕食関係を構築
for _ in range(N):
    predator, prey = input().split()
    graph[predator].append(prey)
    indegree[prey] += 1
    animal_set.add(predator)
    animal_set.add(prey)

# マップ上の動物すべてを indegree に入れておく（0も含めて）
for row in grid:
    for animal in row:
        animal_set.add(animal)

for a in animal_set:
    indegree.setdefault(a, 0)

# トポロジカルソート（入次数が0のものから）
queue = deque()
for animal in animal_set:
    if indegree[animal] == 0:
        queue.append(animal)

# 捕食対象リスト（逆参照）
prey_map = defaultdict(set)
for predator in graph:
    prey_map[predator].update(graph[predator])

# 8方向（上下左右＋斜め）
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

# 捕食シミュレーション
while queue:
    predator = queue.popleft()
    for y in range(H):
        for x in range(W):
            if result[y][x] != predator:
                continue
            # 捕食者の周囲8マスを見る
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W:
                    target = result[ny][nx]
                    if target in prey_map[predator]:
                        result[ny][nx] = "-"  # 捕食成功で消える

    # 次に処理できる動物をキューへ
    for prey in graph[predator]:
        indegree[prey] -= 1
        if indegree[prey] == 0:
            queue.append(prey)

# 出力（フォーマット厳守）
for row in result:
    print(" ".join(row))
