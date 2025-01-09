n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr2=[]
for i in range(n):
    if i==0 or arr[i]*arr[i-1]<0:
        arr2.append(i)


arr3=[]
for i in range(len(arr2)-1):
    arr3.append(arr2[i+1]-arr2[i])
    
print(max(arr3))
