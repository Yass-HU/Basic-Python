a, b = map(int,input().split())
d = a // b
r = a % b
f = a / b
#print(f"a is {a:.3f}")
print(f"{d} {r} {f:.5f}")
#print(d,r,f)
#print('{1},{2},{:.5f}'.format(d, r, f))#-5f{0:.5f}
#error result check fについては0.00001以下の誤差があってもよいものとします？5keta