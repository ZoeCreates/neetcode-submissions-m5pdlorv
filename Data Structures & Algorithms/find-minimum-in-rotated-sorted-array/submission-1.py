class Solution:
    def findMin(self, nums: List[int]) -> int:
        #核心思路：拿 mid 和 right 比较，找崖式下跌的地方。

        
        left, right = 0, len(nums) -1

        while left< right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid 
        
        return nums[left]
