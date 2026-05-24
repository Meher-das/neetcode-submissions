class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        max_len = 0

        for num in nums:
            hashset.add(num)

        for num in nums:
            if num - 1 not in hashset:
                counter = 1
                while True:
                    if num + 1 in hashset:
                        counter += 1
                        num += 1
                    else:
                        break
                max_len = max(counter,max_len)
            
        return max_len