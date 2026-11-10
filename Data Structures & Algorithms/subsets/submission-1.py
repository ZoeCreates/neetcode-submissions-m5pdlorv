class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #回溯一般都是用同一个subset为了节省内存，实际上是一种剪枝行为
        res = []
        subset = []
        #subset是id，res要存2d的data，而且subset需要一直变化这个set所以要用两个

        def dfs(i): 
            #注意等于号，i因为是0_indexed所以 = 的时候就要停          
        
            if i >= len(nums):
                #用copy不然直接指向一个address了
                res.append(subset.copy())
                return      
           
                
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)  
        dfs(0)  
        return res 
        
        #call the function
        

    



        