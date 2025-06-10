import sys

n, s = map(int, sys.stdin.readline().strip().split())

num = list(map(int, sys.stdin.readline().strip().split()))
# 백트래킹

print(sum(num))
