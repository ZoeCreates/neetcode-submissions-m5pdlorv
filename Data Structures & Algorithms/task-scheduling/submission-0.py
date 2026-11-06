class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. 统计每个任务的出现频次
        count = Counter(tasks)

        #构建最大堆（利用负数变相实现大顶堆）
        maxHeap =  [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)


        # 3. 初始化辅助结构
        time = 0 
        q = deque()
        
        #开始模拟cpu loop
        while maxHeap or q:
            time +=1

            if maxHeap:
                # 取出当前频率最高的任务
                cnt = heapq.heappop(maxHeap) + 1  # 相当于 -(-cnt) - 1
                if cnt < 0:
                    # 还需继续执行，推入冷却队列，冷却结束时间为 time + n
                    q.append((cnt, time + n))
            
            # 检查是否有任务已过冷却期，重新压回最大堆
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        
        return time 

        