a = input()
len_a = len(a)

answer=0
for i in range(len_a-1):
    if(a[i]=='(' and a[i+1]=='('):
        for j in range(i+2,len_a-1):
            if a[j]==')' and a[j+1]==')':
                answer +=1 

print(answer)