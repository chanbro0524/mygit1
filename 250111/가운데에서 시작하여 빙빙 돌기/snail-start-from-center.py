n=int(input())


arr=[[0]*n for i in range(n)]


x,y=n//2,n//2
dx=[0,-1,0,1]
dy=[1,0,-1,0]
d=3
def indirect(x,y):
    if x>=0 and y>=0 and x<=n-1 and y<=n-1:
        return True

for i in range(1,n*n+1):
    arr[x][y]=i
    d1=(d+1)%4
    x1,y1=x+dx[d1],y+dy[d1]
    if arr[x1][y1]!=0:
        x,y=x+dx[d],y+dy[d]
    elif arr[x1][y1]==0:
        d=(d+1)%4
        x,y=x+dx[d],y+dy[d]




for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
