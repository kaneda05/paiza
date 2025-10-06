n, m = map(int,input().split())
h, w = map(int,input().split())

plans = []
for _ in range(n):
    plans.append(list(map(int, input().split())))

field = [[0]*w for _ in range(h)]
harvest = [0] * (m+1)

for plan in plans:
    a, b, c, d = plan
    
    for r in range(a-1, b):
        for c_ in range(c-1, d):
            if 0 <= r < h and 0 <= c_ < w:
                if field[r][c_] != 0:
                    harvest[field[r][c_]] += 1
                
                field[r][c_] = e


for i in range(1, m+1):
    print(harvest[i])

for row in field:
    output_row = ""
    for cell in row:
        if cell == 0:
            output_row += "."
        else:
            output_row += str(cell)
    print(output_row)