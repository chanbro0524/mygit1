N = int(input())
str = input()
intmin=N
for i in range(N):
    num=0
    for j in range(N-i):
        if str[j:j+i] in str[j+i+1:]:
            num+=1
    if num!=0:
        continue
    intmin=min(i,intmin)
print(intmin)