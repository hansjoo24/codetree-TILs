n, b = map(int,input().split())
max_ans = -1

prices = [
    int(input())
    for _ in range(n)
]
prices.sort()

for half in range (n):
    remain = b
    ans = -1
    for i in range(n):
        if half == i:
            remain -= int(prices[half]/2)
            
        else:
            remain -= prices[i]

        if remain < 0:
            #print(half,i,prices[i])
            ans = i
            break
    else:
        ans = n

    max_ans = max(ans,max_ans)

print(max_ans)