class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones,first - second )
            
        #safety guard to handle the edge case where all stones destroy each other
        #from the question: return 0 if none remain.
        stones.append(0)
        
        #there is only gonna be one stone remain 
        return abs(stones[0])

