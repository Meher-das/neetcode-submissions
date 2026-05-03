class Solution:
    def hammingWeight(self, n: int) -> int:
        l = [bit for bit in format(n, '32b') if bit != ' ']
        print(l)
        return l.count('1')