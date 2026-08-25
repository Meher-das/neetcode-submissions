class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for i in range(len(s)):
            if s[i].isalnum():
                string.append(s[i].lower())
        i = 0
        j = len(string) - 1
        while i <= j:
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                return False
        return True