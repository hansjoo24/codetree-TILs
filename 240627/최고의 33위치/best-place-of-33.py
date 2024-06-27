n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]

def get_sum(row,col):
    if(row+2>=n or col+2 >=n):
        return 0
    else:
        sum=0
        for i in range(row,row+3):
            for j in range(col,col+3):
                sum += l[i][j]

        return sum

max_sum = 0
for i in range(n):
    for j in range(n):
        max_sum = max(max_sum,get_sum(i,j))

print(max_sum)