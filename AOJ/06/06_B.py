#cards = [[for n in range(13)] for s in range["S", "H", "C", "D"]]
#input
pattern = ["S", "H", "C", "D"]
cards = [[False for i in range(13)] for j in range(4)]

n = int(input())  # nは入力回数
str_list = []
for i in range(n):
    str_list.append(list(input().split()))#０行０列目に1枚目のカードの記号が入る　#０行１列目に一行目のカードの数字　S 1
    #ｎ行出てくる
    cards[pattern.index(str_list[i][0])][int(str_list[i][1])-1]= True #書き換えている
#str_list をtrue

#output
for j in range(4):
    for i in range(13):
        if cards[j][i]==False:print(pattern[j],i+1)
