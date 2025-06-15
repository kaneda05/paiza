import sys
input = sys.stdin.readline

# 入力の読み取り
H, W = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(H)]

# DP配列の初期化（最後の行はそのまま得点）
dp = [[0]*W for _ in range(H)]
dp[H-1] = s[H-1][:]  # 最後の行をコピー

# 後ろ（H-2）から前（0）へ
for i in range(H-2, -1, -1):
    for j in range(W):
        max_score = 0
        for dj in [-1, 0, 1]:  # 左手前、手前、右手前
            nj = j + dj
            if 0 <= nj < W:
                max_score = max(max_score, dp[i+1][nj])
        dp[i][j] = s[i][j] + max_score

# 最上段から最大スコアを選ぶ
print(max(dp[0]))
