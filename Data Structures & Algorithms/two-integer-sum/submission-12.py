class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memorySet = {}
        for j in range(len(nums)):
            if target - nums[j] in memorySet.keys():
                return memorySet[target - nums[j]], j
            memorySet[nums[j]] = j

