n, k = map(int, input().split())

items = []

for i in range(n):
    w, v = map(int, input().split())
    items.append((w, v))
# n, k = 4, 7 #
# items = [(6, 13), (4, 8), (3, 6), (5, 12)] #
#--------------------------------------------#

dp = [0] * (k+1)

for w, v in items:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[k])