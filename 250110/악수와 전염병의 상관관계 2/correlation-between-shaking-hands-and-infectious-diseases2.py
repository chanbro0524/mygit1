n,k,p,T=tuple(map(int,input().split()))
arr=[0 for i in range(n)]
arr1=[k for i in range(n)]
arr[p-1]=1

class Hand:
    def __init__(self,time,x,y):
        self.time=time
        self.x=x
        self.y=y


arr2=[]
for i in range(T):
    t,x,y=tuple(map(int,input().split()))
    arr2.append(Hand(t,x,y))


arr2.sort(key=lambda x:x.time)
for i in range(T):
    x1=arr2[i].x
    y1=arr2[i].y
    
    if arr1[x1-1]==0:
        continue
    else:
        if (arr[x1-1]==1 and arr[y1-1]==0) :
            if arr1[x1-1]==0:
                continue
            else:
                arr[y1-1]=1
                arr1[x1-1]-=1
        elif (arr[x1-1]==0 and arr[y1-1]==1):
            if arr1[y1-1]==0:
                continue
            else:
                arr[x1-1]=1
                arr1[y1-1]-=1
        elif (arr[x1-1]==1 and arr[y1-1]==1):
            if arr1[y1-1]==0 and arr1[x1-1]!=0:
                arr1[x1-1]-=1
            elif arr1[y1-1]!=0 and arr1[x1-1]==0:
                arr1[y1-1]-=1
            elif arr1[y1-1]!=0 and arr1[x1-1]!=0:
                arr1[x1-1]-=1
                arr1[y1-1]-=1

for i in arr:
    print(i,end="")



