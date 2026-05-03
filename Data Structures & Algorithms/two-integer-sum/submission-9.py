class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap.keys():
                hashMap[nums[i]] = [i]
            else:
                hashMap[nums[i]].append(i)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap.keys():
                if i != hashMap[complement][0]:
                    return sorted([i,hashMap[complement][0]])
