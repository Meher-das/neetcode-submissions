class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            mid = (left + right) // 2
            
            if nums[first] < nums[mid-1]:
                first = mid
            else:
                last = mid
            
            if first == last:
                return nums[first]