a = input()


total = 0
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]=='(' and a[j]==')':
            total+=1

print(total)