N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def key(a,b):
    if abs(a-b)<=2:
        return True
    else:
        if a==N:
            if b==1 or b==2:
                return True
        elif b==N:
            if a==1 or a==2:
                return True
        elif b==N-1:
            if a==1 :
                return True
        elif a==N-1:
            if b==1:
                return True
        elif b==2:
            if a==N :
                return True
        elif a==2:
            if b==N:
                return True
        elif a==1:
            if b==N or b==N-1:
                return True
        elif b==1:
            if a==N or a==N-1:
                return True
        
num=0

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if (key(i,a1) and key(j,b1) and key(k,c1)) or (key(i,a2) and key(j,b2) and key(k,c2)):
                num+=1


print(num)