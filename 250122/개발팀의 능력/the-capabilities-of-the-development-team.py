arr = list(map(int, input().split()))
int_min=1000
n=5
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(n):
            if k==i or k==j:
                continue
            team1=arr[i]+arr[j]
            team3=arr[k]
            team2=sum(arr)-team1-team3
            if team1==team2 or team2==team3 or team3==team1:
                continue
            int_min=min(int_min,max(team1,team2,team3)-min(team1,team2,team3))


print(int_min)