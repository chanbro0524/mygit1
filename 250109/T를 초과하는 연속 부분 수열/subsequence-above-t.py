n,t=tuple(map(int,(input().split())))
arr=list(map(int,input().split()))

cnt=0
mx=1
for i in range(n-1):
    if arr[i]>t:
        cnt+=1
    else:
        cnt=0
    mx=max(mx,cnt)


print(mx)