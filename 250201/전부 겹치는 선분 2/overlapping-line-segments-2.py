n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]
num=0
arr=[0]*101
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        x=x1[j]
        y=x2[j]
        for k in range(x,y+1):
            arr[k]+=1
    if arr.count(n-1)>=1:
        print('Yes')
        num+=1
        break
if num==0:    
    print('No')