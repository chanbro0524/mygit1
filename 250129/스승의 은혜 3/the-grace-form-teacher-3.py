N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

class Student:
    def __init__(self,p,s):
        self.p=p
        self.s=s
        self.m=p+s
int_max=0
for i in range(N):
    arr=[]
    arr.append(Student(P[i]/2,S[i]))
    for j in range(N):
        if j==i:
            continue
        arr.append(Student(P[j],S[j]))
    arr.sort(lambda x:x.m)
    s=0
    n=0
    for k in arr:
        s+=k.m
        if s>B:
            break
        n+=1
    int_max=max(int_max,n)
print(int_max)

