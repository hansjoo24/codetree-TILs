import sys
LENGTH = 19
stones = [
    list(map(int,input().split()))
    for _ in range(LENGTH)
] 

def in_range(x,y):
    return x>=0 and x<LENGTH and y>=0 and y<LENGTH

dxs = [0,1,1,1,0,-1,-1,-1]
dys = [1,1,0,-1,-1,-1,0,1]

win_stone_num = 0

for i in range(LENGTH):
    for j in range(LENGTH):
        cur_stone_num = stones[i][j]
        if cur_stone_num==0:
            continue
    

        cur_r, cur_c = i,j
        
        for dx,dy in zip(dxs,dys):
            cur_r, cur_c = i,j
            #print(f"dx,dy = {dx},{dy}")
            for z in range(4):
                if in_range(cur_r+dx,cur_c+dy):
                    cur_r,cur_c = cur_r+dx, cur_c+dy
                    if stones[cur_r][cur_c] != cur_stone_num:
                        break
                    else:
                        pass
                        #print(cur_r,cur_c,' : ',z)

                else:
                    break
            else:
                print(cur_stone_num)
                print(i+1+2*dx,j+1+2*dy)
                sys.exit()

print(0)