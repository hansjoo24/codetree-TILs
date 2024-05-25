from collections import deque 
n,m = map(int,input().split())
queue = deque()
queue.append((0,0))

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]


def canGo(row,col):
    if row<0 or col<0 or row>=n or col>=m:
        return False

    elif visited[row][col]==True or graph[row][col]==0:
        return False
    else:
        return True


def BFS():
    while len(queue)!= 0:
        x,y = queue[0][0], queue[0][1]
        queue.popleft()

        if x==n-1 and y==m-1:
            return 
            
        #print("visited : ",x,y)

        dxs, dys = [1,0,-1,0],[0,1,0,-1]
        for i in range(4):
            dx, dy = dxs[i], dys[i]
            newx, newy = x+dx, y+dy
            if canGo(newx,newy):
                queue.append((newx,newy))
                visited[newx][newy] = True

BFS()
if visited[n-1][m-1] == True:
    print(1)
else:
    print(0)