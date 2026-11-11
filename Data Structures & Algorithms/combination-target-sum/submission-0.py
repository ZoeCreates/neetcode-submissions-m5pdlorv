class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        #cur maintains the current combinations, eg. [2 2]
        def dfs(i,cur,total):
            if total == target:
                #因为我们只有一个cur来keep track of all combinations
                res.append(cur.copy())
                return 
            
            if i >= len(nums) or total >= target:
                return 
            
            #we do include nums[i]
            cur.append(nums[i])
            dfs(i, cur,total+ nums[i])

            #not including nums[i]
            cur.pop()
            dfs(i+1,cur,total)
        
        dfs(0,[],0)
        return res 
        


            


        
        