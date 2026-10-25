class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0 
        rows,cols = len(grid),len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    q.append([i,j])

        
        while q and fresh > 0:
            for nodes in range(len(q)):
                r,c = q.popleft()

                directions = [[0,1],[1,0],[-1,0],[0,-1]]

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if(nr>=0 and nc>=0 and nr< len(grid) and nc < len(grid[0]) and grid[nr][nc] ==1):
                        grid[nr][nc] = 2
                        q.append([nr,nc])
                        fresh -=1
            
            time+=1
        
        if fresh ==0:
            return time
        else:
            return -1 
                        







        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #     q = collections.deque()
    #     fresh = 0
    #     time = 0

    #     for r in range(len(grid)):
    #         for c in range(len(grid[0])):
    #             if grid[r][c] == "1":
    #                 fresh +=1 
    #             if grid[r][c] == "2":
    #                 q.append((r,c))
        
    #     directions = [[0,1],[1,0],[-1,0],[0,-1]]
    #     while fresh > 0 and q:
    #         length = len(q)
    #         for i in range(length):
    #             r,c = q.popleft()

    #             for dr, dc in directions:
    #                 row, col = r+dr, c+dc
    #                 if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] ==1):
    #                     grid[row][col] ==2
    #                     q.append((row,col))
    #                     fresh -=1
            
    #         time +=1
    
    # return time if fresh == 0 else -1