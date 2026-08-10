class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for s_a, t_a in zip(s,t):
            print(s_a,t_a)