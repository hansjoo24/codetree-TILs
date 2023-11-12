n = int(input())

def recur1(n):
    if n==0:
        return
    else:
        recur1(n-1)
        print(n,end=' ')

def recur2(n):
    if n==0:
        return
    else:
        print(n,end=' ')
        recur2(n-1)

recur1(n)
print()
recur2(n)