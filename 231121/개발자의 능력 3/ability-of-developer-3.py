import sys
score1 = 0
score2 = 0
min_score = sys.maxsize
people = list(map(int,input().split()))

def diff(a,b,c):
    global people
    sum1 = people[a]+people[b]+people[c]
    sum2 = sum(people) - sum1

    return abs(sum1-sum2)

for a in range(6):
    for b in range(6):
        for c in range(6):
            min_score = min(min_score,diff(a,b,c))

print(min_score)