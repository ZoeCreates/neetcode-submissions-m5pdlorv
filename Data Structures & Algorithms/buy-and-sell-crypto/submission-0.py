class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0 
        #注意初始化不能是0不然price永远不会小于min_now
        min_now = prices[0]
        
        for price in prices:
            if price< min_now:
                min_now = price
            elif price - min_now > max_profit:
                max_profit = price-min_now
            
        return max_profit