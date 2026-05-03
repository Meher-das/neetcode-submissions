class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        min_of_subarray = prices[b]
        max_price = 0
        while b < len(prices)-1:
            min_of_subarray = min(min_of_subarray, prices[b])
            max_price = max(prices[b+1]-min_of_subarray, max_price)
            b += 1

        return max_price