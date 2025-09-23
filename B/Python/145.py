N, K = map(int,input().split())


board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)


drawn_numbers = list(map(int, input().split()))


opened = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 0 or board[i][j] in drawn_numbers:
            opened[i][j] = True


bingo_count = 0

# 横のビンゴチェック（行）
for i in range(N):
    all_opened = True
    for j in range(N):
        if not opened[i][j]:
            all_opened = False
            break
    if all_opened:
        bingo_count += 1

# 縦のビンゴチェック（列）
for j in range(N):
    all_opened = True
    for i in range(N):
        if not opened[i][j]:
            all_opened = False
            break
    if all_opened:
        bingo_count += 1

# 左上から右下の対角線のチェック
all_opened = True
for i in range(N):
    if not opened[i][i]:
        all_opened = False
        break
if all_opened:
    bingo_count += 1

# 右上から左下の対角線のチェック
all_opened = True
for i in range(N):
    if not opened[i][N - 1 - i]:
        all_opened = False
        break
if all_opened:
    bingo_count += 1


print(bingo_count)
