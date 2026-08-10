class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for letter in s:
            if letter.isalnum():
                string = string + letter
        print(string)