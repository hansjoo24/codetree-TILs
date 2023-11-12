def change_direction(r,c,n,direction):
    U,D,R,L = 1,2,0,3
    if r==1 and direction == U:
        return True
    elif r==n and direction==D:
        return True
    elif c==1 and direction == L:
        return True
    elif c==n and direction==R:
        return True
    else:
        return False
    
n,t = map(int,input().split())
r,c,direction = input().split()
r,c = int(r), int(c)
dx = [1,0,0,-1]
dy = [0,1,-1,0]
dir_name = {'U':1, 'D':2, 'R':0, 'L':3}
dir_num = dir_name[direction]

for _ in range(t):
    if(change_direction(r,c,n,dir_num)):
        dir_num = 3-dir_num
        continue

    r += dy[dir_num]
    c += dx[dir_num]

print(r,c)