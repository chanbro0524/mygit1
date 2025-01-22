n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
arr=[0]*n
for i in range(n):
    for j in range(n):
        if j==i:
            continue
        if lines[i][0]<lines[j][0]:
           if  lines[i][1]>lines[j][1]:
                arr[i]+=1
        elif lines[i][0]>lines[j][0]:
           if  lines[i][1]<lines[j][1]:
                arr[i]+=1
print(arr.count(0))