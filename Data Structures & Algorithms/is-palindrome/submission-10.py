class Solution:
    def isPalindrome(self, s: str) -> bool:
        for character in s:
            if not character.isalnum():
                print(character)