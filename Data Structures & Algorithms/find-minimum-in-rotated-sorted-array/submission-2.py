class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 0
        last = len(nums) - 1
        while True:
            mid = (first + last) // 2
            
            if nums[first] < nums[mid-1]:
                first = mid
            else:
                last = mid - 1
            
            if first == last:
                break
        return first