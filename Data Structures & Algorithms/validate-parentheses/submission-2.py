class Solution:
    def isValid(self, s: str) -> bool:
        hashtable = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []

        for character in s:
            
            if character in hashtable.values():
                stack.append(character)
            
            elif character in hashtable.keys():
                
                if stack != [] and stack[-1] == hashtable[character]:
                    stack.pop()
                
                else:
                    return False
        
        if stack == []:
            return True
        else:
            return False
