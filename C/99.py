N_D = input().split()
N = int(N_D[0])
D = int(N_D[1])

d = [D - int(input()) for _ in range(N - 1)]
print(D*(sum(d)+D))