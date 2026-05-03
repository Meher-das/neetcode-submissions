class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 1
        min_of_subarray = prices[s-1]
        max_price = 0
        while s < len(prices):
            min_of_subarray = min(min_of_subarray, prices[s-1])
            max_price = max(prices[s]-min_of_subarray, max_price)
            s += 1
        return max_price