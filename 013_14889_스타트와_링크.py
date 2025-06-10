import sys
import itertools

n = int(sys.stdin.readline())
player = [x for x in range(n)]
status = []
result = []

for _ in range(n):
    status.append(list(map(int, sys.stdin.readline().split())))
    
nCr = itertools.combinations(range(n), n//2)

for t1 in nCr:
    t2 = [x for x in player if x not in t1]
    
    com = itertools.combinations(range(n//2), 2)
    s1 = 0
    s2 = 0
    
    for i in com:
        s1 += status[t1[i[0]]][t1[i[1]]] + status[t1[i[1]]][t1[i[0]]]
        s2 += status[t2[i[0]]][t2[i[1]]] + status[t2[i[1]]][t2[i[0]]]
    
    result.append(abs(s1 - s2))
    
    
print(min(result))
    
# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0