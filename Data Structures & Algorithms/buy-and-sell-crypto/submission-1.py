class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        min_of_subarray = prices[b]
        max_price = 0
        while s < len(prices):
            price = prices[s] - min(min_of_subarray, prices[b])
            max_price = max(price, max_price)
            s += 1
            b += 1
        return max_price