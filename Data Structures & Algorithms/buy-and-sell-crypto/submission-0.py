class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            for j in range(i + 1,len(prices)):
                print(prices[i] , prices[j])
                if prices[j] - prices[i] > 0 and prices[j] - prices[i] > profit:
                        profit = prices[j] - prices[i]
        return profit