n = int(input())
points = [
    list(map(int,input().split()))
    for _ in range(n)
]

check = [0]*n

for i in range(n):
    for j in range(n):
        if j==i:
            continue

        else:
            a1,a2 = points[i][0], points[i][1]
            b1,b2 = points[j][0], points[j][1]

            if(a1<b1 and a2>b2):
                check[i] = 1
                check[j] = 1

ans = 0
for i in range(n):
    if check[i] == 0 :
        ans +=1
        #print(points[i][0],points[i][1])

print(ans)