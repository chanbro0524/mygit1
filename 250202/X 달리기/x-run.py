X = int(input())

# Write your code here!
t=0
d=0
ms=1
for i in range(5000):
    if (d+ms)*2<X:
        t+=2
        d+=2*ms
        ms+=1

    elif (d+ms)*2==X:
        t+=2
        ms+=1

        break
    else:
        if (d+ms)<X:
            t+=1
            t+=(X-(d+ms))

            break
        elif (d+ms)==X:
            t+=1

            break
        else:
            t+=X-d

            break


print(t)