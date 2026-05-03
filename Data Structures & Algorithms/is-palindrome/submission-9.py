class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for letter in s:
            if letter.isalnum():
                string = string + letter
        string = string.lower()
        n = len(string)
        i = 0
        while i <= n - i - 1:
            if string[i] != string[n-i-1]:
                return False
            i = i + 1
        return True
