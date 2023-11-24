n, b = map(int,input().split())
max_ans = -1

prices = [
    int(input())
    for _ in range(n)
]

for half in range (n):
    remain = b
    ans = -1
    for i in range(n):
        if half == i:
            remain -= int(prices[half]/2)
        else:
            remain -= prices[i]
            if remain < 0:
                ans = i
                break

    if ans == -1:
        ans = n

    max_ans = max(ans,max_ans)

print(max_ans)