class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = [None]*len(nums)
        result = []
        for i in range(len(nums)):
            l[nums[i]] = True
        for i in range(len(l)):
            if l[i] == None:
                result[i].append(i+1)
        return result