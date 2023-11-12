n = int(input())
def recur(n):
    if n==0:
        return
    else:
        print('HelloWorld')
        recur(n-1)


recur(n)