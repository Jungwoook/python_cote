import sys

# n = int(sys.stdin.readline())
n = 12

def n_queen(n):
    count = 0
    
    def checkdia(v): # ↘ 체크, ↙ 체크
        list1 = []
        list2 = []
        
        for (idx, val) in enumerate(v):
            list1.append(val - idx)
            list2.append(val + idx)
        
        return len(set(list1)) == n and len(set(list2)) == n
    
    def backtrack(col, row, v): # 이전 위치를 받아 다음 위치에 배치
        nonlocal count
        if row > n:
            return 0
        
        v[col] = row
        for i in range(n):
            temp = v.copy()
            if v[i] == 0 :
                backtrack(i, row + 1, temp)
            else:
                if i == n-1:
                    if 0 not in v:
                        if checkdia(v):
                            # print('check', v)
                            
                            # print('+' + '--'*n + '-+')
                            # for val in v:
                            #     print('|' + ' .'*(val-1) + ' Q' + ' .'*(n-val) + ' |')
                            # print('+' + '--'*n + '-+')
                            
                            count += 1
    
    for i in range(n):
        visits = [0] * n
        backtrack(i, 1, visits)
        
    return count

print(n_queen(n))