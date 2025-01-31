n, k = map(int, input().split())
arr = list(map(int, input().split()))

cost=0
if max(arr)-min(arr)<=k:
    print(cost)
else:
    cost=0
    cost1=0
    for i in range(len(arr)):
        if arr[i]<min(arr)+(max(arr)-min(arr)):
            cost+=min(arr)+(max(arr)-min(arr))-arr[i]
    for  j in range(len(arr)):
        if arr[j]>max(arr)-(max(arr)-min(arr)):
            cost1+=max(arr)-(max(arr)-min(arr))-arr[j]
    print(max(cost,cost1))

