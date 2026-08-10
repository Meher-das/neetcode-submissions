class Solution:
    def hammingWeight(self, n: int) -> int:
        l = [bit for bit in format(n, '32b')]
        print(l)