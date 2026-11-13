class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in seen:
                seen[nums[i]] = i 
            else:
                #Return the answer with the smaller index first.
                return [seen[diff], i ]


