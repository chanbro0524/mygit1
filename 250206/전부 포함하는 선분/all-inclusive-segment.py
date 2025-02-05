n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
intmin=100
# Write your code here!
for i in range(n):
    x=[]
    y=[]
    for j in range(n):
        if i==j:
            continue
        x.append(segments[j][0])
        y.append(segments[j][1])

    intmin=min(intmin,max(y)-min(x))

print(intmin)