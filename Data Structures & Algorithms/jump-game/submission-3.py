class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        max_index = len(nums) - 1

        while True:
            if nums[index] == 0:
                return False
            index += nums[index]

            if index == max_index:
                return True
            elif index > max_index:
                return False