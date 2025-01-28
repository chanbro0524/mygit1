N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

class Student:
    def __init__(self,p,s):
        self.p=p
        self.s=s



arr=[Student(P[i],S[i]) for i in range(N)]
arr.sort(lambda x:x.)
for i in range(N):
    for j in range(N):
