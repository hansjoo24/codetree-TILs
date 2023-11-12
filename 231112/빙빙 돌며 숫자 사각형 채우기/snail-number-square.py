def in_range(x,y,n):
    return x>=0 and x<n and y>=0 and y<n

n,m = map(int,input().split())
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
dir_name = {
    'E':0,
    'S':1,
    'W':2,
    'N':3
}
square = [
    [0]*m 
    for _ in range(n)
]

direction = 0
r,c = 0,0
square[0][0] = 1
num = 2
while num <= m*n:
    dx, dy = dxs[direction], dys[direction]
    if(in_range(r+dx,c+dy,n) and square[r+dx][c+dy]==0):
        r+=dx
        c+=dy
        square[r][c] = num
        num +=1 
    else:
        direction = (direction +1)%4

for i in range(n):
    for j in range(m):
        print(square[i][j],end=' ')
    print()