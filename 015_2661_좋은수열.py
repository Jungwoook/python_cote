import sys

n = int(sys.stdin.readline())

def isGood(s):
    length = len(s)
    for l in range(1, length // 2 + 1):  # 부분 수열 길이
        for i in range(length - 2 * l + 1):  # 인접한 두 구간 비교
            if s[i:i+l] == s[i+l:i+2*l]:
                return False
    return True

def dfs(s):
    if len(s) == n:
        print(s)
        exit(0)
    
    for i in '123':
        if isGood(s + i):
            dfs(s + i)

print(dfs('1'))


# 1
# 12
# 121
# 1213
# 12131
# 121312
# 1213121
# 12131231
# 1213123121
# 12131231213123