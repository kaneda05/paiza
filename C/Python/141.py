from collections import Counter
N = int(input())
A = [input() for _ in range(N)]
c = Counter(A)

ans = -1
for key,value in c.items():
    if ans < value:
        ans = value
        name = key

print(name)