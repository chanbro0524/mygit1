arr=input()
dy=[1,0,-1,0]
dx=[0,1,0,-1]
d=0
x,y=0,0

for i in range(len(arr)):
    if arr[i]=='R':
        d=(d+1)%4
    elif arr[i]=='L':
        d=(d+3)%4
    elif arr[i]=='F':
        x,y=x+dx[d],y+dy[d]
        if x==0 and y==0:
            print(i+1)
            break
    
    
    