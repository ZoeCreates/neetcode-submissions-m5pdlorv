class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        
        #创建4个空列表的数组
    
    ##    adj = [
   ## [],  # 节点 0 的邻居列表
  ##  [],  # 节点 1 的邻居列表
   ## [],  # 节点 2 的邻居列表
   ## []   # 节点 3 的邻居列表
##. ]

       
        adj = [[]for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit =set()
        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei,node):
                    return False
            return True 
        
        return dfs(0,-1) and len(visit) == n 

            


        