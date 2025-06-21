n, l = map(int,input().split())
for _ in range(n):
    x = int(input())
    if l > x:
        l += x // 2
    elif l < x:
        l //= 2
print(l)