
'''
# rows 的形式：行号 -> 集合
rows = {
    0: {"5", "3", "7"},  # 第 0 行，目前已经有 "5", "3", "7" 这三个数字了
    1: {"6", "1", "9"},  # 第 1 行，目前已经有 "6", "1", "9" 
    2: {"8", "2"}        # 第 2 行...
}

# cols 的形式：列号 -> 集合
cols = {
    0: {"5", "6", "8"},  # 第 0 列，目前有 "5", "6", "8"
    1: {"3", "1"},       # 第 1 列，目前有 "3", "1"
    4: {"7"}             # 第 4 列...
}

# squares 的形式：(行块, 列块)元组 -> 集合
squares = {
    (0, 0): {"5", "3", "6", "1", "8"}, # 左上角这个 3x3 的方格里，已经塞了 5个数字
    (0, 1): {"7"},                     # 第一排中间的 3x3 方格里，目前只有 "7"
    (1, 0): {"4", "9"}                 # 第二排左边的 3x3 方格...
}

'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue 
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                    return False 
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
            
        return True 