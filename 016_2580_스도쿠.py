import sys

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
sqs = [set() for _ in range(9)]

for i, line in enumerate(board):
    for j, val in enumerate(line):
        if val != 0:
            rows[i].add(val)
            cols[j].add(val)
            sqs[(i // 3 * 3) + j // 3].add(val)

def isValid(x, y, i):
    if i in rows[x]:
        return False
    
    if i in cols[y]:
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
        sys.exit(0)

    for i in range(1, 10):
        # blank를 순서대로 넣고 dfs
        # isValid 체크
        if isValid(blanks[index][0], blanks[index][1], i): # 유효하면

            board[blanks[index][0]][blanks[index][1]] = i
            rows[blanks[index][0]].add(i)
            cols[blanks[index][1]].add(i)
            sqs[(blanks[index][0] // 3 * 3) + blanks[index][1] // 3].add(i)

            dfs(index + 1)
            
            # 되돌리기
            board[blanks[index][0]][blanks[index][1]] = 0
            rows[blanks[index][0]].remove(i)
            cols[blanks[index][1]].remove(i)
            sqs[(blanks[index][0] // 3 * 3) + blanks[index][1] // 3].remove(i)
        
dfs(0)