name = input()
li = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]
ans = ""
for i in range(len(name)):
    if name[i] not in li:
        ans += name[i]
print(ans)