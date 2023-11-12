dx = [1,0,-1,0]
dy = [0,-1,0,1]

instruction = input()
elapsed_time = 0
direction = 3
x,y = 0,0

for i in instruction:
    #print(x,y,direction)

    match(i):
        case 'F':
            x,y = x+dx[direction], y+dy[direction]
        case 'R':
            direction = (direction +1)%4
        case 'L':
            direction = (direction-1+4)%4

    if elapsed_time!=0 and x==0 and y==0:
        print(elapsed_time+1)
        break

    else:
        elapsed_time +=1 
else:
    print(-1)