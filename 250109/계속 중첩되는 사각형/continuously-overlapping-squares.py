n=int(input())
arr=[[0 for i in range(201)] for i in range(201)]
for i in range(n):
    x1,y1,x2,y2=tuple(map(int,input().split()))
    x1,y1,x2,y2=x1+100,y1+100,x2+100,y2+100
    if i%2==0:

        for j in range(x1,x2):
            for k in range(y1,y2):
                arr[j][k]='R'
    else:
        for j in range(x1,x2):
            for k in range(y1,y2):
                arr[j][k]='B'
count=0
for j in range(201):
            for k in range(201):
                if arr[j][k]=='B':
                    count+=1


print(count)
    