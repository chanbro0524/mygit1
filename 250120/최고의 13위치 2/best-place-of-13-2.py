n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

num=0

for i in range(n):
    for j in range(n-2):
        s=0
        if arr[i][j]==1:
            s+=1
        if arr[i][j+1]==1:
            s+=1
        if arr[i][j+2]==1:
            s+=1
        for k in range(i+1,n):
            for l in range(n-2):
                s1=0
                if arr[k][l]==1:
                    s1+=1
                if arr[k][l+1]==1:
                    s1+=1
                if arr[k][l+2]==1:
                    s1+=1
                num=max(num,s+s1)

print(num)