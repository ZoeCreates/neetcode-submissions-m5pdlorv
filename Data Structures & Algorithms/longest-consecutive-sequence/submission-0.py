class Solution:
    '''

这段代码的核心精妙之处在于：
只从“序列的起点”开始向后计数。
什么是起点？如果数字 num - 1 不在集合里，说明 num 就是这个连续序列的开头。
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        #将输入的列表转换成一个哈希集合（Set）。作用： 1. 去除重复数字；2. 让后续查找数字是否存在（in 操作）的时间复杂度变成 $O(1)$，这是达到全局 $O(n)$ 的关键。
        numSet = set(nums)
        longest = 0 

        for num in numSet:
            #关键点！ 检查当前数字的前一个数字（num - 1）是否存在于集合中。
            #如果不存在，说明没有比它更小的连续数字了，它就是某个连续序列的绝对起点（例如：如果集合里有 2, 3, 4，遍历到 2 时，1 不在集合里，所以 2 是起点；遍历到 3 时，2 在集合里，直接跳过）。
            if(num-1) not in numSet:
                length = 1 
                #以当前起点为基准，不断检查下一个连续的数字（num + 1, num + 2 ...）是否在集合中。
                #只要在，说明序列还在延长，length 就加 1。
                while (num+ length) in numSet:
                    length +=1
                longest = max(length,longest)
        
        return longest 