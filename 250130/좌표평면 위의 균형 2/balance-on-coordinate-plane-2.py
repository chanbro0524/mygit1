n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!

def sqare(arr,x,y,a,b):
    if a>x and b>y:
        arr[0]+=1
    elif a<x and b>y:
        arr[1]+=1
    elif a<x and b<y:
        arr[2]+=1
    elif a>x and b<y:
        arr[3]+=1
intmin=1000
for i in range(2,1001,2):
    for j in range(2,1001,2):
        arr=[0,0,0,0]
        for a,b in points:
            sqare(arr,i,j,a,b)
        intmax=max(arr)
        intmin=min(intmin,intmax)

print(intmin)
        