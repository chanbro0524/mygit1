n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
intmax=0
for i in range(1,n+1):
    sum=0
    for j in range(m):
        k=arr[i]
        sum+=k
        i=k
    intmax=max(intmax,sum)
print(intmax)