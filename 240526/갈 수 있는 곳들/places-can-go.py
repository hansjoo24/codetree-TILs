from collections import deque

n,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
start_points = [tuple(map(int,input().split())) for _ in range(k)]


def init_visited():
    return [[False]*n for _ in range(n)]

def canGo(x,y):
    return 0<=x<n and 0<=y<n and not visited[x][y] and graph[x][y]==0

def bfs(q):
    global cnt
    while len(q)!= 0:
        x,y = q.popleft()
        #print('visited : ',x,y)
        cnt += 1

        dxs, dys = [1,0,-1,0] , [0,1,0,-1]
        for i in range(4):
            dx,dy = dxs[i],dys[i]
            newx,newy = x+dx, y+dy
            if canGo(newx,newy):
                visited[newx][newy] = True
                q.append((newx,newy))


visited = init_visited()
cnt = 0

for start in start_points:
    sx,sy = start
    if canGo(sx,sy):
        visited[sx][sy]=True

        q = deque()
        q.append(start)
        bfs(q)
        #print('----')

print(cnt)