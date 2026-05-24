class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        
        for character in s:
            if character.isalnum():
                new_str += character.lower()

        print(new_str)
        k = len(new_str)
        i = 0
        while i <= k - i - 1:
            if new_str[i] != new_str[k-i-1]:
                return False
            else:
                i += 1
        return True
            
