class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [None for num in range(len(nums))]
        suffix = [None for num in range(len(nums))]

        prefix[1] = nums[0]
        for i in range(2,n):
            prefix[i] = nums[i-1] * prefix[i-1]

        suffix[n-2] = nums[n-1]
        for i in range(1,n):
            if i > 1:
                suffix[n-i-1] = suffix[n-i] * nums[n-i]
        
        result = []
        for i in range(len(nums)):
            if prefix[i] == None:
                result.append(suffix[i])
            elif suffix[i] == None:
                result.append(prefix[i])
            else:
                result.append(prefix[i]*suffix[i])
        
        return result

