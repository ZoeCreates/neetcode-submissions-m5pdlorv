class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or i == len(candidates):
                return 
            
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            
            cur.pop()

            #while 循环 保证了当你决定放弃 1 的时候，绝不给后面的 1 任何机会来“冒充”第一个 1 再重新生成一遍 [1, 2]。
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,cur,total)
        
        dfs(0,[],0)

        return res 

        


        