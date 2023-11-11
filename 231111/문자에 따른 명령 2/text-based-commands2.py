E,S,W,N = 0,1,2,3
direction = N

dx = [1,0,-1,0]
dy = [0,-1,0,1]

x,y = 0,0

instructions = input()

for i in range(len(instructions)):
    match(instructions[i]):
        case "L":
            direction = (direction-1)%4
        case "R":
            direction = (direction+1)%4
        case "F":
            x += dx[direction]
            y += dy[direction]

print(x,y)