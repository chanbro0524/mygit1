n,m=tuple(map(int,input().split()))
arr=[0]
cnt=0
for i in range(n):
    t,d=tuple(input().split())
    t=int(t)
    for i in range(t):
        if d=='L':
            cnt-=1
            arr.append(cnt)
        elif d=='R':
            cnt+=1
            arr.append(cnt)
arr1=[0]
cnt=0
for i in range(m):
    t,d=tuple(input().split())
    t=int(t)
    for i in range(t):
        if d=='L':
            cnt-=1
            arr1.append(cnt)
        elif d=='R':
            cnt+=1
            arr1.append(cnt)
cnt=0            
if len(arr)>len(arr1):
    n=len(arr)-len(arr1)
    for i in range(n):
        arr1.append(arr1[-1])
elif len(arr)<len(arr1):
    n=len(arr1)-len(arr)
    for i in range(n):
        arr.append(arr[-1])

for i in range(len(arr)-1):
    if arr[i]!=arr1[i] and arr[i+1]==arr1[i+1]:
        cnt+=1

print(cnt)
            

