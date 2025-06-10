import sys

def checkWater(lake, x, y, r, c):
    if x > 0:
        if y > 0:
            pass
        elif y < r-1:
            pass
    elif x < c-1:
        pass


r, c = map(int, sys.stdin.readline().split())

lake = []

for i in range(r):
    a = sys.stdin.readline().split('\n')[0]
    lake.append([x for x in a])



print(lake)

for _ in range(5):
    for i in range(r):
        for j in range(c):
            lake[i][j]





# 10 2
# .L
# ..
# XX
# XX
# XX
# XX
# XX
# XX
# ..
# .L