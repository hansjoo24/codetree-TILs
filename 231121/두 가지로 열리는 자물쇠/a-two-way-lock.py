n = int(input())
cnt=0
key1 = tuple(map(int,input().split()))
key2 = tuple(map(int,input().split()))

def get_distance(key,i):
    global n
    sub = abs(key-i)
    if sub >= n/2:
        sub = n-sub
    return sub

def can_open(a,b,c,key):
    k1,k2,k3 = key[0],key[1],key[2]

    if get_distance(a,k1)<=2 and get_distance(b,k2)<=2 and get_distance(c,k3)<=2:
        #print((a,b,c),(k1,k2,k3))
        return True
    else:
        return False

for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            if can_open(a,b,c,key1) or can_open(a,b,c,key2):
                cnt +=1

print(cnt)