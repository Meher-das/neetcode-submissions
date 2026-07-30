class Solution:
    def reverse(self, x: int) -> int:
        strint = str(abs(x))
        lenstr = len(strint)
        reversestr = ""
        for i in range(lenstr):
            reversestr += strint[lenstr - 1 - i]
        if reversestr == '0':
            return 0
        reverseint = int(int(reversestr) * (x/abs(x)))
        if reverseint < -(1<<31) or reverseint > (1<<31) - 1:
            return 0
        else:
            return reverseint