N = int(input().strip())
stones = [list(map(int, input().split())) for _ in range(N)]

total_remove = 0
for i in range(N):
    for j in range(N):
        # 層番号を求める
        layer = min(i, j, N - 1 - i, N - 1 - j)
        need = layer + 1
        total_remove += stones[i][j] - need

print(total_remove)