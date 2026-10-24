class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #BFS is good for shortest path in an unweighted grid 
        if not grid or not grid[0]:
            return 
        
        rows,cols = len(grid), len(grid[0])
        q= deque()

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        
        directions = [[-1,0], [0,1],[1,0],[0,-1]]

        while q:
            r,c = q.popleft()

            for dr,dc in directions:
                nr = r +dr
                nc = c +dc
            
                if(nr <0 or nr >=len(grid) or nc<0 or nc>= len(grid[0]) or grid[nr][nc]!=2147483647):
                    continue 
                
                q.append([nr,nc])
                grid[nr][nc] = grid[r][c]+1
                
                















        