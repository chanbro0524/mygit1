N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

int_max=0
for i in range(N):
    for j in range(N):
        if j==i:
            continue
        if arr[i]==arr[j]:
            if abs(i-j)<=K:
                int_max=max(int_max,arr[i])
    if int_max==0:
        int_max=-1
print(int_max)
