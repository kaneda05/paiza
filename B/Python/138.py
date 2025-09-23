H, W = map(int,input().split())
grid = [input().strip() for _ in range(H)]

count = 0
for i in range(1, H-1):
    for j in range(1, W-1):
        if grid[i][j] != ".":
            continue
        ok = True
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                if grid[i+di][j+dj] != "#":
                    ok = False
        if ok:
            count += 1

print(count)