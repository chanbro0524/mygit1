n,m=tuple(map(int,input().split()))


arr=[[0]*m for i in range(n)]


x,y=0,0
dx=[0,1,0,-1]

dy=[-1,0,1,0]


d=0

def inrange(x,y):
    if x<0 or y<0 or x>n-1 or y>m-1:
        return True
        

for i in range(1,n*m+1):
    arr[x][y]=i
    x1,y1=x+dx[d],y+dy[d]
    if inrange(x1,y1) or arr[x1][y1]!=0:
        d=(d+1)%4
        x,y=x+dx[d],y+dy[d]
    else:
        x,y=x+dx[d],y+dy[d]
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
