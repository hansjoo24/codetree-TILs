MAX_POS = 40001
n = int(input())
points=[]
min_area = MAX_POS*MAX_POS


for i in range(n):
    point = tuple(map(int,input().split()))
    points.append(point)

for i in range(n):
    max_x ,max_y = -1,-1
    min_x, min_y = MAX_POS,MAX_POS
    for j in range(n):
        if j != i:
            point = points[j]
            x,y = point[0],point[1]

            max_x, max_y = max(x,max_x), max(y,max_y)
            min_x, min_y = min(x,min_x), min(y,min_y)
    
    area = (max_x - min_x)*(max_y - min_y)
    min_area = min(min_area,area)
    
print(min_area)