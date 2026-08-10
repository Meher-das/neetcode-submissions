class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = nums.sort()
        i = 0
        j = len(nums) - 1
        while i!=j:
            if nums[i] == target - nums[j]:
                return [i,j]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1