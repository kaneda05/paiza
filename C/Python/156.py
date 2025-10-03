N = int(input())
l1 = []
l2 = []
for i in range(N):
    l, e = input().split()
    l1.append(l)
    l2.append(e)
    

ans = 0

for i in range(N):
    hh1,hh2 = int(l1[i][0:2]), int(l2[i][0:2])
    mm1,mm2 = int(l1[i][3:5]), int(l2[i][3:5])
    
    ans += (hh2*60+mm2) - (hh1*60+mm1)
    
print(ans//60, ans%60)