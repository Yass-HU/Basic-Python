while True:
    table = input().split()
    a = int(table[0])
    op = table[1]
    b = int(table[2])
    if op == "?":
        break
    elif op == "+":
        print(int(a + b))
    elif op == "-":
        print(int(a - b))
    elif op == "*":
        print(int(a * b))
    elif op == "/":
        print(int(a / b))
    else:
        pass