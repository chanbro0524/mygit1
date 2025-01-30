A, B, C = map(int, input().split())
int_max=0
for i in range((C//A)+2):
    for j in range((C//B)+2):
        if A*i+B*j<=C:
            int_max=max(int_max,A*i+B*j) 

print(int_max)