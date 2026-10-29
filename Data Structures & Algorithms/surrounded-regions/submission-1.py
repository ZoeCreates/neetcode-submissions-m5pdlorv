class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return 
        
        ROWS, COLS = len(board), len(board[0])

        def capture(r,c):
            if r < 0 or c<0 or r ==ROWS or c == COLS or board[r][c] != "O":
                return 
            
            board[r][c] = "T"

            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        
        for c in range(COLS):
            if board[0][c] == "O":
                capture(0,c)
            if board[ROWS-1][c] =="O":
                capture(ROWS-1,c)
        
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r,0)
            if board[r][COLS-1] == "O":
                capture(r,COLS-1)
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
            
            
        
'''
第一步（捕获边界连通区）： 遍历矩阵的四条边界，只要遇到 'O'，就以它为起点进行 DFS（或 BFS），把所有能到达的 'O' 临时标记为临时符号，比如 'T'（或 '#'）。

第二步（翻转与还原）： 遍历整个矩阵：

如果是 'O'，说明它与边界不连通，属于被完全包围的区域，将它替换为 'X'。

如果是 'T'（或 '#'），说明它是安全的（与边界连通），将它还原为 'O'。

'''



        