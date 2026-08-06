class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        hash_map = {}
        longestLength = 0

        for num in nums:
            if num not in hash_map.keys():
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        def isStart(num):
            if num - 1 not in hash_map.keys():
                return True
            return False

        for num in nums:
            if isStart(num):
                sequenceLength = 0
                curr = num

                while True:
                    
                    if curr in hash_map.keys():
                        sequenceLength += 1
                    else:
                        break

                    curr += 1

                longestLength = max(longestLength,sequenceLength)

            else:
                continue

        return longestLength