N, M = map(int, input().split())

winners = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int,input().split())
    winners[x].append(y)
    # 勝った場合はこれまでの人を追加
    if len(winners[y]) != 0:
        for j in winners[y]:
            winners[x].append(j)
    # 負けた場合は初期化
    winners[y] = []

# 勝った数をそれぞれ追加
counts_list = []
for i in range(N):
    counts_list.append(len(winners[i+1]))

# 最大勝利数の算出
max_winner = max(counts_list)
for i in range(N):
    if max_winner == counts_list[i]:
        print(i+1)
        