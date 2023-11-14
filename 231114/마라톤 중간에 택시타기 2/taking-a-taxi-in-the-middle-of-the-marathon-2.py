import sys
MAX_INT = sys.maxsize
n = int(input())

def get_distance(start,end):
    sx,sy = start[0], start[1]
    ex,ey = end[0], end[1]

    return abs(ex-sx)+abs(ey-sy)

positions = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

total = 0
min_total = MAX_INT


for i in range(1,n-1):
    total = 0
    cur = positions[0]
    for j in range(n):
        if j==i:
            continue
        else: 
            #print(positions[j],cur)
            total+= get_distance(cur,positions[j])
            cur = positions[j]
    
    min_total = min(total,min_total)

print(min_total)