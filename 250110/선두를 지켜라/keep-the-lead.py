n,m=tuple(map(int,input().split()))
arr=[]
d=0
for i in range(n):
    v,t=tuple(map(int,input().split()))
    for j in range(t):
        d+=v
        arr.append(d)
arr1=[]
d=0
for i in range(m):
    v,t=tuple(map(int,input().split()))
    for j in range(t):
        d+=v
        arr1.append(d)
arr3=[]
lead=0 
cnt=0
for i in range(len(arr)):
    if arr[i]>arr1[i]:
        if lead==2:
            cnt+=1
        lead=1
    elif arr[i]<arr1[i]:
        if lead==1:
            cnt+=1
        lead=2
print(cnt)



