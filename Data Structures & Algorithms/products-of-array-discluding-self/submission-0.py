class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n 
        pref =[0] *n
        suff = [0] *n

        #(nothing to the left of index 0)
        #(nothing to the right of last index)
        pref[0] = suff[n-1] = 1

        for i in range(1,n):
            #pref[i] 代表：第 i 个位置左边所有数的乘积
            pref[i] = nums[i-1]*pref[i-1]
        for i in range(n-2,-1,-1):
            suff[i] = nums[i+1]*suff[i+1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

        
            

        