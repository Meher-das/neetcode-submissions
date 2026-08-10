class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap.keys():
                hashMap[nums[i]] = [i]
            else:
                hashMap[nums[i]].append(i)

        for i in range(len(nums)):
            if hashMap[target - nums[i]]:
                if i != hashMap[target - nums[i]]:
                    return [i,hashMap[target - nums[i]]]
