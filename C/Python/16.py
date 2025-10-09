S = input()
d = {"A":4,"E":3,"G":6,"I":1,"O":0,"S":5,"Z":2}

ans = ""
for i in range(len(S)):
    if S[i] in d:
        ans += d[S[i]]
    else:
        ans += S[i]
print(ans)