n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Write your code her

num=0
for i in range(n):
    if A[i]>B[i] :
        num+=A[i]-B[i]
        A[i+1]+=A[i]-B[i]

print(num)