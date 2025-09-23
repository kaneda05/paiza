N = int(input())
x = int(input())

ans = N
for i in range(6):
    ans += int(N*(x/100))
    N = int(N*(x/100))

print(ans)