n = int(input())
numbers = list(map(int,input().split()))
cnt=0

for i in range(n):
    for j in range(i,n):
        total = 0
        for k in range(i,j+1):
            total += numbers[k]

        avg = total / (j-i+1)
        if avg in numbers[i:j+1]:
            cnt+=1

print(cnt)