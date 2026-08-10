class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memorySet = set()
        for i in range(len(nums)):
            if nums[i] in memorySet:
                return True
            memorySet.append(nums[i])
        return False