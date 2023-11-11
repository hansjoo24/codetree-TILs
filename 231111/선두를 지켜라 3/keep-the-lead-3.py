n,m = map(int,input().split())
a_cur, b_cur = 0,0
a_pos, b_pos = [0],[0]
code = ""
for _ in range(n):
    velocity, time = map(int,input().split())
    for t in range(time):
        a_cur += velocity
        a_pos.append(a_cur)

for _ in range(m):
    velocity, time = map(int,input().split())
    for t in range(time):
        b_cur += velocity
        b_pos.append(b_cur)



answer = 0
for i in range(len(a_pos)):
    if i==0:
        continue
    elif a_pos[i]>b_pos[i] and code != "a":
        answer +=1
        code = 'a'
    elif a_pos[i]<b_pos[i] and code != "b":
        answer+=1
        code = 'b'
    elif a_pos[i] == b_pos[i] and code != "ab":
        answer+=1
        code = "ab"

print(answer)