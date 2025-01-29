T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))
    num=0
for i in range(a,b+1):
    int_mint=1000
    int_mins=1000
    for j in range(T):

        if c[j]=='N':
            int_mint=min(abs(i-x[j]),int_mint)

        elif c[j]=='S':
            int_mins=min(abs(i-x[j]),int_mins)
    if int_mins<=int_mint:
            num+=1
print(num)