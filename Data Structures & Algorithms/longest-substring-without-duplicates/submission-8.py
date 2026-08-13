class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxlength = 0
        bag = set()
        for r in range(len(s)):
            if s[r] in bag:
                while s[r] in bag:
                    bag.remove(s[l])
                    l += 1
            length = r - l + 1
            maxlength = max(maxlength,length)
            bag.add(s[r])
        return maxlength