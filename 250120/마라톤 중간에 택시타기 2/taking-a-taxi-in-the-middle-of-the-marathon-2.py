n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
import sys
num=sys.maxsize
for i in range(1,n):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    del x[1]
    del y[1]
    dis=0
    for j in range(len(x)-1):
        dis+=abs(x[j]-x[j+1])+abs(y[j]-y[j+1])
    num=min(num,dis)

print(num)
