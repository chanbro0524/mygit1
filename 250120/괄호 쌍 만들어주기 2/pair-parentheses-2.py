A = input()

# Write your code here!
arr=[i for i in A]
num=0
for i in range(len(arr)-2):
    for j in range(i+2,len(arr)-1):
        if arr[i]=='(' and arr[i+1]=='(':
            if arr[j]==')'and arr[j+1]==')':
                num+=1

print(num)