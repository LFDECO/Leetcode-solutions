class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final_profit=0
        min_price=prices[0]
        running=0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            running=prices[i]-min_price
            if running>final_profit:
                final_profit=running
           

        return final_profit