N, K = map(int,input().split())
p = [list(map(int,input().split())) for _ in range(N)]

ans = 0
shop_number = set()
for k in range(K):
    min_pnk = 10**3
    for n in range(N):
        if p[n][k]<min_pnk:
            shop_number = n
    shop_number.add(n)

print(len(shop_number))