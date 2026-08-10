class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        length = 0
        max_length = 0
        table = {}

        for j in range(len(s)):
            if s[j] not in table:
                table[s[j]] = j
                j += 1
            
            else:
                length = j - i
                i = table[s[j]] + 1
                table[s[j]] = j
                max_length = max(length, max_length)

        return max_length