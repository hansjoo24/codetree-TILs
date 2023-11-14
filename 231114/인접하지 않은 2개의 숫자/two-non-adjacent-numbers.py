n = int(input())
nums = list(map(int,input().split()))
max_total = -1


for i in range(n):
    for j in range(i+2,n):
        result = nums[i]+nums[j]
        max_total = max(result,max_total)

print(max_total)