n=int(input())
arr1 = [[0 for _ in range(201)] for _ in range(201)]
for i in range(n):
    x,y=tuple(map(int,input().split()))
    x,y=(x+100,y+100)
    x1,y1=(x+8,y+8)
    for i in range(x,x1):
        for j in range(y,y1):
            arr1[i][j]+=1

count=0
for i in range(0,201):
    for j in range(0,201):
        if arr1[i][j]!=0:
            count+=1

print(count)