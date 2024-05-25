n,m = map(int,input().split())
graph = [[0]*n for _ in range(n)]
visited = [False]*n

for i in range(m):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

def DFS(node):
    if not visited[node]:
        visited[node] = True
        #print(node,' : visited')
        for i in range(n):
            if graph[node][i]==1:
                DFS(i)

DFS(0)
print(visited.count(True)-1)