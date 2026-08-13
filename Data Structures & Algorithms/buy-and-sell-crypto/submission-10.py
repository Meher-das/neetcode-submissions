class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minidx = 0
        maxProfit = 0
        for i in range(1,len(prices)):
            maxProfit = max(maxProfit, prices[i] - prices[minidx])
            if prices[i] < prices[minidx]:
                minidx = i
        return maxProfit