import sys

n,h,t = map(int,input().split())
min_total = sys.maxsize

field = list(map(int,input().split()))

for start in range(n):
    for end in range(start+1,n):
        total = 0
        if end-start+1 < t :
            continue
        for i in range(start,end+1):
            total += abs(field[i]-h)
        
        min_total = min(total,min_total)

print(min_total)