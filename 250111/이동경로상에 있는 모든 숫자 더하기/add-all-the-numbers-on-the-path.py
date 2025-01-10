n,t=tuple(map(int,input().split()))
order=input()

arr=[list(map(int,input().split())) for i in range(3)]

dx=[-1,0,1,0]
dy=[0,-1,0,1]
d=0
x,y=n//2,n//2
cnt=0
def inrange(x, y):
    return 0 <= x < n and 0 <= y < n

        
arr2=[]   
for i in range(t):
    o=order[i]
    if o=='L':
        d=(d+1)%4
    elif o=="R":
        d=(d+3)%4
    elif o=="F":
        x1,y1=x+dx[d],y+dy[d]
        if inrange(x1,y1):
            x,y=x+dx[d],y+dy[d]      
    if arr[x][y] not in arr2:
        arr2.append(arr[x][y])
cnt=0
for i in arr2:
    cnt+=i
print(cnt)