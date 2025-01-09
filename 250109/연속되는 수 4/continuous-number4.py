n=int(input())
arr=[int(input()) for i in range(n)]

cnt=1
mx=1
for i in range(n-1):
    if arr[i+1]>arr[i]:
        cnt+=1
    else:
        cnt=1
    mx=max(mx,cnt)


print(mx)