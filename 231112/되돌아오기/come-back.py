dxs = [1,0,-1,0]
dys = [0,-1,0,1]
dir_name = {
    'E':0,
    'S':1,
    'W':2,
    'N':3
}
x,y = 0,0

n = int(input())
cnt = 0
answer = -1

for i in range(n):
    direction, distance = input().split()
    distance = int(distance)
    dx = dxs[dir_name[direction]]
    dy = dys[dir_name[direction]]

    for _ in range(distance):
        x += dx
        y += dy
        if cnt != 0 and x==0 and y==0:
            answer = cnt+1
        else: cnt +=1 

print(answer)