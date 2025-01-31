n, k = map(int, input().split())
arr = list(map(int, input().split()))
import sys

cost=0
costmax=sys.maxsize
for i in range(max(arr)-min(arr)-k+1):
    cost=0
    minnum=min(arr)+i
    maxnum=minnum+2
    for j in arr:
        if j<minnum:
            cost+=minnum-j
        elif j>maxnum:
            cost+=j-maxnum
    costmax=min(costmax,cost)

print(costmax)