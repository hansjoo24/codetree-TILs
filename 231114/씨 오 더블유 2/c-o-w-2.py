n = int(input())
s = input()
s_len = len(s)

answer = 0
for i in range(n-2):
    if s[i] == 'C':
        for j in range(i+1,n-1):
            if s[j] == 'O':
                for k in range(j+1,n):
                    if s[k] == 'W':
                        answer+=1 
                        #print(i,j,k)

print(answer)