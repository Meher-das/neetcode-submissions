class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)
        print(num_set)