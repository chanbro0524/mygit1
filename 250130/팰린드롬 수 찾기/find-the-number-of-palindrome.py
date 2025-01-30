X, Y = map(int, input().split())
num=0
for i in range(X,Y+1):
    arr=[j for j in str(i)]
    arr1=[k for k in str(i)]
    arr1.reverse()
    if arr==arr1:
        num+=1


print(num)