import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    # def add(self, data):
        

# str = sys.stdin.readline().strip()
# n = int(sys.stdin.readline())

# c = len(str)
# head = Node(str[0])

# for c in str:
    # print(c)

    

# for _ in range(n):
#     input = sys.stdin.readline().strip()
    
#     if input[0] == 'L':
#         if c > 0:
#             c -= 1
#     elif input[0] == 'D':
#         if c < len(str):
#             c += 1
#     elif input[0] == 'B':
#         if c > 0:
#             str = str[:c-1] + str[c:]
#             c -= 1
#     elif input[0] == 'P':
#         ch = input.split(' ')[1]
#         str = str[:c] + ch + str[c:]
#         c += 1

# print(str)



