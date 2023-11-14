def is_carry(a,b,c):
    max_len = max(len(a),len(b),len(c))
    
    while len(a) < max_len:
        a = '0'+a 
    while len(b) < max_len:
        b = '0'+b 
    while len(c) < max_len:
        c = '0'+c 

    for i in range(max_len):
        num = int(a[i]) + int(b[i]) + int(c[i])
        if num >= 10:
            return True

    return False 

n = int(input())
max_result = -1

nums = [
    input()
    for _ in range(n)
]

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if(is_carry(nums[i],nums[j],nums[k]) != True):
                result = int(nums[i]) + int(nums[j]) + int(nums[k])
                max_result = max(max_result,result)

print(max_result)