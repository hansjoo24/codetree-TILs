import sys
INT_MAX = sys.maxsize
n = int(input())
houses = list(map(int,input().split()))


min_distance = INT_MAX

for i in range(n):
    distance = 0
    for j in range(n):
        distance += abs(i-j)*houses[j]
    
    if distance < min_distance:
        min_distance = distance


print(min_distance)