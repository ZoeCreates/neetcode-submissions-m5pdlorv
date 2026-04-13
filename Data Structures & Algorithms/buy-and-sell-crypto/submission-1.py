class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Greedy approch
        #局部最优：当我里边到第i天时，如果我在今天卖出，最大利润取决于之前出现的最低价格
        #决策简化：不需要知道未来的价格只需要记住当前见过最便宜的价格
        #全局最优：如果我例遍了每一天，并假设每一天都是卖出日，计算出的所有利润中的最大值，必然就是全局的最大利润
        max_profit = 0

        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price 
            if profit > max_profit:
                max_profit= profit
        
        return max_profit


    