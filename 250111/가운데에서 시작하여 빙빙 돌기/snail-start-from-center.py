n=int(input())


arr=[[0]*n for i in range(n)]


x,y=n//2,n//2
dx=[0,-1,0,1]
dy=[1,0,-1,0]
d=0


for i in range(1,n*n+1):
    arr[x][y]=i
    d1=(d+1)%4
    x,y=x+dx[d1],y+dy[d1]
    if arr[x][y]!=0:
        x,y=x+dx[d],y+dy[d]
    else:
        d=(d+1)%4
        x,y=x+dx[d],y+dy[d]




for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
