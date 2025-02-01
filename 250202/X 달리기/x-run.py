X = int(input())

# Write your code here!
t=0
d=0
ms=1
for i in range(10000):
    if d+2*ms<X:
        d+=2*ms
        t+=2
        ms+=1
    else:
        if d+ms<X:
            d+=ms
            t+=1
            ms+=1
        else:
            t+=X-d

            break


print(t)