# 入力の受け取り
N, M = map(int, input().split())

# A[i][j] = i番目路線の 1駅目 → j駅目 の累積運賃
A = [list(map(int, input().split())) for _ in range(N)]

X = int(input())   # 経由する駅の数
route = [tuple(map(int, input().split())) for _ in range(X)]

# スタート地点
cur_line, cur_station = 1, 1
total_cost = 0

# 経由駅を順に処理
for Ri, Si in route:
    # Ri, Si は 1始まりなので0始まりに直す
    Ri -= 1
    Si -= 1

    # 無料で駅番号cur_stationのままRi路線に移動できるので、
    # Ri路線上で (cur_station-1) → Si の運賃を計算
    total_cost += abs(A[Ri][Si] - A[Ri][cur_station - 1])

    # 現在位置を更新
    cur_line = Ri + 1
    cur_station = Si + 1

# 答えを出力
print(total_cost)
