class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
                    curr += 1
                    if curr in hash_map.keys():
                        sequenceLength += hash_map[curr]
                    else:
                        curr = 0
                        break

                longestLength = max(longestLength,sequenceLength)

            else:
                continue

        return longestLength