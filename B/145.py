# 入力の読み込み
N, K = map(int,input().split())

# ビンゴカードの読み込み
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

# 抽選された数字の読み込み
drawn_numbers = list(map(int, input().split()))

# 抽選された数字＋中央の0を「開いた数字」として記録
opened = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 0 or board[i][j] in drawn_numbers:
            opened[i][j] = True

# ビンゴの数を数える
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

# 結果を出力
print(bingo_count)
