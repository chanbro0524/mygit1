N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

int_max=0
for i in range(N):
    count=0
    s=P[i]/2
    if s>B:
        continue
    count+=1
    for j in range(N):
        if i==j:
            continue
        if s+P[j]<=B:
            count+=1
            s=s+P[j]
    int_max=max(int_max,count)
print(count)
