n,m=tuple(map(int,input().split()))
arr=[[0]*n for i in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def inrange(x,y):
    if x!=0 and x!=n-1 and y!=0 and y!=n-1:
        return True

for i in range(m):
    r,c=tuple(map(int,input().split()))
    r,c=r-1,c-1
    arr[r][c]=1
    cnt=0

    if inrange(r,c):
        for i in range(4):
            if arr[r+dx[i]][c+dy[i]]==1:
                cnt+=1

    if cnt==3:
        print(1)
    else:
        print(0) 

