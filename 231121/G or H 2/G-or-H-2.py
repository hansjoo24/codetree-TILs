MAX_LOCATE = 101
n = int(input())
max_size = 0 

photo = [0] * MAX_LOCATE
for i in range(n):
    pos,code = input().split()
    pos = int(pos)

    photo[pos] = code

for start in range(MAX_LOCATE):
    if photo[start] == 0: 
        continue
    for end in range(start+1,MAX_LOCATE):
        if photo[end] == 0:
            continue
        g_cnt = 0
        h_cnt = 0
        empty_cnt = 0
        result = False
        for i in range(start,end+1):
            if photo[i] == 'G':
                g_cnt +=1
            elif photo[i] == 'H':
                h_cnt +=1
            else:
                empty_cnt +=1

        if empty_cnt == 0 and g_cnt == 0 and h_cnt != 0:
            result = True
        elif empty_cnt == 0 and g_cnt !=0 and h_cnt == 0:
            result = True
        elif g_cnt == h_cnt and g_cnt != 0:
            result = True
        
        if result == True:
            max_size = max(max_size,end-start)
            
print(max_size)