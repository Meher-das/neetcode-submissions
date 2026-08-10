class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        for i in range(0,n+1):
            if nums[i] != i:
                return i
            