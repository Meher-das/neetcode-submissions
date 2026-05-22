class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i,num in enumerate(nums):
            if num in dictionary.keys():
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        
        frequencies = []
        for key, value in dictionary.items():
            frequencies.append([value,key])
        
        frequencies.sort()

        ans = []
        for i in range(-1,-k-1,-1):
            ans.append(frequencies[i][1])
        return ans
