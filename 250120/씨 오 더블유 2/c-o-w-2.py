n = int(input())
str = input()
num=0
for i in range(n-2):
    if str[i]=='C':
        for j in range(i+1,n-1):
            if str[j]=='O':
                for k in range(j+1,n):
                    if str[k]=='W':
                        num+=1

print(num)