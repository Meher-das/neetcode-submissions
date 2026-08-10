class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = [None]*(len(nums)+1)
        result = []
        for i in range(len(nums)+1):
            l[nums[i]] = True
        for i in range(len(l)):
            if l[i] == None:
                result[i].append(i+1)
        return result