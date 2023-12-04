def get_works(Ta,Tb,C,G,H,num):
    if num < Ta:
        return C
    elif num >=Ta and num < Tb:
        return G 
    else:
        return H

n,c,g,h = map(int,input().split())
max_total = -1

ta_list = []
tb_list = []

for _ in range(n):
    ta, tb = map(int,input().split())

    ta_list.append(ta)
    tb_list.append(tb)

for num in range(max(tb_list)+10):
    total = 0
    for i in range(n):
        total += get_works(ta_list[i],tb_list[i],c,g,h,num)
    
    max_total = max(total,max_total)

print(max_total)