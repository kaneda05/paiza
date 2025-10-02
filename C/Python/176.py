N = int(input())
for i in range(N):
    s = list(input())
    t = list(input())

    t.sort()
    s.sort()
    
    if s == t:
        print("Yes")
    else:
        print("No")