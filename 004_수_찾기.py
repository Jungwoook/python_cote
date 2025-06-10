import sys
import bisect

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_num = list(map(int, sys.stdin.readline().split()))

num.sort()
# m_num.sort()
# print(num)
# print(m_num)

for i in m_num:
    idx = bisect.bisect_left(num, i)
    print(1 if idx < len(num) and num[idx] == i else 0)

    


