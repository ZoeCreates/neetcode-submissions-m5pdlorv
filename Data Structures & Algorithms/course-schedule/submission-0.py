class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                #cycle detected
                return False 
            if preMap[crs] == []:
                return True 
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            preMap[crs] = []
            return True 
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True 


'''

构建邻接表：记录每门课程依赖哪些先修课程。

状态标记：

使用集合 visiting 记录当前递归路径中的节点（用来检测是否存在环）。

递归遍历：

如果当前节点已经在 visiting 中，说明出现了回边（环），直接返回 False。

如果当前课程的先修列表为空，说明该课程安全，可以修读，返回 True。

遍历完该节点的所有依赖后，将其从 visiting 移除，并清空其依赖（标记为已处理过），防止重复计算。

'''



        