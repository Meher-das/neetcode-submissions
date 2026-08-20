class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1

        
        l = 0
        r = len(nums) - 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        while r - l > 1:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            m = (l + r) //2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
                continue
            else:
                l = m
                continue
        return -1