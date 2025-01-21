N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def key(a,b):
    if abs(a-b)<=2:
        return True
    else:
        if a==9:
            if b==1 or b==2:
                return True
        elif b==9:
            if a==1 or a==2:
                return True
        elif b==8:
            if a==1 :
                return True
        elif a==8:
            if b==1:
                return True

num=0

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if (key(i,a1) and key(j,b1) and key(k,c1)) or (key(i,a2) and key(j,b2) and key(k,c2)):
                num+=1


print(num)