n,k = map(int,input().split())
numbers = list(map(int,input().split()))

max_total = -1

for i in range(n-k+1):
    total = 0
    for j in range(i,i+k):
        total += numbers[j]

    max_total = max(total,max_total)

print(max_total)