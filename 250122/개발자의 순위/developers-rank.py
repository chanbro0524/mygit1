K, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]
s=0

for i in range(1,n):
    for j in range(i+1,n+1):
        if j==i:
            continue
        cnt1=0
        cnt2=0    
        for k in range(K):
            if arr[k].index(i)<arr[k].index(j):
                cnt1+=1
            elif arr[k].index(i)>arr[k].index(j):
                cnt2+=1
        if cnt1==K or cnt2==K:
            s+=1
print(s)
        
