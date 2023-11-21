n = int(input())
key = list(map(int,input().split()))

cnt = 0
for first in range(1,n+1):
    for second in range(1,n+1):
        for third in range(1,n+1):
            if abs(first-key[0])<=2 or abs(second-key[1])<=2 or abs(third-key[2])<=2:
                cnt+=1 

print(cnt)