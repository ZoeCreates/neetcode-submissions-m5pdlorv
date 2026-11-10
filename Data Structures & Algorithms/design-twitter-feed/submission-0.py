class Twitter:
    '''
    从用户自己以及他关注的所有人发出的推文中，高效地提取出最新的 10 条推文。
    '''
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # 最终要返回的 10 条推文 ID 列表
        minHeap = []  # 最小堆，用来做 K 路归并

        #获取 Feed 流时，用户不仅要看关注者的推文，也要能看到自己发过的推文。因此先将 userId 自身加入到关注列表中
        self.followMap[userId].add(userId)
        
        #把每个关注者【最新的一条推文】压入堆中
        #遍历所有关注者（包括自己），如果这个人发过推文（在 tweetMap 中）
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                #index 是该用户推文数组的最后一个下标（最新推文）
                index = len(self.tweetMap[followeeId]) - 1 

                #将 [count, tweetId, followeeId, index - 1] 入堆
                count, tweetId = self.tweetMap[followeeId][index]
                #Python 的 heapq 默认根据列表的第 0 个元素来对节点进行大小排序，所以count先放进去，负数绝对值越大代表推文越新
                #需要tweetid因为最后要返回给用户
                #followeeId：记录“这是谁发的推文”，当这条推文被拿走后，系统必须知道去谁的推文列表（即self.tweetMap[followeeId]）里去寻找该用户的下一条推文
                #index - 1：指示“下一次该取哪一条”
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])


        #循环从堆顶弹出最新推文，并补充下一条推文
        while minHeap and len(res) < 10:
            #heappop(minHeap) 弹出的总是目前堆里 count 最小（即时间最新）的那条推文
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            #把 tweetId 追加到 res 中
            res.append(tweetId)
            #追溯下一条：推文被取走后，检查该关注者是否还有更早的推文（即 index >= 0）。如果有，把该关注者更早的一条推文压入堆中，并将指针指再向更早的一条（index - 1）
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) 
        return res    #当收集满了 10 条推文（len(res) == 10）或者堆为空（所有人加起来推文都不够 10 条）时停止循环。

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)