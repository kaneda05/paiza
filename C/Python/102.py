M = int(input())
A = [int(input()) for _ in range(M)]
N = int(input())
B = [int(input()) for _ in range(N)]

date = ["x"*32]
flag = True
for i in range(1,len(date)):
    if i in A and i in B:
        if flag:
            date[i] = "A"
            flag = False
        else:
            date[i] = "B"
            flag = True
    elif i in A:
        date[i] = "A"
    elif i in B:
        date[i] = "B"

for i in range(1,32):
    print(date[i])