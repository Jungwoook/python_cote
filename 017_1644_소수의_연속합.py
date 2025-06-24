import sys

n = int(sys.stdin.readline())

# n이하의 소수 구하기
def getNum(num):
    arr = [True] * (num + 1) # 모든 요소를 소수로 가정
    arr[0] = False # 0, 1은 소수가 아님
    arr[1] = False

    for i in range(2, num + 1):
        if arr[i] == True:
            j = 2

            while i * j < (num + 1):
                arr[i * j] = False
                j += 1

    return [i for i, p in enumerate(arr) if p]

numArr = getNum(n)

left, right = 0, 0
current_sum = 0
cnt = 0

while True:
    if current_sum >= n:
        if current_sum == n:
            cnt += 1
        current_sum -= numArr[left]
        left += 1
    elif right == len(numArr):
        break
    else:
        current_sum += numArr[right]
        right += 1

print(cnt)