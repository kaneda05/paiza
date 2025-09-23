N, M = map(int,input().split())
t = list(map(int,input().split()))

point = 0
for i in range(N):
    point += t[i]//100

if point >= M:
    print(0)
else:
    print((M-point)*100)