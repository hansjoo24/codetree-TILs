LENGTH = 19
stones = [
    list(map(int,input().split()))
    for _ in range(LENGTH)
] 

def horizontal_win(r,c):
    global stones
    stone_num = stones[r][c]
    if stone_num == 0:
        return False 

    for i in range(c,c+5):
        if i >= LENGTH:
            return False
        else:
            if stones[r][i]!=stone_num:
                return False
    #print(r,c,"가로")
    return True

def vertical_win(r,c):
    global stones
    stone_num = stones[r][c]
    if stone_num == 0:
        return False 

    for i in range(r,r+5):
        if i >= LENGTH:
            return False
        else:
            if stones[i][c]!=stone_num:
                return False
    #print(r,c,"세로")
    return True

def diagonal_win(r,c):
    global stones
    stone_num = stones[r][c]
    if stone_num == 0:
        return False

    for i in range(5):
        newr,newc = r+i, c+i
        if newr>= LENGTH or newc>= LENGTH:
            return False
        else:
            if stones[newr][newc]!=stone_num:
                return False
    #print(r,c,"대각선")
    return True



win_stone = 0
center_x, center_y = -1,-1
for i in range(LENGTH):
    for j in range(LENGTH):
        if horizontal_win(i,j):
            win_stone = stones[i][j]
            center_x,center_y = i+1,j+3
            break

        elif vertical_win(i,j):
            win_stone = stones[i][j]
            center_x,center_y = i+3,j+1
            break

        elif diagonal_win(i,j):
            win_stone = stones[i][j]
            center_x,center_y = i+3,j+3
            break
    else:
        break

if win_stone == 0:
    print(0)
else:
    print(win_stone)
    print(center_x,center_y)