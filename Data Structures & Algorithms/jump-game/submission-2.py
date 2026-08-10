class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        max_index = len(nums) - 1

        while True:
            index += nums[index]
            if nums[index] == 0:
                return False
            if index == max_index:
                return True
            elif index > max_index:
                return False