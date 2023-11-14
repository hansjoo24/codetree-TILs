import sys
n = int(input())
MAX_INT = sys.maxsize
room = [
    int(input())
    for _ in range(n)
]
total = 0
min_total = MAX_INT
for i in range(n):
    total = 0
    num = (i+1)%n
    for j in range(1,n):
        #print(i, j*room[num])
        total += j*room[num]
        num = (num+1)%n

    min_total = min(min_total,total)

print(min_total)