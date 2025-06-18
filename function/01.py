# ビンゴゲームにおける縦横斜めが揃っているか探索する関数
# 全部揃っていた場合Trueを返す

def check_rows(opened, N):
    count = 0
    for i in range(N):
        if all(opened[i][j] for j in range(N)):
            count += 1
    return count

def check_columns(opened, N):
    count = 0
    for j in range(N):
        if all(opened[i][j] for i in range(N)):
            count += 1
    return count

def check_main_diagonal(opened, N):
    return 1 if all(opened[i][i] for i in range(N)) else 0

def check_anti_diagonal(opened, N):
    return 1 if all(opened[i][N - 1 - i] for i in range(N)) else 0