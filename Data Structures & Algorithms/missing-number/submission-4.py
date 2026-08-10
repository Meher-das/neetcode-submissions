class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i+1] - nums[i] > 1:
                return nums[i] + 1
            else:
                return 0