n=int(input())
arr=[tuple(map(int,input().split())) for i in range(n)]
int_max=0
for i in range(n):
    arr1=[0]*1000
    for j in range(n):
        if j==i:
            continue
        a,b=arr[j]
        for k in range(a,b):
            arr1[k]+=1
    c=1000-arr1.count(0)
    int_max=max(int_max, c)

print(int_max)