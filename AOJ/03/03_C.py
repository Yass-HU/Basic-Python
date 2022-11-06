#https://tysonblog-whitelabel.com/aoj-itp-1-40#index_id12
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    elif x < y:
        print(x, y)
    else:
        print(y, x)
        