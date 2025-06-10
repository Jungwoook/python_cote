import sys
import itertools

while True:
    num = list(map(int, sys.stdin.readline().strip().split()))

    n = num[0]
    num = num[1:]
    if n == 0:
        break

    nCr = list(itertools.combinations(num, 6))

    for c in nCr:
        print(c[0], c[1], c[2], c[3], c[4], c[5])
    print()
