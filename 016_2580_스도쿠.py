import sys

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
sqs = [set() for _ in range(9)]

for i, line in enumerate(board):
    for j, val in enumerate(line):
        if val != 0:
            rows[j].add(val)
            cols[i].add(val)
            sqs[(i // 3 * 3) + j // 3].add(val)

def isValid(x, y, i):
    if i in rows[y]:
        return False
    
    if i in cols[x]:
        return False
    
    if i in sqs[(x // 3 * 3) + y // 3]:
        return False
    
    return True
    

def dfs(index):
    if index == len(blanks):
        for li in board:
            for i in li:
                print(i, end=' ')
            print()
        return

    for i in range(1, 10):
        # blank를 순서대로 넣고 dfs
        board[blanks[index][0]][blanks[index][1]] = i
        # isValid 체크
        if isValid(blanks[index][0], blanks[index][1], i): # 유효하면
            dfs(index + 1)
        
dfs(0)