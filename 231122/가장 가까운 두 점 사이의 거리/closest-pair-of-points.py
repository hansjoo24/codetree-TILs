import sys
n = int(input())
distance = sys.maxsize 
points = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

for i in range(n):
    for j in range(i+1,n):
        p1 = points[i]
        p2 = points[j]

        x1,y1 = p1[0],p1[1]
        x2,y2 = p2[0],p2[1]

        distance = min(distance, (x2-x1)**2+(y2-y1)**2)

print(distance)