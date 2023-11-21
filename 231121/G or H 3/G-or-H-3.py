n,k = map(int,input().split())
max_pos = -1
max_total = -1
photo = [0]*10000

for i in range(n):
    pos, code = input().split()
    pos = int(pos)
    max_pos = max(pos,max_pos)

    match(code):
        case 'G':
            photo[pos] = 1
        case 'H':
            photo[pos] = 2

for i in range(max_pos-k):
    total = 0
    for j in range(i,i+k+1):
        total += photo[j]

    max_total = max(total,max_total)

print(max_total)