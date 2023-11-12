dxs = [0,-1,0,1]
dys = [1,0,-1,0]


def in_range(x,y,n):
    return x>0 and x<=n and y>0 and y<=n

n, m = map(int,input().split())

coordinate = [
    [0]*(n+1)
    for _ in range(n+1)
]

for _ in range(m):
    r,c = map(int,input().split())
    coordinate[r][c] = 1
    cnt = 0

    for dx,dy in zip(dxs,dys):
        if(in_range(r+dx,c+dy,n) and coordinate[r+dx][c+dy]==1):
            cnt+=1 
    if cnt==3:
        print(1)
    else:
        print(0)