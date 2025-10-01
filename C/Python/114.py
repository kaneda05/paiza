N = int(input())
ls = [input() for i in range(N)]
for i in range(N-1):
    if ls[i][-1] == ls[i+1][0]:
        continue
    else:
        print(ls[i][-1], ls[i+1][0])
        exit()
        
print("Yes")