class Solution:
    def reverseBits(self, n: int) -> int:
        binarynumber = bin(n)[2:]
        # print(binarynumber)
        result = binarynumber[::-1] + "0"*(32-len(binarynumber))
        return int(result,2)