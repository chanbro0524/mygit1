n,m=tuple(map(int,input().split()))
arr=[[0]*n for i in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def inrange(x,y):
    if x<0 or x>n-1 or y<0 or y>n-1:
        return False
    else:
        return True

for i in range(m):
    r,c=tuple(map(int,input().split()))
    r,c=r-1,c-1
    arr[r][c]=1
    cnt=0

    for i in range(4):
        if inrange(r+dx[i],c+dy[i]):
            if arr[r+dx[i]][c+dy[i]]==1:
                cnt+=1

    if cnt==3:
        print(1)
    else:
        print(0) 

