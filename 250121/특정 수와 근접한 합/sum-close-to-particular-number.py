N, S = map(int, input().split())
arr = list(map(int, input().split()))
import sys
int_min=sys.maxsize
for i in range(N):
    for j in range(i+1,N):
        s=sum(arr)-arr[i]-arr[j]
        int_min=min(int_min,abs(s-S))

print(int_min)