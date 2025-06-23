import sys

lines = sys.stdin.read().splitlines()
N, M = map(int, lines[0].split())
A = list(map(int, lines[1:]))

total = 0
for d in A:
    if d <= M:
        total += d

print(total)