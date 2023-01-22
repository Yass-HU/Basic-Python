#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja

#組み合わせの数

#1 から n までの数の中から、重複無しで３つの数を選びそれらの合計が x となる組み合わせの数を求めるプログラムを作成して下さい。

#例えば、1 から 5 までの数から３つを選んでそれらの合計が 9 となる組み合わせは、

#1 + 3 + 5 = 9
#2 + 3 + 4 = 9
#の２通りがあります。

#Input
#複数のデータセットが入力として与えられます。各データセットでは、空白で区切られた n、x が 1 行に与えられます。

#n、x がともに 0 のとき入力の終わりとします。
#nC3 = n! / (3! * (n-3)!) = n(n-1)(n-2) / (321)
# n, x = map(int, input().split())
# if n == 0 and x == 0:
       
    #n(n-1)(n-2)//6


while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i + j + k == x:
                    count += 1
    print(count)