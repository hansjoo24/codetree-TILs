n,m = map(int,input().split())
strs = [
    list(input())
    for _ in range(n)
]
def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m
dxs = [0,1,1,1,0,-1,-1,-1]
dys = [1,1,0,-1,-1,-1,0,1]

answer = 0
for i in range(n):
    for j in range(m):
        if strs[i][j]=='L':
            for dx,dy in zip(dxs,dys):
                for k in range(1,3):
                    if in_range(i+k*dx,j+k*dy):
                        if strs[i+k*dx][j+k*dy] != 'E':
                            break
                    else: break
                else:
                    answer += 1

print(answer)