class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = [(4,2), (1,2),(0,1),(7,1)]
        pair = [(p,s) for p,s in zip(position,speed)]
        
        #从最后一个位置（离终点最近）的车开始放进stack
        pair.sort(reverse =True)
        stack = []
        #reverse sorted order
        for p,s in pair:
            #算一下两个车到终点需要的时间
            #如果比如离终点第二近的车到终点需要的时间比第一近的车少
            #那么把这个车销毁（stack.pop()）
            stack.append((target-p)/s) #注意这里python是decimal division
            if len(stack) >= 2 and stack[-1]<= stack[-2]:
                stack.pop()
            #最后还留在stack上的车的数量就是我们的number of carfeet
        return len(stack)



