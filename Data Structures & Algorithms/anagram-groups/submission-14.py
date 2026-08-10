class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_encodings = {}
        # print(ord('a'),type(ord('a')))
        for i,string in enumerate(strs):
            str_encoding = [0] * (ord('z') - ord('a') + 1)
            for letter in string:
                str_encoding[ord(letter)-ord('a')] += 1
            
            if tuple(str_encoding) not in strs_encodings:
                strs_encodings[tuple(str_encoding)] = [i]    
            else:
                strs_encodings[tuple(str_encoding)].append(i)
        
        answer = []
        for key, value in strs_encodings.items():
            answer.append(value)
        return answer