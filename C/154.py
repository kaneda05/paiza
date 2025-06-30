N, L = map(int, input().split())
u = list(map(int, input().split()))

total = sum(u)

max_u = max(u)
if max_u >= L:
    print(total-max_u//2)
else:
    print(total)