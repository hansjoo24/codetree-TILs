x,y = map(int,input().split())
max_total = -1

for i in range(x,y+1):
    total = 0
    str_i = str(i)
    for j in str_i:
        total += int(j)
    
    max_total = max(total,max_total)

print(max_total)