# n, k = map(int, input().split())

# item = []

# for i in range(n):
#     a, b = map(int, input().split())
#     item.append((a, b))
n, k = 4, 7 #
item = [(6, 13), (4, 8), (3, 6), (5, 12)] #
#--------------------------------------------#

dp = [0] * (k+1)

for w, v in item:
    for i in range(k, w-1, -1):  # 거꾸로 탐색
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[k])