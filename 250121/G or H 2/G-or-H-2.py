n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]
arr1=[0]*101
for i,j in zip(pos,alpha):
    arr1[i]=j


num=0
if len(alpha)==1:
    print(num)
else:
    for i in range(100):
        for j in range(i,100):
            arr=arr1[i:j+1]
            if (arr.count('G')==arr.count('H')or arr.count('H')==0 or arr.count('G')==0)and (arr1[i]=='G' or arr1[i]=='H') and (arr1[j]=='G' or arr1[j]=='H'):
               num=max(num,j-i)
    print(num)