MAX_BASKET = 100
n,k = map(int,input().split())
max_total = -1

basket = [0]*(MAX_BASKET+1)

for _ in range(n):
    candy_num,basket_pos = map(int,input().split())
    basket[basket_pos] +=candy_num


for c in range(MAX_BASKET):
    total = 0
    if c-k<0:
        start = 0
    else:
        start = c-k
    if c+k > MAX_BASKET:
        end = MAX_BASKET
    else:
        end = c+k

    for j in range(start,end+1):
        total+=basket[j]
        
    max_total = max(total,max_total)


print(max_total)