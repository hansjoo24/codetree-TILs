n=int(input())
def recur(n):
    if n==0:
        return
    else:
        recur(n-1)
        for _ in range(n):
            print('*',end='')
        print()

recur(n)