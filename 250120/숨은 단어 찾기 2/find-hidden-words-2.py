N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dx=[1,1,0,-1,-1,-1,0,1]
dy=[0,-1,-1,-1,0,1,1,1]


def in_range(x,y):
    if x>=0 and x<N and y>=0 and y<M:
        return True
    else:
        return False
num=0
for i in range(N):
    for j in range(M):
        if arr[i][j]=='L':
            for a,b in zip(dx,dy):
                x,y=i,j
                if in_range(x+a,y+b):
                    x=x+a
                    y=y+b
                    if arr[x][y]=='E':
                        if in_range(x+a,y+b):
                            x=x+a
                            y=y+b
                            if arr[x][y]=='E':
                                num+=1

print(num)