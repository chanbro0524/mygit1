n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]
maxx2=1
minx1=100
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        maxx2=max(maxx2,x2[j])
        minx1=min(minx1,x1[j])
    if maxx2<minx1:
        continue
    else:
        print('Yes')
        break