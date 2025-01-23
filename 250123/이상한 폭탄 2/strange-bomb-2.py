N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

int_max=1
for i in range(N):
    for j in range(N):
        if j==i:
            continue
        if arr[i]==arr[j]:
            if abs(i-j)<=K:
                int_max=max(int_max,arr[i])
print(int_max)
