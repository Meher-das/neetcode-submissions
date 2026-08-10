class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        l = 0
        h = 0
        max_len = 1
        while h < len(s):
            if s[h] not in hash_map.keys():
                hash_map[s[h]] = h
            else:
                l = hash_map[s[h]] + 1
                hash_map[s[h]] = h
            
            max_len = max(max_len,h-l+1)
            h += 1
        return max_len