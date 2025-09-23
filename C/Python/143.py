S = input()
ans = ""
flag = True
for i in range(len(S)):
    if S[i] == "-" :
        if flag == True:
            ans += S[i]
            flag = False

    else:
        flag = True
        ans += S[i]
    
print(ans)