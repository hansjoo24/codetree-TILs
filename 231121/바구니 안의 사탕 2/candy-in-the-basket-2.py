MAX_BASKET = 100
n,k = map(int,input().split())

basket = [0]*MAX_BASKET

for _ in range(n):
    candy_num,basket_pos = map(int,input().split())
    basket[basket_pos] = candy_num


for i in range(k,MAX_BASKET-4):
    print(i)