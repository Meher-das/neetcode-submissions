class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memorySet = set()
        print(dir(sum(nums)))
        for num in nums:
            if num in memorySet:
                return True
            # memorySet.add(num)
        return False
    
