class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        l = 0
        r=1
        
        max_profit= 0

        while r< len(prices):
            #注意这里判断条件是右边的price比左边大
            # 不能直接写 if prices[r]- prices[l] > max_profit:
            # 因为这样的话else case会不对
            if prices[r] > prices[l]:
                max_profit = max(max_profit,prices[r]-prices[l])
            else:
                l=r
            
            r+=1
        
        return max_profit
        


                
            

        