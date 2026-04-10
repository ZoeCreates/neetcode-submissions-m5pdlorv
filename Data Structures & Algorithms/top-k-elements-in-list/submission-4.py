class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create the num: frequency dic 
        count = {}
        for num in nums:
            count[num] = 1+ count.get(num,0)
       
        #create the heap
        heap = []
        # iterating through all the num as keys in the dic
        for num in count.keys():        
            #push the freq num pair into the heap
            heapq.heappush(heap, (count[num],num))
         
            # if the len of the heap > k, pop 
            if len(heap) > k:
                heapq.heappop(heap)
                           

        #extract the num that has top k freq from the heap
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
                
      





        





        