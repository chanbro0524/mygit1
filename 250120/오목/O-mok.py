b = [list(map(int, input().split())) for _ in range(19)]
num=0

for i in range(15):
    for j in range(15):
        if b[i][j]==1:
            if b[i+1][j]==1 and b[i+2][j]==1 and b[i+3][j]==1 and b[i+4][j]==1:
                num=1
                k=i+2
                s=j
            elif b[i][j+1]==1 and b[i][j+2]==1 and b[i][j+3]==1 and b[i][j+4]==1:
                num=1
                k=i
                s=j+2
            elif b[i+1][j+1]==1 and b[i+2][j+2]==1 and b[i+3][j+3]==1 and b[i+4][j+4]==1:
                num=1
                k=i+2
                s=j+2
        elif b[i][j]==2:
            if b[i+1][j]==2 and b[i+2][j]==2 and b[i+3][j]==2 and b[i+4][j]==2:
                num=2
                k=i+2
                s=j
            elif b[i][j+1]==2 and b[i][j+2]==2 and b[i][j+3]==2 and b[i][j+4]==2:
                num=2
                k=i
                s=j+2
            elif b[i+1][j+1]==2 and b[i+2][j+2]==2 and b[i+3][j+3]==2 and b[i+4][j+4]==2:
                num=2
                k=i+2
                s=j+2


if num==0:
    print(num)
else:
    print(num)
    print(k+1,s+1)