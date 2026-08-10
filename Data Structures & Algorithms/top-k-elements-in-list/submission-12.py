class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i,num in enumerate(nums):
            if num in nums.keys():
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        
        frequencies = []
        for key, value in dictionary.items():
            frequencies.append([value,key])
        
        frequencies.sort()

        ans = []
        for i in range(k):
            ans.append(frequencies[i][1])
        return ans
