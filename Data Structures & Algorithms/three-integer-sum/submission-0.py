class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        
        
        for i in range(len(nums)):
            # 1. 对 i 去重：如果这个数和上一个一样，跳过
            if i> 0 and nums[i] == nums[i-1]:
                continue 
            # 2. j 从 i+1 开始，保证不重复使用数字
            j,k = i+1, len(nums)-1
            target = -nums[i]
            
            while j<k:
                if nums[j] + nums[k]< target:
                    j+=1
                    
                elif  nums[j] + nums[k]> target:
                    k-=1
        
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    
                    # 3.先移动指针，再判断去重
                    j+=1
                    k-=1
                    while j <k and nums[j] == nums[j-1]:
                        j+=1

        
        return res 
                

                

        







        
        