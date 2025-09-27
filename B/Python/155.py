H, W, N = map(int,input().split())
stamps = []
for _ in range(N):
    stamp = [input().rstrip('\n') for __ in range(H)]
    stamps.append(stamp)

R, C = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(R)]

ans = []
for i in range(R):
    for subrow in range(H):
        parts = []
        for j in range(C):
            idx = B[i][j] - 1
            parts.append(stamps[idx][subrow])
        ans.append(''.join(parts))

print('\n'.join(ans))