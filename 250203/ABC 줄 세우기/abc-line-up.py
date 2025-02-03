n = int(input())
arr = list(input().split())
arr1=[arr[i] for i in range(n)]
arr.sort()
num=0
for i in range(n):
    if arr1[i]!=arr[i]:
        num+=1
if num==0:
    print(0)
else:
    print(num-1)