# 入力の読み込み
N, H, W = map(int, input().split())
sy, sx = map(int, input().split())
s = input().strip()

# 0-indexed に調整
sy -= 1
sx -= 1

# チョコレート数の2次元配列の取得
choco_grid = [list(map(int, input().split())) for _ in range(H)]

# 移動方向の辞書（dy, dx）
directions = {
    'F': (-1, 0),
    'B': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

# 記録開始
y, x = sy, sx
visited = set()
visited.add((y, x))

# 最初の座席でもらったチョコ
result = [choco_grid[y][x]]

# 移動処理
for move in s:
    dy, dx = directions[move]
    ny, nx = y + dy, x + dx

    # 移動可能かチェック
    if 0 <= ny < H and 0 <= nx < W and (ny, nx) not in visited:
        y, x = ny, nx
        visited.add((y, x))
        result.append(choco_grid[y][x])
    # 移動不可または再訪は無視

# 結果の出力（1行で）
for i in range(len(result)-1):
    print(result[i+1])
