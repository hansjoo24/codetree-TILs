def binaryToDecimal(binary):
    offset = 1
    total = 0
    for i in range(len(binary)-1,-1,-1):
        num = int(binary[i]) 
        total += num*offset
        offset *=2 
    
    return total

a = input()
max_num = -1
for i in range(len(a)):
    match(a[i]):
        case '1':
            c = '0'
        case '0':
            c='1'
    changed_a = a[0:i] + c + a[i+1:len(a)]
    
    decimal = binaryToDecimal(changed_a)
    max_num = max(decimal,max_num)

print(max_num)