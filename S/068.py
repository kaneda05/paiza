N, V = map(int,input().split())

items = []
for _ in range(N):
    x, v, c = map(int,input().split())
    
    # ２進分割
    k = 1
    while c > 0:
        take = min(k, c)
        items.append((x * take, v * take))
        c -= take
        k <<= 1

# DP
dp = [0] * (V + 1)
for value, volume in items:
    for w in range(V, volume-1, -1):
        dp[w] = max(dp[w], dp[w - volume] + value)

print(max(dp))
        