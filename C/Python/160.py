import math
N = int(input())
d = list(map(int,input().split()))
avg = sum(d)/N
print(math.ceil(avg))