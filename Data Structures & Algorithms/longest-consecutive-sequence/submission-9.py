class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxlen = 0
        for num in nums:
            if num - 1 not in hashset:
                curlen = 1
                currnum = num + 1
                while currnum in hashset:
                    curlen += 1
                    currnum += 1
                maxlen = max(curlen,maxlen)
        return maxlen