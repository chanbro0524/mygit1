a = input()
arr1=[int(i) for i in a]
arr=[]
for i in range(len(a)):
    arr1=[int(j) for j in a]
    num=0
    if arr1[i]==0:
        arr1[i]=1
    else:
        arr1[i]=0
    for k in range(len(a)):
        num=num*2+arr1[k]
    arr.append(num)
print(max(arr))