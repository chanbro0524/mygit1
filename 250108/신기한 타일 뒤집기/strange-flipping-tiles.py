n=int(input())
k=100000
arr=[0 for i in range(200001)]
for i in range(n):
    num,od = tuple(input().split())
    num=int(num)
    if od=='R':
        for j in range(k,k+num):
            arr[j]='B'
        k=k+num-1
    if od=='L':
        for j in range(k-num+1,k+1):
            arr[j]='W'
        k=k-num+1
                

c1=0
c2=0
c3=0
for i in range(200001):
    if arr[i]=='W':
        c1+=1
    elif arr[i]=='B':
        c2+=1
print(c1,c2)