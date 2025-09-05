H = int(input())
grid = [list(input().strip()) for _ in range(H)]

W = 5

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while True:
    marked = [[False]*W for _ in range(H)]
    any_marked = False
    
    # マーキング（同時消去のため）
    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                continue
            neigh = []
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < H and 0 <= nj < W:
                    neigh.append((ni, nj))
            
            if not neigh:
                continue
            ok = True
            digits = []
            for ni, nj in neigh:
                if grid[ni][nj] == ".":
                    ok = False
                    break
                digits.append(grid[ni][nj])
            if not ok:
                continue
            # 隣接がすべて同じ数字で、かつその数字が中心セル自身と同じであることを要求する
            if len(set(digits)) == 1 and digits[0] == grid[i][j]:
                marked[i][j] = True
                for ni, nj in neigh:
                    marked[ni][nj] = True
                any_marked = True

    if not any_marked:
        break

    # 消去
    for i in range(H):
        for j in range(W):
            if marked[i][j]:
                grid[i][j] = "."
                
    # 重力（各列を下に詰める）
    for j in range(W):
        write = H - 1
        for i in range(H - 1, -1, -1):
            if grid[i][j] != ".":
                grid[write][j] = grid[i][j]
                if write != i:
                    grid[i][j] = "."
                write -= 1

for i in range(H):
    print(''.join(grid[i]))
                    
                    
                    
                    