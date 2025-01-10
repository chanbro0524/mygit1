n=int(input())


dx={'E':1,'N':0,'W':-1,'S':0}

dy={'E':0,'N':1,'W':0,'S':-1}


x,y=0,0

cnt=0
cnt1=0
for i in range(n):
    d,num=tuple(input().split())
    num=int(num)

    for j in range(num):
        x,y=x+dx[d],y+dy[d]
        
        cnt+=1
        if x==0 and y==0:
            cnt1=cnt
            break


    
if cnt1==0:
    print(-1)
else:
    print(cnt1)

