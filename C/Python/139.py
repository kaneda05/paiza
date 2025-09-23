N = int(input())
x_set = set()
for i in range(N):
    x = int(input())
    if N < x:
        continue
    else:
        x_set.add(x)
    
print(N-len(x_set))