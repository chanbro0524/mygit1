n = int(input())
arr = list(map(int, input().split()))

# Write your code here!f
arr1=[]
arr2=[]
for i in range(n):
    if arr[i]>0:
        arr1.append(arr[i])
    elif arr[i]<0:
        arr2.append(arr[i])


if len(arr2)==1 :
    if 0 in arr:
        print(0)
    else:
        arr1.sort()
        arr2.sort(reverse=True)
        print(arr2[0]*arr1[1]*arr1[2])
elif len(arr1)==0:
    if 0 in arr:
        print(0)
    else:
        arr2.sort(reverse=True)
        print(arr2[0]*arr2[1]*arr2[2])
else:
    arr1.sort(reverse=True)
    arr2.sort()
    print(arr1[0]*arr2[0]*arr2[1])