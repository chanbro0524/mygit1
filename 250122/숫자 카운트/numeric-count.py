n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(str(num))
    b.append(cnt1)
    c.append(cnt2)

def number(d,e,f):
    d=str(d)
    e=str(e)
    f=str(f)
    
    s=0
    for i in range(n):
        ct1=0
        ct2=0
        if d==a[i][0]:
            ct1+=1
        elif d==a[i][1] or d==a[i][2]:
            ct2+=1
        if e==a[i][1]:
            ct1+=1
        elif e==a[i][0] or e==a[i][2]:
            ct2+=1
        if f==a[i][2]:
            ct1+=1
        elif f==a[i][1] or f==a[i][0]:
            ct2+=1
        if ct1==b[i] and ct2==c[i]:
            s+=1    
    return s  


num1=0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i!=j and j!=k and k!=i:
                if  number(i,j,k)==n:
                    num1+=1
print(num1)