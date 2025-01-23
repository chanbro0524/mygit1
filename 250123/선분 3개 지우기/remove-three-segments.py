n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)



num1=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            arr=[0]*101
            for m in range(n):
                if m!=i and m!=j and m!=k:
                    a=l[m]
                    b=r[m]
                    for o in range(a,b+1):
                        arr[o]+=1        
            num=0
            for p in range(101):
                if arr[p]>1:
                    num+=1
            if num==0:
                num1+=1
print(num1)