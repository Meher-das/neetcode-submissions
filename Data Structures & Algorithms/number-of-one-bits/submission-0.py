class Solution:
    def hammingWeight(self, n: int) -> int:
        string_int = str(n)
        len_str = 0
        for i in string_int:
            if i == "1":
                len_str += 1
        return len_str