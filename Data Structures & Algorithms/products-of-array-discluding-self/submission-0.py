class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [None for num in range(nums)]
        suffix = [None for num in range(nums)]

        for i in range(1,n):
            if prefix[i-1] != None:
                prefix[i] = num[i-1] * prefix[i-1]

        suffix[n-2] = nums[n-1]
        for i in range(1,n):
            if i > 1:
                suffix[n-i-1] = suffix[n-i] * nums[n-i]
        
        print(suffix)
        print(prefix)
