import sys
score1 = 0
score2 = 0
min_score = sys.maxsize
people = list(map(int,input().split()))

for a in range(6):
    for b in range(6):
        if b==a:
            continue
        for c in range(6):
            if c==a or c==b:
                continue
            
            score1 = 0
            score2 = 0

            for i in range(6):
                if i==a or i==b or i==c:
                    score1 += people[i]
                else:
                    score2 += people[i]

            score = abs(score1-score2)
            min_score = min(score,min_score)
            
print(min_score)