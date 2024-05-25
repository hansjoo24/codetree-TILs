n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]

def canGo(x,y):
    if x>=n or y>=m or x<0 or y<0:
        return False
    
    elif graph[x][y]==0:
        return False

    elif visited[x][y]:
        return False

    else:
        return True

def DFS(x,y):
    if not visited[x][y]:
        visited[x][y] = True
        #print("visited : ",x,y)
        dxs,dys = [1,0],[0,1]
        for i in range(2):
            dx,dy = dxs[i],dys[i]
            newx,newy = x+dx, y+dy

            if canGo(newx,newy):
                DFS(newx,newy)


DFS(0,0)
#print(visited)

if visited[m-1][n-1]:
    print(1)
else:
    print (0)