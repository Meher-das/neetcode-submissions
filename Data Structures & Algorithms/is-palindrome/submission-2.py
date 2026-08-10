class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1
        string = ""
        for letter in s:
            if letter.isalnum():
                string += letter
        while i != j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1

        return True