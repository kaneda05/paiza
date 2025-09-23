N = int(input())

ans = []

for i in range(N):
    a, b = input().split()
    if a == "y" and b == "y":
        continue
    else:
        ans.append(i+1)

print(len(ans))
for i in range(len(ans)):
    print(ans[i])
