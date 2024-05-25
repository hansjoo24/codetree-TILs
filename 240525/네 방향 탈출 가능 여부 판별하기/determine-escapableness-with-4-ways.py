from collections import deque 
n,m = map(int,input().split())
queue = deque()
queue.append((0,0))

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def canGo(x,y):
    if x<0 or y<0 or x>=m or y>=n:
        return False

    elif visited[x][y]==True or graph[x][y]==0:
        return False
    else:
        return True

def BFS():
    while len(queue)!= 0:
        x,y = queue[0][0], queue[0][1]
        queue.popleft()
        visited[x][y]=True

        if x==m-1 and y==n-1:
            return 
            
        #print("visited : ",x,y)

        dxs, dys = [1,0,-1,0],[0,1,0,-1]
        for i in range(4):
            dx, dy = dxs[i], dys[i]
            newx, newy = x+dx, y+dy
            if canGo(newx,newy):
                queue.append((newx,newy))

BFS()
if visited[m-1][n-1] == True:
    print(1)
else:
    print(0)