N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

import sys
int_max=-sys.maxsize

for i in range(min(pos),max(pos)):
    s=0
    for j in range(i-K,i+1+K):

        arr=[]
        arr.append(j)

        for c,p in zip(candy,pos):
            if p in arr:
                s+=c
    int_max=max(int_max,s)
print(int_max)