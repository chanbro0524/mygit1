n = int(input())
arr = list(input().split())
arr1=[arr[i] for i in range(n)]
arr.sort()
num=0
for i in range(n):
    for j in range(n):
        if arr1[i]==arr[j]:
            if i==j:
                break
            t=arr1[i-1]
            arr1[i-1]=arr[i]
            arr[i]=t
            num+=1
            break
print(num)