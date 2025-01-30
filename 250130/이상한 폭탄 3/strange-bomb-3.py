N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]
arr=[0]*1000000
for i in range(N-1):
    for j in range(i+1,N):
        if num[i]==num[j]:
            if j-i<K:
                arr[num[i]]+=1

print(arr.index(max(arr)))
