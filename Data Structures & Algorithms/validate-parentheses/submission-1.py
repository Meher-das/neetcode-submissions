class Solution:
    def isValid(self, s: str) -> bool:
        hashtable = {
            '(':')',
            '{':'}',
            '[':']'
        }

        character_str = ""

        for item in s:
            if item in hashtable.keys() or item in hashtable.values():
                character_str += item
        
        if len(character_str) % 2 != 0:
            return False
        else:
            k = len(character_str)
            for i in range(int(k/2)):
                if hashtable[character_str[i]] != character_str[k-i-1]:
                    return False
            return True
