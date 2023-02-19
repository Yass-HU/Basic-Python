alpha = "abcdefghijklmnopqrstuvwxyz"
# 空の辞書
# text = ""
count = {}
for a in alpha:
    count[a] = 0

# 辞書を読み込ませる
while True:
    try:
        input_str = input()
    except EOFError:
        break
    for char in input_str:
        char = char.lower()
        if char in count:
            count[char] += 1

for a in alpha:
    print(f"{a} : {count[a]}")
