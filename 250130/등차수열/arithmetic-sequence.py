n = int(input())
a = list(map(int, input().split()))

a.sort()
int_max=0
for i in range(1,max(a)):
    num=0
    for j in range(len(a)-1):
        for k in range(j+1,len(a)):
            if i-a[j]==a[k]-i:
                num+=1
    int_max=max(int_max,num)

print(int_max)
                