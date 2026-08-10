class Solution:
    def hammingWeight(self, n: int) -> int:
        l = [bit for bit in format(num, '32b')]
        print(l)