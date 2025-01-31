N, L = map(int, input().split())
a = list(map(int, input().split()))

# Write your code here!

numH=0
for i in range(100):
    a.sort()
    num=0
    num1=0
    for j in a:
        if j>=i:
            num+=1
            if num>=i:
                numH=max(numH,i)
                break
        if L==0:
            continue
        
        if j<i:
            j+=1
            if j>=i:
                num+=1
                num1+=1
                if num1>L:
                    continue
                if num>=i:
                    numH=max(numH,i)

                    break
            
            else:
                continue
        
        
print(numH)