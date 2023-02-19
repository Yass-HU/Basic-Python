# 8_B
def new_func():
    return int


while True:
    x = sum(map(new_func(), input()))
    if x > 0:
        print(x)
    else:
        break
