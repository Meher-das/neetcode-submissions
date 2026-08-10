class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        sum = 0

        for i in range(len(nums)):
            if nums[i] >= 0:
                sum += nums[i]
            else:
                max_sum = max(sum, max_sum)
                sum = 0
        return max_sum