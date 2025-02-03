n = int(input())
arr = input().split()
arr1 = arr[:]  # 원본 배열 복사
arr.sort()  # 정렬된 배열

num = 0

for j in range(n):
    for i in range(n):
        if arr1[i] == arr[j]:
            while i > j:
                arr1[i], arr1[i - 1] = arr1[i - 1], arr1[i]  # 스왑
                i -= 1
                num += 1
            break

print(num)
