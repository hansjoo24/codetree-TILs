n = int(input())

numbers = [0,1]

for i in range(n):
    numbers.append(numbers[-1]+numbers[-2])

print(numbers[n])