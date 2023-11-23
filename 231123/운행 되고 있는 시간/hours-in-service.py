n = int(input())
max_work_time = -1
work_time = [0]*1001

schedule = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

for exception in range(n):

    for i in range(n):
        if i==exception:
            continue
        else:
            for t in range(schedule[i][0],schedule[i][1]):
                work_time[t] = 1
    
    total = 0
    for t in range(len(work_time)):
        total += work_time[t]
        work_time[t]=0
    
    max_work_time = max(total,max_work_time)

print(max_work_time)