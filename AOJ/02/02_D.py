W, H, x, y, r = map(int, input().split())

if x - r < 0:
    print("No")
elif y - r < 0:
    print("No")
elif x + r > W:
    print("No")
elif y + r > H:
    print("No")
else:
    print("Yes")