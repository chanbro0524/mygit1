n = int(input())
sequence = list(map(int, input().split()))
sequence1=sequence[:]
sequence1.sort()
while True:
    for i in range(1,n):
        if sequence[i]>sequence[0] and sequence[i+1]<sequence[0]
            