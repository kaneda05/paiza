N, M = map(int,input().split())
A, B, C = map(int,input().split())
R = [int(input()) for _ in range(N)]

cost = A + B * M
ans = 0
for i in range(N):
    if R[i]*C < cost:
        ans += 1
print(ans)