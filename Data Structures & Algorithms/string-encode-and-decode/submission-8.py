class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = "".join(strs)

        for item in strs:
            l = len(item)
            l_str = str(l)
            while len(l_str) != 3:
                l_str = "0" + l_str
            msg += l_str
        
        n = len(strs)
        n_str = str(n)
        while len(n_str) != 3:
            n_str = "0" + n_str
        msg += n_str
        # print(msg)
        return msg

    def decode(self, s: str) -> List[str]:
        n = int(s[-3:-1])
        l = [int(s[-3-2*i:-1-2*i]) for i in range(n)]
        strs = []
        i = 0
        for item in l:
            strs.append(s[i:i+item])
            i += item - 1
        print(n,l,strs)
        return strs

