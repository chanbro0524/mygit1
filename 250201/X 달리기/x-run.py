X = int(input())

t = 0
d = 0
ms = 1

for i in range(5000):
    if d + 2 * ms < X:
        t += 2
        d += 2 * ms
        ms += 1

    
    elif d + 2 * ms == X:
        t += 2

        break

    elif d + ms < X:
        t += 1
        d += ms
        ms += 1


    elif d + ms == X:
        t += 1

        break

    else:
        t += X - d

        break

print(t)
