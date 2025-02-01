n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# Write your code here!

letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

letters=letter[:n]


for i in range(p-1,m):
    if c[i] in letters:
        letters.remove(c[i])
if u[p-1]==0:
    letters=[]
if p-1>0:
    if u[p-1]==u[p-2]:
        if c[p-2]in letters:
            letters.remove(c[p-2])
for j in letters:
    print(j,end=' ')
