n = int(input())
numbers = list(map(int, input().split()))

# Write your code here!
s=0
import sys
mnum=-sys.maxsize
for i in range(n-2):
    for j in range(i+2,n):
        s=numbers[i]+numbers[j]
        mnum=max(mnum,s)


print(mnum)



