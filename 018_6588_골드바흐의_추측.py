import sys

# n이하의 소수 구하기
def getNum(num):
    arr = [True] * (num + 1) # 모든 요소를 소수로 가정
    arr[0] = False # 0, 1은 소수가 아님
    arr[1] = False

    for i in range(2, num + 1):
        if arr[i] == True:
            j = 2

            while i * j < (n + 1):
                arr[i * j] = False
                j += 1

    return [i for i, p in enumerate(arr) if p]

while True:
    n = int(sys.stdin.readline())

    if n == 0: break

    arr = getNum(n)

    left, right = 0, len(arr) - 1
    current_sum = 0

    while True:
        current_sum = arr[left] + arr[right]

        if current_sum > n:
            right -= 1
        elif current_sum < n:
            left += 1
        else:
            print(f"{n} = {arr[left]} + {arr[right]}")
            break

        if left > right:
            print("Goldbach's conjecture is wrong.")
            break