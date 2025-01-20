n = int(input())
a = [int(input()) for _ in range(n)]
import sys
# Write yforour code here!
mnum=sys.maxsize
for i in range(n):
    s=0
    for j in range(1,n):
        s=s+j*a[(i+j)%n]

    mnum=min(mnum,s)
print(mnum)