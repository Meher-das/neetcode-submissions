class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        result = [[]]
        for i in range(l):
            result += [subset + [nums[i]] for subset in result]
            # print(result)
        # print([2] + [3])
        return result