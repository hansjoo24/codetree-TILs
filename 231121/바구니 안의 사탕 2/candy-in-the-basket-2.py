MAX_BASKET = 100
n,k = map(int,input().split())
max_total = -1

basket = [0]*MAX_BASKET+1

for _ in range(n):
    candy_num,basket_pos = map(int,input().split())
    basket[basket_pos] +=candy_num


for c in range(k,MAX_BASKET-k):
    total = 0
    for j in range(c-k,c+k+1):
        total+=basket[j]
        
    max_total = max(total,max_total)


print(max_total)