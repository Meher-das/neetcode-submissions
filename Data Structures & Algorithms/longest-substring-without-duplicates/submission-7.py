class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        hash_map = {}
        for i in range(len(s)):
            if s[i] not in hash_map.keys():
                hash_map[s[i]] = i
            else:
                start = hash_map[s[i]] + 1
                hash_map[s[i]] = i

            length = i - start + 1
            max_length = max(length,max_length)
        return max_length
            