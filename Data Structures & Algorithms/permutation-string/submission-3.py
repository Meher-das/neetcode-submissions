class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowlength = len(s1)
        targetmap = {}
        for i in range(windowlength):
            if s1[i] not in targetmap:
                targetmap[s1[i]] = 1
            else:
                targetmap[s1[i]] += 1

        for j in range(0,len(s2)-windowlength+1):
            referencemap = {}
            for i in range(j,j + windowlength):
                if s2[i] not in referencemap:
                    referencemap[s2[i]] = 1
                else:
                    referencemap[s2[i]] += 1
            print(targetmap)
            print(referencemap)
            if targetmap == referencemap:
                return True
        
        return False
