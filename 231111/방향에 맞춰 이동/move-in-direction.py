dx = [1,0,-1,0]
dy = [0,-1,0,1]
cur = [0,0]
dir_indexs = ('E','S','W','N')
n = int(input())

for _ in range(n):
    direction,distance = input().split()
    distance = int(distance)

    dir_index = dir_indexs.index(direction)

    cur[0] += distance* dx[dir_index]
    cur[1] += distance* dy[dir_index]

    
print(cur[0],cur[1])