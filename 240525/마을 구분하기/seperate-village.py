n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
cnt=0

def canGo(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return False

    elif graph[x][y]==0 or visited[x][y]:
        return False
    else:
        return True

def DFS(x,y):
    global cnt 
    visited[x][y]=True
    #print('visited : ',x,y)

    cnt += 1

    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    for i in range(4):
        dx,dy = dxs[i],dys[i]
        newx,newy = x+dx, y+dy

        if canGo(newx,newy):
            DFS(newx,newy)

village_cnt = 0
cnt_list = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]==1:
            cnt=0
            DFS(i,j)
            cnt_list.append(cnt)
            village_cnt += 1

cnt_list.sort()

print(village_cnt)
for i in cnt_list:
    print(i)