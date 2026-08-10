class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            "]":"[",
            ")":"(",
            "}":"{"
        }

        for i in range(len(s)):
            stack.append(s[i])
            if s[i] in dictionary.keys():
                if dictionary[s[i]] == stack[-2]:
                    stack.pop()
                    stack.pop()
        
        return stack == []
