class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap_s = {}
        hashMap_t = {}
        for i in range(len(s)):
            if s[i] not in hashMap_s.keys():
                hashMap_s[s[i]] = 1
            else:
                hashMap_s[s[i]] += 1
        
            if t[i] not in hashMap_t.keys():
                hashMap_t[t[i]] = 1
            else:
                hashMap_t[t[i]] += 1
        
        return hashMap_s == hashMap_t