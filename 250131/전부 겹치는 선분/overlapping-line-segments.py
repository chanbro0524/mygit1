n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)
arr=[0]*101
# Write your code here!

for x,y in zip(x1,x2):
    for i in range(x,y+1):
        arr[i]+=1

if arr.count(n)>=1:
    print('Yes')
else:
    print('No')