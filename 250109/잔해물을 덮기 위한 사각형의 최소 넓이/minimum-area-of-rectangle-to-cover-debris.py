arr=[[0 for i in range(2001)] for i in range(2001)]
for i in range(2):
    x1,y1,x2,y2=tuple(map(int,input().split()))
    for j in range(x1,x2+1):
        for k in range(y1,y2+1):
            arr[j][k]+=1
    if i==0:
        a,b,c,d=(x1,y1,x2,y2)
        
x1,y1,x2,y2=a,b,c,d
mx=x1
my=y1
for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        if arr[i][j]==1:
            if i>mx:
                mx=i
            if j>my:
                my=j

print((mx-x1)*(my-y1))


