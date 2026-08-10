class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for s_a, t_a in zip(s,t):
            if s_a not in map_s:
                map_s[s_a] = 1
            else:
                map_s[s_a] += 1

            if t_a not in map_t:
                map_t[t_a] = 1
            else:
                map_t[t_a] += 1     
        
        return map_s == map_t