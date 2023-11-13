r, c = map(int,input().split())

arr = [
    list(input().split())
    for _ in range(r)
]

start,end = arr[0][0], arr[r-1][c-1]
if(start == end):
    print(0)
else:
    answer = 0
    for i1 in range(1,r-2):
        for j1 in range(1,c-2):
            if arr[i1][j1] != start:
                #print("1 :",i1,j1)

                for i2 in range(i1+1,r-1):
                    for j2 in range(j1+1,c-1):
                        if arr[i2][j2] == start: 
                            #print("2 : ",i2,j2)
                            answer +=1 
        
        #print()
    print(answer)