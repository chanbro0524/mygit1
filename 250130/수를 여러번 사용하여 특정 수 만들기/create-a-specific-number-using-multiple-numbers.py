A, B, C = map(int, input().split())
int_max=0
for i in range((C//B)+1):
    for j in range((C//B)+1):
        if A*i+B*j<=C:
            int_max=max(int_max,A*i+B*j) 

print(int_max)