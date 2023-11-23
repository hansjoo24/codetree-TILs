max_area = -1
n = int(input())
points = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

def get_triangle_area(p1,p2,p3):
    x1,x2,x3 = p1[0],p2[0],p3[0]
    y1,y2,y3 = p1[1],p2[1],p3[1]

    x_list = list(set({x1,x2,x3}))
    y_list = list(set({y1,y2,y3}))

    if len(x_list)!=2 or len(y_list)!=2:
        return -1
    else:
        return abs(x_list[0]-x_list[1])*abs(y_list[0]-y_list[1])


for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            p1,p2,p3 = points[i],points[j],points[k]
            result = get_triangle_area(p1,p2,p3)
            if result != -1:
                max_area = max(max_area,result)
            
print(max_area)