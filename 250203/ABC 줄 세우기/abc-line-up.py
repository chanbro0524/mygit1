n = int(input())
arr = list(input().split())
arr1=arr[:]
arr.sort()
num=0
for j in range(n):
    for i in range(n):
        k=i
        if arr1[i]==arr[j]:
            for l in range(n):
                if k==j:
                    break
                t=arr1[i-1]
                arr1[i-1]=arr1[i]
                arr1[i]=t
                k-=1
                num+=1
            break
print(num)