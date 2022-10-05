W,H,x,y,r= map(int,input().split())
r=abs(r)
if x-r>=0 and y-r>=0 and x+r<=W and y+r<=H:
    print("Yes")
else:
    print("No")
