N = int(input())
times = []

for _ in range(N):
    s, f, t = map(int,input().split())
    day_length = s + f + (24 - t)
    times.append(day_length)

print(min(times))
print(max(times))