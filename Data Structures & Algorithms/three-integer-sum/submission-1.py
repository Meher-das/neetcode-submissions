class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = nums.sort()

        while i != len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return results