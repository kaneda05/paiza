from collections import Counter
import sys

sys.setrecursionlimit(10000)  # ネストが深くなる可能性を考慮

def parse(s, i=0):
    def parse_number():
        nonlocal i
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        return num if num > 0 else 1

    counter = Counter()
    while i < len(s):
        if s[i].isdigit():
            repeat = parse_number()
            if s[i] == '(':
                i += 1  # skip '('
                inner_counter, i = parse(s, i)
                for char in inner_counter:
                    counter[char] += repeat * inner_counter[char]
            else:
                # 単一文字の繰り返し
                if 'a' <= s[i] <= 'z':
                    counter[s[i]] += repeat
                    i += 1
        elif s[i] == ')':
            i += 1  # skip ')'
            return counter, i
        elif 'a' <= s[i] <= 'z':
            counter[s[i]] += 1
            i += 1
        else:
            i += 1  # 不正文字はスキップ
    return counter, i

# 入力例
compressed = input().strip()
count, _ = parse(compressed)

# 出力（a〜zの出現回数）
for ch in 'abcdefghijklmnopqrstuvwxyz':
    print(f"{ch} {count[ch]}")
