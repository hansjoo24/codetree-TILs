n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt=0

for i in range(n-m+1):
    part_a = a[i:i+m]
    temp_b = b.copy()
    for num in part_a:
        if num in temp_b:
            temp_b.remove(num)
        else:
            break
    else:
        cnt+=1

print(cnt)