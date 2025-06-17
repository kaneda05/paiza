# 月ごとの累積日数（0始まりでアクセスしやすいようにダミー0を先頭に）
days_in_month = [0, 31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]

# 各月の開始日を求めて累積和にする
def date_to_day_of_year(month, day):
    return sum(days_in_month[:month]) + day

# 入力
N = int(input())
M_D_list = [tuple(map(int, input().split())) for _ in range(N+1)]

# パイザさんの誕生日
M0, D0 = M_D_list[0]
paiza_day = date_to_day_of_year(M0, D0)

# クラスメートの誕生日（通し日数に変換）
classmate_days = [date_to_day_of_year(m, d) for m, d in M_D_list[1:]]


sorted_days = sorted(classmate_days + [paiza_day])
rank_from_jan1 = sorted_days.index(paiza_day) + 1


base_day = date_to_day_of_year(4, 2)

def loop_sort_key(day):
    return (day - base_day) % 365

sorted_days_from_apr2 = sorted(classmate_days + [paiza_day], key=loop_sort_key)
rank_from_apr2 = sorted_days_from_apr2.index(paiza_day) + 1

# 出力
print(rank_from_jan1)
print(rank_from_apr2)
