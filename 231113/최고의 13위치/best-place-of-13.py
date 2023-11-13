max_coin = 0
n = int(input())
def in_range(x,n):
    return x>=0 and x<n

arrs = [
    list(map(int,input().split()))
    for _ in range(n)
]

for arr in arrs:
    for j in range(n):
        if in_range(j+2,n) and in_range(j+1,n) and in_range(j,n):
            coin = arr[j]+arr[j+1]+arr[j+2]
            max_coin = max(max_coin,coin)

print(max_coin)