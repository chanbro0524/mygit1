N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Write your code here!
num=0
num1=0
for i in range(N-M+1):
    num=0
    for j in range(M):
        if B[j] in A[i:i+M]:
            num+=1
    if num==M:
        num1+=1


print(num1)