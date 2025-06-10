import sys

n, m = map(int, sys.stdin.readline().strip().split())
city = []

for _ in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))
    # 0은 빈 칸, 1은 집, 2는 치킨집

N = []
M = []

for i, r in enumerate(city):
    for j, c in enumerate(r):
        if c == 1:
            N.append((i, j))
        elif c == 2:
            M.append((i, j))

distance = []

for i in M:
    temp = []
    for j in N:
        temp.append(abs(i[0]-j[0]) + abs(i[1]-j[1]))
    distance.append(temp)

sorted_dist = sorted(distance, key=sum)

# print(distance)
# print(sorted_dist)
dist = sorted_dist[:m]
minval = []

for i in range(len(N)):
    temp = []
    for d in dist:
        temp.append(d[i])
    minval.append(min(temp))
    
print(sum(minval))
    
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2
# 가로 집, 세로 치킨