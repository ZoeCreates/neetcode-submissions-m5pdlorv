class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #从数组 nums 中找出前 $k$ 个最大的元素
        return heapq.nlargest(k,nums)[-1]


#时间复杂度： nlogk
#比较一次，如果进去了，调整堆最多走 $\log_2(k)$ 步
#一共n次比较最多


'''
最小堆 / 优先队列（Min-Heap）：维护一个只保存 k 个元素 的最小堆。遍历数组，依次把元素放入堆中。如果堆的大小超过了 k，就把堆顶（最小的那个）弹出。

遍历结束后，堆里剩下的就是前 k 个最大的数，而堆顶正好就是这 k 个数里最小的，也就是第 k 大的元素。时间复杂度：$O(n \log k)$，空间复杂度：$O(k)$。

'''