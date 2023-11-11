def in_range(x,y,n):
    if x<n and y<n and x>=0 and y>=0:
        return True
    else:
        return False

n = int(input())
coordinate = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        point = coordinate[i][j]
        for dx,dy in zip(dxs,dys):
            if(in_range(i+dx,j+dy,n)):
                close_point = coordinate[i+dx][j+dy]
                if close_point == 1:
                    cnt += 1
        
        if cnt>=3:
            answer+=1

print(answer)