class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subsum = nums[0]
        max_sum = subsum
        start = 0
        end = 0
        for end in range(len(nums)):
            subsum = sum(nums[start:end+1])
            max_sum = max(max_sum, subsum)
            if subsum < 0:
                start = end + 1
        
        return max_sum