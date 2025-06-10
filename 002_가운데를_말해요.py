import sys
import heapq

n = int(sys.stdin.readline())

ih = []
xh = []
heapq.heapify(ih)
heapq.heapify(xh)

t = int(sys.stdin.readline())
med = (t, t)
print(med[1])

for i in range(1, n):
    a = int(sys.stdin.readline())
    
    if len(xh) == len(ih): # ih에 큰수
        if a < med[1]:
            heapq.heappush(ih, (med[1], med[1]))
            med = heapq.heappushpop(xh, (-a, a))
        else:
            heapq.heappush(ih, (a, a))
            
    else: # xh에 작은수
        if a < med[1]:
            heapq.heappush(xh, (-a, a))
        else:
            heapq.heappush(xh, (-med[1], med[1]))
            med = heapq.heappushpop(ih, (a, a))
    print(med[1])